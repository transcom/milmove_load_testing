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
    domain = MilMoveDomain.PRIME
    is_api = True
    cert_kwargs = PRIME_CERT_KWARGS  # TODO will need to be handled differently for staging/experimental

    wait_time = between(1, 9)
    tasks = {PrimeTasks: 1}


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
