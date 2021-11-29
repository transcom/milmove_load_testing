# -*- coding: utf-8 -*-
""" Locust test for all APIs """
from locust import events

from utils.hosts import clean_milmove_host_users
from utils.parsers import GHCAPIParser, PrimeAPIParser, SupportAPIParser

from prime import PrimeUser, SupportUser
from prime_workflow import PrimeWorkflowUser
from office import ServicesCounselorUser, TOOUser

from gevent.pool import Group

########################################################################
#
#  TODO: This file contains all the users in one place. If a user is
#  created in another locustfile, it should be added here along with a
#  custom argument for controlling the weight
#
#  Maybe we should just consolidate all user definitions into this
#  file, or maybe we should move the user definitions elsewhere?
#
########################################################################


# init these classes just once because we don't need to parse the API over and over:
prime_api = PrimeAPIParser()
support_api = SupportAPIParser()
ghc_api = GHCAPIParser()


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
        "--prime-workflow-user-weight",
        env_var="PRIME_WORKFLOW_USER_WEIGHT",
        type=int,
        default=1,
        help="Weight for Prime Workflow user",
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
    prime_workflow_class = PrimeWorkflowUser
    services_counselor_class = ServicesCounselorUser
    support_class = SupportUser
    too_class = TOOUser

    prime_class.weight = environment.parsed_options.prime_user_weight
    prime_workflow_class.weight = environment.parsed_options.prime_workflow_user_weight
    services_counselor_class.weight = environment.parsed_options.services_counselor_user_weight
    support_class.weight = environment.parsed_options.support_user_weight
    too_class.weight = environment.parsed_options.too_user_weight

    environment.user_classes = [
        prime_class,
        prime_workflow_class,
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
