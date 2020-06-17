# -*- coding: utf-8 -*-
import os
import time
import datetime
import random
from urllib.parse import urljoin

from bravado_core.formatter import SwaggerFormat
from bravado_core.exception import SwaggerMappingError
from bravado.exception import HTTPError
from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient

from locust import SequentialTaskSet, task, events

# TODO: most of this code is non-functional and needs to be reviewed and then fixed or deleted as appropriate


def get_swagger_config():
    """
    Generate the config used in generating the swagger client from the spec
    """

    # MilMove uses custom formats for some fields. Without wanting to duplicate them here but
    # still wanting to not get warnings about them being undefined the UDFs are created here.
    # See https://bravado-core.readthedocs.io/en/stable/formats.html
    milmove_formats = []
    string_fmt_list = [
        "basequantity",
        "cents",
        "edipi",
        "millicents",
        "mime-type",
        "ssn",
        "telephone",
        "uri",
        "uuid",
        "x-email",
        "zip",
    ]
    for fmt in string_fmt_list:
        swagger_fmt = SwaggerFormat(
            format=fmt,
            to_wire=str,
            to_python=str,
            validate=lambda x: x,
            description="Converts [wire]string:string <=> python string",
        )
        milmove_formats.append(swagger_fmt)
    swagger_config = {
        # Validate our own requests to catch any problems with python type conversions
        "validate_requests": True,
        # Many of our payloads have invalid responses per the spec because of OpenAPI 2.0 issues
        "validate_responses": False,
        "formats": milmove_formats,
        "use_models": False,
    }
    return swagger_config


def swagger_request(callable_operation, *args, **kwargs):
    """
    Swagger client uses requests send() method instead of request(). This means we need to send off
    events to Locust on our own.
    """
    method = callable_operation.operation.http_method.upper()
    path_name = callable_operation.operation.path_name
    response_future = callable_operation(*args, **kwargs)
    start_time = time.time()
    try:
        response = response_future.response()
    except HTTPError as e:
        events.request_failure.fire(
            request_type=method, name=path_name, response_time=time.time() - start_time, exception=e,
        )
        print(e.response)
        return e.swagger_result
    except SwaggerMappingError as e:
        # Even though we don't return the result here we at least fire off the failure event
        events.request_failure.fire(
            request_type=method, name=path_name, response_time=time.time() - start_time, exception=e,
        )
        raise e
    else:
        metadata = response.metadata

        events.request_success.fire(
            request_type=method,
            name=path_name,
            response_time=metadata.elapsed_time,
            response_length=len(metadata.incoming_response.raw_bytes),
        )
        # this is equivalent to json.loads(metadata.incoming_response.text)
        return response.result


class BaseTaskSequence(SequentialTaskSet):

    csrf = None

    def kill(self, message="no message"):
        print(message)
        return self.interrupt()

    def _get_csrf_token(self):
        """
        Pull the CSRF token from the website by hitting the root URL.

        The token is set as a cookie with the name `masked_gorilla_csrf`
        """
        self.client.get("/")
        self.csrf = self.client.cookies.get("masked_gorilla_csrf")
        self.client.headers.update({"x-csrf-token": self.csrf})

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self._get_csrf_token()


class InternalAPIMixin(object):
    swagger_internal = None

    def load_swagger_file_internal(self):
        self.client.get("/internal/swagger.yaml")


class PublicAPIMixin(object):
    swagger_public = None

    def load_swagger_file_public(self):
        self.client.get("/api/v1/swagger.yaml")


