# -*- coding: utf-8 -*-
from utils.flows import FlowContext
from utils.openapi_client import FlowSessionManager

import datetime

from prime_client.api import move_task_order_api
from prime_client.api import mto_service_item_api
from prime_client.model.mto_service_item import MTOServiceItem
from prime_client.model.address import Address


def do_hhg_prime_service_items(
    flow_context: FlowContext,
    flow_session_manager: FlowSessionManager,
) -> None:
    if "move_id" not in flow_context:
        raise Exception("Cannot find move_id in flow_context")
    move_id = flow_context["move_id"]
    if move_id is None:
        raise Exception("move_id is None in flow_context")

    api_client = flow_session_manager.prime_api_client()
    mto_api_client = move_task_order_api.MoveTaskOrderApi(api_client)
    mto_service_item_api_client = mto_service_item_api.MtoServiceItemApi(api_client)
    since_date = datetime.datetime.now() + datetime.timedelta(days=-7)
    moves = mto_api_client.list_moves(since=since_date)
    pmoves = [m for m in moves.get("value") if m.id == move_id]
    if len(pmoves) != 1:
        raise Exception(f"Cannot find prime move_id: {move_id}")

    move = mto_api_client.get_move_task_order(move_id)
    mto_shipment_id = move.mto_shipments.value[0].id

    entry_date = (datetime.datetime.now() + datetime.timedelta(days=1)).date()
    departure_date = (datetime.datetime.now() + datetime.timedelta(days=6)).date()
    origin_addr = Address(
        street_address1="987 Any Avenue",
        street_address2="P.O. Box 9876",
        city="Fairfield",
        state="CA",
        postal_code="94535",
    )

    # cannot type check this, seemingly because the python
    # generated code isn't handling the way we define allOf +
    # a subtype
    mto_service_item = MTOServiceItem(
        move_task_order_id=move_id,
        mto_shipment_id=mto_shipment_id,
        model_type="MTOServiceItemOriginSIT",
        re_service_code="DOFSIT",
        reason="reason",
        sit_departure_date=departure_date,
        sit_entry_date=entry_date,
        sit_hhg_actual_origin=origin_addr,
        sit_postal_code=origin_addr.postal_code,
        _check_type=False,
    )
    mto_service_item_api_client.create_mto_service_item(
        body=mto_service_item,
        # UGH: The response type is actually invalid according to our
        # swagger definition, so do not try to load the response
        #
        # The server code also creates a DOPSIT re_service_code
        # service_item, but our swagger definition reuses the
        # input object definition for the output object definition
        # and that is incorrect
        _preload_content=False,
    )
