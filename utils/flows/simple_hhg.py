# -*- coding: utf-8 -*-
from utils.flows import FlowContext, FlowStep, FlowSequence, SequenceQueableFlow, WorkerQueueType
from typing import Optional

from utils.flows.steps.milmove import do_flow_create_single_hhg, do_flow_create_double_hhg, do_flow_create_nts
from utils.flows.steps.service_counselor import do_hhg_sc_review
from utils.flows.steps.too import do_hhg_too_approve, do_hhg_too_approve_service_items
from utils.flows.steps.prime import do_hhg_prime_service_items, do_hhg_request_payment_for_service_items


class SingleHHGFlow(SequenceQueableFlow):
    """Flow creating a single HHG Move."""

    def __init__(self, flow_context: Optional[FlowContext] = None) -> None:
        """Call super init."""
        super().__init__(flow_context)

    def flow_steps(self) -> FlowSequence:
        """Return the FlowSequence for this flow."""
        return [
            FlowStep(callback=do_flow_create_single_hhg, queue=WorkerQueueType.SERVICE_MEMBER),
            FlowStep(callback=do_hhg_sc_review, queue=WorkerQueueType.SERVICE_COUNSELOR),
            FlowStep(callback=do_hhg_too_approve, queue=WorkerQueueType.TOO),
            FlowStep(callback=do_hhg_prime_service_items, queue=WorkerQueueType.PRIME),
        ]


class DoubleHHGFlow(SequenceQueableFlow):
    """Flow creating two HHG Moves."""

    def __init__(self, flow_context: Optional[FlowContext] = None) -> None:
        """Call super init."""
        super().__init__(flow_context)

    def flow_steps(self) -> FlowSequence:
        """Return the FlowSequence for this flow."""
        return [
            FlowStep(callback=do_flow_create_double_hhg, queue=WorkerQueueType.SERVICE_MEMBER),
            FlowStep(callback=do_hhg_sc_review, queue=WorkerQueueType.SERVICE_COUNSELOR),
            FlowStep(callback=do_hhg_too_approve, queue=WorkerQueueType.TOO),
            FlowStep(callback=do_hhg_prime_service_items, queue=WorkerQueueType.PRIME),
        ]


class NTSFlow(SequenceQueableFlow):
    """Flow creating an NTS Move."""

    def __init__(self, flow_context: Optional[FlowContext] = None) -> None:
        """Call super init."""
        super().__init__(flow_context)

    def flow_steps(self) -> FlowSequence:
        """Return the FlowSequence for this flow."""
        return [
            FlowStep(callback=do_flow_create_nts, queue=WorkerQueueType.SERVICE_MEMBER),
            FlowStep(callback=do_hhg_sc_review, queue=WorkerQueueType.SERVICE_COUNSELOR),
            FlowStep(callback=do_hhg_too_approve, queue=WorkerQueueType.TOO),
            FlowStep(callback=do_hhg_prime_service_items, queue=WorkerQueueType.PRIME),
        ]


class SingleHHGMultiplePaymentRequestFlow(SequenceQueableFlow):
    """Flow creating a HHG move with multiple payment requests."""

    def __init__(self, flow_context: Optional[FlowContext] = None) -> None:
        """Call super init."""
        super().__init__(flow_context)

    def flow_steps(self) -> FlowSequence:
        """Return the FlowSequence for this flow."""
        return [
            FlowStep(callback=do_flow_create_single_hhg, queue=WorkerQueueType.SERVICE_MEMBER),
            FlowStep(callback=do_hhg_sc_review, queue=WorkerQueueType.SERVICE_COUNSELOR),
            FlowStep(callback=do_hhg_too_approve, queue=WorkerQueueType.TOO),
            FlowStep(callback=do_hhg_prime_service_items, queue=WorkerQueueType.PRIME),
            FlowStep(callback=do_hhg_too_approve_service_items, queue=WorkerQueueType.TOO),
            FlowStep(callback=do_hhg_request_payment_for_service_items, queue=WorkerQueueType.PRIME),
        ]


# disable for now while refactoring to pass user.client
#
# if __name__ == "__main__":
#     from utils.base import MilMoveEnv

#     f = SingleHHGFlow()
#     milmove_env = MilMoveEnv(os.getenv("MILMOVE_ENV", MilMoveEnv.LOCAL))
#     f.run_entire_flow(milmove_env)
