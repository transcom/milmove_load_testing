# -*- coding: utf-8 -*-
""" Locust test for the MilMove Office interface. """
from locust import HttpUser, between

from tasks import ServicesCounselorTasks, TOOTasks
from utils.hosts import MilMoveDomain, MilMoveHostMixin


class ServicesCounselorUser(MilMoveHostMixin, HttpUser):
    """
    Tests the MilMove Office app with the Services Counselor role.
    """

    local_protocol = "http"
    local_port = "8080"

    deployed_subdomain = "office"

    domain = MilMoveDomain.OFFICE

    wait_time = between(0.25, 9)
    tasks = {ServicesCounselorTasks: 1}


class TOOUser(MilMoveHostMixin, HttpUser):
    """
    Tests the MilMove Office app with the TOO role.
    """

    local_protocol = "http"
    local_port = "8080"

    deployed_subdomain = "office"

    domain = MilMoveDomain.OFFICE

    wait_time = between(0.25, 9)
    tasks = {TOOTasks: 1}
