# -*- coding: utf-8 -*-
""" TaskSets and tasks for the Prime & Support APIs """
import json
import logging
import random
from copy import deepcopy
from datetime import datetime
from http import HTTPStatus
from typing import Dict, Union

from locust import tag, task

from utils.auth import UserType, create_user
from utils.base import is_local
from utils.constants import (
    MOVE_TASK_ORDER,
    MTO_AGENT,
    MTO_SERVICE_ITEM,
    MTO_SHIPMENT,
    PAYMENT_REQUEST,
    TEST_PDF,
    ZERO_UUID,
)
from utils.parsers import APIKey, get_api_fake_data_generator
from utils.request import log_response_failure, log_response_info
from utils.rest import RestResponseContextManager, parse_response_json
from utils.task import RestTaskSet
from utils.types import JSONArray, JSONObject


logger = logging.getLogger(__name__)
fake_data_generator = get_api_fake_data_generator()


class PrimeDataStorageMixin:
    """
    TaskSet mixin used to store data from the Prime API during load testing so that it can be passed around and reused.
    We store a number of objects in a local store that can be requested by tasks.
    The tasks then hit an endpoint and call add or replace to update our local store with a list of viable objects.
    This mixin allows storing multiple items of each kind.
    """

    DATA_LIST_MAX: int = 50
    # contains the ID values needed when creating moves using createMoveTaskOrder:
    default_mto_ids: Dict[str, str] = {
        "contractorID": "",
        "destinationDutyLocationID": "",
        "originDutyLocationID": "",
        "uploadedOrdersID": "",
    }
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

    def set_default_mto_ids(self: Union[RestTaskSet, "PrimeDataStorageMixin"], move_id: str):
        """
        Given a list of Move Task Orders, gets the four ID values needed to create more MTOs:
          - contractorID
          - uploadedOrdersID
          - destinationDutyLocationID
          - originDutyLocationID

        To get these values, this function hits the getMoveTaskOrder endpoint in the Support API to get all of the
        details on an MTO. The Prime API doesn't have access to all of this info, which is why we need to use the
        Support API instead. It will go through and hit this endpoint for all of the moves in the list until it finally
        gets a complete set of IDs.

        CAN ONLY be used when subclassed with RestTaskSet.

        :param move_id: Move UUID
        :return: None
        """
        # Checks that we have a full set of MTO IDs already and halts processing if so:
        if self.has_all_default_mto_ids():
            return

        # Call the Support API to get full details on the move:
        url, request_kwargs = self.request_preparer.prep_support_request(
            endpoint=f"/move-task-orders/{move_id}", endpoint_name="/move-task-orders/{moveTaskOrderID}"
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            move_details: JSONObject = resp.js

        # Get the values we need from the move and set them in self.default_move_ids.
        # If this move is missing any of these values, we default to using whatever value is already in
        # self.default_mto_ids, which could be nothing, or could be a value gotten from a previous move.
        # This way we never override good ID values from earlier moves in the list.
        self.default_mto_ids["contractorID"] = move_details.get("contractorID", self.default_mto_ids["contractorID"])
        if order_details := move_details.get("order"):
            self.default_mto_ids["uploadedOrdersID"] = order_details.get(
                "uploadedOrdersID", self.default_mto_ids["uploadedOrdersID"]
            )
            self.default_mto_ids["destinationDutyLocationID"] = order_details.get(
                "destinationDutyLocationID", self.default_mto_ids["destinationDutyLocationID"]
            )
            self.default_mto_ids["originDutyLocationID"] = order_details.get(
                "originDutyLocationID", self.default_mto_ids["originDutyLocationID"]
            )

    def has_all_default_mto_ids(self) -> bool:
        """Boolean indicating that we have all the values we need for creating new MTOs."""
        return self.default_mto_ids and all(self.default_mto_ids.values())


@tag("prime")
class PrimeTasks(PrimeDataStorageMixin, RestTaskSet):
    """
    Set of the tasks that can be called on the Prime API. Make sure to mark tasks with the `@task` decorator and add
    tags where appropriate to make filtering for custom tests easier.
    """

    def on_start(self) -> None:
        """
        Set up data we'll need for the load tests.
        """
        # Customer login using dev local
        success = create_user(request_preparer=self.request_preparer, session=self.client, user_type=UserType.MILMOVE)

        if not success:
            logger.error("Failed to create a user")
            self.interrupt()

        url, request_kwargs = self.request_preparer.prep_internal_request(endpoint="/users/logged_in")

        logged_in_user_resp = self.client.get(url=url, **request_kwargs)
        logged_in_user, error_msg = parse_response_json(response=logged_in_user_resp)

        if error_msg:
            logger.error(error_msg)
            self.interrupt()

        service_member_id = logged_in_user["service_member"]["id"]
        email = logged_in_user["email"]
        user_id = logged_in_user["id"]

        # Setup customer profile
        url, request_kwargs = self.request_preparer.prep_internal_request(
            endpoint="/duty_locations?search=white%20sands"
        )

        resp = self.client.get(url=url, **request_kwargs)

        duty_locations, error_msg = parse_response_json(response=resp)
        duty_locations: JSONArray

        if error_msg:
            logger.error(error_msg)
            self.interrupt()

        overrides = {
            "id": service_member_id,
            "user_id": user_id,
            "edipi": "9999999999",
            "personal_email": email,
            "email_is_preferred": True,
            "current_station_id": duty_locations[0]["id"],
        }

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.INTERNAL,
            path="/service_members/{serviceMemberId}",
            method="patch",
            overrides=overrides,
            require_all=True,
        )

        url, request_kwargs = self.request_preparer.prep_internal_request(
            endpoint=f"/service_members/{service_member_id}", endpoint_name="/service_members/{serviceMemberId}"
        )

        service_member_resp = self.client.patch(url=url, data=json.dumps(payload), **request_kwargs)

        service_member, error_msg = parse_response_json(response=service_member_resp)
        service_member: JSONObject

        if error_msg:
            logger.error(error_msg)
            self.interrupt()

        overrides = {"permission": "NONE"}

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.INTERNAL,
            path="/service_members/{serviceMemberId}/backup_contacts",
            method="post",
            overrides=overrides,
        )

        url, request_kwargs = self.request_preparer.prep_internal_request(
            endpoint=f"/service_members/{service_member_id}/backup_contacts",
            endpoint_name="/service_members/{serviceMemberId}/backup_contacts",
        )

        self.client.post(url=url, data=json.dumps(payload), **request_kwargs)

        # Setup customer order
        overrides = {
            "service_member_id": service_member_id,
            "issue_date": datetime.now().strftime("%Y-%m-%d"),
            "report_by_date": datetime.now().strftime("%Y-%m-%d"),
            "orders_type": "PERMANENT_CHANGE_OF_STATION",
            "has_dependents": False,
            "spouse_has_pro_gear": False,
            "new_duty_station_id": duty_locations[1]["id"],
            "orders_number": None,
            "tac": None,
            "sac": None,
            "department_indicator": None,
        }

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.INTERNAL,
            path="/orders",
            method="post",
            overrides=overrides,
            require_all=True,
        )

        url, request_kwargs = self.request_preparer.prep_internal_request(endpoint="/orders")

        order_resp = self.client.post(url=url, data=json.dumps(payload), **request_kwargs)

        order, error_msg = parse_response_json(response=order_resp)
        order: JSONObject

        if error_msg:
            logger.error(error_msg)
            self.interrupt()

        document_id = order["uploaded_orders"]["id"]
        upload_file = {"file": open(TEST_PDF, "rb")}

        url, request_kwargs = self.request_preparer.prep_internal_request(
            endpoint=f"/uploads?documentId={document_id}",
            endpoint_name="/uploads",
        )

        request_kwargs.pop("headers")  # Don't want the JSON headers for this one

        self.client.post(url=url, files=upload_file, **request_kwargs)

        # Setup customer shipment
        move_id = order["moves"][0]["id"]

        url, request_kwargs = self.request_preparer.prep_internal_request(
            endpoint=f"/moves/{move_id}", endpoint_name="/moves/{moveId}"
        )

        self.client.patch(url=url, data=json.dumps({"selected_move_type": "HHG"}), **request_kwargs)

        address: JSONObject = service_member["residential_address"]
        address.pop("id")  # remove unneeded id
        overrides = {
            "moveTaskOrderID": move_id,
            "shipmentType": "HHG",
            "pickupAddress": address,
            "agents": [],
        }

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.INTERNAL,
            path="/mto_shipments",
            method="post",
            overrides=overrides,
            require_all=True,
        )

        url, request_kwargs = self.request_preparer.prep_internal_request(endpoint="/mto_shipments")

        self.client.post(url=url, data=json.dumps(payload), **request_kwargs)

        # Confirm move request
        full_name = f"{service_member['first_name']} {service_member['last_name']}"
        overrides = {
            "certification_type": "SHIPMENT",
            "signature": full_name,
            "date": datetime.now().strftime(
                "%Y-%m-%dT%H:%M:%S-05:00"
            ),  # needed because yaml uses date instead of date-time
            "personally_procured_move_id": None,
        }

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.INTERNAL,
            path="/moves/{moveId}/submit",
            method="post",
            overrides=overrides,
            require_all=True,
        )

        url, request_kwargs = self.request_preparer.prep_internal_request(
            endpoint=f"/moves/{move_id}/submit", endpoint_name="/moves/{moveId}/submit"
        )

        self.client.post(url=url, data=json.dumps(payload), **request_kwargs)

        # Set local variables with needed info to create a move
        self.set_default_mto_ids(move_id)

    @tag(MOVE_TASK_ORDER, "getMoves")
    @task(2)
    def get_moves(self) -> None:
        """
        Retrieves moves available to the Prime
        """
        url, request_kwargs = self.request_preparer.prep_prime_request(endpoint="/moves")

        if is_local(env=self.env):
            request_kwargs["timeout"] = 15  # set a timeout of 15sec if we're running locally for this endpoint

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code != HTTPStatus.OK:
                resp.failure("Unable to get moves available to prime.")

                log_response_failure(response=resp)

                return

    @tag(MTO_SERVICE_ITEM, "createMTOServiceItem")
    @task
    def create_mto_service_item(self, overrides=None):
        # If mtoShipmentID was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("mtoShipmentID") if overrides else None
        mto_shipment = self.get_stored(MTO_SHIPMENT, object_id)
        if not mto_shipment:
            logger.debug("createMTOServiceItem: ⚠️ No mto_shipment found")
            return None

        overrides_local = {
            # override moveTaskOrderID because we don't want a random one
            "moveTaskOrderID": mto_shipment["moveTaskOrderID"],
            # override mtoShipmentID because we don't want a random one
            "mtoShipmentID": mto_shipment["id"],
        }
        # Merge local overrides with passed-in overrides
        overrides_local.update(overrides or {})

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.PRIME,
            path="/mto-service-items",
            method="post",
            overrides=overrides_local,
        )

        url, request_kwargs = self.request_preparer.prep_prime_request(endpoint="/mto-service-items")

        with self.rest(method="POST", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            task_name = f"create_mto_service_item {payload['reServiceCode']}"

            log_response_info(response=resp, task_name=task_name)

            if resp.status_code == HTTPStatus.OK:
                mto_service_items = resp.js

                self.add_stored(MTO_SERVICE_ITEM, mto_service_items)

                return mto_service_items

            resp.failure("Unable to create MTO service item.")

            log_response_failure(response=resp, task_name=task_name)

    @tag(MTO_SHIPMENT, "createMTOShipment")
    @task
    def create_mto_shipment(self, overrides=None):
        def guarantee_unique_agent_type(agents):
            agent_types = {agent["agentType"] for agent in agents}
            if len(agents) >= 2 and len(agent_types) < 2:
                possible_types = {"RELEASING_AGENT", "RECEIVING_AGENT"}
                agents[1]["agentType"] = (possible_types - agent_types).pop()

        # If moveTaskOrderID was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("moveTaskOrderID") if overrides else None

        move_task_order = self.get_stored(MOVE_TASK_ORDER, object_id)
        if not move_task_order:
            logger.debug("createMTOShipment: ⚠️ No move_task_order found")
            return (
                None  # we can't do anything else without a default value, and no pre-made MTOs satisfy our requirements
            )

        overrides_local = {
            # Override moveTaskorderID because we don't want a random one
            "moveTaskOrderID": move_task_order["id"],
            # Set agents UUIDs to ZERO_UUID because we can't actually set the UUID on creation
            "agents": {"id": ZERO_UUID, "mtoShipmentID": ZERO_UUID},
            # Set pickupAddress to ZERO_UUID because we can't actually set the UUID on creation
            "pickupAddress": {"id": ZERO_UUID},
            # Set destinationAddress to ZERO_UUID because we can't actually set the UUID on creation
            "destinationAddress": {"id": ZERO_UUID},
            # Set mtoServiceItems to empty to let the createMTOServiceItems endpoint do the creation
            "mtoServiceItems": [],
        }
        # Merge local overrides with passed-in overrides
        if overrides:
            overrides_local.update(overrides)

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.PRIME,
            path="/mto-shipments",
            method="post",
            overrides=overrides_local,
        )

        guarantee_unique_agent_type(payload["agents"])  # modifies the payload directly

        url, request_kwargs = self.request_preparer.prep_prime_request(endpoint="/mto-shipments")

        with self.rest(method="POST", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                mto_shipment = resp.js

                self.add_stored(MTO_SHIPMENT, mto_shipment)

                return mto_shipment

            resp.failure("Unable to create MTO shipment.")

            log_response_failure(response=resp)

    @tag(MTO_SHIPMENT, "createMTOShipment", "expectedFailure")
    @task
    def create_mto_shipment_with_duplicate_agents(self, overrides=None):
        # If moveTaskOrderID was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("moveTaskOrderID") if overrides else None

        move_task_order = self.get_stored(MOVE_TASK_ORDER, object_id)
        if not move_task_order:
            logger.debug("createMTOShipment — expected failure: ⚠️ No move_task_order found")
            return (
                None  # we can't do anything else without a default value, and no pre-made MTOs satisfy our requirements
            )

        agent_type = random.choice(["RELEASING_AGENT", "RECEIVING_AGENT"])
        agent_override = {"id": ZERO_UUID, "mtoShipmentID": ZERO_UUID, "agentType": agent_type}
        overrides_local = {
            # Override moveTaskorderID because we don't want a random one
            "moveTaskOrderID": move_task_order["id"],
            # Set agents UUIDs to ZERO_UUID because we can't actually set the UUID on creation and guarantee two agents
            "agents": [agent_override, agent_override],
            # Set pickupAddress to ZERO_UUID because we can't actually set the UUID on creation
            "pickupAddress": {"id": ZERO_UUID},
            # Set destinationAddress to ZERO_UUID because we can't actually set the UUID on creation
            "destinationAddress": {"id": ZERO_UUID},
            # Set mtoServiceItems to empty to let the createMTOServiceItems endpoint do the creation
            "mtoServiceItems": [],
        }
        # Merge local overrides with passed-in overrides
        if overrides:
            overrides_local.update(overrides)

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.PRIME,
            path="/mto-shipments",
            method="post",
            overrides=overrides_local,
        )

        url, request_kwargs = self.request_preparer.prep_prime_request(
            endpoint="/mto-shipments", endpoint_name="/mto-shipments — expected failure"
        )

        with self.rest(method="POST", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                resp.success()
            else:
                resp.failure("Got an unexpected result for creating a shipment with duplicate agents.")

                log_response_failure(response=resp)

    @tag(PAYMENT_REQUEST, "createUpload")
    @task
    def create_upload(self, overrides=None):
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        payment_request = self.get_stored(PAYMENT_REQUEST, object_id)
        if not payment_request:
            return

        upload_file = {"file": open(TEST_PDF, "rb")}

        url, request_kwargs = self.request_preparer.prep_prime_request(
            endpoint=f"/payment-requests/{payment_request['id']}/uploads",
            endpoint_name="/payment-requests/{paymentRequestID}/uploads",
        )

        request_kwargs.pop("headers")  # don't want the JSON headers for this one

        with self.client.post(url=url, files=upload_file, catch_response=True, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code != HTTPStatus.CREATED:
                resp.failure("Unable to create an upload.")

                log_response_failure(response=resp)

    @tag(PAYMENT_REQUEST, "createPaymentRequest")
    @task
    def create_payment_request(self, overrides=None):
        # If mtoServiceItemID was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("mtoServiceItemID") if overrides else None
        service_item = self.get_stored(MTO_SERVICE_ITEM, object_id)
        if not service_item:
            return

        payload = {
            "moveTaskOrderID": service_item["moveTaskOrderID"],
            "serviceItems": [{"id": service_item["id"]}],
            "isFinal": False,
        }

        shipment = self.get_stored(MTO_SHIPMENT, service_item["mtoShipmentID"])
        if not shipment:
            logger.info("unable to find shipment of payment request service item")

        # if the actual weight hasn't been provided, creating the payment request will fail
        if not shipment.get("primeActualWeight"):
            url, request_kwargs = self.request_preparer.prep_prime_request(
                endpoint="/payment-requests", endpoint_name="/payment-requests — expected failure"
            )

            self.rest(method="POST", url=url, data=json.dumps(payload), **request_kwargs)

            return None

        url, request_kwargs = self.request_preparer.prep_prime_request(endpoint="/payment-requests")

        with self.rest(method="POST", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.CREATED:
                payment_request = resp.js

                self.add_stored(PAYMENT_REQUEST, payment_request)

                return payment_request

            resp.failure("Unable to create payment request.")

            log_response_failure(response=resp)

    @tag(MTO_SHIPMENT, "updateMTOShipment")
    @task
    def update_mto_shipment(self, overrides=None):
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        mto_shipment = self.get_stored(MTO_SHIPMENT, object_id)
        if not mto_shipment:
            return  # can't run this task

        payload: JSONObject = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.PRIME,
            path="/mto-shipments/{mtoShipmentID}",
            method="patch",
            overrides=overrides,
        )

        # Agents and addresses should not be updated by this endpoint, and primeEstimatedWeight cannot be updated after
        # it is initially set (and it is set in create_mto_shipment)
        fields_to_remove = [
            "agents",
            "pickupAddress",
            "destinationAddress",
            "secondaryPickupAddress",
            "secondaryDeliveryAddress",
            "primeEstimatedWeight",
        ]

        # nts weight is only valid when the shipment type is nts release
        if payload.get("ntsRecordedWeight"):
            shipmentType = payload.get("shipmentType") or mto_shipment.get("shipmentType")
            if shipmentType != "HHG_OUTOF_NTS_DOMESTIC":
                fields_to_remove.append("ntsRecordedWeight")

        for f in fields_to_remove:
            payload.pop(f, None)

        url, request_kwargs = self.request_preparer.prep_prime_request(
            endpoint=f"/mto-shipments/{mto_shipment['id']}",
            endpoint_name="/mto-shipments/{mtoShipmentID}",
        )

        request_kwargs["headers"]["If-Match"] = mto_shipment["eTag"]

        with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                new_mto_shipment = resp.js

                self.update_stored(MTO_SHIPMENT, mto_shipment, new_mto_shipment)

                return new_mto_shipment

            resp.failure("Unable to update MTO shipment.")

            log_response_failure(response=resp)

    @tag(MTO_SHIPMENT, "updateMTOShipmentAddress")
    @task
    def update_mto_shipment_address(self, overrides=None):
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        mto_shipment = self.get_stored(MTO_SHIPMENT, object_id)
        if not mto_shipment:
            return

        address_tuple = self.get_stored_shipment_address(mto_shipment)  # returns a (field_name, address_dict) tuple
        if not address_tuple:
            return  # this shipment didn't have any addresses, we will try again later with a different shipment

        field, address = address_tuple

        overrides_local = {"id": address["id"]}
        overrides_local.update(overrides or {})

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.PRIME,
            path="/mto-shipments/{mtoShipmentID}/addresses/{addressID}",
            method="put",
            overrides=overrides_local,
        )

        url, request_kwargs = self.request_preparer.prep_prime_request(
            endpoint=f"/mto-shipments/{mto_shipment['id']}/addresses/{address['id']}",
            endpoint_name="/mto-shipments/{mtoShipmentID}/addresses/{addressID}",
        )

        request_kwargs["headers"]["If-Match"] = address["eTag"]

        # update mto_shipment address
        with self.rest(method="PUT", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                # we only got the address, so we're gonna pop it back into the shipment to store
                updated_shipment = deepcopy(mto_shipment)

                updated_shipment[field] = resp.js

                self.update_stored(MTO_SHIPMENT, mto_shipment, updated_shipment)

                return updated_shipment

            resp.failure("Unable to update MTO shipment address.")

            log_response_failure(response=resp)

    @tag(MTO_AGENT, "updateMTOAgent")
    @task
    def update_mto_agent(self, overrides=None):
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("mtoShipmentID") if overrides else None
        mto_shipment = self.get_stored(MTO_SHIPMENT, object_id)

        if not mto_shipment:
            return  # can't run this task
        if mto_shipment.get("agents") is None:
            return  # can't update agents if there aren't any

        overrides = {}
        mto_agents = mto_shipment["agents"]
        mto_agent = mto_shipment["agents"][0]
        if len(mto_agents) >= 2:
            overrides = {"agentType": mto_agent["agentType"]}  # ensure agentType does not change

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.PRIME,
            path="/mto-shipments/{mtoShipmentID}/agents/{agentID}",
            method="put",
            overrides=overrides,
        )

        mto_agent = mto_shipment["agents"][0]

        url, request_kwargs = self.request_preparer.prep_prime_request(
            endpoint=f"/mto-shipments/{mto_shipment['id']}/agents/{mto_agent['id']}",
            endpoint_name="/mto-shipments/{mtoShipmentID}/agents/{agentID}",
        )

        request_kwargs["headers"]["If-Match"] = mto_agent["eTag"]

        with self.rest(method="PUT", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                # we only got the agent, so we're gonna pop it back into the shipment to store
                new_shipment = deepcopy(mto_shipment)
                new_shipment["agents"][0] = resp.js

                self.update_stored(MTO_SHIPMENT, mto_shipment, new_shipment)

                return new_shipment

            resp.failure("Unable to update MTO shipment agent.")

            log_response_failure(response=resp)

    @tag(MTO_SERVICE_ITEM, "updateMTOServiceItem")
    @task
    def update_mto_service_item(self, overrides=None):
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        mto_service_item = self.get_stored(MTO_SERVICE_ITEM, object_id)
        if not mto_service_item:
            return  # can't run this task

        try:
            re_service_code = mto_service_item["reServiceCode"]
        except KeyError:
            logger.error(f"⛔️ update_mto_service_item recvd mtoServiceItem without reServiceCode \n{mto_service_item}")
            return

        if re_service_code not in ["DDDSIT", "DOPSIT"]:
            logging.info(
                "update_mto_service_item recvd mtoServiceItem from store. Discarding because reServiceCode not in "
                "[DDDSIT, DOPSIT]"
            )
            return

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.PRIME,
            path="/mto-service-items/{mtoServiceItemID}",
            method="patch",
            overrides={
                "id": mto_service_item["id"],
                "sitDestinationFinalAddress": {
                    "id": mto_service_item["sitDestinationFinalAddress"]["id"]
                    if mto_service_item.get("sitDestinationFinalAddress")
                    and mto_service_item["sitDestinationFinalAddress"].get("id")
                    else ZERO_UUID,
                },
            },
        )

        url, request_kwargs = self.request_preparer.prep_prime_request(
            endpoint=f"/mto-service-items/{mto_service_item['id']}",
            endpoint_name="/mto-service-items/{mtoServiceItemID}",
        )

        request_kwargs["headers"]["If-Match"] = mto_service_item["eTag"]

        with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            task_name = f"update_mto_service_item {re_service_code}"

            log_response_info(response=resp, task_name=task_name)

            if resp.status_code == HTTPStatus.OK:
                self.update_stored(MTO_SERVICE_ITEM, mto_service_item, resp.js)

                return resp.js

            resp.failure("Unable to update MTO service item.")

            log_response_failure(response=resp, task_name=task_name)

    @tag(MOVE_TASK_ORDER, "updateMTOPostCounselingInformation")
    @task
    def update_post_counseling_information(self, overrides=None):
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        move_task_order = self.get_stored(MOVE_TASK_ORDER, object_id)
        if not move_task_order:
            logger.debug("updateMTOPostCounselingInformation: ⚠️ No move_task_order found")
            return  # we can't do anything else without a default value, and no pre-made MTOs satisfy our requirements

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.PRIME,
            path="/move-task-orders/{moveTaskOrderID}/post-counseling-info",
            method="patch",
        )

        move_task_order_id = move_task_order["id"]  # path parameter

        url, request_kwargs = self.request_preparer.prep_prime_request(
            endpoint=f"/move-task-orders/{move_task_order_id}/post-counseling-info",
            endpoint_name="/move-task-orders/{moveTaskOrderID}/post-counseling-info",
        )

        request_kwargs["headers"]["If-Match"] = move_task_order["eTag"]

        with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                new_mto = resp.js

                self.update_stored(MOVE_TASK_ORDER, move_task_order, new_mto)

                return new_mto

            resp.failure("Unable to post counseling information.")

            log_response_failure(response=resp)

    # You can add the expectedFailure tag so that they can all be run if needed.

    @tag(MTO_SHIPMENT, "updateMTOShipmentStatus", "expectedFailure")
    @task
    def update_mto_shipment_with_invalid_status(self) -> None:
        """
        Tries updating an MTO shipment to an invalid status.
        """
        # Need a move to work with first. We'll get a random move that is available to prime.
        url, request_kwargs = self.request_preparer.prep_prime_request(endpoint="/moves")

        if is_local(env=self.env):
            request_kwargs["timeout"] = 15  # set a timeout of 15sec if we're running locally for this endpoint

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                moves: JSONArray = resp.js
            else:
                resp.failure("Unable to get moves available to prime.")

                log_response_failure(response=resp)

                return

        move = random.choice(moves)

        # Now we need to retrieve the shipments for this move
        url, request_kwargs = self.request_preparer.prep_prime_request(
            endpoint=f"/move-task-orders/{move['id']}",
            endpoint_name="/move-task-orders/{moveID}",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                move: JSONObject = resp.js
            else:
                resp.failure("Unable to get the move.")

                log_response_failure(response=resp)

                return

        # Since we're going to try setting an invalid status that the shipments we recieved above
        # can't be in, we'll just grab a random one.
        mto_shipment = deepcopy(random.choice(move["mtoShipments"]))

        overrides = {"status": "DRAFT"}

        # Generate fake payload based on the endpoint's required fields
        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.PRIME,
            path="/mto-shipments/{mtoShipmentID}/status",
            method="patch",
            overrides=overrides,
        )

        # Note that we have an em dash plus "expected failure" to put these in a separate locust group
        # than the regular shipment status updates.
        url, request_kwargs = self.request_preparer.prep_prime_request(
            endpoint=f"/mto-shipments/{mto_shipment['id']}/status",
            endpoint_name="/mto-shipments/{mtoShipmentID}/status — expected failure",
        )

        request_kwargs["headers"]["If-Match"] = mto_shipment["eTag"]

        with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                # Note that by default, locust would fail this request because its status code is >
                # 400 so
                # we need to explicitly mark it as a failure.
                resp.success()
            else:
                # If we get any other status code, we didn't get the expected request failure,
                # so let's mark
                # it as a load test failure.
                resp.failure("Got an unexpected result for updating a shipment with an invalid status.")

                log_response_failure(response=resp)


