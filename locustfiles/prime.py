# -*- coding: utf-8 -*-
""" Locust test for the Prime & Support APIs """
from locust import HttpUser, between

from utils.constants import MilMoveDomain, LOCAL_TLS_CERT_KWARGS
from utils.hosts import MilMoveHostMixin
from utils.parsers import PrimeAPIParser, SupportAPIParser
from tasks import PrimeTasks, SupportTasks

# init these classes just once because we don't need to parse the API over and over:
prime_api = PrimeAPIParser()
support_api = SupportAPIParser()


class PrimeUser(MilMoveHostMixin, HttpUser):
    """
    Tests the Prime API.
    """

    local_port = "9443"
    domain = MilMoveDomain.PRIME  # the base domain for the host
    is_api = True  # if True, uses the api base domain in deployed environments

    # cert_kwargs are used by CertTaskMixin for verifying requests:
    cert_kwargs = LOCAL_TLS_CERT_KWARGS  # TODO will need to be handled differently for staging/experimental
    parser = prime_api

    wait_time = between(0.25, 9)  # the time period to wait in between tasks (in seconds, accepts decimals and 0)
    tasks = {PrimeTasks: 1}  # the set of tasks to be executed and their relative weight
    weight = 5


class SupportUser(MilMoveHostMixin, HttpUser):
    """
    Tests the Support API.
    """

    local_port = "9443"
    domain = MilMoveDomain.PRIME
    is_api = True

    cert_kwargs = LOCAL_TLS_CERT_KWARGS  # TODO will need to be handled differently for staging/experimental
    parser = support_api

    wait_time = between(0.25, 9)
    tasks = {SupportTasks: 1}
    weight = 1
