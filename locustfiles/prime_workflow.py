# -*- coding: utf-8 -*-
from locust import HttpUser, between

from tasks.prime_endpoint_workflows import PrimeEndpointWorkflowsTasks
from tasks.prime_hhg_workflow import PrimeWorkflowTasks
from utils.hosts import MilMoveDomain, MilMoveHostMixin


class PrimeWorkflowUser(MilMoveHostMixin, HttpUser):
    """This is the Workflow user that will be calling the workflows in prime_workflow.py.
    This user needs access to both prime and support apis.
    """

    local_port = "9443"
    domain = MilMoveDomain.PRIME  # the base domain for the host

    wait_time = between(0.25, 9)  # the time period to wait in between tasks (in seconds, accepts decimals and 0)
    weight = 1

    # For the tasks, we can define all the workflow tasksets we have set up:
    tasks = {PrimeWorkflowTasks: 1, PrimeEndpointWorkflowsTasks: 1}