class OfficeQueue(InternalAPIMixin, PublicAPIMixin, BaseTaskSequence):

    login_gov_user = None
    session_token = None

    # User is the LoggedInUserPayload
    user_payload = {}

    def update_user(self):
        self.user_payload = swagger_request(self.swagger_internal.users.showLoggedInUser)

    @task
    def login(self):
        resp = self.client.post("/devlocal-auth/create", data={"userType": "office"})
        try:
            self.login_gov_user = resp.json()
        except Exception as e:
            print(e)
            return self.kill("login could not be parsed. content: {}".format(resp.content))

        try:
            self.session_token = self.client.cookies.get("office_session_token")
        except Exception as e:
            print(e)
            return self.kill("missing session token")

        self.requests_client = RequestsClient()
        # Set the session to be the same session as locust uses
        self.requests_client.session = self.client

        # Set the csrf token in the global headers for all requests
        # Don't validate requests or responses because we're using OpenAPI Spec 2.0
        # which doesn't respect nullable sub-definitions
        self.swagger_internal = SwaggerClient.from_url(
            urljoin(self.parent.host, "internal/swagger.yaml"),
            request_headers={"x-csrf-token": self.csrf},
            http_client=self.requests_client,
            config=get_swagger_config(),
        )

        self.swagger_public = SwaggerClient.from_url(
            urljoin(self.parent.host, "api/v1/swagger.yaml"),
            request_headers={"x-csrf-token": self.csrf},
            http_client=self.requests_client,
            config=get_swagger_config(),
        )

        self.load_swagger_file_public()
        self.load_swagger_file_internal()

    @task
    def retrieve_user(self):
        self.update_user()

    @task
    def view_move_in_random_queue(self):
        """
        Choose a random queue to visit and pick a random move to view

        This task pretents to be a user who has work to do in a specific queue.
        """
        queue_types = [
            "new",
            "ppm_payment_requested",
            "ppm_approved",
            "ppm_completed",
        ]  # Excluding 'all' queue
        q_type = random.choice(queue_types)

        queue = swagger_request(self.swagger_internal.queues.showQueue, queueType=q_type)

        if not queue:
            return
        if len(queue) == 0:
            return

        # Pick a random move
        item = random.choice(queue)

        # These are all the requests loaded in a single move in rough order of execution

        # Move Requests
        move_id = item["id"]
        move = swagger_request(self.swagger_internal.moves.showMove, moveId=move_id)
        swagger_request(self.swagger_internal.move_docs.indexMoveDocuments, moveId=move_id)
        swagger_request(
            self.swagger_public.accessorials.getTariff400ngItems, requires_pre_approval=True,
        )
        swagger_request(self.swagger_internal.ppm.indexPersonallyProcuredMoves, moveId=move_id)

        # Orders Requests
        orders_id = move["orders_id"]
        swagger_request(self.swagger_internal.orders.showOrders, ordersId=orders_id)

        # Service Member Requests
        service_member_id = move["service_member_id"]
        swagger_request(
            self.swagger_internal.service_members.showServiceMember, serviceMemberId=service_member_id,
        )

        swagger_request(
            self.swagger_internal.backup_contacts.indexServiceMemberBackupContacts, serviceMemberId=service_member_id,
        )

        # Shipment Requests
        if "shipments" not in move:
            return
        if not isinstance(move["shipments"], list):
            return
        if len(move["shipments"]) == 0:
            return

        shipment_id = move["shipments"][0]["id"]
        swagger_request(self.swagger_public.shipments.getShipment, shipmentId=shipment_id)

        swagger_request(
            self.swagger_public.transportation_service_provider.getTransportationServiceProvider,
            shipmentId=shipment_id,
        )

        swagger_request(
            self.swagger_public.accessorials.getShipmentLineItems, shipmentId=shipment_id,
        )

        swagger_request(self.swagger_public.shipments.getShipmentInvoices, shipmentId=shipment_id)

        swagger_request(
            self.swagger_public.service_agents.indexServiceAgents, shipmentId=shipment_id,
        )

        swagger_request(
            self.swagger_public.storage_in_transits.indexStorageInTransits, shipmentId=shipment_id,
        )

    @task
    def logout(self):
        self.client.post("/auth/logout")
        self.login_gov_user = None
        self.session_token = None
        self.user_payload = {}
        self.interrupt()


