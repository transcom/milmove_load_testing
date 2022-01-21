# -*- coding: utf-8 -*-
""" TaskSets and tasks for the MilMove interface. """
import json
import logging
from http import HTTPStatus
from typing import Optional

from locust import tag, task

from utils.auth import UserType, create_user
from utils.constants import DataType
from utils.fake_data import MilMoveData
from utils.request import log_response_failure, log_response_info
from utils.rest import RestResponseContextManager
from utils.task import RestTaskSet
from utils.types import JSONArray, JSONObject


logger = logging.getLogger(__name__)


class MilMoveTasks(RestTaskSet):
    """
    Set of tasks that can be called for the MilMove interface.
    """

    def on_start(self):
        """
        Creates a login right at the start of the TaskSet and stops task execution if the login fails.
        """
        success = create_user(request_preparer=self.request_preparer, session=self.client, user_type=UserType.MILMOVE)

        if not success:
            logger.error("Failed to create a user")
            self.interrupt()

    @task
    def stop(self) -> None:
        """
        This ensures that at some point, the user will stop running the tasks in this task set.
        """
        self.interrupt()

    @tag("getUserInfo")
    @task(2)
    def get_user_info(self) -> Optional[JSONObject]:
        """
        Gets the user info for the currently logged-in user.
        :return: logged-in user, or None if there is an error
        """
        url, request_kwargs = self.request_preparer.prep_internal_request(endpoint="/users/logged_in")

        with self.rest(method="GET", url=url, **request_kwargs) as resp:
            resp: RestResponseContextManager

            log_response_info(response=resp)

            if resp.status_code == HTTPStatus.OK:
                user: JSONObject = resp.js

                logger.info(f"ℹ️ User email: {user['email']}")

                return user
            else:
                resp.failure("Unable to get logged-in user.")

                log_response_failure(response=resp)

                return

    @tag("onboardCustomerWorkflow")
    @task
    def onboard_customer(self) -> None:
        """
        Goes through the basic on-boarding flow for a customer.

        We're going to be re-using the same endpoint for several requests in this workflow.
        Because of that, we won't use the api fake data generator because we would end up having
        to delete a lot of the data it gave back in order to simulate the step-by-step process
        that on-boarding actually takes. Instead, we'll use the lower-level `MilMoveData` which is
        what the api fake data generate uses internally because it gives us more control. It's
        essentially a wrapper around faker, but we'll still use it to remain more consistent in
        the faker helper functions we use for different data types.

        Another thing to note is that because we'll be hitting a lot of endpoints in this load test,
        we'll pass task_name values to the logging functions whenever we hit an endpoint to make it
        easier to see in the logs what is happening.
        """
        user = self.get_user_info()

        if user is None:
            return  # get_user_info will log the error

        service_member_id = user["service_member"]["id"]

        milmove_faker = MilMoveData()

        # First let's create the profile.
        payload = {
            "id": service_member_id,
            "affiliation": "ARMY",
            "edipi": "1234567890",
            "rank": "E_1",
        }

        sm_url, sm_request_kwargs = self.request_preparer.prep_internal_request(
            endpoint=f"/service_members/{service_member_id}",
            endpoint_name="/service_members/{serviceMemberId}",
        )

        with self.rest(method="PATCH", url=sm_url, data=json.dumps(payload), **sm_request_kwargs) as resp:
            resp: RestResponseContextManager

            task_name = "create_user_profile"

            log_response_info(response=resp, task_name=task_name)

            if resp.status_code != HTTPStatus.OK:
                resp.failure("Unable to create customer profile.")

                log_response_failure(response=resp, task_name=task_name)

                return

        # Now we can add name info. The url and request_kwargs will actually be the same, so we only
        # need to prepare the payload.

        payload = {
            "id": service_member_id,
            "first_name": milmove_faker.get_fake_data_for_type(data_type=DataType.FIRST_NAME),
            "middle_name": milmove_faker.get_fake_data_for_type(data_type=DataType.FIRST_NAME),
            "last_name": milmove_faker.get_fake_data_for_type(data_type=DataType.LAST_NAME),
            "suffix": "",
        }

        with self.rest(method="PATCH", url=sm_url, data=json.dumps(payload), **sm_request_kwargs) as resp:
            resp: RestResponseContextManager

            task_name = "add_name_info"

            log_response_info(response=resp, task_name=task_name)

            if resp.status_code != HTTPStatus.OK:
                resp.failure("Unable to add customer name.")

                log_response_failure(response=resp, task_name=task_name)

                return

        # Now we can add contact info. Again, url and request_kwargs will be the same, so only need
        # a payload.

        payload = {
            "id": service_member_id,
            "telephone": milmove_faker.get_fake_data_for_type(data_type=DataType.PHONE),
            "secondary_telephone": milmove_faker.get_fake_data_for_type(data_type=DataType.PHONE),
            "personal_email": milmove_faker.get_fake_data_for_type(data_type=DataType.EMAIL),
            "email_is_preferred": milmove_faker.get_fake_data_for_type(data_type=DataType.BOOLEAN),
            "phone_is_preferred": milmove_faker.get_fake_data_for_type(data_type=DataType.BOOLEAN),
        }

        with self.rest(method="PATCH", url=sm_url, data=json.dumps(payload), **sm_request_kwargs) as resp:
            resp: RestResponseContextManager

            task_name = "add_contact_info"

            log_response_info(response=resp, task_name=task_name)

            if resp.status_code != HTTPStatus.OK:
                resp.failure("Unable to add customer contact info.")

                log_response_failure(response=resp, task_name=task_name)

                return

        # Next we need a duty location

        duty_location_url, duty_location_request_kwargs = self.request_preparer.prep_internal_request(
            endpoint="/duty_locations?search=fort"
        )

        with self.rest(method="GET", url=duty_location_url, **duty_location_request_kwargs) as resp:
            resp: RestResponseContextManager

            task_name = "search_duty_locations"

            log_response_info(response=resp, task_name=task_name)

            if resp.status_code == HTTPStatus.OK:
                duty_locations: JSONArray = resp.js
            else:
                resp.failure("Unable to find duty locations.")

                log_response_failure(response=resp, task_name=task_name)

                return

        # Don't care too much about which one for this load test, so just grabbing the first one.
        origin_duty_location = duty_locations[0]

        payload = {"id": service_member_id, "current_station_id": origin_duty_location["id"]}

        with self.rest(method="PATCH", url=sm_url, data=json.dumps(payload), **sm_request_kwargs) as resp:
            resp: RestResponseContextManager

            task_name = "add_current_duty_location"

            log_response_info(response=resp, task_name=task_name)

            if resp.status_code != HTTPStatus.OK:
                resp.failure("Unable to add current duty location.")

                log_response_failure(response=resp, task_name=task_name)

                return

        # Next we'll input the current mailing address. We could use a fully random one, or base it
        # in part on where the duty location is, which we'll do.

        # First, we'll get the address of the duty location.
        address_url, address_request_kwargs = self.request_preparer.prep_internal_request(
            endpoint=f"/addresses/{origin_duty_location['address_id']}",
            endpoint_name="/addresses/{addressId}",
        )

        with self.rest(method="GET", url=address_url, **address_request_kwargs) as resp:
            resp: RestResponseContextManager

            task_name = "get_duty_location_address"

            log_response_info(response=resp, task_name=task_name)

            if resp.status_code == HTTPStatus.OK:
                duty_location_address: JSONObject = resp.js
            else:
                resp.failure("Unable to find duty location address.")

                log_response_failure(response=resp, task_name=task_name)

                return

        # Zip code is validated as part of on-boarding.

        zip_code_url, zip_code_request_kwargs = self.request_preparer.prep_internal_request(
            endpoint=f"/rate_engine_postal_codes/{duty_location_address['postalCode']}?postal_code_type=origin",
            endpoint_name="/rate_engine_postal_codes/{postal_code}",
        )

        with self.rest(method="GET", url=zip_code_url, **zip_code_request_kwargs) as resp:
            resp: RestResponseContextManager

            task_name = "validate_zip_code"

            log_response_info(response=resp, task_name=task_name)

            if resp.status_code != HTTPStatus.OK:
                resp.failure("Unable to validate zip code.")

                log_response_failure(response=resp, task_name=task_name)

                return

        # Now we can add the current mailing address.

        payload = {
            "id": service_member_id,
            "residential_address": {
                "streetAddress1": milmove_faker.get_fake_data_for_type(data_type=DataType.STREET_ADDRESS),
                "city": duty_location_address["city"],
                "state": duty_location_address["state"],
                "postalCode": duty_location_address["postalCode"],
            },
        }

        with self.rest(method="PATCH", url=sm_url, data=json.dumps(payload), **sm_request_kwargs) as resp:
            resp: RestResponseContextManager

            task_name = "add_current_mailing_address"

            log_response_info(response=resp, task_name=task_name)

            if resp.status_code != HTTPStatus.OK:
                resp.failure("Unable to add current mailing address.")

                log_response_failure(response=resp, task_name=task_name)

                return

        # Next is the backup mailing address

        # We'll use mostly the same address as the current one, just changing out the street address
        payload["residential_address"]["streetAddress1"] = milmove_faker.get_fake_data_for_type(
            data_type=DataType.STREET_ADDRESS
        )

        with self.rest(method="PATCH", url=sm_url, data=json.dumps(payload), **sm_request_kwargs) as resp:
            resp: RestResponseContextManager

            task_name = "add_backup_mailing_address"

            log_response_info(response=resp, task_name=task_name)

            if resp.status_code != HTTPStatus.OK:
                resp.failure("Unable to add backup mailing address.")

                log_response_failure(response=resp, task_name=task_name)

                return

        # Finally, we'll add the backup contact information.

        backup_contact_url, backup_contact_request_kwargs = self.request_preparer.prep_internal_request(
            endpoint=f"/service_members/{service_member_id}/backup_contacts",
            endpoint_name="/service_members/{serviceMemberId}/backup_contacts",
        )

        backup_contact_name = f"{milmove_faker.get_fake_data_for_type(data_type=DataType.FIRST_NAME)} {milmove_faker.get_fake_data_for_type(data_type=DataType.LAST_NAME)}"

        payload = {
            "name": backup_contact_name,
            "email": milmove_faker.get_fake_data_for_type(data_type=DataType.EMAIL),
            "telephone": milmove_faker.get_fake_data_for_type(data_type=DataType.PHONE),
            "permission": "NONE",
        }

        with self.rest(
            method="POST", url=backup_contact_url, data=json.dumps(payload), **backup_contact_request_kwargs
        ) as resp:
            resp: RestResponseContextManager

            task_name = "add_backup_contact"

            log_response_info(response=resp, task_name=task_name)

            if resp.status_code != HTTPStatus.CREATED:
                resp.failure("Unable to add backup contact info.")

                log_response_failure(response=resp, task_name=task_name)

                return
