# -*- coding: utf-8 -*-
""" TaskSets and tasks for the Prime & Support APIs """
import logging
import json
import random

from locust import tag, task, TaskSet

from utils.constants import TEST_PDF, ZERO_UUID, MilMoveEnv
from .base import check_response, CertTaskMixin, ParserTaskMixin

logger = logging.getLogger(__name__)


def prime_path(url):
    return f"/prime/v1{url}"


def support_path(url):
    return f"/support/v1{url}"


class PrimeDataTaskMixin:
    """

    """

    DATA_LIST_MAX = 25
    prime_data = {
        "mto": [],
        "mtoShipment": [],
        "mtoServiceItem": [],
        "paymentRequest": [],
    }  # data stored will be shared among class instances thanks to mutable dict

    def get_random_data(self, object_key):
        """  """
        data_list = self.prime_data[object_key]

        if len(data_list) > 0:  # otherwise we return None
            return random.choice(data_list)

    def get_data_for_mto(self, object_key, mto_id):
        """  """
        field = "moveTaskOrderID"
        if object_key == "mto":
            field = "id"

        data_list = self.prime_data[object_key]

        for item in data_list:
            if item[field] == mto_id:
                return item  # return None if never found

    def set_prime_data(self, object_key, object_data):
        """  """
        data_list = self.prime_data[object_key]

        if len(data_list) >= self.DATA_LIST_MAX:
            num_to_delete = random.randint(1, self.DATA_LIST_MAX)
            del data_list[:num_to_delete]

        data_list.append(object_data)

    def replace_prime_data(self, object_key, old_data, new_data):
        """  """
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

    @tag("mto", "fetchMTOUpdates")
    @task
    def fetch_mto_updates(self):
        resp = self.client.get(prime_path("/move-task-orders"), **self.user.cert_kwargs)
        check_response(resp, "Fetch MTOs")

    @tag("mtoServiceItem", "createMTOServiceItem")
    @task
    def create_mto_service_item(self):
        move_task_order = self.get_random_data("mto")
        mto_shipment = None

        if move_task_order:
            mto_shipment = self.get_data_for_mto("mtoShipment", move_task_order["id"])

        if not move_task_order or not mto_shipment:
            if not self.user.env == MilMoveEnv.LOCAL:
                return  # we can't do anything else without a default value

            move_task_order = {"id": "5d4b25bb-eb04-4c03-9a81-ee0398cb779e"}
            mto_shipment = {"id": "475579d5-aaa4-4755-8c43-c510381ff9b5"}

        overrides = {
            "moveTaskOrderID": move_task_order["id"],
            "mtoShipmentID": mto_shipment["id"],
        }
        payload = self.fake_request("/mto-service-items", "post", overrides=overrides)

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/mto-service-items"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        resp, success = check_response(resp, "Create MTO Service Item", payload)

        if success:
            self.set_prime_data("mtoServiceItem", resp)

    @tag("mtoShipment", "createMTOShipment")
    @task
    def create_mto_shipment(self):
        move_task_order = self.get_random_data("mto")
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
            self.set_prime_data("mtoShipment", resp)

    @tag("paymentRequest", "createUpload")
    @task
    def create_upload(self):
        payment_request = self.get_random_data("paymentRequest")
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

    @tag("paymentRequest", "createPaymentRequest")
    @task
    def create_payment_request(self):
        move_task_order = self.get_random_data("mto")
        service_item = None

        if move_task_order:
            service_item = self.get_data_for_mto("mtoServiceItem", move_task_order["id"])

        if not move_task_order or not service_item:
            if not self.user.env == MilMoveEnv.LOCAL:
                return  # we can't do anything else without a default value

            move_task_order = {"id": "da3f34cc-fb94-4e0b-1c90-ba3333cb7791"}
            service_item = {"id": "8a625314-1922-4987-93c5-a62c0d13f053"}

        payload = {
            "moveTaskOrderID": move_task_order["id"],
            "serviceItems": [{"id": service_item["id"]}],
            "isFinal": False,
        }

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/payment-requests"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        resp, success = check_response(resp, "Create Payment Request", payload)

        if success:
            self.set_prime_data("paymentRequest", resp)

    @tag("mtoShipment", "updateMTOShipment")
    @task
    def update_mto_shipment(self):
        mto_shipment = self.get_random_data("mtoShipment")
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
            self.replace_prime_data("mtoShipment", mto_shipment, resp)


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

    @tag("mto", "createMoveTaskOrder")
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
            self.set_prime_data("mto", mto_data)
