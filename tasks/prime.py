# -*- coding: utf-8 -*-
""" TaskSets and tasks for the Prime & Support APIs """
import logging
import json
import random

from locust import tag, task, TaskSet

from utils.constants import (
    TEST_PDF,
    ZERO_UUID,
    PRIME_API_KEY,
    SUPPORT_API_KEY,
    MOVE_TASK_ORDER,
    MTO_SHIPMENT,
    MTO_AGENT,
    MTO_SERVICE_ITEM,
    PAYMENT_REQUEST,
)

from .base import check_response, CertTaskMixin, ParserTaskMixin
from copy import deepcopy

logger = logging.getLogger(__name__)


def prime_path(url):
    return f"/prime/v1{url}"


def support_path(url):
    return f"/support/v1{url}"


class PrimeDataTaskMixin:
    """
    TaskSet mixin used to store data from the Prime API during load testing so that it can be passed around and reused.
    We store a number of objects in a local store that can be requested by tasks.
    The tasks then hit an endpoint and call add or replace to update our local store with a list of viable objects.
    This mixin allows storing multiple items of each kind.
    """

    DATA_LIST_MAX = 50
    local_store = {
        MOVE_TASK_ORDER: [],
        MTO_SHIPMENT: [],
        MTO_SERVICE_ITEM: [],
        PAYMENT_REQUEST: [],
    }  # data stored will be shared among class instances thanks to mutable dict

    def get_stored(self, object_key):
        """Given an object_key that represents a type of object, returns a object of that type from the list.

        :param object_key: str in [MOVE_TASK_ORDER, MTO_SHIPMENT, MTO_AGENT, MTO_SERVICE_ITEM, PAYMENT_REQUEST]
        """

        data_list = self.local_store[object_key]

        if len(data_list) > 0:  # otherwise we return None
            return random.choice(data_list)

    def get_random_shipment_address(self, mto_shipment=None):
        """
        Grabs one of either pickupAddress or destinationAddress from a shipment and returns the specific field and
        payload for that address.

        :param mto_shipment: JSON/dict of a specific MTO Shipment payload (optional)
        :return: tuple(str name of the address field, dict address payload)
        """
        if not mto_shipment:
            mto_shipment = self.get_stored(MTO_SHIPMENT)

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
        """Given an object key, it replaces a stored object in the local store with a new updated object.

        :param object_key: str in [MOVE_TASK_ORDER, MTO_SHIPMENT, MTO_AGENT, MTO_SERVICE_ITEM, PAYMENT_REQUEST]
        :param old_data: JSON/dict
        :param new_data: JSON/dict
        :return: None
        """

        data_list = self.local_store[object_key]

        try:
            data_list.remove(old_data)
        except ValueError:
            pass  # this is fine, we didn't want this value in the list anymore anyway

        data_list.append(new_data)


