# -*- coding: utf-8 -*-
from locust import task, TaskSet

from utils.flows import MemoryFlowQueue, QueuableFlow, WorkerQueueType
from utils.flows.simple_hhg import SingleHHGFlow, DoubleHHGFlow, NTSFlow
from utils.openapi_client import FlowSessionManager
from utils.request import MilMoveRequestMixin

global_queue = MemoryFlowQueue()


class QueueTaskSet(MilMoveRequestMixin, TaskSet):
    """
    A convenience class for testing REST JSON endpoints using a queue of workers.
    """

    def run_from_queue(self, worker_queue_type: WorkerQueueType) -> None:
        flow = global_queue.pop(worker_queue_type)

        if flow:
            self.start_flow(flow)
        else:
            self.run_when_empty_queue()

    def start_flow(self, flow: QueuableFlow) -> None:
        flow_session_manager = FlowSessionManager(self.env, self.user)

        if flow.run(flow_session_manager):
            global_queue.enqueue_next(flow)

    def run_when_empty_queue(self: MilMoveRequestMixin) -> None:
        pass


class MilMoveHHGQueueTasks(QueueTaskSet):
    """
    Creates tasks that traverse the entire flow, from customer through TIO. These tasks largely only differ
    based on what kind of shipment(s) the customer is adding to their move. Weighted randomness determines how
    frequently the various customer shipment types are selected.

    See http://docs.locust.io/en/stable/writing-a-locustfile.html#task-decorator for more info
    """

    def on_start(self):
        """ """

    @task(2)
    def start_single_hhg_flow(self):
        """
        Kicks off a flow where the customer creates a single HHG shipment
        """
        f = SingleHHGFlow()
        self.start_flow(f)

    @task(1)
    def start_double_hhg_flow(self):
        """
        Kicks off a flow where the customer creates two seperate HHG shipments
        """
        f = DoubleHHGFlow()
        self.start_flow(f)

    @task(1)
    def start_nts_flow(self):
        """
        Kicks off a flow where the customer creates a single NTS shipment
        """
        f = NTSFlow()
        self.start_flow(f)


class ServiceCounselorQueueTasks(QueueTaskSet):
    """ """

    def on_start(self):
        """ """

    @task
    def run_flow(self):
        """
        run from the queue
        """

        self.run_from_queue(WorkerQueueType.SERVICE_COUNSELOR)


class TOOQueueTasks(QueueTaskSet):
    """ """

    def on_start(self):
        """ """

    @task
    def run_flow(self):
        """
        run from the queue
        """

        self.run_from_queue(WorkerQueueType.TOO)


class TIOQueueTasks(QueueTaskSet):
    """ """

    def on_start(self):
        """ """

    @task
    def run_flow(self):
        """
        run from the queue
        """

        self.run_from_queue(WorkerQueueType.TIO)


class PrimeQueueTasks(QueueTaskSet):
    """ """

    def on_start(self):
        """ """

    @task
    def run_flow(self):
        """
        run from the queue
        """

        self.run_from_queue(WorkerQueueType.PRIME)
