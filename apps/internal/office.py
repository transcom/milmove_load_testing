# -*- coding: utf-8 -*-
import random
from urllib.parse import urljoin

from locust import TaskSet
from locust import seq_task
from locust import task
from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient

from .base import BaseTaskSequence
from .base import InternalAPIMixin
from .base import PublicAPIMixin
from .base import get_swagger_config
from .base import swagger_request


class OfficeQueue(BaseTaskSequence, InternalAPIMixin, PublicAPIMixin):

    login_gov_user = None
    session_token = None

    # User is the LoggedInUserPayload
    user = {}

    def update_user(self):
        self.user = swagger_request(self.swagger_internal.users.showLoggedInUser)

    @seq_task(1)
    def login(self):
        resp = self.client.post("/devlocal-auth/create", data={"userType": "office"})
        try:
            self.login_gov_user = resp.json()
        except Exception as e:
            print(e)
            return self.kill(
                "login could not be parsed. content: {}".format(resp.content)
            )

        try:
            self.session_token = self.client.cookies.get("office_session_token")
        except Exception as e:
            print(e)
            return self.kill("missing session token")

        self.requests_client = RequestsClient()
        # Set the session to be the same session as locust uses
        self.requests_client.session = self.client

        try:
            # Set the csrf token in the global headers for all requests
            # Don't validate requests or responses because we're using OpenAPI Spec 2.0
            # which doesn't respect nullable sub-definitions
            self.swagger_internal = SwaggerClient.from_url(
                urljoin(self.parent.parent.host, "internal/swagger.yaml"),
                request_headers={"x-csrf-token": self.csrf},
                http_client=self.requests_client,
                config=get_swagger_config(),
            )
            if not self.swagger_internal:
                self.kill("internal swagger client failure")

            # self.swagger_internal = SwaggerClient.from_url(
            #     urljoin(self.parent.parent.host, "api/v1/swagger.yaml"),
            #     request_headers={"x-csrf-token": self.csrf},
            #     http_client=self.requests_client,
            #     config=get_swagger_config(),
            # )
            # if not self.swagger_internal:
            #     self.kill("public swagger client failure")
        except Exception as e:
            print(e)
            return self.kill("unknown swagger client failure")

    @seq_task(2)
    def retrieve_user(self):
        self.update_user()

    @seq_task(3)
    @task(10)
    def view_move_in_random_queue(self):
        """
        Choose a random queue to visit and pick a random move to view

        This task pretents to be a user who has work to do in a specific queue.
        """
        queue_types = [
            "new",
            "ppm_payment_requested",
            "ppm_approved",
            "ppm_completed",
        ]  # Excluding 'all' queue
        q_type = random.choice(queue_types)

        queue = swagger_request(
            self.swagger_internal.queues.showQueue, queueType=q_type
        )

        if not queue:
            return
        if len(queue) == 0:
            return

        # Pick a random move
        item = random.choice(queue)

        # These are all the requests loaded in a single move in rough order of execution

        # Move Requests
        move_id = item["id"]
        move = swagger_request(self.swagger_internal.moves.showMove, moveId=move_id)
        swagger_request(
            self.swagger_internal.move_docs.indexMoveDocuments, moveId=move_id
        )
        swagger_request(
            self.swagger_internal.accessorials.getTariff400ngItems,
            requires_pre_approval=True,
        )
        swagger_request(
            self.swagger_internal.ppm.indexPersonallyProcuredMoves, moveId=move_id
        )

        # Orders Requests
        orders_id = move["orders_id"]
        swagger_request(self.swagger_internal.orders.showOrders, ordersId=orders_id)

        # Service Member Requests
        service_member_id = move["service_member_id"]
        swagger_request(
            self.swagger_internal.service_members.showServiceMember,
            serviceMemberId=service_member_id,
        )

        swagger_request(
            self.swagger_internal.backup_contacts.indexServiceMemberBackupContacts,
            serviceMemberId=service_member_id,
        )

        # Shipment Requests
        if "shipments" not in move:
            return
        if not isinstance(move["shipments"], list):
            return
        if len(move["shipments"]) == 0:
            return

        shipment_id = move["shipments"][0]["id"]
        swagger_request(
            self.swagger_internal.shipments.getShipment, shipmentId=shipment_id
        )

        swagger_request(
            self.swagger_internal.transportation_service_provider.getTransportationServiceProvider,
            shipmentId=shipment_id,
        )

        swagger_request(
            self.swagger_internal.accessorials.getShipmentLineItems,
            shipmentId=shipment_id,
        )

        swagger_request(
            self.swagger_internal.shipments.getShipmentInvoices, shipmentId=shipment_id
        )

        swagger_request(
            self.swagger_internal.service_agents.indexServiceAgents,
            shipmentId=shipment_id,
        )

        swagger_request(
            self.swagger_internal.storage_in_transits.indexStorageInTransits,
            shipmentId=shipment_id,
        )

    @seq_task(4)
    def logout(self):
        self.client.post("/auth/logout")
        self.login_gov_user = None
        self.session_token = None
        self.user = {}
        self.interrupt()


class OfficeUserBehavior(TaskSet):
    tasks = {OfficeQueue: 1}