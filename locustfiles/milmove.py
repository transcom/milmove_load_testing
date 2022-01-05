# -*- coding: utf-8 -*-
""" Locust test for the MilMove Customer Signup interface. """
from locust import HttpUser, between

from tasks import MilMoveTasks
from utils.hosts import MilMoveDomain, MilMoveHostMixin


class MilMoveUser(MilMoveHostMixin, HttpUser):
    """
    Tests the MilMove app.
    """

    local_protocol = "http"
    local_port = "8080"

    deployed_subdomain = "my"

    domain = MilMoveDomain.MILMOVE

    wait_time = between(1, 9)
    tasks = {MilMoveTasks: 1}
