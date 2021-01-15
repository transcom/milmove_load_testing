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
class WorkflowTasks(PrimeTasks, SupportTasks):
    """Workflow Task Set
    Each task is a workflow from start to finish. Each workflow acts on only one MTO from start to finish.
    There are multiple workflows for different scenarios such as a single shipment HHG move, or an HHG move with a SIT.
    Multiple instances of the tasks will run during load testing and will interleave their hits to the server.
    However they will run in sequence and should all complete without any errors.
    """

    # current_move is the move the whole task will be acting on
    # all updates to the move and nested objects will be stored to this mto
    current_move = None
    # workflow_descriptor
    workflow_descriptor = None

    def on_start(self):
        """
        Runs on instantiation of each taskset.
        We need to set up this task set with the list of tasks/workflows we want to run. If we don't define this, all
        the tasks in PrimeTasks and SupportTasks will all be run independently and will likely have errors.
        """
        self.tasks = [self.hhg_move, self.fetch_mto_updates]

    # WORKFLOWS
    @tag("hhgMove")
    @task
    def hhg_move(self):
        """
        This is a basic HHG move workflow where we have one shipment and no additional requested service items.
        To create a new flow, copy this function, but don't forget to add the workflow to the tasks array in the on_start function
        """
        self.workflow_title = "HHG Move Basic"

        # Move steps for this workflow
        super().create_move_task_order()
        super().update_post_counseling_information()
        logger.info(f"{self.workflow_title} - Created move and completed counseling {self.current_move['id'][:8]}")

    # STORAGE FUNCTIONALITY
    """ We only store one current move in the sequential workflow and keep it updated as we move through the workflow.
        These functions override functions in the PrimeDataTaskMixin and will get automatically called by the tasks
        in PrimeTasks and SupportTasks.
    """

    def get_stored(self, object_key, id=None):
        """ Override the get_stored function from PrimeDataTaskMixin """

        # Return whichever part of the move was requested - such as a shipment:
        if object_key == MOVE_TASK_ORDER:
            return self.current_move

        if object_key == MTO_SHIPMENT:
            return self._get_mto_nested(object_key, id)

    def add_stored(self, object_key, object_data):
        """Adds the object to the main move."""

        # If it's a moveTaskOrder, we only keep track of one move per workflow, so add actually replaces.
        if object_key == MOVE_TASK_ORDER:
            self.current_move = object_data

        # If it's the following object types, we add them into nested array in the MTO
        elif object_key in [MTO_SHIPMENT, MTO_SERVICE_ITEM, PAYMENT_REQUEST]:
            self._add_to_mto_nested(object_key, object_data)

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
            self._update_mto_nested(object_key, old_data, new_data)

    def _add_to_mto_nested(self, object_key, object_data):
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
        array_key = self._get_array_name(object_key)
        nested_array = self.current_move.get(array_key, None)

        # If nested array is not an array create one
        if nested_array is None:
            nested_array = []

        # if item does not exist already, add it
        preexisting = list(filter(lambda elem: elem["id"] == object_data["id"], nested_array))
        if len(preexisting) == 0:
            nested_array.append(object_data)
            self.current_move[array_key] = nested_array
        else:
            raise ImplementationError(
                f"Cannot add object with id of {object_data['id']} since it already exists in {array_key}."
            )

    def _get_array_name(self, object_key):
        # Based on the object key, find the right array for nested objects in the mto
        object_array_map = {
            MTO_SERVICE_ITEM: "mtoServiceItems",
            MTO_SHIPMENT: "mtoShipments",
            PAYMENT_REQUEST: "paymentRequests",
        }
        try:
            array_key = object_array_map[object_key]
        except KeyError:
            logger.exception(f"An unexpected type of {object_key} was passed into _add_to_mto_nested")
            return None
        return array_key

    def _update_mto_nested(self, object_key, old_data, new_data):
        """Replaces an object in an array directly nested under the MTO.
        Can be used for mtoServiceItems, mtoShipments and mtoPaymentRequests
        as they are all held in top level arrays.
        Cannot be used for mtoAgent as it is nested further within the mtoShipment
        """
        # Replacement object should be associated with the current move, we assume it has a moveTaskOrderID field to check
        if old_data["moveTaskOrderID"] != self.current_move["id"]:
            raise ImplementationError(
                (
                    f"Cannot add object to store because its moveTaskOrderID of {old_data['moveTaskOrderID']} "
                    f"does not match the current move's id of {self.current_move['id']}."
                )
            )

        # Get the nested array from the current move, or None if it doesn't exist
        array_key = self._get_array_name(object_key)
        nested_array = self.current_move.get(array_key, None)

        # If nested array does not exist or is empty, raise error, we should have found the object to replace
        if nested_array is None or nested_array == []:
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

    def _get_mto_nested(self, object_key, id):
        """Return object of type requested. If no id is provided return a random element.
        If id is provided, return the specific element or raise error
        """

        # Get the nested array from the current move, or None if it doesn't exist
        array_key = self._get_array_name(object_key)
        nested_array = self.current_move.get(array_key, None)

        # If nested array does not exist or is empty, return None
        if nested_array is None or nested_array == []:
            return None

        # If id was provided return the specific object or None
        requested_object = None
        if id:
            for elem in nested_array:
                if elem["id"] == id:
                    requested_object = elem
                    break
        # If id was not provided select an object at random
        else:
            requested_object = random.choice(nested_array)

        return requested_object
