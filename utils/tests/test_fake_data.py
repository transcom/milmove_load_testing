# -*- coding: utf-8 -*-
""" Tests utils/fake_data.py """
import re
from copy import deepcopy
from datetime import datetime

import pytest
from faker import Faker

from utils.constants import DataType
from utils.fake_data import MilMoveData, MilMoveProvider


class TestMilMoveProvider:
    """Tests the MilMoveProvide class and its methods."""

    fake: Faker

    @classmethod
    def setup_class(cls):
        """Initialize the MilMoveProvide that will be tested."""
        cls.fake = Faker()
        cls.fake.add_provider(MilMoveProvider)

        # Grab the initialized provider to make it easier to check some data.
        cls.provider: MilMoveProvider = cls.fake.factories[0].provider(name=MilMoveProvider.__provider__)

    def test_init(self):
        """
        Tests that the __init__ from the setup_class method worked correctly.
        """
        assert self.provider.current_name == {"first_name": "", "middle_name": "", "last_name": ""}
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
        Tests the current name does not equal empty strings and sets variables to false. Also ensure
        that we do change the same from the previous one.
        """
        # We'll set only two names in the safe data to increase the likelihood of the same one being
        # picked twice. This way we can be more sure that this is working properly. This way we can
        # also make it so that "all" names have a middle name, which lets us make assertions on it.
        self.provider.safe_data["names"] = [
            {"first_name": "Jason", "middle_name": "Theodore", "last_name": "Ash"},
            {"first_name": "Nevaeh", "middle_name": "Evans", "last_name": "Wilson"},
        ]

        self.provider._set_safe_name()
        assert self.provider.current_name["first_name"] != ""
        assert self.provider.current_name["middle_name"] != ""
        assert self.provider.current_name["last_name"] != ""
        assert self.provider.first_name_used is False
        assert self.provider.middle_name_used is False
        assert self.provider.last_name_used is False

        previous_name = deepcopy(self.provider.current_name)

        self.provider._set_safe_name()

        assert self.provider.current_name != previous_name

    def test_safe_first_name(self):
        """
        Tests the first name is a string and does not equal the current first name
        """
        valid_first_names = {name["first_name"] for name in self.provider.safe_data["names"]}

        fake_name1 = self.fake.safe_first_name()

        assert fake_name1 in valid_first_names
        assert fake_name1 == self.provider.current_name["first_name"]

        fake_name2 = self.fake.safe_first_name()

        assert fake_name1 != self.provider.current_name["first_name"]
        assert fake_name2 == self.provider.current_name["first_name"]

        assert fake_name2 in valid_first_names

    def test_safe_middle_name(self):
        """
        Tests the middle name is a string and does not equal the current middle name
        """
        valid_middle_names = {name["middle_name"] for name in self.provider.safe_data["names"]}

        fake_name1 = self.fake.safe_middle_name()

        assert fake_name1 in valid_middle_names
        assert fake_name1 == self.provider.current_name["middle_name"]

        fake_name2 = self.fake.safe_middle_name()

        # A lot of the fake names have blank middle names, so we only want to check that they aren't
        # equal if at least one of them isn't blank.
        if fake_name1 or fake_name2:
            assert fake_name1 != self.provider.current_name["middle_name"]

        assert fake_name2 == self.provider.current_name["middle_name"]

        assert fake_name2 in valid_middle_names

    def test_safe_last_name(self):
        """
        Tests the last name is a string and does not equal the current last name
        """
        valid_last_names = {name["last_name"] for name in self.provider.safe_data["names"]}

        fake_name1 = self.fake.safe_last_name()

        assert fake_name1 in valid_last_names
        assert fake_name1 == self.provider.current_name["last_name"]

        fake_name2 = self.fake.safe_last_name()

        assert fake_name1 != self.provider.current_name["last_name"]
        assert fake_name2 == self.provider.current_name["last_name"]

        assert fake_name2 in valid_last_names

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

    def test_safe_uuid(self):
        assert self.fake.safe_uuid() == "00000000-0000-0000-0000-000000000000"

    def test_safe_city_state_zip(self):
        city_state_zip = self.fake.safe_city_state_zip()

        assert city_state_zip.get("city") is not None
        assert len(city_state_zip["city"]) > 0

        assert city_state_zip.get("state") is not None
        assert len(city_state_zip["state"]) == 2

        assert city_state_zip.get("postalCode") is not None
        assert re.match("^[0-9]{5}$", city_state_zip["postalCode"])


class TestMilMoveData:
    """Tests the MilMoveData class and its methods."""

    @classmethod
    def setup_class(cls):
        """Initialize the MilMoveData that will be tested."""
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
