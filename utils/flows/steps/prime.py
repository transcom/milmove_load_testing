# -*- coding: utf-8 -*-
from utils.flows import FlowContext
from utils.openapi_client import FlowSessionManager

import datetime

from prime_client.api import move_task_order_api
from prime_client.api import mto_service_item_api
from prime_client.api import payment_request_api
from prime_client.api import mto_shipment_api
from prime_client.model.mto_service_item import MTOServiceItem
from prime_client.model.address import Address
from prime_client.model.create_payment_request import CreatePaymentRequest
from prime_client.model.service_item import ServiceItem
from prime_client.model.update_mto_shipment import UpdateMTOShipment


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
    mto_shipment_api_client = mto_shipment_api.MtoShipmentApi(api_client)

    since_date = datetime.datetime.now() + datetime.timedelta(days=-7)
    moves = mto_api_client.list_moves(since=since_date)
    pmoves = [m for m in moves.get("value") if m.id == move_id]
    if len(pmoves) != 1:
        raise Exception(f"Cannot find prime move_id: {move_id}")

    move = mto_api_client.get_move_task_order(
        move_id,
        # getting some errors
        # about missing address
        _check_return_type=False,
    )
    first_shipment = move["mto_shipments"][0]
    mto_shipment_id = first_shipment["id"]
    etag = first_shipment["eTag"]

    # Having both the dates >10 days in the future is one of the ways
    # to pass date validation
    #
    # To bypass any local timezone problems, use 12 and 13 days as 11
    # days could hit a boundary condition
    scheduled_pickup_date = datetime.date.today() + datetime.timedelta(days=12)
    actual_pickup_date = datetime.date.today() + datetime.timedelta(days=13)

    payload = UpdateMTOShipment(
        prime_estimated_weight=1000,
        prime_actual_weight=1000,
        scheduled_pickup_date=scheduled_pickup_date,
        actual_pickup_date=actual_pickup_date,
    )
    mto_shipment_api_client.update_mto_shipment(
        mto_shipment_id,
        etag,
        payload,
        # getting some errors
        # about missing address
        _check_return_type=False,
    )

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


def do_hhg_request_payment_for_service_items(
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
    payment_request_api_client = payment_request_api.PaymentRequestApi(api_client)

    # The Swagger definition for the response type for this endpoint only allows certain service codes
    # So, for example, if we get a response with a DOPSIT service item, the return type check will fail.
    # This bug in our spec is caused by reusing the same type for multiple endpoints with
    # different requirements.
    move = mto_api_client.get_move_task_order(move_id, _check_return_type=False)
    service_items = move.mto_service_items

    service_items_for_payload = [ServiceItem(id=si["id"]) for si in service_items]

    # Create payment request for first service item
    create_payment_request_payload = CreatePaymentRequest(move_id, service_items_for_payload[:1])
    payment_request_api_client.create_payment_request(body=create_payment_request_payload)

    # Create payment request for the rest of the service items
    # This split is arbitrary. It's just a simple way to get multiple payment requests.
    if len(service_items_for_payload) > 1:
        create_payment_request_payload = CreatePaymentRequest(move_id, service_items_for_payload[1:])
        payment_request_api_client.create_payment_request(body=create_payment_request_payload)