@tag("support")
class SupportTasks(PrimeDataStorageMixin, RestTaskSet):
    """
    Set of the tasks that can be called on the Support API. Make sure to mark tasks with the `@task` decorator and add
    tags where appropriate to make filtering for custom tests easier. Ex:

    @tag('updates', 'shipments')
    @task
    def update_mto_shipment_status(self):
        # etc.
    """

    @tag(MTO_SHIPMENT, "updateMTOShipmentStatus")
    @task(2)
    def update_mto_shipment_status(self, overrides=None):
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        mto_shipment = self.get_stored(MTO_SHIPMENT, object_id)
        if not mto_shipment:
            logger.debug("updateMTOShipmentStatus: ⚠️ No mto_shipment found.")
            return None  # can't run this task
        # To avoid issues with the mto shipment being stale
        # retrieve the move associated with the shipment
        # and then use the newly fetched move to the find most up to date version of the shipment
        move_id = mto_shipment["moveTaskOrderID"]

        url, request_kwargs = self.request_preparer.prep_support_request(
            endpoint=f"/move-task-orders/{move_id}",
            endpoint_name="/move-task-orders/{moveTaskOrderID}",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code != HTTPStatus.OK:
                resp.failure("Unable to retrieve MTO.")

                log_response_failure(response=resp)

                return

            move_details: JSONObject = resp.js

        for fetched_mto_shipment in move_details["mtoShipments"]:
            if fetched_mto_shipment["id"] != mto_shipment["id"]:
                continue

            # Generate fake payload based on the endpoint's required fields
            payload = fake_data_generator.generate_fake_request_data(
                api_key=APIKey.SUPPORT,
                path="/mto-shipments/{mtoShipmentID}/status",
                method="patch",
                overrides=overrides,
            )

            if fetched_mto_shipment["status"] == "CANCELLATION_REQUESTED" and payload["status"] != "CANCELED":
                return None
            elif fetched_mto_shipment["status"] == "SUBMITTED" and payload["status"] not in [
                "APPROVED",
                "REJECTED",
            ]:
                return None
            elif fetched_mto_shipment["status"] == "DIVERSION_REQUESTED" and payload["status"] != "APPROVED":
                return None
            elif fetched_mto_shipment["status"] == "APPROVED" and payload["status"] != "DIVERSION_REQUESTED":
                return None
            elif fetched_mto_shipment["status"] in ["DRAFT", "REJECTED", "CANCELED"]:
                return None

            url, request_kwargs = self.request_preparer.prep_support_request(
                endpoint=f"/mto-shipments/{fetched_mto_shipment['id']}/status",
                endpoint_name="/mto-shipments/{mtoShipmentID}/status",
            )

            request_kwargs["headers"]["If-Match"] = fetched_mto_shipment["eTag"]

            with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
                resp: RestResponseContextManager

                log_response_info(response=resp)

                if resp.status_code == HTTPStatus.OK:
                    new_mto_shipment = resp.js
                    self.update_stored(MTO_SHIPMENT, mto_shipment, new_mto_shipment)

                    return mto_shipment

                resp.failure("Unable to update MTO shipment status.")

                log_response_failure(response=resp)

    @tag(MTO_SHIPMENT, "updateMTOShipmentStatus", "expectedFailure")
    # run this task less frequently than the others since this is testing an expected failure
    @task(1)
    def update_mto_shipment_with_invalid_status(self, overrides=None):
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        mto_shipment = self.get_stored(MTO_SHIPMENT, object_id)
        if not mto_shipment:
            logger.debug("updateMTOShipmentStatus: ⚠️ No mto_shipment found.")
            return None  # can't run this task

        overrides_local = {"status": "DRAFT"}

        # Merge local overrides with passed-in overrides
        if overrides:
            overrides_local.update(overrides)

        # Generate fake payload based on the endpoint's required fields
        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.SUPPORT,
            path="/mto-shipments/{mtoShipmentID}/status",
            method="patch",
            overrides=overrides_local,
        )

        payload["status"] = "DRAFT"

        url, request_kwargs = self.request_preparer.prep_support_request(
            endpoint=f"/mto-shipments/{mto_shipment['id']}/status",
            endpoint_name="/mto-shipments/{mtoShipmentID}/status — expected failure",
        )

        request_kwargs["headers"]["If-Match"] = mto_shipment["eTag"]

        with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                resp.success()
            else:
                resp.failure("Got an unexpected result for updating a shipment with an invalid status.")

                log_response_failure(response=resp)

    @tag(MOVE_TASK_ORDER, "createMoveTaskOrder")
    @task(2)
    def create_move_task_order(self):
        # Check that we have all required ID values for this endpoint:
        if not self.has_all_default_mto_ids():
            logger.debug(f"⚠️ Missing createMoveTaskOrder IDs for environment {self.env}")
            return

        overrides = {
            "contractorID": self.default_mto_ids["contractorID"],
            # Moves that are in DRAFT or CANCELED mode cannot be used by the rest of the load testing
            "status": "SUBMITTED",
            # If this date is set here, the status will not properly transition to APPROVED
            "availableToPrimeAt": None,
            "order": {
                "status": "APPROVED",
                "tac": "F8J1",
                # We need these objects to exist
                "destinationDutyLocationID": self.default_mto_ids["destinationDutyLocationID"],
                "originDutyLocationID": self.default_mto_ids["originDutyLocationID"],
                "uploadedOrdersID": self.default_mto_ids["uploadedOrdersID"],
                # To avoid the overrides being inserted into these nested objects...
                "entitlement": {},
                "customer": {},
            },
        }

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.SUPPORT,
            path="/move-task-orders",
            method="post",
            overrides=overrides,
        )

        url, request_kwargs = self.request_preparer.prep_support_request(endpoint="/move-task-orders")

        with self.rest(method="POST", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code != HTTPStatus.CREATED:
                resp.failure("Unable to create an MTO.")

                log_response_failure(response=resp)

                return

            move: JSONObject = resp.js

        move_task_order_id = move["id"]

        url, request_kwargs = self.request_preparer.prep_support_request(
            endpoint=f"/move-task-orders/{move_task_order_id}/available-to-prime",
            endpoint_name="/move-task-orders/{moveTaskOrderID}/available-to-prime",
        )

        request_kwargs["headers"]["If-Match"] = move["eTag"]

        with self.rest(method="PATCH", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                new_mto: JSONObject = resp.js

                self.add_stored(MOVE_TASK_ORDER, new_mto)

                return new_mto

            resp.failure("Unable to make MTO available to prime.")

            log_response_failure(response=resp)

    # @tag(MTO_SERVICE_ITEM, "updateMTOServiceItemStatus")
    @task(2)
    def update_mto_service_item_status(self, overrides=None):
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        mto_service_item = self.get_stored(MTO_SERVICE_ITEM, object_id)
        # if we don't have an mto shipment we can't run this task
        if not mto_service_item:
            logger.debug("updateMTOServiceItemStatus: ⚠️ No mto_service_item found")
            return None

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.SUPPORT,
            path="/mto-service-items/{mtoServiceItemID}/status",
            method="patch",
            overrides=overrides,
        )

        url, request_kwargs = self.request_preparer.prep_support_request(
            endpoint=f"/mto-service-items/{mto_service_item['id']}/status",
            endpoint_name="/mto-service-items/{mtoServiceItemID}/status",
        )

        request_kwargs["headers"]["If-Match"] = mto_service_item["eTag"]

        with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                mto_service_item = resp.js

                self.update_stored(MTO_SERVICE_ITEM, mto_service_item, mto_service_item)

                return mto_service_item

            resp.failure("Unable to update MTO service item status.")

            log_response_failure(response=resp)

    @tag(PAYMENT_REQUEST, "updatePaymentRequestStatus")
    @task(2)
    def update_payment_request_status(self, overrides=None):
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        payment_request = self.get_stored(PAYMENT_REQUEST, object_id)
        if not payment_request:
            return

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.SUPPORT,
            path="/payment-requests/{paymentRequestID}/status",
            method="patch",
        )

        url, request_kwargs = self.request_preparer.prep_support_request(
            endpoint=f"/payment-requests/{payment_request['id']}/status",
            endpoint_name="/payment-requests/{paymentRequestID}/status",
        )

        request_kwargs["headers"]["If-Match"] = payment_request["eTag"]

        with self.rest(method="PATCH", url=url, data=json.dumps(payload), **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                new_payment_request = resp.js

                self.update_stored(PAYMENT_REQUEST, payment_request, new_payment_request)

                return new_payment_request

            resp.failure("Unable to update payment request status.")

            log_response_failure(response=resp)

    @tag(MOVE_TASK_ORDER, "getMoveTaskOrder")
    @task(2)
    def get_move_task_order(self, overrides=None):
        # If id was provided, get that specific one. Else get any stored one.
        object_id = overrides.get("id") if overrides else None
        move_task_order = self.get_stored(MOVE_TASK_ORDER, object_id)
        if not move_task_order:
            logger.debug("getMoveTaskOrder: ⚠️ No move_task_order found")
            return

        url, request_kwargs = self.request_preparer.prep_support_request(
            endpoint=f"/move-task-orders/{move_task_order['id']}",
            endpoint_name="/move-task-orders/{moveTaskOrderID}",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                new_mto: JSONObject = resp.js

                self.update_stored(MOVE_TASK_ORDER, move_task_order, new_mto)

                return new_mto

            resp.failure("Unable to get MTO.")

            log_response_failure(response=resp)
