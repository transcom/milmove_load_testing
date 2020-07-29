# -*- coding: utf-8 -*-
""" TaskSets and tasks for the Prime & Support APIs """
import logging
import json

from locust import tag, task, TaskSet

from utils.constants import TEST_PDF, ZERO_UUID
from .base import check_response, CertTaskMixin, ParserTaskMixin

logger = logging.getLogger(__name__)


def prime_path(url):
    return f"/prime/v1{url}"


def support_path(url):
    return f"/support/v1{url}"


@tag("prime")
class PrimeTasks(ParserTaskMixin, CertTaskMixin, TaskSet):
    """
    Set of the tasks that can be called on the Prime API. Make sure to mark tasks with the `@task` decorator and add
    tags where appropriate to make filtering for custom tests easier.
    """

    # TODO rework with ticket to update architecture to pass data from one task to another
    mto_shipment_id = ""
    mto_shipment_etag = ""

    @tag("mto", "fetchMTOUpdates")
    @task
    def fetch_mto_updates(self):
        resp = self.client.get(prime_path("/move-task-orders"), **self.user.cert_kwargs)
        check_response(resp, "Fetch MTOs")

    @tag("mtoServiceItem", "createMTOServiceItem")
    @task
    def create_mto_service_item(self):
        overrides = {
            "moveTaskOrderID": "5d4b25bb-eb04-4c03-9a81-ee0398cb779e",
            "mtoShipmentID": "475579d5-aaa4-4755-8c43-c510381ff9b5",
        }
        payload = self.fake_request("/mto-service-items", "post", overrides=overrides)

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/mto-service-items"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        check_response(resp, "Create MTO Service Item", payload)

    @tag("mtoShipment", "createMTOShipment")
    @task
    def create_mto_shipment(self):
        overrides = {
            "moveTaskOrderID": "5d4b25bb-eb04-4c03-9a81-ee0398cb779e",
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

        if not success:
            return

        self.mto_shipment_id = resp["id"]
        self.mto_shipment_etag = resp["eTag"]

    @tag("paymentRequest", "createUpload")
    @task
    def create_upload(self):
        payment_request_id = "a2c34dba-015f-4f96-a38b-0c0b9272e208"
        upload_file = {"file": open(TEST_PDF, "rb")}

        resp = self.client.post(
            prime_path(f"/payment-requests/{payment_request_id}/uploads"),
            name=prime_path("/payment-requests/:paymentRequestID/uploads"),
            files=upload_file,
            **self.user.cert_kwargs,
        )
        check_response(resp, "Create Upload")

    @tag("paymentRequest", "createPaymentRequest")
    @task
    def create_payment_request(self):
        payload = {
            "moveTaskOrderID": "da3f34cc-fb94-4e0b-1c90-ba3333cb7791",
            "serviceItems": [{"id": "8a625314-1922-4987-93c5-a62c0d13f053"}],
            "isFinal": False,
        }

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/payment-requests"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        check_response(resp, "Create Payment Request", payload)

    @tag("mtoShipment", "updateMTOShipment")
    @task
    def update_mto_shipment(self):
        if not self.mto_shipment_id or not self.mto_shipment_etag:
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

        headers = {"content-type": "application/json", "If-Match": self.mto_shipment_etag}
        resp = self.client.put(
            prime_path(f"/mto-shipments/{self.mto_shipment_id}"),
            name=prime_path("/mto-shipments/:mtoShipmentID"),
            data=json.dumps(payload),
            headers=headers,
            **self.user.cert_kwargs,
        )
        resp, success = check_response(resp, "Update MTO Shipment", payload)

        if not success:
            return

        self.mto_shipment_id = resp["id"]
        self.mto_shipment_etag = resp["eTag"]


@tag("support")
class SupportTasks(ParserTaskMixin, CertTaskMixin, TaskSet):
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
        check_response(resp, "Make MTO available to Prime")
