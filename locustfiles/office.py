# -*- coding: utf-8 -*-
""" Locust test for the MilMove Office interface. """
from locust import HttpUser, between

from utils.hosts import MilMoveHostMixin, MilMoveDomain
from utils.parsers import GHCAPIParser
from tasks import ServicesCounselorTasks, TOOTasks

ghc_api = GHCAPIParser()


class ServicesCounselorUser(MilMoveHostMixin, HttpUser):
    """
    Tests the MilMove Office app with the Services Counselor role.
    """

    local_protocol = "http"
    local_port = "8080"

    deployed_subdomain = "office"

    domain = MilMoveDomain.OFFICE

    # This attribute is used for generating fake requests when hitting the GHC API:
    parser = ghc_api

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

    # This attribute is used for generating fake requests when hitting the GHC API:
    parser = ghc_api

    wait_time = between(0.25, 9)
    tasks = {TOOTasks: 1}
