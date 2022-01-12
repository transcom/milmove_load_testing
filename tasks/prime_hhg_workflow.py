# -*- coding: utf-8 -*-
import logging
import random

from locust import tag, task

from tasks.prime import PrimeTasks, SupportTasks
from utils.constants import MOVE_TASK_ORDER, MTO_SERVICE_ITEM, MTO_SHIPMENT, PAYMENT_REQUEST

# from utils.base import ImplementationError
from utils.types import JSONObject


logger = logging.getLogger(__name__)


@tag("workflow")
class PrimeWorkflowTasks(PrimeTasks, SupportTasks):
    """Workflow Task Set
    Each task is a workflow from start to finish. Each workflow acts on only one MTO from start to finish.
    There are multiple workflows for different scenarios such as a single shipment HHG move, or an HHG move with a SIT.
    Multiple instances of the tasks will run during load testing and will interleave their hits to the server.
    However they will run in sequence and should all complete without any errors.
    """

    # current_move is the move the whole task will be acting on
    # all updates to the move and nested objects will be stored to this mto
    # current_move = None

    # The id for the move we are fetching
    current_move_id = None
    # workflow_title is a descriptor that can be used in logging anywhere in the workflow
    workflow_title = None

    def on_start(self):
        """
        Runs on instantiation of each taskset.
        We need to set up this task set with the list of tasks/workflows we want to run. If we don't define this, all
        the tasks in PrimeTasks and SupportTasks will all be run independently and will likely have errors.
        """
        self.tasks = [self.hhg_move]

    # WORKFLOWS
    @tag("hhgMove")
    @task
    def hhg_move(self):
        """
        This is a basic HHG move workflow where we have one shipment and no additional requested service items.
        To create a new flow, copy this function, but don't forget to add the workflow to the tasks array in the
        on_start function
        """
        self.workflow_title = "HHG Move Basic"

        # Move steps for this workflow
        move = super().create_move_task_order()
        if not move:
            logger.debug(f"{self.workflow_title} ⚠️ No move_task_order returned")
            return

        super().update_post_counseling_information()
        logger.info(f"{self.workflow_title} - Created move and completed counseling {self.current_move['id'][:8]}")

        self.add_shipment_with_doshut_service()
        self.update_shipment()
        self.create_payment_request()

    def add_shipment_with_doshut_service(self):
        # Get a realistic primeEstimatedWeight
        estimated_weight = int(98 / 100 * self.current_move["order"]["entitlement"]["totalWeight"])

        # Add a shipment and approve it
        overrides = {"primeEstimatedWeight": estimated_weight}
        ship = super().create_mto_shipment(overrides)

        if not ship:
            logger.info("creating a shipment failed, skipping updating status and creating doshut service item")
            return

        overrides = {"id": ship["id"], "status": "APPROVED"}
        ship = super().update_mto_shipment_status(overrides)

        # Add a DOSHUT service item to this shipment and approve it
        overrides = {"mtoShipmentID": ship["id"], "modelType": "MTOServiceItemShuttle", "reServiceCode": "DOSHUT"}
        service_items = super().create_mto_service_item(overrides)

        # DOSHUT should return exactly one service item, which we will approve
        doshut = service_items[0]
        overrides = {"id": doshut["id"], "status": "APPROVED"}
        super().update_mto_service_item_status(overrides)

        logger.info(
            f"{self.workflow_title} - Added and approved shipment and DOSHUT service item {self.current_move['id'][:8]}"
        )

    def update_shipment(self):
        # Get the shipment from the mto (this is expecting just one shipment)
        ship = self.get_stored(MTO_SHIPMENT)

        if not ship:
            logger.info("No shipment object found on the current move, skipping update shipment")
            return

        overrides = {"id": ship["id"]}
        ship = super().update_mto_shipment(overrides)

        if not ship:
            logger.info("Updating shipment failed, skipping updating address and agents")
            return

        # Update an address
        overrides = {"mtoShipmentID": ship["id"]}
        ship = super().update_mto_shipment_address(overrides)

        # Update an agent
        overrides = {"mtoShipmentID": ship["id"]}
        ship = super().update_mto_agent(overrides)

        logger.info(f"{self.workflow_title} - Updated shipment and agent {self.current_move['id'][:8]}")

    def create_payment_request(self):
        # Get service item from the mto and create payment request
        service_item = self.get_stored(MTO_SERVICE_ITEM)

        if not service_item:
            logger.info("No service item found in stored move, skipping creating payment request")
            return

        overrides = {"mtoServiceItemID": service_item["id"]}
        request = super().create_payment_request(overrides)

        if not request:
            logger.info("creating payment request failed, skipping creating upload for payment request")
            return

        # Create upload for payment request
        overrides = {"id": request["id"]}
        super().create_upload(overrides)

        logger.info(f"{self.workflow_title} - Created payment request and upload {self.current_move['id'][:8]}")

    # STORAGE FUNCTIONALITY
    def get_stored(self, object_key, object_id=None):
        """
        We only store one current move in the sequential workflow and keep it updated as we move through the workflow.
        These functions override functions in the PrimeDataTaskMixin and will get automatically called by the tasks
        in PrimeTasks and SupportTasks.
        """

        # Return whichever part of the move was requested - such as a shipment:
        if object_key == MOVE_TASK_ORDER:
            return self.current_move

        if object_key in [MTO_SHIPMENT, MTO_SERVICE_ITEM, PAYMENT_REQUEST]:
            return self._get_nested_object_from_mto(object_key, object_id)

    def add_stored(self, object_key, object_data):
        """Adds the object to the main move."""
        if object_key == MOVE_TASK_ORDER:
            self.current_move_id = object_data["id"]

        # NOTE: Code was updated to use move_id rather than just the move. For the code before this change check out: https://github.com/transcom/milmove_load_testing/pull/94

    def update_stored(self, object_key, old_data, new_data):
        """Replaces the object in old_data with the one in new_data"""
        # New change is to just retrieve the original move again
        # For the code before this change check out: https://github.com/transcom/milmove_load_testing/pull/94.
        pass

    @staticmethod
    def _get_nested_array_name(object_key):
        # Based on the object key, find the right array for nested objects in the mto
        nested_array_names = {
            MTO_SERVICE_ITEM: "mtoServiceItems",
            MTO_SHIPMENT: "mtoShipments",
            PAYMENT_REQUEST: "paymentRequests",
        }
        return nested_array_names[object_key]

    def _get_nested_object_from_mto(self, object_key, object_id):
        """Return object of type requested. If no id is provided return a random element.
        If id is provided, return the specific element or raise error
        """

        # Get the nested array from the current move, or None if it doesn't exist
        array_key = self._get_nested_array_name(object_key)
        nested_array = self.current_move.get(array_key)

        # If nested array does not exist or is empty, return None
        if not nested_array:
            return None

        # If id was provided return the specific object or None
        if object_id:
            for elem in nested_array:
                if elem["id"] == object_id:
                    return elem
            return None

        # If id was not provided select an object at random
        return random.choice(nested_array)

    @property
    def current_move(self) -> JSONObject:
        url, request_kwargs = self.request_preparer.prep_prime_request(
            endpoint=f"/move-task-orders/{self.current_move_id}",
            endpoint_name="/move-task-orders/{moveID}",
        )

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            return resp.js
