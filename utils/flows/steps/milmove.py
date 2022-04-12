# -*- coding: utf-8 -*-
from utils.flows import FlowContext
from utils.auth import UserType
from utils.openapi_client import FlowSessionManager

from datetime import datetime, timedelta
from faker import Faker

from internal_client.api import users_api
from internal_client.api import service_members_api
from internal_client.api import duty_locations_api
from internal_client.api import backup_contacts_api
from internal_client.api import orders_api
from internal_client.api import uploads_api
from internal_client.api import moves_api
from internal_client.api import mto_shipment_api

from internal_client.model.patch_service_member_payload import PatchServiceMemberPayload
from internal_client.model.address import Address
from internal_client.model.affiliation import Affiliation
from internal_client.model.service_member_rank import ServiceMemberRank
from internal_client.model.create_service_member_backup_contact_payload import CreateServiceMemberBackupContactPayload
from internal_client.model.backup_contact_permission import BackupContactPermission
from internal_client.model.create_update_orders import CreateUpdateOrders
from internal_client.model.orders_type import OrdersType
from internal_client.model.orders_type_detail import OrdersTypeDetail
from internal_client.model.patch_move_payload import PatchMovePayload
from internal_client.model.selected_move_type import SelectedMoveType
from internal_client.model.mto_shipment_type import MTOShipmentType
from internal_client.model.create_shipment import CreateShipment
from internal_client.model.submit_move_for_approval_payload import SubmitMoveForApprovalPayload
from internal_client.model.create_signed_certification_payload import CreateSignedCertificationPayload
from internal_client.model.signed_certification_type_create import SignedCertificationTypeCreate
from internal_client.model.dept_indicator import DeptIndicator


def create_hhg_shipment(move_id: str, issue_date: datetime, pickup_address: Address) -> CreateShipment:
    return CreateShipment(
        move_task_order_id=move_id,
        shipment_type=MTOShipmentType("HHG"),
        requested_pickup_date=(issue_date + timedelta(days=1)).date(),
        requested_delivery_date=(issue_date + timedelta(days=7)).date(),
        pickup_address=pickup_address,
    )


def create_nts_shipment(move_id: str, issue_date: datetime, pickup_address: Address) -> CreateShipment:
    return CreateShipment(
        move_task_order_id=move_id,
        shipment_type=MTOShipmentType("HHG_INTO_NTS_DOMESTIC"),
        requested_pickup_date=(issue_date + timedelta(days=1)).date(),
        pickup_address=pickup_address,
    )


