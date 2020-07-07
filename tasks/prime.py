# -*- coding: utf-8 -*-
""" TaskSets and tasks for the Prime & Support APIs """
import logging
import json

from locust import tag, task, TaskSet

from .base import CertTaskMixin, ParserTaskMixin

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

    @tag("mto", "fetchMTOUpdates")
    @task
    def fetch_mto_updates(self):
        resp = self.client.get(prime_path("/move-task-orders"), **self.user.cert_kwargs)
        logger.info(f"ℹ️ Fetch MTOs status code: {resp.status_code}")

        try:
            json_body = json.loads(resp.content)
        except (json.JSONDecodeError, TypeError):
            logger.exception("Non-JSON response")
        else:
            if str(resp.status_code).startswith("2"):
                logger.info(f"ℹ️ Num MTOs returned: {len(json_body)}")
            else:
                logger.error(f"⚠️ {json_body}")

    @tag("mtoServiceItem", "createMTOServiceItem")
    @task
    def create_mto_service_item(self):
        overrides = {
            "moveTaskOrderID": "5d4b25bb-eb04-4c03-9a81-ee0398cb779e",
            "mtoShipmentID": "475579d5-aaa4-4755-8c43-c510381ff9b5",
        }
        payload = self.fake_request("/mto-service-items", "post", overrides=overrides, nested_overrides=overrides)
        print("🔆", payload)

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/mto-service-items"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        logger.info(f"ℹ️ Create MTO Service Item status code: {resp.status_code}")

        try:
            json_body = json.loads(resp.content)
        except (json.JSONDecodeError, TypeError):
            logger.exception("Non-JSON response")
        else:
            if str(resp.status_code).startswith("2"):
                logger.info(f"ℹ️ MTOServiceItem {json_body['id']} created!")
            else:
                logger.error(f"⚠️ {json_body}")
                logger.error(payload)

    @tag("mtoShipment", "createMTOShipment")
    @task
    def create_mto_shipment(self):
        overrides = {"moveTaskOrderID": "5d4b25bb-eb04-4c03-9a81-ee0398cb779e", "mtoServiceItems": []}
        payload = self.fake_request("/mto-shipments", "post", overrides=overrides, nested_overrides=overrides)
        print("🐙", payload)

        headers = {"content-type": "application/json"}
        resp = self.client.post(
            prime_path("/mto-shipments"), data=json.dumps(payload), headers=headers, **self.user.cert_kwargs
        )
        logger.info(f"ℹ️ Create MTO Shipment status code: {resp.status_code}")

        try:
            json_body = json.loads(resp.content)
        except (json.JSONDecodeError, TypeError):
            logger.exception("Non-JSON response")
        else:
            if str(resp.status_code).startswith("2"):
                logger.info(f"ℹ️ MTOShipment {json_body['id']} created!")
            else:
                logger.error(f"⚠️ {json_body}")
                logger.error(payload)


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
        # overrides = {
        #     "contractorId": "5db13bb4-6d29-4bdb-bc81-262f4513ecf6",
        #     "destinationDutyStationID": "71b2cafd-7396-4265-8225-ff82be863e01",
        #     "originDutyStationID": "1347d7f3-2f9a-44df-b3a5-63941dd55b34",
        #     "mtoServiceItems": []
        # }
        # payload = self.fake_request("/move-task-orders", "post", overrides=overrides, nested_overrides={"uploads": []})
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
        logger.info(f"ℹ️ Create MTO status code: {resp.status_code}")

        try:
            json_body = json.loads(resp.content)
        except (json.JSONDecodeError, TypeError):
            logger.exception("Non-JSON response")
            return  # we're done here

        if not str(resp.status_code).startswith("2"):
            logger.error(f"⚠️ {json_body}")
            logger.error(payload)
            return  # also done

        logger.info(f"ℹ️ MoveTaskOrder {json_body['id']} created!")

        move_task_order_id = json_body["id"]
        e_tag = json_body["eTag"]
        headers["if-match"] = e_tag
        resp = self.client.patch(
            support_path(f"/move-task-orders/{move_task_order_id}/available-to-prime"),
            headers=headers,
            **self.user.cert_kwargs,
            name=support_path("/move-task-orders/:moveTaskOrderID/available-to-prime"),
        )

        logger.info(f"ℹ️ Make MTO available to Prime status code: {resp.status_code}")
