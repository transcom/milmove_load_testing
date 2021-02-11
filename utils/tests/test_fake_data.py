# -*- coding: utf-8 -*-
""" Tests utils/fake_data.py """
import pytest

from utils.fake_data import MilMoveProvider
from utils.fake_data import MilMoveData
from faker import Faker
from faker.generator import Generator
from datetime import datetime
from utils.constants import DataType


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

    def test_safe_phone_number(self):
        """
        Tests the returned phone number is the correct length and structure
        """
        phone_number = self.fake.safe_phone_number()
        assert type(phone_number) is str
        assert len(phone_number) == 12
        assert phone_number.index("555") == 4

    def test_time_military(self):
        """
        Tests the returned time is the correct length and structure
        """
        time = self.fake.time_military()
        assert type(time) is str
        assert len(time) == 5
        assert time.endswith("Z")

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
        first_name = self.fake.safe_first_name()
        assert type(first_name) is str
        assert first_name != self.provider.current_name["first_name"]

    def test_safe_last_name(self):
        """
        Tests the last name is a string and does not equal the current last name
        """
        last_name = self.fake.safe_first_name()
        assert type(last_name) is str
        assert last_name != self.provider.current_name["last_name"]

    def test_safe_street_address(self):
        """
        Tests the return address is a string
        """
        assert type(self.fake.safe_street_address()) is str


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
        assert len(self.data.data_types) == 16

    def test_get_random_choice(self):
        """
        Tests that an element is returned from the provided list
        """
        list = ["string1", 4, True, "string2"]
        assert self.data.get_random_choice(list) in list

    def test_get_fake_data_for_type(self):
        """
        Tests data is returned that matches the requested data type if the data type exists
        """
        assert isinstance(self.data.get_fake_data_for_type(DataType.BOOLEAN), bool)
        assert self.data.get_fake_data_for_type("time") is None
