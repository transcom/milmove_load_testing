# -*- coding: utf-8 -*-
from locust import HttpUser, between

from tasks.prime_endpoint_workflows import PrimeEndpointWorkflowsTasks
from tasks.prime_hhg_workflow import PrimeWorkflowTasks


class PrimeWorkflowUser(HttpUser):
    """This is the Workflow user that will be calling the workflows in prime_workflow.py.
    This user needs access to both prime and support apis.
    """

    tasks = {PrimeWorkflowTasks: 1, PrimeEndpointWorkflowsTasks: 1}
    wait_time = between(0.25, 9)
    weight = 1
