# -*- coding: utf-8 -*-
import logging

from locust import tag, task

from .prime import PrimeTasks, SupportTasks
from utils.constants import MOVE_TASK_ORDER

logger = logging.getLogger(__name__)


@tag("endpointWorkflows")
class PrimeEndpointWorkflowsTasks(PrimeTasks, SupportTasks):
    """Workflow Task Set
    Each task is a workflow from start to finish. Each workflow acts on only one MTO from start to finish.
    There are multiple workflows for different scenarios such as a single shipment HHG move, or an HHG move with a SIT.
    Multiple instances of the tasks will run during load testing and will interleave their hits to the server.
    However they will run in sequence and should all complete without any errors.
    """

    # workflow_title is a descriptor that can be used in logging anywhere in the workflow
    workflow_title = None

    # WORKFLOWS
    @tag("createMTOShipmentWorkflow")
    @task
    def create_mto_shipment_workflow(self):
        """
        This is a basic workflow that checks if there is an existing move, then calls the create_mto_shipment endpoint.
        """
        self.workflow_title = "create_mto_shipment endpoint"

        # Ensure there is a move avaliable for a shipment
        if not self._get_move():
            return

        # Set shipment type to HHG, so there can be multiple shipments on the same move
        overrides = {"shipmentType": "HHG"}
        shipment = super().create_mto_shipment(overrides)
        logger.info(f"{self.workflow_title} - Created shipment {shipment['id'][:8]}")

    def _get_move(self):
        move_task_order = super().get_stored(MOVE_TASK_ORDER)
        if not move_task_order:
            if not self.has_all_default_mto_ids():
                super().fetch_mto_updates()
            move_task_order = super().create_move_task_order()
        if not move_task_order:
            logger.debug(f"{self.workflow_title} ⚠️ No move_task_order returned or created")
            return None
        return move_task_order