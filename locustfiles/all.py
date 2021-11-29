# -*- coding: utf-8 -*-
""" Locust test for all APIs """
from locust import HttpUser, between, events

from utils.hosts import MilMoveHostMixin, MilMoveDomain, clean_milmove_host_users
from utils.parsers import GHCAPIParser, PrimeAPIParser, SupportAPIParser
from tasks import PrimeTasks, SupportTasks, ServicesCounselorTasks, TOOTasks

from gevent.pool import Group


# init these classes just once because we don't need to parse the API over and over:
prime_api = PrimeAPIParser()
support_api = SupportAPIParser()
ghc_api = GHCAPIParser()


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


class ServicesCounselorUser(MilMoveHostMixin, HttpUser):
    """
    Tests the MilMove Office app with the Services Counselor role.
    """

    local_protocol = "http"
    local_port = "8080"
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
    domain = MilMoveDomain.OFFICE

    # This attribute is used for generating fake requests when hitting the GHC API:
    parser = ghc_api

    wait_time = between(0.25, 9)
    tasks = {TOOTasks: 1}


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    """
    Clean up steps to run when the load test stops. Removes any cert files that may have been created during the setup.
    """
    clean_milmove_host_users(locust_env=kwargs["environment"])


@events.init_command_line_parser.add_listener
def on_locust_command(parser, **_kwargs):
    parser.add_argument(
        "--prime-user-weight", env_var="PRIME_USER_WEIGHT", type=int, default=1, help="Weight for Prime user"
    )
    parser.add_argument(
        "--services-counselor-user-weight",
        env_var="SERVICES_COUNSELOR_USER_WEIGHT",
        type=int,
        default=1,
        help="Weight for Services Counselor user",
    )
    parser.add_argument(
        "--support-user-weight", env_var="SUPPORT_USER_WEIGHT", type=int, default=1, help="Weight for Support user"
    )
    parser.add_argument("--too-user-weight", env_var="TOO_USER_WEIGHT", type=int, default=1, help="Weight for TOO user")


@events.test_start.add_listener
def on_test_start(environment, **_kwargs):
    prime_class = PrimeUser
    services_counselor_class = ServicesCounselorUser
    support_class = SupportUser
    too_class = TOOUser

    prime_class.weight = environment.parsed_options.prime_user_weight
    services_counselor_class.weight = environment.parsed_options.services_counselor_user_weight
    support_class.weight = environment.parsed_options.support_user_weight
    too_class.weight = environment.parsed_options.too_user_weight

    environment.user_classes = [
        prime_class,
        services_counselor_class,
        support_class,
        too_class,
    ]
    environment._remove_user_classes_with_weight_zero()

    # if the user classes change between runs (because user classes
    # with 0 weights have been removed), we have to do some manual /
    # hacky cleanups
    setattr(environment.runner, "target_user_classes_count", {})
    setattr(environment.runner, "target_user_count", 0)
    setattr(environment.runner, "_users_dispatcher", None)
    setattr(environment.runner, "user_greenlets", Group())
