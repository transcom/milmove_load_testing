# -*- coding: utf-8 -*-
from locust import HttpUser, between

from utils.hosts import MilMoveHostMixin, MilMoveDomain
from utils.constants import PRIME_API_KEY, SUPPORT_API_KEY
from tasks.prime_hhg_workflow import PrimeWorkflowTasks
from tasks.prime_endpoint_workflows import PrimeEndpointWorkflowsTasks
from utils.parsers import SupportAPIParser, PrimeAPIParser

support_api = SupportAPIParser()
prime_api = PrimeAPIParser()


class PrimeWorkflowUser(MilMoveHostMixin, HttpUser):
    """This is the Workflow user that will be calling the workflows in prime_workflow.py.
    This user needs access to both prime and support apis.
    """

    local_port = "9443"
    domain = MilMoveDomain.PRIME  # the base domain for the host

    wait_time = between(0.25, 9)  # the time period to wait in between tasks (in seconds, accepts decimals and 0)
    weight = 1
    parser = {PRIME_API_KEY: prime_api, SUPPORT_API_KEY: support_api}

    # For the tasks, we can define all the workflow tasksets we have set up:
    tasks = {PrimeWorkflowTasks: 1, PrimeEndpointWorkflowsTasks: 1}
