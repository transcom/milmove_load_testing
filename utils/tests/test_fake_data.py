# -*- coding: utf-8 -*-
""" Tests utils/fake_data.py """
import pytest

from utils.fake_data import MilMoveProvider
from faker import Faker
from faker.generator import Generator
from datetime import datetime


class TestMilMoveProvider:
    """ Tests the MilMoveProvide class and its methods. """

    @classmethod
    def setup_class(cls):
        """ Initialize the MilMoveProvide that will be tested. """
        cls.fake = Faker()
        cls.fake.add_provider(MilMoveProvider)
        cls.provider = MilMoveProvider(Generator())

    # faker takes functions and makes own, attributes is different

    def test_init(self):
        """
        Tests that the __init__ from the setup_class method worked correctly.
        """
        assert self.provider.current_name == {"first_name": "", "last_name": ""}
        assert self.provider.first_name_used is True
        assert self.provider.last_name_used is True

    def test_safe_phone_number(self):
        phone_number = self.fake.safe_phone_number()
        assert type(phone_number) is str
        assert len(phone_number) == 12
        assert phone_number.index("555") == 4

    def test_time_military(self):
        time = self.fake.time_military()
        assert type(time) is str
        assert len(time) == 5
        assert time.endswith("Z")

    def test_iso_date_time(self):
        date_value = self.fake.iso_date_time()
        assert type(date_value) is str
        try:
            format_string = "%Y-%m-%dT%H:%M:%S"
            datetime.strptime(date_value, format_string)
        except ValueError:
            pytest.fail(ValueError)

    def test__set_safe_name(self):
        self.provider._set_safe_name()
        assert self.provider.current_name["first_name"] != ""
        assert self.provider.current_name["last_name"] != ""
        assert self.provider.first_name_used is False
        assert self.provider.last_name_used is False

    def test_safe_first_name(self):
        first_name = self.fake.safe_first_name()
        assert type(first_name) is str
        assert first_name != self.provider.current_name["first_name"]

    def test_safe_last_name(self):
        last_name = self.fake.safe_first_name()
        assert type(last_name) is str
        assert last_name != self.provider.current_name["last_name"]

    def test_safe_street_address(self):
        assert type(self.fake.safe_street_address()) is str
