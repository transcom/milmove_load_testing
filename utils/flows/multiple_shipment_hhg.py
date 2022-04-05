# -*- coding: utf-8 -*-
from utils.flows import FlowContext, FlowStep, FlowSequence, SequenceQueableFlow, WorkerQueueType

from utils.flows.steps.milmove import do_hhg_create_move_with_multiple_shipments
from utils.flows.steps.service_counselor import do_hhg_sc_review
from utils.flows.steps.too import do_hhg_too_approve
from utils.flows.steps.prime import do_hhg_prime_service_items

import os


class MultipleShipmentHHGFlow(SequenceQueableFlow):
    def __init__(self, flow_context: FlowContext = None) -> None:
        super().__init__(flow_context)

    def flow_steps(self) -> FlowSequence:
        return [
            FlowStep(callback=do_hhg_create_move_with_multiple_shipments, queue=WorkerQueueType.SERVICE_MEMBER),
            FlowStep(callback=do_hhg_sc_review, queue=WorkerQueueType.SERVICE_COUNSELOR),
            FlowStep(callback=do_hhg_too_approve, queue=WorkerQueueType.TOO),
            FlowStep(callback=do_hhg_prime_service_items, queue=WorkerQueueType.PRIME),
        ]


if __name__ == "__main__":
    from utils.base import MilMoveEnv

    f = MultipleShipmentHHGFlow()
    milmove_env = MilMoveEnv(os.getenv("MILMOVE_ENV", MilMoveEnv.LOCAL))
    f.run_entire_flow(milmove_env)