def start_flow(flow_context: FlowContext, flow_session_manager: FlowSessionManager, shipments: list[str]) -> None:
    """
    Creates a move. Can raise internal_client.ApiException
    """
    api_client = flow_session_manager.internal_api_client(UserType.MILMOVE)

    users_api_client = users_api.UsersApi(api_client)

    user = users_api_client.show_logged_in_user()

    duty_locations_api_client = duty_locations_api.DutyLocationsApi(api_client)
    sm_id = user.service_member.id
    duty_location_with_counseling_in_KKFA_gbloc = "Blue Grass Army Depot"
    old_locations = duty_locations_api_client.search_duty_locations(
        duty_location_with_counseling_in_KKFA_gbloc,
        _check_return_type=False,
    )

    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    state = "CA"
    zip_in_KKFA_gbloc = "90210"
    duty_location_id = old_locations.value[0]["id"]
    if not duty_location_id:
        raise Exception("Cannot find duty location: " + duty_location_with_counseling_in_KKFA_gbloc)
    residential_address = Address(
        street_address1=fake.street_address(),
        city=fake.city(),
        state=state,
        postal_code=zip_in_KKFA_gbloc,
    )

    sm_pdata = PatchServiceMemberPayload(
        edipi=fake.unique.numerify("##########"),
        affiliation=Affiliation("ARMY"),
        rank=ServiceMemberRank("E_1"),
        first_name=first_name,
        last_name=last_name,
        telephone=fake.numerify("2##-555-####"),
        email_is_preferred=True,
        personal_email=user["email"],
        current_location_id=duty_location_id,
        residential_address=residential_address,
        backup_mailing_address=Address(
            street_address1=fake.street_address(),
            street_address2="P.O. Box " + fake.building_number(),
            city=fake.city(),
            state=state,
            postal_code=fake.postcode(),
        ),
    )

    service_members_api_client = service_members_api.ServiceMembersApi(api_client)
    service_members_api_client.patch_service_member(sm_id, sm_pdata)

    backup_contacts_api_client = backup_contacts_api.BackupContactsApi(api_client)
    backup_contacts_api_client.create_service_member_backup_contact(
        sm_id,
        CreateServiceMemberBackupContactPayload(
            name=fake.name(),
            email=fake.ascii_safe_email(),
            permission=BackupContactPermission("NONE"),
            telephone=fake.numerify("3##-555-####"),
        ),
    )

    new_duty_location_name = "Fort Gordon"
    new_locations = duty_locations_api_client.search_duty_locations(
        new_duty_location_name,
        _check_return_type=False,
    )
    new_duty_location_id = new_locations.value[0]["id"]
    if not duty_location_id:
        raise Exception("Cannot find duty location: " + new_duty_location_name)
    issue_date = user.service_member.created_at
    odt = OrdersTypeDetail(value=None, _check_type=False)

    orders_api_client = orders_api.OrdersApi(api_client)
    orders = orders_api_client.create_orders(
        CreateUpdateOrders(
            service_member_id=sm_id,
            issue_date=issue_date.date(),
            report_by_date=(issue_date + timedelta(days=7)).date(),
            orders_type=OrdersType("PERMANENT_CHANGE_OF_STATION"),
            has_dependents=False,
            spouse_has_pro_gear=False,
            new_duty_location_id=new_duty_location_id,
            orders_type_detail=odt,
            department_indicator=DeptIndicator("ARMY"),
        ),
        # looks like the python openapi code generator doesn't
        # handle a $ref that is also x-nullable?
        _check_return_type=False,
    )
    current_move = orders.moves[0]
    order_upload_id = orders.uploaded_orders["id"]
    orders_file = open("fixtures/fake_orders_image.jpg", "rb")
    uploads_api_client = uploads_api.UploadsApi(api_client)
    uploads_api_client.create_upload(orders_file, document_id=order_upload_id)

    move_id = current_move["id"]
    flow_context["move_id"] = move_id
    moves_api_client = moves_api.MovesApi(api_client)
    moves_api_client.patch_move(move_id, PatchMovePayload(selected_move_type=SelectedMoveType("HHG")))

    mto_shipment_api_client = mto_shipment_api.MtoShipmentApi(api_client)

    for shipmentType in shipments:
        shipment = {
            "HHG": create_hhg_shipment(move_id, issue_date, residential_address),
            "NTS": create_nts_shipment(move_id, issue_date, residential_address),
        }.get(shipmentType, create_hhg_shipment(move_id, issue_date, residential_address))

        mto_shipment_api_client.create_mto_shipment(body=shipment)

    hhg_certification_text = """
**Financial Liability**

For a HHG shipment, I am entitled to move a certain amount of HHG by weight ...
"""
    moves_api_client.submit_move_for_approval(
        move_id,
        SubmitMoveForApprovalPayload(
            certificate=CreateSignedCertificationPayload(
                date=datetime.now(),
                signature=f"{first_name} {last_name}",
                certification_text=hhg_certification_text,
                certification_type=SignedCertificationTypeCreate("SHIPMENT"),
            ),
        ),
    )


def do_flow_create_single_hhg(
    flow_context: FlowContext,
    flow_session_manager: FlowSessionManager,
) -> None:
    start_flow(flow_context, flow_session_manager, ["HHG"])


def do_flow_create_double_hhg(
    flow_context: FlowContext,
    flow_session_manager: FlowSessionManager,
) -> None:
    start_flow(flow_context, flow_session_manager, ["HHG", "HHG"])


def do_flow_create_nts(
    flow_context: FlowContext,
    flow_session_manager: FlowSessionManager,
) -> None:
    start_flow(flow_context, flow_session_manager, ["NTS"])
