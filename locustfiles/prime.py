# -*- coding: utf-8 -*-
""" Locust test for the Prime & Support APIs """
from locust import HttpUser, between, events
from locust.env import Environment, RunnerType

from tasks import PrimeTasks, SupportTasks
from utils.auth import remove_certs, set_up_certs
from utils.base import ImplementationError, MilMoveEnv


class PrimeUser(HttpUser):
    """
    Tests the Prime API.
    """

    tasks = {PrimeTasks: 1}
    wait_time = between(0.25, 9)


class SupportUser(HttpUser):
    """
    Tests the Support API.
    """

    tasks = {SupportTasks: 1}
    wait_time = between(0.25, 9)


@events.init.add_listener
def on_init(environment: Environment, runner: RunnerType, **_kwargs) -> None:
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
        milmove_env = MilMoveEnv(value=environment.host)
    except ValueError as err:
        # For some reason exceptions don't stop the runner automatically, so we have to do it
        # ourselves.
        runner.quit()

        raise err

    try:
        set_up_certs(env=milmove_env)
    except ImplementationError as err:
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
    try:
        milmove_env = MilMoveEnv(value=environment.host)
    except ValueError as err:
        # This should in theory never happen since a similar check is done on init, but just in
        # case...
        environment.runner.quit()

        raise err

    remove_certs(env=milmove_env)
