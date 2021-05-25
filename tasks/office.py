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
    ORDER,
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
    local_store: Dict[str, Dict[str, Dict]] = {
        MOVE_TASK_ORDER: {},
        MTO_SHIPMENT: {},
        MTO_SERVICE_ITEM: {},
        ORDER: {},
        PAYMENT_REQUEST: {},
    }  # data stored will be shared among class instances thanks to mutable dict

    def get_stored(self, object_key, object_id=None, *args, **kwargs):
        """
        Given an object_key that represents an object type from the MilMove app, returns an object of that type from the
        list.

        :param object_key: str in [MOVE_TASK_ORDER, MTO_SHIPMENT, MTO_SERVICE_ITEM, ORDER, PAYMENT_REQUEST]
        :param object_id: str uuid of a single object item key to return
        """
        data_dict = self.local_store[object_key]
        data_item = data_dict.get(object_id)
        if data_item is not None:
            return data_item

        if len(data_dict) > 0:
            return random.choice(list(data_dict.values()))

    def add_stored(self, object_key, object_data):
        """
        Adds data to the dict for the object key provided. Also checks if the dict is already at the max number of
        elements, and if so, it randomly removes 1 to the size of elements in the dict so that the cycle can start again
        (and so we don't hog too much memory).  Entries are keyed by the id value of the object data, a list will not
        overwrite existing keys as they may have been individually updated.

        :param object_key: str in [MOVE_TASK_ORDER, MTO_SHIPMENT, MTO_AGENT, MTO_SERVICE_ITEM, PAYMENT_REQUEST]
        :param object_data: JSON/dict
        :return: None
        """
        data_dict = self.local_store[object_key]

        if len(data_dict) >= self.DATA_LIST_MAX:
            print("removing item from local store")
            num_to_delete = random.randint(1, len(data_dict) - 1)
            print(f"num to delete {num_to_delete}")
            # Convert a dict to a list so we can take a slice by insertion order fifo
            self.local_store[object_key] = dict(list(data_dict.items())[num_to_delete:])

        # Some creation endpoint auto-create multiple objects and return an array,
        # but each object in the array should still be considered individually here:
        if isinstance(object_data, list):
            # transforms a list of objects with ids into a dictionary keyed by their id values
            normalized = {value["id"]: value for value in object_data}
            # merge the new data being added with the existing objects, not overwriting existing keys
            self.local_store[object_key] = {**normalized, **data_dict}
        else:
            self.local_store[object_key][object_data["id"]] = object_data


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
        if move is None:
            logger.info("Skipping get move none are stored yet")
            return

        headers = {"content-type": "application/json"}

        resp = self.client.get(
            ghc_path(f"/move/{move['locator']}"),
            name=ghc_path("/move/{locator}"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        new_mto, success = check_response(resp, "getMove")
        if success:
            self.add_stored(MOVE_TASK_ORDER, new_mto)
        return new_mto

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
        if success:
            # these are not full move models and will be those in needs counseling status
            self.add_stored(MOVE_TASK_ORDER, moves["queueMoves"])

    @tag(ORDER, "getOrder")
    @task
    def get_orders(self, overrides=None):
        """
        Fetches a single service member's orders
        """
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        move = self.get_stored(MOVE_TASK_ORDER, object_id)
        if move is None:
            logger.info("Skipping get orders no move is stored yet")
            return

        orders_id = move.get("ordersId")
        if orders_id is None:
            move = self.get_move({"id": move["id"]})

        headers = {"content-type": "application/json"}
        resp = self.client.get(
            ghc_path(f"/orders/{move['ordersId']}"),
            name=ghc_path("/orders/{ordersId}"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        order, success = check_response(resp, "getOrder")
        if success:
            self.add_stored(ORDER, order)

    @tag(MTO_SHIPMENT, "listMTOShipments")
    @task
    def get_shipments(self, overrides=None):
        """
        Fetches all of the shipments for a given move id
        """
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        move = self.get_stored(MOVE_TASK_ORDER, object_id)
        if move is None:
            logger.info("Skipping get shipments no moves are stored yet")
            return

        headers = {"content-type": "application/json"}
        resp = self.client.get(
            ghc_path(f"/move_task_orders/{move['id']}/mto_shipments"),
            name=ghc_path("/move_task_orders/{moveId}/mto_shipments"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        shipments, success = check_response(resp, "listMTOShipments")
        if success:
            self.add_stored(MTO_SHIPMENT, shipments)


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
        if move is None:
            logger.info("Skipping get move none are stored yet")
            return

        headers = {"content-type": "application/json"}

        resp = self.client.get(
            ghc_path(f"/move/{move['locator']}"),
            name=ghc_path("/move/{locator}"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        new_mto, success = check_response(resp, "getMove")
        if success:
            self.add_stored(MOVE_TASK_ORDER, new_mto)
        return new_mto

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
        if success:
            self.add_stored(MOVE_TASK_ORDER, moves["queueMoves"])

    @tag(ORDER, "getOrder")
    @task
    def get_orders(self, overrides=None):
        """
        Fetches a single service member's orders
        """
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        move = self.get_stored(MOVE_TASK_ORDER, object_id)
        if move is None:
            logger.info("Skipping get orders no move is stored yet")
            return

        orders_id = move.get("ordersId")
        if orders_id is None:
            move = self.get_move({"id": move["id"]})

        headers = {"content-type": "application/json"}
        resp = self.client.get(
            ghc_path(f"/orders/{move['ordersId']}"),
            name=ghc_path("/orders/{ordersId}"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        order, success = check_response(resp, "getOrder")
        if success:
            self.add_stored(ORDER, order)

    @tag(MTO_SHIPMENT, "listMTOShipments")
    @task
    def get_shipments(self, overrides=None):
        """
        Fetches all of the shipments for a given move id
        """
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        move = self.get_stored(MOVE_TASK_ORDER, object_id)
        if move is None:
            logger.info("Skipping get shipments no moves are stored yet")
            return

        headers = {"content-type": "application/json"}
        resp = self.client.get(
            ghc_path(f"/move_task_orders/{move['id']}/mto_shipments"),
            name=ghc_path("/move_task_orders/{moveId}/mto_shipments"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        shipments, success = check_response(resp, "listMTOShipments")
        if success:
            self.add_stored(MTO_SHIPMENT, shipments)

    @tag(MTO_SERVICE_ITEM, "listMTOServiceItems")
    @task
    def get_service_items(self, overrides=None):
        """
        Fetches all of the mto service items for a given move id
        """
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        move = self.get_stored(MOVE_TASK_ORDER, object_id)
        if move is None:
            logger.info("Skipping get service items no moves are stored yet")
            return

        headers = {"content-type": "application/json"}
        resp = self.client.get(
            ghc_path(f"/move_task_orders/{move['id']}/mto_service_items"),
            name=ghc_path("/move_task_orders/{moveId}/mto_service_items"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        service_items, success = check_response(resp, "listMTOServiceItems")
        if success:
            self.add_stored(MTO_SERVICE_ITEM, service_items)
