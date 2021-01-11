# -*- coding: utf-8 -*-
from locust import HttpUser, between

from utils.mixins import MilMoveHostMixin
from utils.constants import MilMoveDomain, PRIME_CERT_KWARGS
from tasks import WorkflowTasks
from utils.parsers import SupportAPIParser

support_api = SupportAPIParser()


# Then, in the prime_sequential.py, define a user like so:
class WorkflowUser(MilMoveHostMixin, HttpUser):
    """ This is the Prime user that will be calling the workflow task sets. """

    # We will set all the attributes we need to work with the Prime API, see the user classes in prime.py

    local_port = "9443"
    domain = MilMoveDomain.PRIME  # the base domain for the host
    is_api = True  # if True, uses the api base domain in deployed environments

    # cert_kwargs are used by CertTaskMixin for verifying requests:
    cert_kwargs = PRIME_CERT_KWARGS  # TODO will need to be handled differently for staging/experimental

    wait_time = between(0.25, 9)  # the time period to wait in between tasks (in seconds, accepts decimals and 0)
    weight = 1
    parser = support_api

    # For the tasks, we can define all the workflow tasksets we have set up:
    tasks = {WorkflowTasks: 1}
    weight = 1