class ServiceMemberSignupFlow(InternalAPIMixin, PublicAPIMixin, BaseTaskSequence):

    login_gov_user = None
    session_token = None

    fixtures_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "static")

    # User is the LoggedInUserPayload
    user = {}
    duty_stations = []
    new_duty_stations = []
    move = None
    ppm = None
    entitlements = None
    rank = None
    allotment = None
    zip_origin = "32168"
    zip_destination = "78626"

    def update_user(self):
        self.user = swagger_request(self.swagger_internal.users.showLoggedInUser)

    def update_service_member(self, service_member):
        self.user["service_member"] = service_member

    def get_dutystations(self, short_name):
        station_list = [short_name[0], short_name[0:3], short_name]
        duty_stations = None
        for station in station_list:
            duty_stations = swagger_request(self.swagger_internal.duty_stations.searchDutyStations, search=station)
        return duty_stations

    def get_user(self):
        if not self.user:
            return self.kill("get_user")
        return self.user

    def get_user_id(self):
        user = self.get_user()
        if not user:
            return self.kill("get_user_id 1")
        if not isinstance(user, dict) or "id" not in user:
            return self.kill("get_user_id 2")
        return user["id"]

    def get_user_email(self):
        user = self.get_user()
        if not user:
            return self.kill("get_user_email 1")
        if not isinstance(user, dict) or "email" not in user:
            return self.kill("get_user_email 2")
        return user["email"]

    def get_service_member(self):
        user = self.get_user()
        if not user:
            return self.kill("get_service_member 1")
        if not isinstance(user, dict) or "service_member" not in user:
            return self.kill("get_service_member 2")
        return self.user["service_member"]

    def get_service_member_id(self):
        service_member = self.get_service_member()
        if not service_member:
            return self.kill("get_service_member_id 1")
        if not isinstance(service_member, dict) or "id" not in service_member:
            return self.kill("get_service_member_id 2")
        return service_member["id"]

    def get_orders(self):
        service_member = self.get_service_member()
        if "orders" not in service_member:
            return self.kill("get_orders 1")
        orders = service_member["orders"]
        if len(orders) == 0:
            return self.kill("get_orders 2")
        return orders

    def get_move_id(self):
        orders = self.get_orders()
        first_order = orders[0]
        if "moves" not in first_order:
            return self.kill("get_move_id 1")
        moves = first_order["moves"]
        if len(moves) == 0:
            return self.kill("get_move_id 2")
        first_move = moves[0]
        if "id" not in first_move:
            return self.kill("get_move_id 3")
        move_id = first_move["id"]
        return move_id

    def get_ppm_id(self):
        if not self.ppm:
            return self.kill("get_ppm 1")
        if "id" not in self.ppm:
            return self.kill("get_ppm 2")
        return self.ppm["id"]

    def get_duty_station_id(self):
        if len(self.duty_stations) == 0:
            return self.kill("get_duty_station_id 1")
        if "id" not in self.duty_stations[0]:
            return self.kill("get_duty_station_id 2")
        return self.duty_stations[0]["id"]

    def get_new_duty_station_id(self):
        if len(self.new_duty_stations) == 0:
            return self.kill("get_new_duty_station_id 1")
        if "id" not in self.new_duty_stations[0]:
            return self.kill("get_new_duty_station_id 2")
        return self.new_duty_stations[0]["id"]

    def get_address_origin(self):
        address = self.swagger_internal.get_model("Address")
        return address(street_address_1="12345 Fake St", city="Crescent City", state="FL", postal_code=self.zip_origin,)

    def get_address_destination(self):
        address = self.swagger_internal.get_model("Address")
        return address(street_address_1="12345 Fake St", city="Austin", state="TX", postal_code=self.zip_destination,)

    @task
    def login(self):
        resp = self.client.post("/devlocal-auth/create", data={"userType": "milmove"})
        try:
            self.login_gov_user = resp.json()
        except Exception as e:
            print(e)
            return self.kill("login could not be parsed. content: {}".format(resp.content))

        try:
            self.session_token = self.client.cookies.get("mil_session_token")
        except Exception as e:
            print(e)
            return self.kill("missing session token")

        self.requests_client = RequestsClient()
        # Set the session to be the same session as locust uses
        self.requests_client.session = self.client

        try:
            # Set the csrf token in the global headers for all requests
            # Don't validate requests or responses because we're using OpenAPI Spec 2.0
            # which doesn't respect nullable sub-definitions
            self.swagger_internal = SwaggerClient.from_url(
                urljoin(self.parent.parent.host, "internal/swagger.yaml"),
                request_headers={"x-csrf-token": self.csrf},
                http_client=self.requests_client,
                config=get_swagger_config(),
            )
            if not self.swagger_internal:
                self.kill("internal swagger client failure")

            self.swagger_public = SwaggerClient.from_url(
                urljoin(self.parent.parent.host, "api/v1/swagger.yaml"),
                request_headers={"x-csrf-token": self.csrf},
                http_client=self.requests_client,
                config=get_swagger_config(),
            )
            if not self.swagger_public:
                self.kill("public swagger client failure")
        except Exception as e:
            print(e)
            return self.kill("unknown swagger client failure")

        self.load_swagger_file_public()
        self.load_swagger_file_internal()

    @task
    def retrieve_user(self):
        self.update_user()

    @task
    def create_service_member(self):
        model = self.swagger_internal.get_model("CreateServiceMemberPayload")
        payload = model(user_id=self.get_user_id())
        service_member = swagger_request(
            self.swagger_internal.service_members.createServiceMember, createServiceMemberPayload=payload,
        )
        self.update_service_member(service_member)

    @task
    def create_your_profile(self):

        # Need the entitlements to get ranks and weight allotments
        self.entitlements = swagger_request(self.swagger_internal.entitlements.indexEntitlements)
        self.rank = random.choice(list(self.entitlements.keys()))
        self.allotment = self.entitlements[self.rank]

        # Now set the profile
        model = self.swagger_internal.get_model("PatchServiceMemberPayload")
        payload = model(
            affiliation=random.choice(["ARMY", "NAVY", "MARINES", "AIR_FORCE", "COAST_GUARD"]),
            edipi=str(random.randint(10 ** 9, 10 ** 10 - 1)),
            social_security_number="333-33-3333",  # Random
            rank=self.rank,
        )
        service_member = swagger_request(
            self.swagger_internal.service_members.patchServiceMember,
            serviceMemberId=self.get_service_member_id(),
            patchServiceMemberPayload=payload,
        )
        self.update_service_member(service_member)

    @task
    def create_your_name(self):
        model = self.swagger_internal.get_model("PatchServiceMemberPayload")
        payload = model(first_name="Alice", middle_name="Carol", last_name="Bob", suffix="",)  # Random  # Random
        service_member = swagger_request(
            self.swagger_internal.service_members.patchServiceMember,
            serviceMemberId=self.get_service_member_id(),
            patchServiceMemberPayload=payload,
        )
        self.update_service_member(service_member)

    @task
    def create_your_contact_info(self):
        model = self.swagger_internal.get_model("PatchServiceMemberPayload")
        payload = model(
            email_is_preferred=True,
            personal_email=self.get_user_email(),  # Email is derived from logging in
            phone_is_preferred=True,
            secondary_telephone="333-333-3333",
            telephone="333-333-3333",
        )
        service_member = swagger_request(
            self.swagger_internal.service_members.patchServiceMember,
            serviceMemberId=self.get_service_member_id(),
            patchServiceMemberPayload=payload,
        )
        self.update_service_member(service_member)

    @task
    def search_for_duty_station(self):
        self.duty_stations = self.get_dutystations("eglin")

    @task
    def current_duty_station(self):
        model = self.swagger_internal.get_model("PatchServiceMemberPayload")
        payload = model(current_station_id=self.get_duty_station_id())
        service_member = swagger_request(
            self.swagger_internal.service_members.patchServiceMember,
            serviceMemberId=self.get_service_member_id(),
            patchServiceMemberPayload=payload,
        )
        self.update_service_member(service_member)

    @task
    def current_residence_address(self):
        model = self.swagger_internal.get_model("PatchServiceMemberPayload")
        payload = model(residential_address=self.get_address_origin())
        service_member = swagger_request(
            self.swagger_internal.service_members.patchServiceMember,
            serviceMemberId=self.get_service_member_id(),
            patchServiceMemberPayload=payload,
        )
        self.update_service_member(service_member)

    @task
    def backup_mailing_address(self):
        model = self.swagger_internal.get_model("PatchServiceMemberPayload")
        payload = model(backup_mailing_address=self.get_address_origin())
        service_member = swagger_request(
            self.swagger_internal.service_members.patchServiceMember,
            serviceMemberId=self.get_service_member_id(),
            patchServiceMemberPayload=payload,
        )
        self.update_service_member(service_member)

    @task
    def backup_contact(self):
        model = self.swagger_internal.get_model("CreateServiceMemberBackupContactPayload")
        payload = model(name="Alice", email="alice@example.com", permission="NONE", telephone="333-333-3333",)
        swagger_request(
            self.swagger_internal.backup_contacts.createServiceMemberBackupContact,
            serviceMemberId=self.get_service_member_id(),
            createBackupContactPayload=payload,
        )

    #
    # At this point the user profile is complete so let's refresh our knowledge
    # of the user's profile.
    #

    @task
    def refresh_user_profile(self):
        self.update_user()

    #
    # Start adding move orders
    #

    @task
    def move_orders(self):
        # Get new duty station
        self.new_duty_stations = self.get_dutystations("travis")

        # Determine a few things randomly
        issue_date = datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 15))
        report_by_date = issue_date + datetime.timedelta(days=random.randint(30, 60))
        spouse_has_pro_gear = False
        has_dependents = bool(random.getrandbits(1))
        if has_dependents:
            spouse_has_pro_gear = bool(random.getrandbits(1))

        model = self.swagger_internal.get_model("CreateUpdateOrders")
        payload = model(
            service_member_id=self.get_service_member_id(),
            issue_date=issue_date.date(),
            report_by_date=report_by_date.date(),
            orders_type="PERMANENT_CHANGE_OF_STATION",
            has_dependents=has_dependents,
            spouse_has_pro_gear=spouse_has_pro_gear,
            new_duty_station_id=self.get_new_duty_station_id(),
        )
        swagger_request(self.swagger_internal.orders.createOrders, createOrders=payload)

    @task
    def upload_orders(self):
        with open(os.path.join(self.fixtures_path, "test.pdf"), "rb") as f:
            swagger_request(self.swagger_internal.uploads.createUpload, file=f)

    #
    # At this point orders have been uploaded so let's refresh our knowledge
    # of the user's profile.
    #

    @task
    def refresh_user_profile_2(self):
        self.update_user()

    #
    # Create the PPM Move
    #

    @task
    def select_ppm_move(self):
        model = self.swagger_internal.get_model("PatchMovePayload")
        payload = model(selected_move_type="PPM")
        swagger_request(
            self.swagger_internal.moves.patchMove, moveId=self.get_move_id(), patchMovePayload=payload,
        )

    @task
    def ppm_dates_and_locations(self):
        self.original_move_date = (datetime.datetime.now() + datetime.timedelta(days=random.randint(15, 30))).date()
        swagger_request(
            self.swagger_internal.ppm.showPPMEstimate,
            original_move_date=self.original_move_date,
            origin_zip=self.zip_origin,
            destination_zip=self.zip_destination,
            weight_estimate=11500,  # This appears to be hard coded in the original API call
        )

    @task
    def create_ppm(self):
        model = self.swagger_internal.get_model("CreatePersonallyProcuredMovePayload")
        payload = model(
            days_in_storage=None,
            destination_postal_code="94535",
            has_additional_postal_code=False,
            has_sit=False,
            original_move_date=self.original_move_date,
            pickup_postal_code=self.zip_origin,
        )
        self.ppm = swagger_request(
            self.swagger_internal.ppm.createPersonallyProcuredMove,
            moveId=self.get_move_id(),
            createPersonallyProcuredMovePayload=payload,
        )

    @task
    def select_ppm_weight(self):
        # Choose the TShirt size but don't update weight just yet
        model = self.swagger_internal.get_model("PatchPersonallyProcuredMovePayload")
        tshirt_size = random.choice(["S", "M", "L"])
        payload = model(size=tshirt_size, weight_estimate=0)

        # Sometimes the patch doesn't succeed because discount data is missing
        ppm_id = self.get_ppm_id()
        new_ppm = swagger_request(
            self.swagger_internal.ppm.patchPersonallyProcuredMove,
            moveId=self.get_move_id(),
            personallyProcuredMoveId=ppm_id,
            patchPersonallyProcuredMovePayload=payload,
        )
        # This could mean that the PPM discount doesn't exist for the provided move dates
        if new_ppm is not None:
            self.ppm = new_ppm

        # Weights are decided by TShirt size
        allotment = self.allotment["total_weight_self"]
        size_weight = {
            "S": {"min": int(allotment * 0.01), "max": int(allotment * 0.10)},  # 1% - 10%
            "M": {"min": int(allotment * 0.10), "max": int(allotment * 0.25)},  # 10% - 25%
            "L": {"min": int(allotment * 0.25), "max": int(allotment)},  # 25% to max
        }

        weight_min = size_weight[tshirt_size]["min"]
        weight_max = size_weight[tshirt_size]["max"]

        # Make initial estimate call
        swagger_request(
            self.swagger_internal.ppm.showPPMEstimate,
            original_move_date=self.original_move_date,
            origin_zip=self.zip_origin,
            destination_zip=self.zip_destination,
            weight_estimate=int((weight_max - weight_min) / 2 + weight_min),
        )
        # Now modify the estimate within a random range
        weight_step = 5
        weight_estimate = random.randrange(weight_min, weight_max, weight_step)
        swagger_request(
            self.swagger_internal.ppm.showPPMEstimate,
            original_move_date=self.original_move_date,
            origin_zip=self.zip_origin,
            destination_zip=self.zip_destination,
            weight_estimate=weight_estimate,
        )
        payload = model(has_requested_advance=False, weight_estimate=weight_estimate)
        new_ppm_2 = swagger_request(
            self.swagger_internal.ppm.patchPersonallyProcuredMove,
            moveId=self.get_move_id(),
            personallyProcuredMoveId=ppm_id,
            patchPersonallyProcuredMovePayload=payload,
        )
        if new_ppm_2 is not None:
            self.ppm = new_ppm_2

    @task
    def update_move(self):
        self.move = swagger_request(self.swagger_internal.moves.showMove, moveId=self.get_move_id())

    @task
    def validate_entitlements(self):
        self.move = swagger_request(self.swagger_internal.entitlements.validateEntitlement, moveId=self.get_move_id(),)

    @task
    def signature(self):
        model = self.swagger_internal.get_model("CreateSignedCertificationPayload")
        swagger_request(
            self.swagger_internal.certification.createSignedCertification,
            moveId=self.get_move_id(),
            createSignedCertificationPayload=model(
                date=datetime.datetime.now(), signature="ABC", certification_text="clatto verata necktie",
            ),
        )

    @task
    def submit_move(self):
        model = self.swagger_internal.get_model("SubmitMoveForApprovalPayload")
        swagger_request(
            self.swagger_internal.moves.submitMoveForApproval,
            moveId=self.get_move_id(),
            submitMoveForApprovalPayload=model(ppm_submit_date=datetime.datetime.now()),
        )

    @task
    def get_transportation_offices(self):
        swagger_request(
            self.swagger_internal.transportation_offices.showDutyStationTransportationOffice,
            dutyStationId=self.get_duty_station_id(),
        )
        swagger_request(
            self.swagger_internal.transportation_offices.showDutyStationTransportationOffice,
            dutyStationId=self.get_new_duty_station_id(),
        )

    @task
    def logout(self):
        self.client.post("/auth/logout")
        self.login_gov_user = None
        self.session_token = None
        self.user = {}
        self.interrupt()
