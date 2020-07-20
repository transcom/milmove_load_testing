# -*- coding: utf-8 -*-
""" Locust test for the MilMove Customer Signup interface. """
from locust import HttpUser, between

from utils.constants import MilMoveDomain
from utils.mixins import MilMoveHostMixin
from tasks import MilMoveTasks


class MilMoveUser(MilMoveHostMixin, HttpUser):
    """
    Tests the MilMove app.
    """

    local_protocol = "http"
    domain = MilMoveDomain.MILMOVE

    wait_time = between(1, 9)
    tasks = {MilMoveTasks: 1}
