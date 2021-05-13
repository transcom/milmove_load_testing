# -*- coding: utf-8 -*-
""" TaskSets and tasks for the MilMove interface. """
import logging
import json
import random
from typing import Dict

from locust import tag, task

from utils.constants import (
    ZERO_UUID,
    SERVICE_MEMBER,
    MOVE_TASK_ORDER,
    MTO_SHIPMENT,
)
from .base import check_response, LoginTaskSet, ParserTaskMixin

logger = logging.getLogger(__name__)


def local_path(url: str) -> str:
    return f"/internal/v1{url}"


def support_path(url: str) -> str:
    return f"/support/v1{url}"


class MilMoveDataStorageMixin:
    """
    TaskSet mixin used to store data from the Internal API during load testing so that it can be passed around and reused.
    We store a number of objects in a local store that can be requested by tasks.
    The tasks then hit an endpoint and call add or replace to update our local store with a list of viable objects.
    This mixin allows storing multiple items of each kind.
    """

    DATA_LIST_MAX: int = 50
    # contains the ID values needed when creating moves using createMoveTaskOrder:
    default_mto_ids: Dict[str, str] = {
        "contractorID": "",
        "destinationDutyStationID": "",
        "originDutyStationID": "",
        "uploadedOrdersID": "",
    }
    local_store: Dict[str, list] = {
        MOVE_TASK_ORDER: [],
        MTO_SHIPMENT: [],
        SERVICE_MEMBER: [],
    }  # data stored will be shared among class instances thanks to mutable dict

    def get_stored(self, object_key, *args, **kwargs):
        """
        Given an object_key that represents an object type from the MilMove app, returns an object of that type from the
        list.

        :param object_key: str in [MOVE_TASK_ORDER, MTO_SHIPMENT, MTO_AGENT, MTO_SERVICE_ITEM, PAYMENT_REQUEST]
        """
        data_list = self.local_store[object_key]

        if len(data_list) > 0:  # otherwise we return None
            return random.choice(data_list)

    def get_stored_shipment_address(self, mto_shipment=None):
        """
        Grabs one of either pickupAddress or destinationAddress from a shipment and returns the specific field and
        payload for that address.

        :param mto_shipment: JSON/dict of a specific MTO Shipment payload (optional)
        :return: tuple(str name of the address field, dict address payload)
        """
        if not mto_shipment:
            mto_shipment = self.get_stored(MTO_SHIPMENT) or {}

        address_fields = ["pickupAddress", "destinationAddress"]
        valid_addresses = [
            (field, mto_shipment[field])
            for field in address_fields
            if mto_shipment.get(field) and mto_shipment[field].get("id", ZERO_UUID) != ZERO_UUID
        ]

        if len(valid_addresses) > 0:  # otherwise we return None
            return random.choice(valid_addresses)

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
            num_to_delete = random.randint(1, self.DATA_LIST_MAX)
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

    def set_default_mto_ids(self, moves):
        """
        Given a list of Move Task Orders, gets the four ID values needed to create more MTOs:
          - contractorID
          - uploadedOrdersID
          - destinationDutyStationID
          - originDutyStationID

        To get these values, this function hits the getMoveTaskOrder endpoint in the Support API to get all of the
        details on an MTO. The Prime API doesn't have access to all of this info, which is why we need to use the
        Support API instead. It will go through and hit this endpoint for all of the moves in the list until it finally
        gets a complete set of IDs.

        CAN ONLY be used when subclassed with TaskSet and CertTaskMixin.

        :param moves: list of JSON/dict objects
        :return: None
        """
        # Checks that we have a full set of MTO IDs already and halts processing if so:
        if self.has_all_default_mto_ids():
            return

        headers = {"content-type": "application/json"}
        for move in moves:
            # Call the Support API to get full details on the move:
            resp = self.client.get(
                support_path(f"/move-task-orders/{move['id']}"),
                name=support_path("/move-task-orders/{moveTaskOrderID}"),
                headers=headers,
                **self.cert_kwargs,
            )
            move_details, success = check_response(resp, "getMoveTaskOrder")

            if not success:
                continue  # try again with the next move in the list

            # Get the values we need from the move and set them in self.default_move_ids.
            # If this move is missing any of these values, we default to using whatever value is already in
            # self.default_mto_ids, which could be nothing, or could be a value gotten from a previous move.
            # This way we never override good ID values from earlier moves in the list.
            self.default_mto_ids["contractorID"] = move_details.get(
                "contractorID", self.default_mto_ids["contractorID"]
            )
            if order_details := move_details.get("order"):
                self.default_mto_ids["uploadedOrdersID"] = order_details.get(
                    "uploadedOrdersID", self.default_mto_ids["uploadedOrdersID"]
                )
                self.default_mto_ids["destinationDutyStationID"] = order_details.get(
                    "destinationDutyStationID", self.default_mto_ids["destinationDutyStationID"]
                )
                self.default_mto_ids["originDutyStationID"] = order_details.get(
                    "originDutyStationID", self.default_mto_ids["originDutyStationID"]
                )

            # Do we have all the ID values we need? Cool, then stop processing.
            if self.has_all_default_mto_ids():
                logger.info(f"☑️ Set default MTO IDs for createMoveTaskOrder: \n{self.default_mto_ids}")
                break

        # If we're in the local environment, and we have gone through the entire list without getting a full set of IDs,
        # set our hardcoded IDs as the default:
        if not self.has_all_default_mto_ids() and self.user.is_local:
            logger.warning("⚠️ Using hardcoded MTO IDs for LOCAL env")
            self.default_mto_ids.update(
                {
                    "contractorID": "5db13bb4-6d29-4bdb-bc81-262f4513ecf6",
                    "destinationDutyStationID": "71b2cafd-7396-4265-8225-ff82be863e01",
                    "originDutyStationID": "1347d7f3-2f9a-44df-b3a5-63941dd55b34",
                    "uploadedOrdersID": "c26421b0-e4c3-446b-88f3-493bb25c1756",
                }
            )

    def has_all_default_mto_ids(self) -> bool:
        """ Boolean indicating that we have all the values we need for creating new MTOs. """
        return self.default_mto_ids and all(self.default_mto_ids.values())


