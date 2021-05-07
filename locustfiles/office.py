# -*- coding: utf-8 -*-
""" Locust test for the MilMove Office interface. """
from locust import HttpUser, between

from utils.hosts import MilMoveHostMixin, MilMoveDomain
from utils.parsers import GHCAPIParser
from tasks import OfficeTasks

ghc_api = GHCAPIParser()


class OfficeUser(MilMoveHostMixin, HttpUser):
    """
    Tests the MilMove Office app.
    """

    local_protocol = "http"
    local_port = "3000"
    domain = MilMoveDomain.OFFICE

    # This attribute is used for generating fake requests when hitting the GHC API:
    parser = ghc_api

    wait_time = between(1, 9)
    tasks = {OfficeTasks: 1}
