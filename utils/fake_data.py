# -*- coding: utf-8 -*-
""" utils/fake_data.py is for Faker classes and functions to set up test data """
import logging
from typing import Optional
from copy import deepcopy
from datetime import datetime

from faker import Faker
from faker.providers.date_time import Provider as DateProvider  # extends BaseProvider

from .constants import DataType

logger = logging.getLogger(__name__)


class MilMoveProvider(DateProvider):
    """ Faker Provider class for sending back customized MilMove data. """

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


class MilMoveData:
    """ Base class to return fake data to use in MilMove endpoints. """

    def __init__(self):
        """
        Sets up a Faker attribute and a dict of handled data types for this instance.
        """
        self.fake = Faker()
        self.fake.add_provider(MilMoveProvider)

        self.data_types = {
            DataType.FIRST_NAME: self.fake.first_name,  # TODO: replace with data from milmove fake address spreadsheet
            DataType.LAST_NAME: self.fake.last_name,  # TODO: same ^
            DataType.PHONE: self.fake.safe_phone_number,
            DataType.EMAIL: self.fake.safe_email,
            DataType.STREET_ADDRESS: self.fake.street_address,  # TODO: same ^^
            DataType.CITY: self.fake.city,
            DataType.STATE: self.fake.state_abbr,
            DataType.POSTAL_CODE: self.fake.postalcode,
            DataType.COUNTRY: self.fake.country,
            DataType.DATE: self.fake.date,
            DataType.DATE_TIME: self.fake.iso_date_time,
            DataType.TIME_MILITARY: self.fake.time_military,
            DataType.SENTENCE: self.fake.sentence,
            DataType.BOOLEAN: self.fake.boolean,
            DataType.INTEGER: self.fake.random_number,
            DataType.UUID: self.fake.uuid4,
        }

    def populate_fake_data(self, fields: dict, overrides: Optional[dict] = None) -> dict:
        """
        Takes in a dictionary of field names and their intended data types, returns a dictionary of those field name
        with fake data populated. Optionally accepts a dictionary of override data to use instead of the fake data for
        certain fields.

        :param fields: dict, format: [str field_name, enum data_type]
        :param overrides: optional dict of set values to use
        :return: data dict, format: [str field_name, value]
        """
        data = deepcopy(fields)
        for field_name, data_type in fields.items():
            try:
                data[field_name] = self.data_types[data_type]()
            except (KeyError, TypeError):  # the data_type isn't in our dict or it's unhashable
                try:  # assume it was an iterable and try to pick an element from it:
                    data[field_name] = self.fake.random_element(data_type)
                except TypeError:
                    logging.exception(f"No data gen handling for field {field_name} type {data_type}.")
                    pass  # it wasn't an iterable value, so just leave this field alone

        # Now we're going to use the override data that was passed in instead of any generated fake data for those
        # fields:
        data.update(overrides if overrides else {})

        return data
