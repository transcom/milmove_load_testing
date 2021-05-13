# -*- coding: utf-8 -*-
""" Locust test for the MilMove Customer Signup interface. """
from locust import HttpUser, between, events

from utils.hosts import MilMoveHostMixin, MilMoveDomain, clean_milmove_host_users
from utils.parsers import InternalAPIParser, SupportAPIParser
from tasks import MilMoveTasks

internal_api = InternalAPIParser()
support_api = SupportAPIParser()


class MilMoveUser(MilMoveHostMixin, HttpUser):
    """
    Tests the MilMove app.
    """

    # These attributes are used in MilMoveHostMixin to set up the proper hostname for any MilMove environment:
    local_protocol = "http"
    domain = MilMoveDomain.MILMOVE
    is_api = True  # if True, uses the api base domain in deployed environments

    # This attribute is used for generating fake requests when hitting the Internal API:
    parser = internal_api

    # These are locust HttpUser attributes that help define and shape the load test:
    wait_time = between(1, 9)  # the time period to wait in between tasks (in seconds, accepts decimals and 0)
    tasks = {MilMoveTasks: 1}  # the set of tasks to be executed and their relative weight


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    """
    Clean up steps to run when the load test stops. Removes any cert files that may have been created during the setup.
    """
    clean_milmove_host_users(locust_env=kwargs["environment"])
