# -*- coding: utf-8 -*-
""" Tests utils/fake_data.py """
import re
from datetime import datetime

import pytest
from faker import Faker
from faker.generator import Generator

from utils.constants import DataType
from utils.fake_data import MilMoveProvider, MilMoveData


class TestMilMoveProvider:
    """ Tests the MilMoveProvide class and its methods. """

    @classmethod
    def setup_class(cls):
        """ Initialize the MilMoveProvide that will be tested. """
        cls.fake = Faker()
        cls.fake.add_provider(MilMoveProvider)
        cls.provider = MilMoveProvider(Generator())

    def test_init(self):
        """
        Tests that the __init__ from the setup_class method worked correctly.
        """
        assert self.provider.current_name == {"first_name": "", "last_name": ""}
        assert self.provider.first_name_used is True
        assert self.provider.last_name_used is True
        assert self.provider.safe_data is not None

    def test_safe_phone_number(self):
        """
        Tests the returned phone number is the correct length and structure
        """
        phone_number = self.fake.safe_phone_number()
        assert type(phone_number) is str
        assert re.match("^[2-9]\\d{2}-555-\\d{4}$", phone_number)

    def test_time_military(self):
        """
        Tests the returned time is the correct length and structure
        """
        time = self.fake.time_military()
        assert type(time) is str
        assert re.match("^[0-9]{4}Z$", time)

    def test_iso_date_time(self):
        """
        Tests the returned time is a string in ISO date time format
        """
        date_value = self.fake.iso_date_time()
        assert type(date_value) is str
        try:
            format_string = "%Y-%m-%dT%H:%M:%S"
            datetime.strptime(date_value, format_string)
        except ValueError:
            pytest.fail(ValueError)

    def test__set_safe_name(self):
        """
        Tests the current name does not equal empty strings and sets variables to false
        """
        self.provider._set_safe_name()
        assert self.provider.current_name["first_name"] != ""
        assert self.provider.current_name["last_name"] != ""
        assert self.provider.first_name_used is False
        assert self.provider.last_name_used is False

    def test_safe_first_name(self):
        """
        Tests the first name is a string and does not equal the current first name
        """
        fake_name = self.fake.safe_first_name()
        for name in self.provider.safe_data["names"]:
            if name["first_name"] == fake_name:
                found = True
        assert found

    def test_safe_last_name(self):
        """
        Tests the last name is a string and does not equal the current last name
        """
        fake_name = self.fake.safe_last_name()
        for name in self.provider.safe_data["names"]:
            if name["last_name"] == fake_name:
                found = True
        assert found

    def test_safe_street_address(self):
        """
        Tests the return address is a string
        """
        address = self.fake.safe_street_address()
        assert type(address) is str
        assert address in self.provider.safe_data["addresses"]

    def test_safe_postal_code(self):
        code = self.fake.safe_postal_code()
        assert type(code) is str
        assert re.match("^[0-9]{5}$", code)


class TestMilMoveData:
    """ Tests the MilMoveData class and its methods. """

    @classmethod
    def setup_class(cls):
        """ Initialize the MilMoveData that will be tested. """
        cls.data = MilMoveData()

    def test_init(self):
        """
        Tests that the __init__ from the setup_class method worked correctly.
        """
        assert isinstance(self.data.fake, Faker)
        assert type(self.data.data_types) is dict
        assert self.data.data_types is not None

    def test_get_random_choice(self):
        """
        Tests that an element is returned from the provided list
        """
        random_list = ["string1", 4, True, "string2"]
        assert self.data.get_random_choice(random_list) in random_list

    def test_get_fake_data_for_type(self):
        """
        Tests data is returned that matches the requested data type if the data type exists
        """
        assert isinstance(self.data.get_fake_data_for_type(DataType.BOOLEAN), bool)
        assert self.data.get_fake_data_for_type("time") is None
