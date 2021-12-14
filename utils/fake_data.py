# -*- coding: utf-8 -*-
""" utils/fake_data.py is for Faker classes and functions to set up test data """
import logging
import json
import string
from datetime import datetime

from faker import Faker
from faker.providers.date_time import Provider as DateProvider  # extends BaseProvider
from faker.providers.address.en_US import Provider as AddressProvider  # extends BaseProvider

from .constants import DataType, ZERO_UUID

logger = logging.getLogger(__name__)


class MilMoveProvider(AddressProvider, DateProvider):
    """Faker Provider class for sending back customized MilMove data."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with open("static/fake_data.json") as f:
            self.safe_data = json.load(f)

        self.current_name = {"first_name": "", "last_name": ""}
        self.first_name_used = True
        self.last_name_used = True

    def safe_phone_number(self):
        """
        Sends back a standard US phone number with 555 as the middle three digits. First digit must be 2-9.
        Ex: 242-555-6674
        """
        area_code = f"{self.random_int(2, 9)}{str(self.random_number(digits=2)).zfill(2)}"
        last_four = f"{self.random_number(digits=4)}".zfill(4)

        return f"{area_code}-555-{last_four}"

    def time_military(self):
        """
        Returns a time in military format. Ex: 0830Z
        """
        hours = f"{self.random_int(0, 23)}".zfill(2)
        minutes = f"{self.random_int(0, 59)}".zfill(2)

        return f"{hours}{minutes}Z"

    def iso_date_time(self):
        """
        Returns an ISO-formatted date as a string. Ex: 2020-06-01T16:06:22
        """
        return datetime.isoformat(self.date_time())

    def _set_safe_name(self):
        """
        Randomly selects a safe full name to use.
        """
        random_name = self.random_element(self.safe_data["names"])
        self.first_name_used, self.last_name_used = False, False

        self.current_name.update({"first_name": random_name["first_name"], "last_name": random_name["last_name"]})

    def safe_first_name(self):
        """
        Returns a safe first name as a string.
        """
        if self.first_name_used:
            self._set_safe_name()

        self.first_name_used = True
        return self.current_name["first_name"]

    def safe_last_name(self):
        """
        Returns a safe last name as a string.
        """
        if self.last_name_used:
            self._set_safe_name()

        self.last_name_used = True
        return self.current_name["last_name"]

    def safe_street_address(self):
        """
        Returns a safe street address as a string.
        """
        return self.random_element(self.safe_data["addresses"])

    def safe_postal_code(self):
        """
        Returns a safe postal code as a string.
        """
        while True:
            state = self.state_abbr(include_territories=False)
            if state != "AK" and state != "HI":
                return self.postalcode_in_state(state)

    def safe_uuid(self):
        """
        Returns an empty uuid as a string.
        """
        return ZERO_UUID

    def tac(self):
        """
        Returns an uppercase alphanumeric transportation accounting code 4 chars in length, there is no guarantee these
        correspond to the stored list of validated TACs in the database
        """
        return "".join(self.random_elements(string.ascii_uppercase + string.digits, 4))


class MilMoveData:
    """Base class to return fake data to use in MilMove endpoints."""

    def __init__(self):
        """
        Sets up a Faker attribute and a dict of handled data types for this instance.
        """
        self.fake = Faker()
        self.fake.add_provider(MilMoveProvider)
        self.data_types = {
            DataType.FIRST_NAME: self.fake.safe_first_name,
            DataType.LAST_NAME: self.fake.safe_last_name,
            DataType.PHONE: self.fake.safe_phone_number,
            DataType.EMAIL: self.fake.safe_email,
            DataType.STREET_ADDRESS: self.fake.safe_street_address,
            DataType.CITY: self.fake.city,
            DataType.STATE: self.fake.state_abbr,
            DataType.POSTAL_CODE: self.fake.safe_postal_code,
            DataType.POSTAL_CODE_VARIANT: self.fake.safe_postal_code,
            DataType.COUNTRY: self.fake.country,
            DataType.DATE: self.fake.date_between,
            DataType.DATE_TIME: self.fake.iso_date_time,
            DataType.TIME_MILITARY: self.fake.time_military,
            DataType.SENTENCE: self.fake.sentence,
            DataType.BOOLEAN: self.fake.boolean,
            DataType.INTEGER: self.fake.random_int,
            DataType.UUID: self.fake.safe_uuid,
            DataType.TAC: self.fake.tac,
        }

    def get_random_choice(self, choices):
        """Given a list of random choices, returns one of them."""
        return self.fake.random_element(choices)

    def get_fake_data_for_type(self, data_type, params=None):
        """Given a specific data type, returns faker data for that type (if a mapping exists)."""
        if not params:
            params = []
        try:
            return self.data_types[data_type](*params)
        except KeyError:  # data_type isn't in dictionary
            logger.exception(f"An unexpected data type was passed into get_fake_data_for_type: {data_type}")
            return None
