# -*- coding: utf-8 -*-
""" Locust test for the MilMove Office interface. """
from locust import HttpUser, between

from utils.constants import MilMoveDomain
from utils.hosts import MilMoveHostMixin
from tasks import OfficeTasks


class OfficeUser(MilMoveHostMixin, HttpUser):
    """
    Tests the MilMove Office app.
    """

    local_protocol = "http"
    domain = MilMoveDomain.OFFICE

    wait_time = between(1, 9)
    tasks = {OfficeTasks: 1}
