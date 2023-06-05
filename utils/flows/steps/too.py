# -*- coding: utf-8 -*-

from requests import Session

from utils.flows import FlowContext
from utils.auth import UserType
from utils.openapi_client import ghc_api_client
from utils.request import MilMoveRequestPreparer

import datetime

from ghc_client.api import order_api
from ghc_client.api import queues_api
from ghc_client.api import move_api
from ghc_client.api import move_task_order_api
from ghc_client.api import mto_service_item_api
from ghc_client.api import shipment_api
from ghc_client.api import mto_shipment_api

from ghc_client.model.mto_approval_service_item_codes import MTOApprovalServiceItemCodes
from ghc_client.model.dept_indicator import DeptIndicator
from ghc_client.model.update_order_payload import UpdateOrderPayload
from ghc_client.model.orders_type import OrdersType
from ghc_client.model.orders_type_detail import OrdersTypeDetail
from ghc_client.model.patch_mto_service_item_status_payload import PatchMTOServiceItemStatusPayload


def do_hhg_too_approve(
    flow_context: FlowContext,
    request_preparer: MilMoveRequestPreparer,
    session: Session,
) -> None:
    if "move_id" not in flow_context:
        raise Exception("Cannot find move_id in flow_context")
    move_id = flow_context["move_id"]
    if move_id is None:
        raise Exception("move_id is None in flow_context")

    api_client = ghc_api_client(request_preparer, session, UserType.TOO)
    mto_api_client = move_task_order_api.MoveTaskOrderApi(api_client)
    queues_api_client = queues_api.QueuesApi(api_client)
    moves_api_client = move_api.MoveApi(api_client)
    order_api_client = order_api.OrderApi(api_client)
    shipment_api_client = shipment_api.ShipmentApi(api_client)
    mto_shipment_api_client = mto_shipment_api.MtoShipmentApi(api_client)

    tooq = queues_api_client.get_moves_queue(
        page=1,
        locator=flow_context["locator"],
        per_page=100,
        # looks like the python openapi code generator doesn't
        # handle a $ref that is also x-nullable?
        _check_return_type=False,
    )
    moves = [m for m in tooq.queue_moves if m["id"] == move_id]
    if len(moves) != 1:
        raise Exception(f"Cannot find prime move_id: {move_id}")

    locator = moves[0]["locator"]
    move = moves_api_client.get_move(locator)

    order_id = move.orders_id
    order = order_api_client.get_order(
        order_id,
        # looks like the python openapi code generator doesn't
        # handle a $ref that is also x-nullable?
        _check_return_type=False,
    )
    order_api_client.update_order(
        order_id,
        order.e_tag,
        UpdateOrderPayload(
            datetime.datetime.fromisoformat(order.date_issued).date(),
            datetime.datetime.fromisoformat(order.report_by_date).date(),
            OrdersType(order.order_type),
            order.origin_duty_location["id"],
            order.destination_duty_location["id"],
            orders_type_detail=OrdersTypeDetail("HHG_PERMITTED"),
            orders_number="12345689",
            tac="1234",
            sac="9876",
            department_indicator=DeptIndicator("ARMY"),
        ),
        _check_return_type=False,
    )

    move = moves_api_client.get_move(locator)
    mto_api_client.update_move_task_order_status(
        move_id,
        move.e_tag,
        MTOApprovalServiceItemCodes(
            service_code_cs=False,
            service_code_ms=True,
        ),
        _check_return_type=False,
    )

    # Approve all shipments
    shipments = mto_shipment_api_client.list_mto_shipments(move_id)
    for shipment in shipments.value:
        shipment_api_client.approve_shipment(shipment.id, shipment.e_tag)


def do_hhg_too_approve_service_items(
    flow_context: FlowContext,
    request_preparer: MilMoveRequestPreparer,
    session: Session,
) -> None:
    if "move_id" not in flow_context:
        raise Exception("Cannot find move_id in flow_context")
    move_id = flow_context["move_id"]
    if move_id is None:
        raise Exception("move_id is None in flow_context")

    if "locator" not in flow_context:
        raise Exception("Cannot find locator in flow_context")
    locator = flow_context["locator"]
    if locator is None:
        raise Exception("locator is None in flow_context")

    api_client = ghc_api_client(request_preparer, session, UserType.TOO)
    queues_api_client = queues_api.QueuesApi(api_client)
    service_item_api_client = mto_service_item_api.MtoServiceItemApi(api_client)

    tooq = queues_api_client.get_moves_queue(
        page=1,
        per_page=20,
        locator=locator,
        # looks like the python openapi code generator doesn't
        # handle a $ref that is also x-nullable?
        _check_return_type=False,
    )
    moves = [m for m in tooq.queue_moves if m["id"] == move_id]
    if len(moves) != 1:
        raise Exception(f"Cannot find move_id {move_id} in TOO queue")

    service_items = service_item_api_client.list_mto_service_items(move_id)
    for service_item in service_items.value:
        payload = PatchMTOServiceItemStatusPayload(status="APPROVED")
        service_item_api_client.update_mto_service_item_status(
            move_id, service_item["id"], service_item["e_tag"], payload
        )
