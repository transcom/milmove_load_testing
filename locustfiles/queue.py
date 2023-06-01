# -*- coding: utf-8 -*-
""" Locust test for all APIs """

import os

from flask import Blueprint, render_template_string
from gevent.pool import Group
from locust import between, events, task
from locust.env import Environment, RunnerType

from utils.auth import remove_certs, set_up_certs, UserType
from utils.base import ImplementationError, MilMoveEnv
from utils.flows import WorkerQueueType
from utils.flows.simple_hhg import SingleHHGFlow, DoubleHHGFlow, NTSFlow, SingleHHGMultiplePaymentRequestFlow
from utils.request import RequestHost
from utils.queue_user import QueueUser, OfficeQueueUser


class MilMoveHHGUser(QueueUser):
    """
    Tests the internal HHG API.
    """

    request_host = RequestHost.MY
    wait_time = between(0.25, 9)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @task(2)
    def start_single_hhg_flow(self):
        """
        Kicks off a flow where the customer creates a single HHG shipment
        """
        f = SingleHHGFlow()
        self.run_flow(f)

    @task(1)
    def start_double_hhg_flow(self):
        """
        Kicks off a flow where the customer creates two seperate HHG shipments
        """
        f = DoubleHHGFlow()
        self.run_flow(f)

    @task(1)
    def start_nts_flow(self):
        """
        Kicks off a flow where the customer creates a single NTS shipment
        """
        f = NTSFlow()
        self.run_flow(f)

    @task(1)
    def start_hhg_multiple_payment_request_flow(self):
        """
        Kicks off a flow where the customer creates a HHG shipment and the Prime
        creates multiple payment requests for it.
        """
        f = SingleHHGMultiplePaymentRequestFlow()
        self.run_flow(f)


class ServiceCounselorUser(OfficeQueueUser):
    """
    Tests the GHC SC API.
    """

    user_type = UserType.SERVICE_COUNSELOR
    wait_time = between(0.25, 9)

    @task
    def task_sc(self):
        """
        run from the queue
        """

        self.run_from_queue(WorkerQueueType.SERVICE_COUNSELOR)


class TOOUser(OfficeQueueUser):
    """
    Tests the GHC TOO API.
    """

    user_type = UserType.TOO
    wait_time = between(0.25, 9)

    @task
    def task_too(self):
        """
        run from the queue
        """

        self.run_from_queue(WorkerQueueType.TOO)


class TIOUser(OfficeQueueUser):
    """
    Tests the GHC TIO API.
    """

    user_type = UserType.TIO
    wait_time = between(0.25, 9)

    @task
    def task_tio(self):
        """
        run from the queue
        """

        self.run_from_queue(WorkerQueueType.TIO)


class PrimeUser(QueueUser):
    """
    Tests the Prime API.
    """

    certs_required = True
    request_host = RequestHost.PRIME
    wait_time = between(0.25, 9)

    @task
    def run_prime(self):
        """
        run from the queue
        """

        self.run_from_queue(WorkerQueueType.PRIME)


extend = Blueprint(
    "extend",
    "deployed_version",
)


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

    if environment.web_ui:
        # this code is only run on the master node (the web_ui
        # instance doesn't exist on workers)

        @extend.route("/deployed-version")
        def deployed_version():
            """
            Add route to access the extended web UI with our new tab.
            """
            # ensure the template_args are up to date before using
            # them
            environment.web_ui.update_template_args()  # type: ignore
            git_commit = os.getenv("GIT_COMMIT", "UNKNOWN")
            return render_template_string(
                """
            {% block extended_panes %}
            <pre>{{ git_commit }}</pre>
            {% endblock extended_panes %}
            """,
                git_commit=git_commit,
            )

        # register our new routes and extended UI with the Locust web UI
        environment.web_ui.app.register_blueprint(extend)  # type: ignore


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
        environment.runner.quit()  # type: ignore

        raise err

    remove_certs(env=milmove_env)


@events.init_command_line_parser.add_listener
def on_locust_command(parser, **_kwargs):
    parser.add_argument(
        "--prime-user-weight",
        env_var="PRIME_USER_WEIGHT",
        type=int,
        default=1,
        help="Weight for Prime user",
    )
    parser.add_argument(
        "--milmove-hhg-user-weight",
        env_var="MILMOVE_HHG_USER_WEIGHT",
        type=int,
        default=1,
        help="Weight for MilMove HHG user",
    )
    parser.add_argument(
        "--services-counselor-user-weight",
        env_var="SERVICES_COUNSELOR_USER_WEIGHT",
        type=int,
        default=1,
        help="Weight for Services Counselor user",
    )
    parser.add_argument("--tio-user-weight", env_var="TIO_USER_WEIGHT", type=int, default=1, help="Weight for TIO user")
    parser.add_argument("--too-user-weight", env_var="TOO_USER_WEIGHT", type=int, default=1, help="Weight for TOO user")


@events.test_start.add_listener
def on_test_start(environment, **_kwargs):
    milmove_hhg_class = MilMoveHHGUser
    prime_class = PrimeUser
    tio_class = TIOUser
    too_class = TOOUser
    services_counselor_class = ServiceCounselorUser

    milmove_hhg_class.weight = environment.parsed_options.milmove_hhg_user_weight
    prime_class.weight = environment.parsed_options.prime_user_weight
    services_counselor_class.weight = environment.parsed_options.services_counselor_user_weight
    tio_class.weight = environment.parsed_options.tio_user_weight
    too_class.weight = environment.parsed_options.too_user_weight

    environment.user_classes = [
        milmove_hhg_class,
        prime_class,
        services_counselor_class,
        tio_class,
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
