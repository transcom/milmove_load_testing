# -*- coding: utf-8 -*-
from utils.flows import FlowContext
from utils.auth import UserType
from utils.openapi_client import FlowSessionManager

from ghc_client.api import queues_api
from ghc_client.api import move_api
from ghc_client.api import move_task_order_api


def do_hhg_sc_review(
    flow_context: FlowContext,
    flow_session_manager: FlowSessionManager,
) -> None:
    if "move_id" not in flow_context:
        raise Exception("Cannot find move_id in flow_context")
    move_id = flow_context["move_id"]
    if move_id is None:
        raise Exception("move_id is None in flow_context")

    api_client = flow_session_manager.ghc_api_client(UserType.SERVICE_COUNSELOR)

    queues_api_client = queues_api.QueuesApi(api_client)
    moves_api_client = move_api.MoveApi(api_client)
    mto_api_client = move_task_order_api.MoveTaskOrderApi(api_client)

    scq = queues_api_client.get_services_counseling_queue(
        per_page=100,
        _check_return_type=False,
    )
    moves = [m for m in scq.queue_moves if m["id"] == move_id]
    if len(moves) != 1:
        raise Exception(f"Cannot find service counselor move_id in queue: {move_id}")
    locator = moves[0]["locator"]
    move = moves_api_client.get_move(locator)

    mto_api_client.update_mto_status_service_counseling_completed(
        move_id,
        move.e_tag,
        # looks like the python openapi code generator doesn't
        # handle a $ref that is also x-nullable?
        _check_return_type=False,
        _preload_content=False,
    )
