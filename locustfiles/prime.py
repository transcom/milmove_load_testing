# -*- coding: utf-8 -*-
""" Locust test for the Prime & Support APIs """
from locust import HttpUser, between, events
from locust.env import Environment

from tasks import PrimeTasks, SupportTasks
from utils.base import ImplementationError
from utils.constants import INTERNAL_API_KEY, PRIME_API_KEY
from utils.hosts import MilMoveDomain, MilMoveHostMixin, remove_certs, set_up_certs
from utils.parsers import InternalAPIParser, PrimeAPIParser, SupportAPIParser
from utils.types import LOCUST_RUNNER_TYPE

# init these classes just once because we don't need to parse the API over and over:
prime_api = PrimeAPIParser()
support_api = SupportAPIParser()
internal_api = InternalAPIParser()


class PrimeUser(MilMoveHostMixin, HttpUser):
    """
    Tests the Prime API.
    """

    # These attributes are used in MilMoveHostMixin to set up the proper hostname for any MilMove environment:
    local_port = "9443"
    domain = MilMoveDomain.PRIME  # the base domain for the host

    # This attribute is used for generating fake requests when hitting the Prime API:
    parser = {PRIME_API_KEY: prime_api, INTERNAL_API_KEY: internal_api}

    # These are locust HttpUser attributes that help define and shape the load test:
    wait_time = between(0.25, 9)  # the time period to wait in between tasks (in seconds, accepts decimals and 0)
    tasks = {PrimeTasks: 1}  # the set of tasks to be executed and their relative weight


class SupportUser(MilMoveHostMixin, HttpUser):
    """
    Tests the Support API.
    """

    local_port = "9443"
    domain = MilMoveDomain.PRIME

    parser = support_api

    wait_time = between(0.25, 9)
    tasks = {SupportTasks: 1}


@events.init.add_listener
def on_init(environment: Environment, runner: LOCUST_RUNNER_TYPE, **_kwargs) -> None:
    """
    Event hook that gets run after the locust environment has been set up. See docs for more info:
    https://docs.locust.io/en/stable/api.html?#locust.event.Events.init

    In our case, we're setting up certs.
    :param environment: locust environment.
    :param runner: locust runner that can be used to shut down the test run.
    :param _kwargs: Other kwargs we aren't using that are passed to hook functions.
    :return: None
    """
    try:
        set_up_certs(host=environment.host)
    except ImplementationError as err:
        # For some reason exceptions don't stop the runner automatically, so we have to do it
        # ourselves.
        runner.quit()

        raise err


@events.quitting.add_listener
def on_quitting(environment: Environment, **_kwargs):
    """
    Event hook that gets run when locust is shutting down.

    We're using it to clean up certs that were created during setup.
    :param environment: locust environment.
    :param _kwargs: Other kwargs we aren't using that are passed to hook functions.
    :return: None
    """
    remove_certs(host=environment.host)
