# -*- coding: utf-8 -*-
from locust import HttpUser, between

from utils.mixins import MilMoveHostMixin
from utils.constants import MilMoveDomain, PRIME_CERT_KWARGS, PRIME_API_KEY, SUPPORT_API_KEY
from tasks import WorkflowTasks
from utils.parsers import SupportAPIParser, PrimeAPIParser

support_api = SupportAPIParser()
prime_api = PrimeAPIParser()


class WorkflowUser(MilMoveHostMixin, HttpUser):
    """This is the Workflow user that will be calling the workflows in prime_workflow.py.
    This user needs access to both prime and support apis.
    """

    local_port = "9443"
    domain = MilMoveDomain.PRIME  # the base domain for the host
    is_api = True  # if True, uses the api base domain in deployed environments

    # cert_kwargs are used by CertTaskMixin for verifying requests:
    cert_kwargs = PRIME_CERT_KWARGS  # TODO will need to be handled differently for staging/experimental

    wait_time = between(0.25, 9)  # the time period to wait in between tasks (in seconds, accepts decimals and 0)
    weight = 1
    parser = {PRIME_API_KEY: prime_api, SUPPORT_API_KEY: support_api}

    # For the tasks, we can define all the workflow tasksets we have set up:
    tasks = {WorkflowTasks: 1}
    weight = 1
