# -*- coding: utf-8 -*-
from utils.flows import FlowContext
from utils.auth import UserType
from utils.openapi_client import FlowSessionManager

import datetime

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


def do_hhg_create_move(
    flow_context: FlowContext,
    flow_session_manager: FlowSessionManager,
) -> None:
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
    duty_station_id = old_locations.value[0]["id"]
    residential_address = Address(
        street_address1="123 Any Street",
        street_address2="P.O. Box 12345",
        city="Beverly Hills",
        state="CA",
        postal_code="90210",
    )

    sm_pdata = PatchServiceMemberPayload(
        edipi="9999009999",
        affiliation=Affiliation("ARMY"),
        rank=ServiceMemberRank("E_1"),
        first_name="First",
        last_name="Last",
        telephone="212-555-1212",
        email_is_preferred=True,
        personal_email=user["email"],
        current_station_id=duty_station_id,
        residential_address=residential_address,
        backup_mailing_address=Address(
            street_address1="987 Any Avenue",
            street_address2="P.O. Box 9876",
            city="Fairfield",
            state="CA",
            postal_code="94535",
        ),
    )

    service_members_api_client = service_members_api.ServiceMembersApi(api_client)
    service_members_api_client.patch_service_member(sm_id, sm_pdata)

    backup_contacts_api_client = backup_contacts_api.BackupContactsApi(api_client)
    backup_contacts_api_client.create_service_member_backup_contact(
        sm_id,
        CreateServiceMemberBackupContactPayload(
            name="Backup Context",
            email="backup@example.com",
            permission=BackupContactPermission("NONE"),
            telephone="212-555-9999",
        ),
    )

    new_locations = duty_locations_api_client.search_duty_locations(
        "Fort Gordon",
        _check_return_type=False,
    )
    new_duty_station_id = new_locations.value[0]["id"]
    issue_date = user.service_member.created_at
    odt = OrdersTypeDetail(value=None, _check_type=False)

    orders_api_client = orders_api.OrdersApi(api_client)
    orders = orders_api_client.create_orders(
        CreateUpdateOrders(
            service_member_id=sm_id,
            issue_date=issue_date.date(),
            report_by_date=(issue_date + datetime.timedelta(days=7)).date(),
            orders_type=OrdersType("PERMANENT_CHANGE_OF_STATION"),
            has_dependents=False,
            spouse_has_pro_gear=False,
            new_duty_station_id=new_duty_station_id,
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
    mto_shipment_api_client.create_mto_shipment(
        body=CreateShipment(
            move_task_order_id=move_id,
            shipment_type=MTOShipmentType("HHG"),
            requested_pickup_date=(issue_date + datetime.timedelta(days=1)).date(),
            requested_delivery_date=(issue_date + datetime.timedelta(days=7)).date(),
            pickup_address=residential_address,
        )
    )

    hhg_certification_text = """
**Financial Liability**

For a HHG shipment, I am entitled to move a certain amount of HHG by weight ...
"""
    moves_api_client.submit_move_for_approval(
        move_id,
        SubmitMoveForApprovalPayload(
            certificate=CreateSignedCertificationPayload(
                date=datetime.datetime.now(),
                signature="Firstname Lastname",
                certification_text=hhg_certification_text,
                certification_type=SignedCertificationTypeCreate("SHIPMENT"),
            ),
        ),
    )
