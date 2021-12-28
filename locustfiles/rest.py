# -*- coding: utf-8 -*-
""" Locust test for the Prime & Support APIs """

from locust import between, events, tag, task
from locust.env import Environment

from tasks.prime import get_prime_moves
from utils.auth import remove_certs, set_up_certs
from utils.base import ImplementationError, MilMoveEnv, convert_host_string_to_milmove_env
from utils.constants import MOVE_TASK_ORDER
from utils.request import MilMoveURLCreator, get_cert_kwargs
from utils.rest import RestResponseContextManager
from utils.types import LOCUST_RUNNER_TYPE
from utils.users import RestHttpUser


class PrimeUser(RestHttpUser):
    """
    A user that can test the Prime API
    """

    certs_needed = True

    # These are locust HttpUser attributes that help define and shape the load test:
    wait_time = between(0.25, 9)  # the time period to wait in between tasks (in seconds,
    # accepts decimals and 0)
    # tasks = {PrimeTasks: 1}  # the set of tasks to be executed and their relative weight

    @tag(MOVE_TASK_ORDER, "listMoves")
    @task
    def list_moves(self) -> None:
        with self.rest("GET", self.get_prime_path("/moves")) as resp:
            resp: RestResponseContextManager

            if isinstance(resp.js, list) and resp.js:
                print(f"\n{resp.js[0]=}\n")
            else:
                print("No moves found.")


def set_up_for_prime_load_tests(env: MilMoveEnv) -> None:
    """
    Sample of func that can set up or get data before tests start.
    :param env: MilMoveEnv that we're targeting, e.g. MilMoveEnv.LOCAL
    """
    url_creator = MilMoveURLCreator(env=env)

    cert_kwargs = get_cert_kwargs(env=env)

    moves = get_prime_moves(url_creator=url_creator, cert_kwargs=cert_kwargs)

    if moves:
        print(f"\n{moves[0]=}\n")
    else:
        print("No moves found.")


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

    try:
        milmove_env = convert_host_string_to_milmove_env(host=environment.host)
    except ImplementationError as err:
        runner.quit()

        raise err

    try:
        set_up_for_prime_load_tests(env=milmove_env)
    except Exception as err:
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
