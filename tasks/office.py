# -*- coding: utf-8 -*-
""" TaskSets and tasks for the Office interface. """
import logging
import json

from locust import task, tag

from utils.constants import MOVE

from .base import check_response, LoginTaskSet, ParserTaskMixin

logger = logging.getLogger(__name__)


def ghc_path(url: str) -> str:
    return f"/ghc/v1{url}"


class OfficeTasks(LoginTaskSet, ParserTaskMixin):
    """
    Set of tasks that can be called for the MilMove Office interface.
    """

    def on_start(self):
        """
        Creates a login right at the start of the TaskSet and stops task execution if the login fails.
        """
        super().on_start()  # sets the csrf token

        resp = self._create_login(user_type="PPM office", session_token_name="office_session_token")
        if resp.status_code != 200:
            self.interrupt()  # if we didn't successfully log in, there's no point attempting the other tasks

    @task
    def get_user_info(self):
        """
        Gets the user info for the currently logged in user.
        """
        resp = self.client.get("/internal/users/logged_in")
        try:
            json_body = json.loads(resp.content)
        except json.JSONDecodeError:
            logger.exception("Non-JSON response")
        else:
            logger.info(f"ℹ️ User email: {json_body.get('email', 'None')}")

    @tag(MOVE, "getMove")
    @task
    def get_move(self, overrides=None):
        """
        Fetches a single move
        """
        # If id was provided, get that specific one. Else get any stored one.
        locator = overrides.get("locator") if overrides else "COMBOS"

        headers = {"content-type": "application/json"}

        resp = self.client.get(
            ghc_path(f"/move/{locator}"),
            name=ghc_path("/move/{locator}"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        new_mto, success = check_response(resp, "getMove")
