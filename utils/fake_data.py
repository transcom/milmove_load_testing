# -*- coding: utf-8 -*-
""" utils/fake_data.py is for Faker classes and functions to set up test data """
from typing import Optional
from copy import deepcopy

from faker import Faker
from faker.providers import BaseProvider

from .constants import DataTypes


class MilMoveProvider(BaseProvider):
    """ Faker Provider class for sending back customized MilMove data. """

    def safe_phone_number(self):
        """
        Sends back a standard US phone number with 555 as the middle three digits.
        Ex: 042-555-6674
        """
        area_code = f"{self.random_number(digits=3)}".zfill(3)
        last_four = f"{self.random_number(digits=4)}".zfill(4)

        return f"{area_code}-555-{last_four}"


class MilMoveData:
    """ Base class to return fake data to use in MilMove endpoints. """

    def __init__(self):
        """
        Sets up a Faker attribute and a dict of handled data types for this instance.
        """
        self.fake = Faker()
        self.fake.add_provider(MilMoveProvider)

        self.data_types = {
            DataTypes.FIRST_NAME: self.fake.first_name,  # TODO: replace with data from milmove fake address spreadsheet
            DataTypes.LAST_NAME: self.fake.last_name,  # TODO: same ^
            DataTypes.PHONE: self.fake.safe_phone_number,
            DataTypes.EMAIL: self.fake.safe_email,
            DataTypes.STREET_ADDRESS: self.fake.street_address,  # TODO: same ^^
            DataTypes.CITY: self.fake.city,
            DataTypes.STATE: self.fake.state_abbr,
            DataTypes.POSTAL_CODE: self.fake.postalcode,
            DataTypes.COUNTRY: self.fake.country,
            DataTypes.DATE: self.fake.date,
            DataTypes.SENTENCE: self.fake.sentence,
            DataTypes.BOOLEAN: self.fake.boolean,
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
        for field_name, data_type in data.items():
            try:
                data[field_name] = self.data_types[data_type]()
            except (KeyError, TypeError):  # the data_type isn't in our dict or it's unhashable
                try:  # assume it was an iterable and try to pick an element from it:
                    data[field_name] = self.fake.random_element(data_type)
                except TypeError:
                    pass  # it wasn't an iterable value, so just leave this field alone

        # Now we're going to use the override data that was passed in instead of any generated fake data for those
        # fields:
        data.update(overrides if overrides else {})

        return data
