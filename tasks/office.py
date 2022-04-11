# -*- coding: utf-8 -*-
""" TaskSets and tasks for the Office interface. """
import json
import logging
import random
from http import HTTPStatus
from typing import Dict, Set

from locust import tag, task

from utils.auth import UserType, create_user
from utils.constants import (
    CUSTOMER,
    MOVE,
    MOVE_TASK_ORDER,
    MTO_SERVICE_ITEM,
    MTO_SHIPMENT,
    ORDER,
    PAYMENT_REQUEST,
    QUEUES,
)
from utils.parsers import APIKey, get_api_fake_data_generator
from utils.request import log_response_failure, log_response_info
from utils.rest import RestResponseContextManager
from utils.task import RestTaskSet
from utils.types import JSONObject


logger = logging.getLogger(__name__)
fake_data_generator = get_api_fake_data_generator()


class OfficeDataStorageMixin:
    """
    TaskSet mixin used to store data from the GHC API during load testing so that it can be passed around and reused.
    We store a number of objects in a local store that can be requested by tasks.
    The tasks then hit an endpoint and call add or replace to update our local store with a list of viable objects.
    This mixin allows storing multiple items of each kind.
    """

    DATA_LIST_MAX: int = 100
    default_mto_ids: Dict[str, Set] = {
        "destinationDutyLocationID": set(),
        "originDutyLocationID": set(),
    }
    local_store: Dict[str, Dict[str, Dict]] = {
        CUSTOMER: {},
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
            num_to_delete = random.randint(1, len(data_dict) - 1)
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


class ServicesCounselorTasks(OfficeDataStorageMixin, RestTaskSet):
    """
    Set of tasks that can be called for the MilMove Office interface with the Services Counselor role.
    """

    def on_start(self):
        """
        Creates a login right at the start of the TaskSet and stops task execution if the login fails.
        """
        success = create_user(
            request_preparer=self.request_preparer, session=self.client, user_type=UserType.SERVICE_COUNSELOR
        )

        if not success:
            logger.error("Failed to create a user")
            self.interrupt()

    @task
    def get_user_info(self):
        """
        Gets the user info for the currently logged in user.
        """
        url, request_kwargs = self.request_preparer.prep_internal_request(
            endpoint="/internal/users/logged_in", include_prefix=False
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            logger.info(f"ℹ️ User email: {resp.js.get('email', 'None')}")

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

        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/move/{move['locator']}",
            endpoint_name="/move/{locator}",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                new_mto = resp.js

                self.add_stored(MOVE_TASK_ORDER, new_mto)

                return new_mto

            resp.failure("Unable to get move.")

            log_response_failure(response=resp)

    @tag(QUEUES, "getServicesCounselingQueue")
    @task
    def get_moves_queue(self, overrides=None):
        """
        Fetches a list of paginated moves
        """
        # Use the default queue sort for now, adding a filter to return service counseling completed
        # moves as well
        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint="/queues/counseling?page=1&perPage=50&sort=submittedAt&order=asc&status=NEEDS SERVICE COUNSELING,SERVICE COUNSELING COMPLETED",
            endpoint_name="/queues/counseling",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                moves: JSONObject = resp.js

                # these are not full move models and will be those in needs counseling status
                self.add_stored(MOVE_TASK_ORDER, moves["queueMoves"])
            else:
                resp.failure("Unable to get moves queue.")

                log_response_failure(response=resp)

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

        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/orders/{move['ordersId']}",
            endpoint_name="/orders/{orderId}",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                self.add_stored(ORDER, resp.js)
            else:
                resp.failure("Unable to get orders.")

                log_response_failure(response=resp)

    @tag(CUSTOMER, "getCustomer")
    @task
    def get_customer(self, overrides=None):
        """
        Fetches a single service member's orders
        """
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        order = self.get_stored(ORDER, object_id)
        if order is None:
            logger.info("Skipping get customer no order is stored yet")
            return

        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/customer/{order['customerID']}",
            endpoint_name="/customer/{customerId}",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                self.add_stored(CUSTOMER, resp.js)
            else:
                resp.failure("Unable to get customer.")

                log_response_failure(response=resp)

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

        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/move_task_orders/{move['id']}/mto_shipments",
            endpoint_name="/move_task_orders/{moveId}/mto_shipments",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                self.add_stored(MTO_SHIPMENT, resp.js)
            else:
                resp.failure("Unable to get shipments.")

                log_response_failure(response=resp)

    @tag(ORDER, "updateOrder")
    @task
    def update_orders(self, overrides=None):
        """
        Updates an existing order of a move as a Services Counselor.
        :return:
        """
        object_id = overrides.get("id") if overrides else None
        order = self.get_stored(ORDER, object_id)
        order = self.get_orders() if order is None else order
        if order is None:
            logger.info("skipping update order, no moves exist yet")
            return

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.OFFICE,
            path="/counseling/orders/{orderID}",
            method="patch",
        )

        payload = {key: payload[key] for key in ["issueDate", "reportByDate", "ordersType"]}
        if self.default_mto_ids.get("originDutyLocationID"):
            payload["originDutyLocationId"] = random.choice(list(self.default_mto_ids["originDutyLocationID"]))
        else:
            payload["originDutyLocationId"] = order["originDutyLocation"]["id"]

        if self.default_mto_ids.get("destinationDutyLocationID"):
            payload["newDutyLocationId"] = random.choice(list(self.default_mto_ids["destinationDutyLocationID"]))
        else:
            payload["newDutyLocationId"] = order["destinationDutyLocation"]["id"]

        # The request may result in validation errors if the underlying move is no longer in needs counseling status
        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/counseling/orders/{order['id']}",
            endpoint_name="/counseling/orders/{orderId}",
        )

        request_kwargs["headers"]["If-Match"] = order["eTag"]

        with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                self.add_stored(ORDER, resp.js)
            else:
                resp.failure("Unable to update orders.")

                log_response_failure(response=resp)

    @tag(ORDER, "updateAllowance")
    @task
    def update_allowance(self, overrides=None):
        """
        Updates the existing entitlements of an order as a Services Counselor.
        :return:
        """
        object_id = overrides.get("id") if overrides else None
        order = self.get_stored(ORDER, object_id)
        order = self.get_orders() if order is None else order
        if order is None:
            logger.info("skipping update allowance, no moves exist yet")
            return

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.OFFICE,
            path="/counseling/orders/{orderID}/allowances",
            method="patch",
        )

        # update allowances handler expects the orders eTag because it also updates parents order fields
        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/counseling/orders/{order['id']}/allowances",
            endpoint_name="/counseling/orders/{orderId}/allowances",
        )

        request_kwargs["headers"]["If-Match"] = order["eTag"]

        with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                new_order = resp.js

                self.add_stored(ORDER, new_order)

                self.add_stored(CUSTOMER, new_order["customer"])
            else:
                resp.failure("Unable to update allowance.")

                log_response_failure(response=resp)

    @tag(CUSTOMER, "updateCustomer")
    @task
    def update_customer(self, overrides=None):
        """
        Updates the existing service member of an order as a Services Counselor.
        :return:
        """
        object_id = overrides.get("id") if overrides else None
        customer = self.get_stored(CUSTOMER, object_id) or self.get_customer()
        if customer is None:
            logger.info("skipping update customer, no orders exist yet")
            return

        if not customer.get("current_address"):
            logger.info("Skipping update customer as no current address exists")
            return

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.OFFICE,
            path="/customer/{customerID}",
            method="patch",
            overrides={"current_address": {"id": customer["current_address"]["id"]}},
            require_all=True,
        )

        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/customer/{customer['id']}",
            endpoint_name="/customer/{customerID}",
        )

        request_kwargs["headers"]["If-Match"] = customer["eTag"]

        with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                self.add_stored(CUSTOMER, resp.js)
            else:
                resp.failure("Unable to update customer.")

                log_response_failure(response=resp)


