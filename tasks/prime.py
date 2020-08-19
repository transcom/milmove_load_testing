# -*- coding: utf-8 -*-
""" TaskSets and tasks for the Prime & Support APIs """
import logging
import json
import random

from locust import tag, task, TaskSet

from utils.constants import TEST_PDF, ZERO_UUID, MilMoveEnv, PrimeObjects
from .base import check_response, CertTaskMixin, ParserTaskMixin

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
        check_response(resp, "Fetch MTOs")

    @tag(PrimeObjects.MTO_SERVICE_ITEM.value, "createMTOServiceItem")
    @task
    def create_mto_service_item(self):
        mto_shipment = self.get_random_data(PrimeObjects.MTO_SHIPMENT)
        if not mto_shipment:
            if not self.user.env == MilMoveEnv.LOCAL:
                return  # we can't do anything else without a default value

            # default for local testing
            mto_shipment = {
                "id": "475579d5-aaa4-4755-8c43-c510381ff9b5",
                "moveTaskOrderID": "5d4b25bb-eb04-4c03-9a81-ee0398cb779e",
            }

        overrides = {
            "moveTaskOrderID": mto_shipment["moveTaskOrderID"],
            "mtoShipmentID": mto_shipment["id"],
        }
        payload = self.fake_request("/mto-service-items", "post", overrides=overrides)

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/mto-service-items"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        resp, success = check_response(resp, "Create MTO Service Item", payload)

        if success:
            self.set_prime_data(PrimeObjects.MTO_SERVICE_ITEM, resp)

    @tag(PrimeObjects.MTO_SHIPMENT.value, "createMTOShipment")
    @task
    def create_mto_shipment(self):
        move_task_order = self.get_random_data(PrimeObjects.MOVE_TASK_ORDER)
        if not move_task_order:
            if not self.user.env == MilMoveEnv.LOCAL:
                return  # we can't do anything else without a default value

            move_task_order = {"id": "5d4b25bb-eb04-4c03-9a81-ee0398cb779e"}  # default for local testing

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
        resp, success = check_response(resp, "Create MTO Shipment", payload)

        if success:
            self.set_prime_data(PrimeObjects.MTO_SHIPMENT, resp)

    @tag(PrimeObjects.PAYMENT_REQUEST.value, "createUpload")
    @task
    def create_upload(self):
        payment_request = self.get_random_data(PrimeObjects.PAYMENT_REQUEST)
        if not payment_request:
            if not self.user.env == MilMoveEnv.LOCAL:
                return  # we can't do anything else without a default value

            payment_request = {"id": "a2c34dba-015f-4f96-a38b-0c0b9272e208"}  # default for local testing

        upload_file = {"file": open(TEST_PDF, "rb")}

        resp = self.client.post(
            prime_path(f"/payment-requests/{payment_request['id']}/uploads"),
            name=prime_path("/payment-requests/:paymentRequestID/uploads"),
            files=upload_file,
            **self.user.cert_kwargs,
        )
        check_response(resp, "Create Upload")

    @tag(PrimeObjects.PAYMENT_REQUEST.value, "createPaymentRequest")
    @task
    def create_payment_request(self):
        service_item = self.get_random_data(PrimeObjects.MTO_SERVICE_ITEM)
        if not service_item:
            if not self.user.env == MilMoveEnv.LOCAL:
                return  # we can't do anything else without a default value

            service_item = {
                "id": "8a625314-1922-4987-93c5-a62c0d13f053",
                "moveTaskOrderID": "da3f34cc-fb94-4e0b-1c90-ba3333cb7791",
            }

        payload = {
            "moveTaskOrderID": service_item["moveTaskOrderID"],
            "serviceItems": [{"id": service_item["id"]}],
            "isFinal": False,
        }

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/payment-requests"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        resp, success = check_response(resp, "Create Payment Request", payload)

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
        resp, success = check_response(resp, "Update MTO Shipment", payload)

        if success:
            self.replace_prime_data(PrimeObjects.MTO_SHIPMENT, mto_shipment, resp)


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
        }

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            support_path("/move-task-orders"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        json_body, success = check_response(resp, "Create MTO", payload)

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
        mto_data, success = check_response(resp, "Make MTO available to Prime")

        if success:
            self.set_prime_data(PrimeObjects.MOVE_TASK_ORDER, mto_data)
