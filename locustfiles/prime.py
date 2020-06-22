# -*- coding: utf-8 -*-
""" Locust test for the Prime & Support APIs """
from locust import HttpUser, between

from utils.constants import MilMoveDomain, PRIME_CERT_KWARGS
from utils.mixins import MilMoveHostMixin
from tasks import PrimeTasks, SupportTasks


class PrimeUser(MilMoveHostMixin, HttpUser):
    """
    Tests the Prime API.
    """

    local_port = "9443"
    domain = MilMoveDomain.PRIME  # the base domain for the host
    is_api = True  # if True, uses the api base domain in deployed environments
    # cert_kwargs are used by CertTaskSet for verifying requests:
    cert_kwargs = PRIME_CERT_KWARGS  # TODO will need to be handled differently for staging/experimental

    wait_time = between(0.25, 9)  # the time period to wait in between tasks (in seconds, accepts decimals and 0)
    tasks = {PrimeTasks: 1}  # the set of tasks to be executed and their relative weight


class SupportUser(MilMoveHostMixin, HttpUser):
    """
    Tests the Support API.
    """

    local_port = "9443"
    domain = MilMoveDomain.PRIME
    is_api = True
    cert_kwargs = PRIME_CERT_KWARGS  # TODO will need to be handled differently for staging/experimental

    wait_time = between(1, 9)
    tasks = {SupportTasks: 1}
