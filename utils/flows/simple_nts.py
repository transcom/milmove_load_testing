# -*- coding: utf-8 -*-
from utils.flows import FlowContext, FlowStep, FlowSequence, SequenceQueableFlow, WorkerQueueType

from utils.flows.steps.milmove import do_nts_create_move

import os


class SimpleNTSFlow(SequenceQueableFlow):
    def __init__(self, flow_context: FlowContext = None) -> None:
        super().__init__(flow_context)

    def flow_steps(self) -> FlowSequence:
        return [
            FlowStep(callback=do_nts_create_move, queue=WorkerQueueType.SERVICE_MEMBER),
        ]


if __name__ == "__main__":
    from utils.base import MilMoveEnv

    f = SimpleNTSFlow()
    milmove_env = MilMoveEnv(os.getenv("MILMOVE_ENV", MilMoveEnv.LOCAL))
    f.run_entire_flow(milmove_env)
