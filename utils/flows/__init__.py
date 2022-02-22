# -*- coding: utf-8 -*-
from abc import abstractmethod, ABC
from collections.abc import Callable
from enum import Enum
import importlib
from queue import Queue, Empty
from typing import TypedDict, TYPE_CHECKING, Optional
from utils.openapi_client import FlowSessionManager

FlowContext = dict


class SerializedFlow(TypedDict):
    module_name: str
    class_name: str
    flow_context: FlowContext


if TYPE_CHECKING:
    FlowQueue = Queue[SerializedFlow]
else:
    FlowQueue = Queue


class WorkerQueueType(Enum):
    DONE = 0
    SERVICE_MEMBER = 1
    SERVICE_COUNSELOR = 2
    TOO = 3
    TIO = 4
    PRIME = 5


FlowStepCallable = Callable[[FlowContext, FlowSessionManager], None]


class FlowStep(TypedDict):
    callback: FlowStepCallable
    queue: WorkerQueueType


def noop_callback(*_):
    pass


FlowSequence = list[FlowStep]


class QueuableFlow(ABC):
    """
    A flow that can be enqueued
    """

    flow_context: FlowContext
    queue: Optional[WorkerQueueType]

    def __init__(self, flow_context: FlowContext = None) -> None:
        """ """
        if flow_context:
            self.flow_context = flow_context
        else:
            self.flow_context = {}
        self.queue = None

    @abstractmethod
    def next_step(self) -> Optional[FlowStep]:
        """
        Return the next step in the flow, a Callable that can then be invoked
        """
        raise NotImplementedError

    def run(self, flow_session_manager: FlowSessionManager) -> bool:
        """
        Calls the next step in the flow, returns false if no next step
        """
        flow_step = self.next_step()
        if flow_step:
            flow_step_callback = flow_step["callback"]
            flow_step_callback(self.flow_context, flow_session_manager)
        return flow_step is not None

    def to_serialized_flow(self) -> SerializedFlow:
        return SerializedFlow(
            module_name=self.__module__, class_name=self.__class__.__name__, flow_context=self.flow_context
        )


class SequenceQueableFlow(QueuableFlow):
    def __init__(self, flow_context: FlowContext = None) -> None:
        super().__init__(flow_context)

    @abstractmethod
    def flow_steps(self) -> FlowSequence:
        raise NotImplementedError

    def next_step(self) -> Optional[FlowStep]:
        i = 0
        if "__step_index__" in self.flow_context:
            i = self.flow_context["__step_index__"]

        next_index = i + 1
        self.flow_context["__step_index__"] = next_index
        steps = self.flow_steps()
        if next_index < len(steps):
            self.queue = steps[next_index]["queue"]
        if i < len(steps):
            return steps[i]
        return None


class MemoryFlowQueue(object):
    """
    Class that represents an in memory FlowQueue
    """

    def __init__(self) -> None:
        """
        Sets up a MemoryFlowQueue
        """
        self.work_q = {
            WorkerQueueType.SERVICE_MEMBER: FlowQueue(),
            WorkerQueueType.SERVICE_COUNSELOR: FlowQueue(),
            WorkerQueueType.TOO: FlowQueue(),
            WorkerQueueType.TIO: FlowQueue(),
            WorkerQueueType.PRIME: FlowQueue(),
        }

    def deserialize_flow(self, sflow: SerializedFlow) -> QueuableFlow:
        """Return a class instance from a SerializedFlow"""
        module_name = sflow["module_name"]
        class_name = sflow["class_name"]
        try:
            module_ = importlib.import_module(module_name)
            try:
                return getattr(module_, class_name)(sflow["flow_context"])
            except AttributeError:
                raise Exception(f"Class does not exist: {module_name}.{class_name}")
        except ImportError:
            raise Exception("Module does not exist: {module_name}")

    def pop(self, worker_queue_type: WorkerQueueType) -> Optional[QueuableFlow]:
        """
        Get the next flow from the queue, or raise the Empty exception if
        none are available

        """
        if worker_queue_type not in self.work_q:
            raise Exception(f"Cannot find queue for type {worker_queue_type}")

        q = self.work_q[worker_queue_type]
        try:
            sf = q.get(block=True, timeout=1)
            return self.deserialize_flow(sf)
        except Empty:
            return None

    def enqueue_next(self, flow: QueuableFlow) -> Optional[WorkerQueueType]:
        """
        Enqueue the next step in the Flow for processing
        """

        if not flow.queue or flow.queue == WorkerQueueType.DONE:
            return flow.queue

        if flow.queue not in self.work_q:
            raise BaseException(f"Cannot find queue for {flow.queue}")

        q = self.work_q[flow.queue]
        q.put_nowait(flow.to_serialized_flow())
        return flow.queue