@tag("prime")
class PrimeTasks(PrimeDataTaskMixin, ParserTaskMixin, CertTaskMixin, TaskSet):
    """
    Set of the tasks that can be called on the Prime API. Make sure to mark tasks with the `@task` decorator and add
    tags where appropriate to make filtering for custom tests easier.
    """

    @tag(MOVE_TASK_ORDER, "fetchMTOUpdates")
    @task
    def fetch_mto_updates(self):
        resp = self.client.get(prime_path("/move-task-orders"), **self.user.cert_kwargs)
        check_response(resp, "fetchMTOUpdates")

    @tag(MTO_SERVICE_ITEM, "createMTOServiceItem")
    @task
    def create_mto_service_item(self, overrides=None):
        mto_shipment = self.get_stored(MTO_SHIPMENT)
        if not mto_shipment:
            return

        overrides_local = {
            "moveTaskOrderID": mto_shipment["moveTaskOrderID"],
            "mtoShipmentID": mto_shipment["id"],
        }
        # override local overrides with parameter overrides
        if overrides:
            overrides_local.update(overrides)
        payload = self.fake_request("/mto-service-items", "post", PRIME_API_KEY, overrides=overrides_local)

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/mto-service-items"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )

        resp, success = check_response(resp, f"createMTOServiceItem {payload['reServiceCode']}", payload)

        if success:
            self.add_stored(MTO_SERVICE_ITEM, resp)

    @tag(MTO_SHIPMENT, "createMTOShipment")
    @task
    def create_mto_shipment(self):
        move_task_order = self.get_stored(MOVE_TASK_ORDER)
        if not move_task_order:
            return  # we can't do anything else without a default value, and no pre-made MTOs satisfy our requirements

        overrides = {
            "moveTaskOrderID": move_task_order["id"],
            "agents": {"id": ZERO_UUID, "mtoShipmentID": ZERO_UUID},
            "pickupAddress": {"id": ZERO_UUID},
            "destinationAddress": {"id": ZERO_UUID},
            "mtoServiceItems": [],  # let the create_mto_service_item endpoint handle creating these
        }
        payload = self.fake_request("/mto-shipments", "post", PRIME_API_KEY, overrides=overrides)

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/mto-shipments"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        resp, success = check_response(resp, "createMTOShipment", payload)

        if success:
            self.add_stored(MTO_SHIPMENT, resp)

    @tag(PAYMENT_REQUEST, "createUpload")
    @task
    def create_upload(self):
        payment_request = self.get_stored(PAYMENT_REQUEST)
        if not payment_request:
            return

        upload_file = {"file": open(TEST_PDF, "rb")}

        resp = self.client.post(
            prime_path(f"/payment-requests/{payment_request['id']}/uploads"),
            name=prime_path("/payment-requests/{paymentRequestID}/uploads"),
            files=upload_file,
            **self.user.cert_kwargs,
        )
        check_response(resp, "createUpload")

    @tag(PAYMENT_REQUEST, "createPaymentRequest")
    @task
    def create_payment_request(self):
        service_item = self.get_stored(MTO_SERVICE_ITEM)
        if not service_item:
            return

        payload = {
            "moveTaskOrderID": service_item["moveTaskOrderID"],
            "serviceItems": [{"id": service_item["id"]}],
            "isFinal": False,
        }

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/payment-requests"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        resp, success = check_response(resp, "createPaymentRequest", payload)

        if success:
            self.add_stored(PAYMENT_REQUEST, resp)

    @tag(MTO_SHIPMENT, "updateMTOShipment")
    @task
    def update_mto_shipment(self):
        mto_shipment = self.get_stored(MTO_SHIPMENT)
        if not mto_shipment:
            return  # can't run this task

        payload = self.fake_request("/mto-shipments/{mtoShipmentID}", "put", PRIME_API_KEY)

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
        for f in fields_to_remove:
            payload.pop(f, None)

        headers = {"content-type": "application/json", "If-Match": mto_shipment["eTag"]}
        resp = self.client.put(
            prime_path(f"/mto-shipments/{mto_shipment['id']}"),
            name=prime_path("/mto-shipments/{mtoShipmentID}"),
            data=json.dumps(payload),
            headers=headers,
            **self.user.cert_kwargs,
        )
        resp, success = check_response(resp, "updateMTOShipment", payload)

        if success:
            self.update_stored(MTO_SHIPMENT, mto_shipment, resp)

    @tag(MTO_SHIPMENT, "updateMTOShipmentAddress")
    @task
    def update_mto_shipment_address(self):
        mto_shipment = self.get_stored(MTO_SHIPMENT)
        if not mto_shipment:
            return

        address_tuple = self.get_random_shipment_address(mto_shipment)  # returns a (field_name, address_dict) tuple
        if not address_tuple:
            return  # this shipment didn't have any addresses, we will try again later with a different shipment

        field, address = address_tuple

        overrides = {"id": address["id"]}
        payload = self.fake_request(
            "/mto-shipments/{mtoShipmentID}/addresses/{addressID}", "put", PRIME_API_KEY, overrides=overrides
        )

        headers = {"content-type": "application/json", "If-Match": address["eTag"]}
        # update mto_shipment address
        resp = self.client.put(
            prime_path(f"/mto-shipments/{mto_shipment['id']}/addresses/{address['id']}"),
            name=prime_path("/mto-shipments/{mtoShipmentID}/addresses/{addressID}"),
            data=json.dumps(payload),
            headers=headers,
            **self.user.cert_kwargs,
        )
        resp, success = check_response(resp, "updateMTOShipmentAddress", payload)

        if success:
            updated_shipment = deepcopy(mto_shipment)
            updated_shipment[field] = resp
            self.update_stored(MTO_SHIPMENT, mto_shipment, updated_shipment)

    @tag(MTO_AGENT, "updateMTOAgent")
    @task
    def update_mto_agent(self):
        mto_shipment = self.get_stored(
            MTO_SHIPMENT
        )  # this grabs response payload from the MTO_AGENT list when load testing runs
        if not mto_shipment:
            return  # can't run this task
        if mto_shipment.get("agents") is None:
            return  # can't update agents if there aren't any

        payload = self.fake_request("/mto-shipments/{mtoShipmentID}/agents/{agentID}", "put", PRIME_API_KEY)
        mto_agent = mto_shipment["agents"][0]
        headers = {"content-type": "application/json", "If-Match": mto_agent["eTag"]}
        resp = self.client.put(
            prime_path(f"/mto-shipments/{mto_shipment['id']}/agents/{mto_agent['id']}"),
            name=prime_path("/mto-shipments/{mtoShipmentID}/agents/{agentID}"),
            data=json.dumps(payload),
            headers=headers,
            **self.user.cert_kwargs,
        )

        resp, success = check_response(resp, "updateMTOAgent", payload)

        if success:
            new_shipment = deepcopy(mto_shipment)
            new_shipment["agents"][0] = resp
            self.update_stored(MTO_SHIPMENT, mto_shipment, new_shipment)

    @tag(MTO_SERVICE_ITEM, "updateMTOServiceItem")
    @task
    def update_mto_service_item(self):
        mto_service_item = self.get_stored(MTO_SERVICE_ITEM)
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

        payload = self.fake_request(
            "/mto-service-items/{mtoServiceItemID}", "patch", overrides={"id": mto_service_item["id"]}
        )

        headers = {"content-type": "application/json", "If-Match": mto_service_item["eTag"]}
        resp = self.client.patch(
            prime_path(f"/mto-service-items/{mto_service_item['id']}"),
            name=prime_path("/mto-service-items/{mtoServiceItemID}"),
            data=json.dumps(payload),
            headers=headers,
            **self.user.cert_kwargs,
        )
        resp, success = check_response(resp, f"updateMTOServiceItem {re_service_code}", payload)

        if success:
            self.update_stored(MTO_SERVICE_ITEM, mto_service_item, resp)

    @tag(MOVE_TASK_ORDER, "updateMTOPostCounselingInformation")
    @task
    def update_post_counseling_information(self):
        move_task_order = self.get_stored(MOVE_TASK_ORDER)
        if not move_task_order:
            logger.error(f"⛔️ No move_task_order \n{move_task_order}")
            return  # we can't do anything else without a default value, and no pre-made MTOs satisfy our requirements

        payload = self.fake_request("/move-task-orders/{moveTaskOrderID}/post-counseling-info", "patch", PRIME_API_KEY)

        move_task_order_id = move_task_order["id"]  # path parameter
        headers = {"content-type": "application/json", "If-Match": move_task_order["eTag"]}

        resp = self.client.patch(
            prime_path(f"/move-task-orders/{move_task_order_id}/post-counseling-info"),
            name=prime_path("/move-task-orders/{moveTaskOrderID}/post-counseling-info"),
            data=json.dumps(payload),
            headers=headers,
            **self.user.cert_kwargs,
        )
        new_mto, success = check_response(resp, "updateMTOPostCounselingInformation", payload)

        if success:
            self.update_stored(MOVE_TASK_ORDER, move_task_order, new_mto)


