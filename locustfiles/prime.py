# -*- coding: utf-8 -*-
""" Locust test for the Prime & Support APIs """
from locust import HttpUser, between, events

from utils.hosts import MilMoveHostMixin, MilMoveDomain, clean_milmove_host_users
from utils.parsers import PrimeAPIParser, SupportAPIParser
from tasks import PrimeTasks, SupportTasks

# init these classes just once because we don't need to parse the API over and over:
prime_api = PrimeAPIParser()
support_api = SupportAPIParser()


class PrimeUser(MilMoveHostMixin, HttpUser):
    """
    Tests the Prime API.
    """

    # These attributes are used in MilMoveHostMixin to set up the proper hostname for any MilMove environment:
    local_port = "9443"
    domain = MilMoveDomain.PRIME  # the base domain for the host
    is_api = True  # if True, uses the api base domain in deployed environments

    # This attribute is used for generating fake requests when hitting the Prime API:
    parser = prime_api

    # These are locust HttpUser attributes that help define and shape the load test:
    wait_time = between(0.25, 9)  # the time period to wait in between tasks (in seconds, accepts decimals and 0)
    tasks = {PrimeTasks: 1}  # the set of tasks to be executed and their relative weight


class SupportUser(MilMoveHostMixin, HttpUser):
    """
    Tests the Support API.
    """

    local_port = "9443"
    domain = MilMoveDomain.PRIME
    is_api = True

    parser = support_api

    wait_time = between(0.25, 9)
    tasks = {SupportTasks: 1}


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    """
    Clean up steps to run when the load test stops. Removes any cert files that may have been created during the setup.
    """
    clean_milmove_host_users(locust_env=kwargs["environment"])