class TOOTasks(OfficeDataStorageMixin, RestTaskSet):
    """
    Set of tasks that can be called for the MilMove Office interface with the TOO role.
    """

    def on_start(self):
        """
        Creates a login right at the start of the TaskSet and stops task execution if the login fails.
        """
        success = create_user(request_preparer=self.request_preparer, session=self.client, user_type=UserType.TOO)

        if not success:
            logger.error("Failed to create a user")
            self.interrupt()

    @task
    def get_user_info(self):
        """
        Gets the user info for the currently logged in user.
        """
        url, request_kwargs = self.request_preparer.prep_internal_request(
            endpoint="/internal/users/logged_in", include_prefix=False
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            logger.info(f"ℹ️ User email: {resp.js.get('email', 'None')}")

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

        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/move/{move['locator']}",
            endpoint_name="/move/{locator}",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                new_mto: JSONObject = resp.js

                self.add_stored(MOVE_TASK_ORDER, new_mto)

                return new_mto
            else:
                resp.failure("Unable to get move.")

                log_response_failure(response=resp)

    @tag(QUEUES, "getMovesQueue")
    @task
    def get_moves_queue(self, overrides=None):
        """
        Fetches a list of paginated moves
        """
        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint="/queues/moves?page=1&perPage=50&sort=status&order=asc",
            endpoint_name="/queues/moves",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                moves: JSONObject = resp.js

                self.add_stored(MOVE_TASK_ORDER, moves["queueMoves"])

                # destination duty locations don't have to be in the office user's GBLOC
                destination_duty_location_ids = [move["destinationDutyLocation"]["id"] for move in moves["queueMoves"]]

                self.default_mto_ids["destinationDutyLocationID"].update(destination_duty_location_ids)
            else:
                resp.failure("Unable to get moves queue.")

                log_response_failure(response=resp)

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

        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/orders/{move['ordersId']}",
            endpoint_name="/orders/{orderId}",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                order: JSONObject = resp.js

                self.add_stored(ORDER, order)

                # the origin duty location is not in the queue response and we can't use the destination
                # because they could be outside of the office user's GBLOC
                self.default_mto_ids["originDutyLocationID"].add(order["originDutyLocation"]["id"])
            else:
                resp.failure("Unable to get orders.")

                log_response_failure(response=resp)

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

        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/move_task_orders/{move['id']}/mto_shipments",
            endpoint_name="/move_task_orders/{moveId}/mto_shipments",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                self.add_stored(MTO_SHIPMENT, resp.js)
            else:
                resp.failure("Unable to get shipments.")

                log_response_failure(response=resp)

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

        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/move_task_orders/{move['id']}/mto_service_items",
            endpoint_name="/move_task_orders/{moveId}/mto_service_items",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                self.add_stored(MTO_SERVICE_ITEM, resp.js)
            else:
                resp.failure("Unable to get service items.")

                log_response_failure(response=resp)

    @tag(CUSTOMER, "getCustomer")
    @task
    def get_customer(self, overrides=None):
        """
        Fetches a single service member's orders
        """
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        order = self.get_stored(ORDER, object_id)
        if order is None:
            logger.info("Skipping get customer no order is stored yet")
            return

        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/customer/{order['customerID']}",
            endpoint_name="/customer/{customerId}",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                self.add_stored(CUSTOMER, resp.js)
            else:
                resp.failure("Unable get customer.")

                log_response_failure(response=resp)

    @tag(ORDER, "updateOrder")
    @task
    def update_orders(self, overrides=None):
        """
        Updates an existing order of a move as a TOO
        :return:
        """
        object_id = overrides.get("id") if overrides else None
        order = self.get_stored(ORDER, object_id)
        order = self.get_orders() if order is None else order
        if order is None:
            logger.info("skipping update order, no moves exist yet")
            return

        move = self.get_stored(MOVE_TASK_ORDER, order["moveTaskOrderID"])
        if move and move["status"] == "NEEDS SERVICE COUNSELING":
            logger.info("Skipping update orders as TOO, move is still in services counseling")
            return

        # require all optional fields otherwise nullable fields will be omitted
        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.OFFICE,
            path="/orders/{orderID}",
            method="patch",
            require_all=True,
        )

        if self.default_mto_ids.get("originDutyLocationID"):
            payload["originDutyLocationId"] = random.choice(list(self.default_mto_ids["originDutyLocationID"]))
        else:
            payload["originDutyLocationId"] = order["originDutyLocation"]["id"]

        if self.default_mto_ids.get("destinationDutyLocationID"):
            payload["newDutyLocationId"] = random.choice(list(self.default_mto_ids["destinationDutyLocationID"]))
        else:
            payload["newDutyLocationId"] = order["destinationDutyLocation"]["id"]

        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/orders/{order['id']}",
            endpoint_name="/orders/{orderId}",
        )

        request_kwargs["headers"]["If-Match"] = order["eTag"]

        with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                new_order: JSONObject = resp.js

                self.add_stored(ORDER, new_order)
                self.add_stored(CUSTOMER, new_order["customer"])
            else:
                resp.failure("Unable to update orders.")

                log_response_failure(response=resp)

    @tag(ORDER, "updateAllowance")
    @task
    def update_allowance(self, overrides=None):
        """
        Updates the existing entitlements of an order as a TOO
        :return:
        """
        object_id = overrides.get("id") if overrides else None
        order = self.get_stored(ORDER, object_id)
        order = self.get_orders() if order is None else order
        if order is None:
            logger.info("skipping update allowance, no moves exist yet")
            return

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.OFFICE,
            path="/orders/{orderID}/allowances",
            method="patch",
        )

        # update allowances handler expects the orders eTag because it also updates parents order fields
        url, request_kwargs = self.request_preparer.prep_ghc_request(
            endpoint=f"/orders/{order['id']}/allowances",
            endpoint_name="/orders/{orderId}/allowances",
        )

        request_kwargs["headers"]["If-Match"] = order["eTag"]

        with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                new_order: JSONObject = resp.js

                self.add_stored(ORDER, new_order)

                self.add_stored(CUSTOMER, new_order["customer"])
            else:
                resp.failure("Unable to update allowance.")

                log_response_failure(response=resp)
