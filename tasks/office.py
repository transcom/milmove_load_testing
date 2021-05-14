# -*- coding: utf-8 -*-
""" TaskSets and tasks for the Office interface. """
import logging
import json
import random
from typing import Dict

from locust import task, tag

from utils.constants import (
    MOVE,
    MOVE_TASK_ORDER,
    MTO_SERVICE_ITEM,
    MTO_SHIPMENT,
    QUEUES,
    PAYMENT_REQUEST,
)
from .base import check_response, LoginTaskSet, ParserTaskMixin

logger = logging.getLogger(__name__)


def ghc_path(url: str) -> str:
    return f"/ghc/v1{url}"


class OfficeDataStorageMixin:
    """
    TaskSet mixin used to store data from the GHC API during load testing so that it can be passed around and reused.
    We store a number of objects in a local store that can be requested by tasks.
    The tasks then hit an endpoint and call add or replace to update our local store with a list of viable objects.
    This mixin allows storing multiple items of each kind.
    """

    DATA_LIST_MAX: int = 100
    local_store: Dict[str, list] = {
        MOVE_TASK_ORDER: [],
        MTO_SHIPMENT: [],
        MTO_SERVICE_ITEM: [],
        PAYMENT_REQUEST: [],
    }  # data stored will be shared among class instances thanks to mutable dict

    def get_stored(self, object_key, *args, **kwargs):
        """
        Given an object_key that represents an object type from the MilMove app, returns an object of that type from the
        list.

        :param object_key: str in [MOVE_TASK_ORDER, MTO_SHIPMENT, MTO_SERVICE_ITEM, PAYMENT_REQUEST]
        """
        data_list = self.local_store[object_key]

        if len(data_list) > 0:  # otherwise we return None
            return random.choice(data_list)

    def add_stored(self, object_key, object_data):
        """
        Adds data to the list for the object key provided. Also checks if the list is already at the max number of
        elements, and if so, it randomly removes 1 to MAX number of elements so that the cycle can start again (and so
        we don't hog too much memory).

        :param object_key: str in [MOVE_TASK_ORDER, MTO_SHIPMENT, MTO_AGENT, MTO_SERVICE_ITEM, PAYMENT_REQUEST]
        :param object_data: JSON/dict
        :return: None
        """
        data_list = self.local_store[object_key]

        if len(data_list) >= self.DATA_LIST_MAX:
            num_to_delete = random.randint(1, len(data_list))
            del data_list[:num_to_delete]

        # Some creation endpoint auto-create multiple objects and return an array,
        # but each object in the array should still be considered individually here:
        if isinstance(object_data, list):
            data_list.extend(object_data)
        else:
            data_list.append(object_data)

    def update_stored(self, object_key, old_data, new_data):
        """
        Given an object key, replaces a stored object in the local store with a new updated object.

        :param object_key: str in [MOVE_TASK_ORDER, MTO_SHIPMENT, MTO_AGENT, MTO_SERVICE_ITEM, PAYMENT_REQUEST]
        :param old_data: JSON/dict
        :param new_data: JSON/dict
        :return: None
        """
        data_list = self.local_store[object_key]

        # Remove all instances of the stored object, in case multiples were added erroneously:
        while True:
            try:
                data_list.remove(old_data)
            except ValueError:
                break  # this means we finally cleared the list

        data_list.append(new_data)


class ServicesCounselorTasks(OfficeDataStorageMixin, LoginTaskSet, ParserTaskMixin):
    """
    Set of tasks that can be called for the MilMove Office interface with the Services Counselor role.
    """

    def on_start(self):
        """
        Creates a login right at the start of the TaskSet and stops task execution if the login fails.
        """
        super().on_start()  # sets the csrf token

        resp = self._create_login(user_type="Services Counselor office", session_token_name="office_session_token")
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
        object_id = overrides.get("id") if overrides else None
        move = self.get_stored(MOVE_TASK_ORDER, object_id)
        headers = {"content-type": "application/json"}

        resp = self.client.get(
            ghc_path(f"/move/{move['locator']}"),
            name=ghc_path("/move/{locator}"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        new_mto, success = check_response(resp, "getMove")

    @tag(QUEUES, "getServicesCounselingQueue")
    @task
    def get_moves_queue(self, overrides=None):
        """
        Fetches a list of paginated moves
        """

        headers = {"content-type": "application/json"}

        # Use the default queue sort for now, adding a filter to return service counseling completed moves as well
        resp = self.client.get(
            ghc_path(
                "/queues/counseling?page=1&perPage=50&sort=submittedAt&order=asc"
                "&status=NEEDS SERVICE COUNSELING,SERVICE COUNSELING COMPLETED"
            ),
            name=ghc_path("/queues/counseling"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        moves, success = check_response(resp, "getServicesCounselingQueue")

        # these are not full move models and will be those in needs counseling status
        self.add_stored(MOVE_TASK_ORDER, moves["queueMoves"])


class TOOTasks(OfficeDataStorageMixin, LoginTaskSet, ParserTaskMixin):
    """
    Set of tasks that can be called for the MilMove Office interface with the TOO role.
    """

    def on_start(self):
        """
        Creates a login right at the start of the TaskSet and stops task execution if the login fails.
        """
        super().on_start()  # sets the csrf token

        resp = self._create_login(user_type="TOO office", session_token_name="office_session_token")
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
        object_id = overrides.get("id") if overrides else None
        move = self.get_stored(MOVE_TASK_ORDER, object_id)

        headers = {"content-type": "application/json"}

        resp = self.client.get(
            ghc_path(f"/move/{move['locator']}"),
            name=ghc_path("/move/{locator}"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        new_mto, success = check_response(resp, "getMove")

    @tag(QUEUES, "getMovesQueue")
    @task
    def get_moves_queue(self, overrides=None):
        """
        Fetches a list of paginated moves
        """

        headers = {"content-type": "application/json"}

        resp = self.client.get(
            ghc_path("/queues/moves?page=1&perPage=50&sort=status&order=asc"),
            name=ghc_path("/queues/moves"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        moves, success = check_response(resp, "getMovesQueue")

        self.add_stored(MOVE_TASK_ORDER, moves["queueMoves"])
