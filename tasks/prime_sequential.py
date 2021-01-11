# -*- coding: utf-8 -*-
""" TaskSets and tasks for the Prime & Support APIs """
# import logging
# import json
# import random
from .prime import PrimeTasks, SupportTasks

from locust import tag, task, TaskSet

# from utils.constants import TEST_PDF, ZERO_UUID, PrimeObjects
# from .base import check_response, CertTaskMixin, ParserTaskMixin
# from copy import deepcopy


class SequentialWorkflowTaskSet(PrimeTasks, SupportTasks, TaskSet):
    """ Example of a workflow Sequential Task Set """

    # Set any attributes this task might need here
    current_move = None

    def get_random_data(self, object_key):
        """ Override the get_random_data function from PrimeDataTaskMixin """

        # Add in any custom steps needed here
        # Return whichever part of the move was requested - such as a shipment:
        return self.current_move

    def on_start(self):
        """
        We need to set up this task set with the sequential list of tasks we want to run. If we don't define this, the
        tasks will be run in the order they're written in PrimeTasks and SupportTasks - which is almost certainly NOT
        the correct order.
        """
        self.tasks = [
            self.hhg_move_workflow
            # ...and so on. List all the tasks you need in order. This should be the function name, but do not execute
            # the function - so no () parentheses after the function name.
        ]


@tag("workflow")
class WorkflowTasks(SequentialWorkflowTaskSet):
    """ Example of a workflow Sequential Task Set """

    move_id = None

    # No need to tag this function with @task because we are setting it as a task manually in the on_start function
    @tag("hhgMoveWorkflow")
    @task
    def hhg_move_workflow(self):
        """
        If you need to change a task for this workflow, override the base function and add in whatever custom logic you
        need.
        """
        self.on_start()
        self.create_hhg_move()
        # For example, maybe we just need to pass in overrides to this task:
        # super().create_mto_service_item(overrides={"reServiceCode": "DDFSIT"})

    def create_hhg_move(self):
        self.tasks = [self.hhg_move_workflow]
        mto = super().create_move_task_order()
        self.current_move = mto
        self.move_id = mto["id"]
        print(f"{self.move_id}: Create move")

        super().get_move_task_order()
        print(f"{self.move_id}: pack move")

        super().fetch_mto_updates()
        print(f"{self.move_id}: ship move")
