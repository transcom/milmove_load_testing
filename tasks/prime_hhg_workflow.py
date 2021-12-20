# -*- coding: utf-8 -*-
import logging
import random

from locust import tag, task

from .prime import PrimeTasks, SupportTasks
from utils.constants import (
    MOVE_TASK_ORDER,
    MTO_SHIPMENT,
    MTO_SERVICE_ITEM,
    PAYMENT_REQUEST,
)
from utils.base import ImplementationError

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
    current_move = None
    # workflow_title is a descriptor that can be used in logging anywhere in the workflow
    workflow_title = None

    def on_start(self):
        """
        Runs on instantiation of each taskset.
        We need to set up this task set with the list of tasks/workflows we want to run. If we don't define this, all
        the tasks in PrimeTasks and SupportTasks will all be run independently and will likely have errors.
        """
        self.tasks = [self.hhg_move, self.list_moves]

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
        overrides = {"id": ship["id"]}
        ship = super().update_mto_shipment(overrides)

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
        overrides = {"mtoServiceItemID": service_item["id"]}
        request = super().create_payment_request(overrides)

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

        # If it's a moveTaskOrder, we only keep track of one move per workflow, so add actually replaces.
        if object_key == MOVE_TASK_ORDER:
            self.current_move = object_data

        # If it's the following object types, we add them into nested array in the MTO
        elif object_key in [MTO_SHIPMENT, MTO_SERVICE_ITEM, PAYMENT_REQUEST]:
            if isinstance(object_data, list):
                self._add_nested_array_to_mto(object_key, object_data)
            else:
                self._add_nested_object_to_mto(object_key, object_data)

    def update_stored(self, object_key, old_data, new_data):
        """Replaces the object in old_data with the one in new_data"""
        if object_key == MOVE_TASK_ORDER:
            if self.current_move["id"] == old_data["id"]:
                self.current_move = new_data
            else:
                raise ImplementationError(
                    f"Cannot update move with object because its ID of {old_data['id']} does not "
                    f"match the current move's id of {self.current_move['id']}."
                )
        elif object_key in [MTO_SHIPMENT, MTO_SERVICE_ITEM, PAYMENT_REQUEST]:
            self._update_nested_object_in_mto(object_key, old_data, new_data)

    def _add_nested_object_to_mto(self, object_key, object_data):
        """Adds an object to an array directly nested under the MTO.
        Can be used for mtoServiceItems, mtoShipments and mtoPaymentRequests
        as they are all held in top level arrays.
        Cannot be used for mtoAgent as it is nested further within the mtoShipment
        """
        # New object should be associated with the current move, we assume it has a moveTaskOrderID field to check
        if object_data["moveTaskOrderID"] != self.current_move["id"]:
            raise ImplementationError(
                (
                    f"Cannot add object to store because its moveTaskOrderID of {object_data['moveTaskOrderID']} "
                    f"does not match the current move's id of {self.current_move['id']}."
                )
            )

        # Get the nested array from the current move, or None if it doesn't exist
        array_key = self._get_nested_array_name(object_key)
        nested_array = self.current_move.get(array_key) or []

        # We filter the list of objects to see if we can find the search object (checking ids)
        found = list(filter(lambda elem: elem["id"] == object_data["id"], nested_array))
        if found:
            raise ImplementationError(
                f"Cannot add object with id of {object_data['id']} since it already exists in {array_key}."
            )

        # If not found, we can add the new object
        nested_array.append(object_data)
        self.current_move[array_key] = nested_array

    def _add_nested_array_to_mto(self, object_key, object_data):
        for item in object_data:
            self._add_nested_object_to_mto(object_key, item)

    @staticmethod
    def _get_nested_array_name(object_key):
        # Based on the object key, find the right array for nested objects in the mto
        nested_array_names = {
            MTO_SERVICE_ITEM: "mtoServiceItems",
            MTO_SHIPMENT: "mtoShipments",
            PAYMENT_REQUEST: "paymentRequests",
        }
        return nested_array_names[object_key]

    def _update_nested_object_in_mto(self, object_key, old_data, new_data):
        """Replaces an object in an array directly nested under the MTO.
        Can be used for mtoServiceItems, mtoShipments and mtoPaymentRequests
        as they are all held in top level arrays.
        Cannot be used for mtoAgent as it is nested further within the mtoShipment
        """
        # Replacement object should be associated with the current move, we assume it has a moveTaskOrderID field to
        # check
        if old_data["moveTaskOrderID"] != self.current_move["id"]:
            raise ImplementationError(
                (
                    f"Cannot add object to store because its moveTaskOrderID of {old_data['moveTaskOrderID']} "
                    f"does not match the current move's id of {self.current_move['id']}."
                )
            )

        # Get the nested array from the current move, or None if it doesn't exist
        array_key = self._get_nested_array_name(object_key)
        nested_array = self.current_move.get(array_key)

        # If nested array does not exist or is empty, raise error, we should have found the object to replace
        if not nested_array:
            raise ImplementationError(f"Cannot find {object_key} of id {old_data['id']} to replace in {array_key}")

        # Find item and replace it!
        found = False
        for idx, elem in enumerate(nested_array):
            if elem["id"] == old_data["id"]:
                nested_array[idx] = new_data
                found = True
                break

        if not found:
            raise ImplementationError(f"Cannot find {object_key} of id {old_data['id']} to replace in {array_key}")

        self.current_move[array_key] = nested_array

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
