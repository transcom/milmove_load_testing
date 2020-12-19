# -*- coding: utf-8 -*-
""" TaskSets and tasks for the Prime & Support APIs """
import logging
import json
import random

from locust import tag, task, TaskSet

from utils.constants import TEST_PDF, ZERO_UUID, MilMoveEnv, PrimeObjects
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
    """

    DATA_LIST_MAX = 50
    prime_data = {
        PrimeObjects.MOVE_TASK_ORDER: [],
        PrimeObjects.MTO_SHIPMENT: [],
        PrimeObjects.MTO_SERVICE_ITEM: [],
        PrimeObjects.PAYMENT_REQUEST: [],
    }  # data stored will be shared among class instances thanks to mutable dict

    def get_random_data(self, object_key):
        """ Given a PrimeObjects value, returns a random data element from the list. """
        data_list = self.prime_data[object_key]

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
            mto_shipment = self.get_random_data(PrimeObjects.MTO_SHIPMENT)

        address_fields = ["pickupAddress", "destinationAddress"]
        valid_addresses = [
            (field, mto_shipment[field])
            for field in address_fields
            if mto_shipment.get(field) and mto_shipment[field].get("id", ZERO_UUID) != ZERO_UUID
        ]

        if len(valid_addresses) > 0:  # otherwise we return None
            return random.choice(valid_addresses)

    def set_prime_data(self, object_key, object_data):
        """
        Sets data to the list for the object key provided. Also checks if the list is already at the max number of
        elements, and if so, it randomly removes 1 to MAX number of elements so that the cycle can start again (and so
        we don't hog too much memory).

        :param object_key: PrimeObjects
        :param object_data: JSON/dict
        :return: None
        """
        data_list = self.prime_data[object_key]

        if len(data_list) >= self.DATA_LIST_MAX:
            num_to_delete = random.randint(1, self.DATA_LIST_MAX)
            del data_list[:num_to_delete]

        # Some creation endpoint auto-create multiple objects and return an array,
        # but each object in the array should still be considered individually here:
        if isinstance(object_data, list):
            data_list.extend(object_data)
        else:
            data_list.append(object_data)

    def replace_prime_data(self, object_key, old_data, new_data):
        """ Given an object key, it removes a value in the in list with a new updated value. """
        data_list = self.prime_data[object_key]

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

    @tag(PrimeObjects.MOVE_TASK_ORDER.value, "fetchMTOUpdates")
    @task
    def fetch_mto_updates(self):
        resp = self.client.get(prime_path("/move-task-orders"), **self.user.cert_kwargs)
        check_response(resp, "fetchMTOUpdates")

    @tag(PrimeObjects.MTO_SERVICE_ITEM.value, "createMTOServiceItem")
    @task
    def create_mto_service_item(self, overrides=None):
        mto_shipment = self.get_random_data(PrimeObjects.MTO_SHIPMENT)
        if not mto_shipment:
            return

        overrides_local = {
            "moveTaskOrderID": mto_shipment["moveTaskOrderID"],
            "mtoShipmentID": mto_shipment["id"],
        }
        # override local overrides with parameter overrides
        if overrides:
            overrides_local.update(overrides)
        payload = self.fake_request("/mto-service-items", "post", overrides=overrides_local)

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/mto-service-items"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )

        resp, success = check_response(resp, f"createMTOServiceItem {payload['reServiceCode']}", payload)

        if success:
            self.set_prime_data(PrimeObjects.MTO_SERVICE_ITEM, resp)

    @tag(PrimeObjects.MTO_SERVICE_ITEM.value, "createMTOServiceItemDestSIT")
    @task
    def create_mto_service_item_dest_sit(self):
        # This function ensures some destination SIT service items get requested.
        # DDFSIT requests create the trio of dest SIT items that are needed for update_mto_service_item to function.
        overrides = {
            "reServiceCode": "DDFSIT",
            "modelType": "MTOServiceItemDestSIT",
        }

        self.create_mto_service_item(overrides)

    @tag(PrimeObjects.MTO_SERVICE_ITEM.value, "createMTOServiceItemOriginSIT")
    @task
    def create_mto_service_item_origin_sit(self):
        # This function ensures some origin SIT service items get requested.
        # DOFSIT requests create the trio of origin SIT items that are needed for update_mto_service_item to function.
        overrides = {
            "reServiceCode": "DOFSIT",
            "modelType": "MTOServiceItemOriginSIT",
        }

        self.create_mto_service_item(overrides)

    @tag(PrimeObjects.MTO_SHIPMENT.value, "createMTOShipment")
    @task
    def create_mto_shipment(self):
        move_task_order = self.get_random_data(PrimeObjects.MOVE_TASK_ORDER)
        if not move_task_order:
            if self.user.env != MilMoveEnv.LOCAL.value:
                return  # we can't do anything else without a default value

            move_task_order = {"id": "ecbc2e6a-1b45-403b-9bd4-ea315d4d3d93"}  # default for local testing

        overrides = {
            "moveTaskOrderID": move_task_order["id"],
            "agents": {"id": ZERO_UUID, "mtoShipmentID": ZERO_UUID},
            "pickupAddress": {"id": ZERO_UUID},
            "destinationAddress": {"id": ZERO_UUID},
            "mtoServiceItems": [],
        }
        payload = self.fake_request("/mto-shipments", "post", overrides=overrides)
        payload.pop("primeEstimatedWeight", None)  # keeps the update endpoint happy

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/mto-shipments"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        resp, success = check_response(resp, "createMTOShipment", payload)

        if success:
            self.set_prime_data(PrimeObjects.MTO_SHIPMENT, resp)

    @tag(PrimeObjects.PAYMENT_REQUEST.value, "createUpload")
    @task
    def create_upload(self):
        payment_request = self.get_random_data(PrimeObjects.PAYMENT_REQUEST)
        if not payment_request:
            return

        upload_file = {"file": open(TEST_PDF, "rb")}

        resp = self.client.post(
            prime_path(f"/payment-requests/{payment_request['id']}/uploads"),
            name=prime_path("/payment-requests/:paymentRequestID/uploads"),
            files=upload_file,
            **self.user.cert_kwargs,
        )
        check_response(resp, "createUpload")

    @tag(PrimeObjects.PAYMENT_REQUEST.value, "createPaymentRequest")
    @task
    def create_payment_request(self):
        service_item = self.get_random_data(PrimeObjects.MTO_SERVICE_ITEM)
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
            self.set_prime_data(PrimeObjects.PAYMENT_REQUEST, resp)

    @tag(PrimeObjects.MTO_SHIPMENT.value, "updateMTOShipment")
    @task
    def update_mto_shipment(self):
        mto_shipment = self.get_random_data(PrimeObjects.MTO_SHIPMENT)
        if not mto_shipment:
            return  # can't run this task

        payload = self.fake_request("/mto-shipments/{mtoShipmentID}", "put")

        # These fields need more complicated logic to handle, so remove them for the time being:
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
            name=prime_path("/mto-shipments/:mtoShipmentID"),
            data=json.dumps(payload),
            headers=headers,
            **self.user.cert_kwargs,
        )
        resp, success = check_response(resp, "updateMTOShipment", payload)

        if success:
            self.replace_prime_data(PrimeObjects.MTO_SHIPMENT, mto_shipment, resp)

    @tag(PrimeObjects.MTO_SHIPMENT.value, "updateMTOShipmentAddress")
    @task
    def update_mto_shipment_address(self):
        mto_shipment = self.get_random_data(PrimeObjects.MTO_SHIPMENT)
        if not mto_shipment:
            return

        address_tuple = self.get_random_shipment_address(mto_shipment)  # returns a (field_name, address_dict) tuple
        if not address_tuple:
            return  # this shipment didn't have any addresses, we will try again later with a different shipment

        field, address = address_tuple

        overrides = {"id": address["id"]}
        payload = self.fake_request("/mto-shipments/{mtoShipmentID}/addresses/{addressID}", "put", overrides=overrides)

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
            self.replace_prime_data(PrimeObjects.MTO_SHIPMENT, mto_shipment, updated_shipment)

    @tag(PrimeObjects.MTO_AGENT.value, "updateMTOAgent")
    @task
    def update_mto_agent(self):
        mto_shipment = self.get_random_data(
            PrimeObjects.MTO_SHIPMENT
        )  # this grabs response payload from the PrimeObjects.MTO_AGENT list when load testing runs
        if not mto_shipment:
            return  # can't run this task
        if mto_shipment.get("agents") is None:
            return  # can't update agents if there aren't any

        payload = self.fake_request("/mto-shipments/{mtoShipmentID}/agents/{agentID}", "put")
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
            self.replace_prime_data(PrimeObjects.MTO_SHIPMENT, mto_shipment, new_shipment)

    @tag(PrimeObjects.MTO_SERVICE_ITEM.value, "updateMTOServiceItem")
    @task
    def update_mto_service_item(self):
        mto_service_item = self.get_random_data(PrimeObjects.MTO_SERVICE_ITEM)
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
            name=prime_path("/mto-service-items/:mtoServiceItemID"),
            data=json.dumps(payload),
            headers=headers,
            **self.user.cert_kwargs,
        )
        resp, success = check_response(resp, f"updateMTOServiceItem {re_service_code}", payload)

        if success:
            self.replace_prime_data(PrimeObjects.MTO_SERVICE_ITEM, mto_service_item, resp)


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

    @tag(PrimeObjects.MTO_SHIPMENT.value, "updateMTOShipmentStatus")
    @task
    def update_mto_shipment_status(self):
        # Get shipment we've previously stored in PrimeObjects
        mto_shipment = self.get_random_data(PrimeObjects.MTO_SHIPMENT)
        if not mto_shipment:
            return  # can't run this task

        # Generate fake payload based on the endpoint's required fields
        payload = self.fake_request("/mto-shipments/{mtoShipmentID}/status", "patch")

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
            self.replace_prime_data(PrimeObjects.MTO_SHIPMENT, mto_shipment, resp)

    @tag(PrimeObjects.MOVE_TASK_ORDER.value, "createMoveTaskOrder")
    @task
    def create_move_task_order(self):
        payload = {
            "contractorId": "5db13bb4-6d29-4bdb-bc81-262f4513ecf6",
            "moveOrder": {
                "customer": {
                    "firstName": "Christopher",
                    "lastName": "Swinglehurst-Walters",
                    "agency": "MARINES",
                    "email": "swinglehurst@example.com",
                },
                "entitlement": {"nonTemporaryStorage": False, "totalDependents": 47},
                "orderNumber": "32",
                "rank": "E-6",
                "destinationDutyStationID": "71b2cafd-7396-4265-8225-ff82be863e01",
                "originDutyStationID": "1347d7f3-2f9a-44df-b3a5-63941dd55b34",
                "uploadedOrdersID": "c26421b0-e4c3-446b-88f3-493bb25c1756",
                "ordersType": "GHC",
                "reportByDate": "2020-01-01",
                "status": "SUBMITTED",
                "issueDate": "2020-01-01",
            },
            "status": "SUBMITTED",
        }

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
            name=support_path("/move-task-orders/:moveTaskOrderID/available-to-prime"),
            headers=headers,
            **self.user.cert_kwargs,
        )
        mto_data, success = check_response(resp, "makeMoveTaskOrderAvailable")

        if success:
            self.set_prime_data(PrimeObjects.MOVE_TASK_ORDER, mto_data)

    @tag(PrimeObjects.MTO_SERVICE_ITEM.value, "updateMTOServiceItemStatus")
    @task
    def update_mto_service_item_status(self):
        mto_service_item = self.get_random_data(PrimeObjects.MTO_SERVICE_ITEM)
        # if we don't have an mto shipment we can't run this task
        if not mto_service_item:
            return

        payload = self.fake_request("/service-items/{mtoServiceItemID}/status", "patch")
        headers = {"content-type": "application/json", "If-Match": mto_service_item["eTag"]}

        resp = self.client.patch(
            support_path(f"/service-items/{mto_service_item['id']}/status"),
            name=support_path("/service-items/{mtoShipmentID}/status"),
            data=json.dumps(payload),
            headers=headers,
            **self.user.cert_kwargs,
        )

        mto_service_item_data, success = check_response(resp, "updateMTOServiceItemStatus")

        if success:
            self.replace_prime_data(PrimeObjects.MTO_SERVICE_ITEM, mto_service_item, mto_service_item_data)
