# -*- coding: utf-8 -*-
""" TaskSets and tasks for the MilMove interface. """
import logging

from locust import task

from utils.auth import UserType, create_user
from utils.task import RestTaskSet


logger = logging.getLogger(__name__)


class MilMoveTasks(RestTaskSet):
    """
    Set of tasks that can be called for the MilMove interface.
    """

    def on_start(self):
        """
        Creates a login right at the start of the TaskSet and stops task execution if the login fails.
        """
        success = create_user(request_preparer=self.request_preparer, session=self.client, user_type=UserType.MILMOVE)

        if not success:
            logger.error("Failed to create a user")
            self.interrupt()

    @task
    def get_user_info(self):
        """
        Gets the user info for the currently logged in user.
        """
        url, request_kwargs = self.request_preparer.prep_internal_request(endpoint="/users/logged_in")

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            logger.info(f"ℹ️ User email: {resp.js.get('email', 'None')}")
