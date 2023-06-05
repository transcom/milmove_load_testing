# -*- coding: utf-8 -*-
import typing

from locust import User
from locust.clients import HttpSession
import urllib3

from utils.auth import create_user, UserType
from utils.base import MilMoveEnv
from utils.flows import MemoryFlowQueue, QueuableFlow, WorkerQueueType
from utils.request import MilMoveRequestPreparer, RequestHost

# global memory queue used by all QueueUsers
global_queue = MemoryFlowQueue()


class QueueUser(User):
    """
    Abstract class that runs flows from a queue. Not subclassed
    from HttpUser so we can set up the HttpSession (aka client)
    manually

    """

    abstract = True
    certs_required = False

    # request_host needs to be set by subclasses
    request_host: typing.Optional[RequestHost]

    # This is initialized as part of the constructor
    client: HttpSession

    # This is initialized as part of the constructor
    request_preparer: MilMoveRequestPreparer

    def __init__(self, *args, **kwargs):
        if not self.request_host:
            raise Exception("Cannot initialize QueueUser, request_host not set")

        super().__init__(*args, **kwargs)
        # at this point, after the User constructor is run, we can set
        # up the client
        milmove_env = MilMoveEnv(value=self.environment.host)
        self.request_preparer = MilMoveRequestPreparer(milmove_env)

        num_users = 10
        if self.environment.parsed_options.num_users:
            num_users = self.environment.parsed_options.num_users

            # as a rough approximation, use a pool size that is 1/3 of the
            # number of users, as we have service members, office users,
            # and the prime, but make sure we have at least 4
        pool_size = max(4, int(num_users / 3))
        pool_manager = urllib3.PoolManager(
            num_pools=pool_size,
            maxsize=pool_size,
        )

        self.client = HttpSession(
            base_url=self.request_preparer.base_url(self.request_host),
            request_event=self.environment.events.request,
            user=self,
            pool_manager=pool_manager,
        )

    def run_from_queue(self, worker_queue_type: WorkerQueueType) -> None:
        flow = global_queue.pop(worker_queue_type)

        if flow:
            self.run_flow(flow)
        else:
            self.run_when_empty_queue()

    def run_flow(self, flow: QueuableFlow) -> None:
        if flow.run(self.request_preparer, self.client):
            global_queue.enqueue_next(flow)
        else:
            # this flow is done
            pass

    def run_when_empty_queue(self) -> None:
        pass


class OfficeQueueUser(QueueUser):
    """
    Queue User for the office app. Creates a user once on initialization
    """

    abstract = True
    request_host = RequestHost.OFFICE
    # user_type needs to be set by subclasses
    user_type: typing.Optional[UserType]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.user_type:
            raise Exception("user_type needs to be set")

        if not create_user(self.request_preparer, self.client, self.user_type):
            raise Exception("Cannot create office user")