@tag("milmove")
class MilMoveTasks(MilMoveDataStorageMixin, ParserTaskMixin, LoginTaskSet):
    """
    Set of tasks that can be called for the MilMove interface.
    """

    def on_start(self):
        """
        Creates a login right at the start of the TaskSet and stops task execution if the login fails.
        """
        super().on_start()  # sets the csrf token

        resp = self._create_login(user_type="milmove", session_token_name="mil_session_token")
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

    @tag(SERVICE_MEMBER, "createServiceMember")
    @task
    def create_service_member(self):
        """
        Creates service member for a logged-in user
        """

        payload = {
            "affiliation": "AIR_FORCE",
            "created_at": "2021-05-12T15:50:13.576Z",
            "edipi": "1111111111",
            "id": "f4b3f7c9-832b-4a59-8ba3-f0ae28717767",
            "is_profile_complete": False,
            "orders": [],
            "rank": "E_6",
            "requires_access_code": False,
            "updated_at": "2021-05-12T15:50:45.270Z",
            "user_id": "f146fc04-604b-409d-aa90-678c8afb84e6",
            "weight_allotment": {
                "pro_gear_weight": 2000,
                "pro_gear_weight_spouse": 500,
                "total_weight_self": 8000,
                "total_weight_self_plus_dependents": 11000,
            },
        }

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            local_path("/service_members"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        service_member, success = check_response(resp, "createServiceMember", payload)

        if not success:
            return  # no point continuing if it didn't work out

        if success:
            self.add_stored(SERVICE_MEMBER, service_member)
            return service_member