@tag("support")
class SupportTasks(PrimeDataTaskMixin, ParserTaskMixin, CertTaskMixin, TaskSet):
    """
    Set of the tasks that can be called on the Support API. Make sure to mark tasks with the `@task` decorator and add
    tags where appropriate to make filtering for custom tests easier. Ex:

    @tag('updates', 'shipments')
    @task
    def update_mto_shipment_status(self):
        # etc.
    """

    @tag(MTO_SHIPMENT, "updateMTOShipmentStatus")
    @task
    def update_mto_shipment_status(self):
        # Get shipment we've previously stored in PrimeObjects
        mto_shipment = self.get_stored(MTO_SHIPMENT)
        if not mto_shipment:
            return  # can't run this task

        # Generate fake payload based on the endpoint's required fields
        payload = self.fake_request("/mto-shipments/{mtoShipmentID}/status", "patch", SUPPORT_API_KEY)

        headers = {"content-type": "application/json", "If-Match": mto_shipment["eTag"]}

        resp = self.client.patch(
            support_path(f"/mto-shipments/{mto_shipment['id']}/status"),
            name=support_path("/mto-shipments/{mtoShipmentID}/status"),
            data=json.dumps(payload),
            headers=headers,
            **self.user.cert_kwargs,
        )
        resp, success = check_response(resp, "updateMTOShipmentStatus", payload)

        if success:
            self.update_stored(MTO_SHIPMENT, mto_shipment, resp)

    @tag(MOVE_TASK_ORDER, "createMoveTaskOrder")
    @task
    def create_move_task_order(self):

        overrides = {
            "contractorId": "5db13bb4-6d29-4bdb-bc81-262f4513ecf6",
            # Moves that are in DRAFT or CANCELED mode cannot be used by the rest of the
            # loadtesting
            "status": "SUBMITTED",
            # If this date is set here, the status will not properly transition to APPROVED
            "availableToPrimeAt": None,
            "moveOrder": {
                "status": "APPROVED",
                # We need these objects to exist
                "destinationDutyStationID": "71b2cafd-7396-4265-8225-ff82be863e01",
                "originDutyStationID": "1347d7f3-2f9a-44df-b3a5-63941dd55b34",
                "uploadedOrdersID": "c26421b0-e4c3-446b-88f3-493bb25c1756",
                # To avoid the overrides being inserted into these nested objects...
                "entitlement": {},
                "customer": {},
            },
        }
        payload = self.fake_request("/move-task-orders", "post", SUPPORT_API_KEY, overrides)

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            support_path("/move-task-orders"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        json_body, success = check_response(resp, "createMoveTaskOrder", payload)

        if not success:
            return  # no point continuing if it didn't work out

        move_task_order_id = json_body["id"]
        e_tag = json_body["eTag"]
        headers["if-match"] = e_tag

        resp = self.client.patch(
            support_path(f"/move-task-orders/{move_task_order_id}/available-to-prime"),
            name=support_path("/move-task-orders/{moveTaskOrderID}/available-to-prime"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        new_mto, success = check_response(resp, "makeMoveTaskOrderAvailable")

        if success:
            self.add_stored(MOVE_TASK_ORDER, new_mto)

    @tag(MTO_SERVICE_ITEM, "updateMTOServiceItemStatus")
    @task
    def update_mto_service_item_status(self):
        mto_service_item = self.get_stored(MTO_SERVICE_ITEM)
        # if we don't have an mto shipment we can't run this task
        if not mto_service_item:
            return

        payload = self.fake_request("/mto-service-items/{mtoServiceItemID}/status", "patch", SUPPORT_API_KEY)
        headers = {"content-type": "application/json", "If-Match": mto_service_item["eTag"]}

        resp = self.client.patch(
            support_path(f"/mto-service-items/{mto_service_item['id']}/status"),
            name=support_path("/mto-service-items/{mtoServiceItemID}/status"),
            data=json.dumps(payload),
            headers=headers,
            **self.user.cert_kwargs,
        )

        mto_service_item_data, success = check_response(resp, "updateMTOServiceItemStatus", payload)

        if success:
            self.update_stored(MTO_SERVICE_ITEM, mto_service_item, mto_service_item_data)

    @tag(PAYMENT_REQUEST, "updatePaymentRequestStatus")
    @task
    def update_payment_request_status(self):
        payment_request = self.get_stored(PAYMENT_REQUEST)
        if not payment_request:
            return

        payload = self.fake_request("/payment-requests/{paymentRequestID}/status", "patch", SUPPORT_API_KEY)
        headers = {"content-type": "application/json", "If-Match": payment_request["eTag"]}

        resp = self.client.patch(
            support_path(f"/payment-requests/{payment_request['id']}/status"),
            name=support_path("/payment-requests/{paymentRequestID}/status"),
            data=json.dumps(payload),
            headers=headers,
            **self.user.cert_kwargs,
        )
        new_payment_request, success = check_response(resp, "updatePaymentRequestStatus", payload)

        if success:
            self.update_stored(PAYMENT_REQUEST, payment_request, new_payment_request)

    @tag(MOVE_TASK_ORDER, "getMoveTaskOrder")
    @task
    def get_move_task_order(self):
        move_task_order = self.get_stored(MOVE_TASK_ORDER)
        if not move_task_order:
            logger.error(f"⛔️ No move_task_order \n{move_task_order}")
            return

        headers = {"content-type": "application/json"}

        resp = self.client.get(
            support_path(f"/move-task-orders/{move_task_order['id']}"),
            name=support_path("move-task-orders/{moveTaskOrderID}"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        new_mto, success = check_response(resp, "getMoveTaskOrder")

        if success:
            self.update_stored(MOVE_TASK_ORDER, move_task_order, new_mto)
