# -*- coding: utf-8 -*-
""" Tests utils/parsers.py """
import re

from utils.fields import BaseAPIField, ArrayField, EnumField
from utils.constants import DataType
from utils.fake_data import MilMoveProvider, MilMoveData
from faker.generator import Generator


class TestBaseAPIField:
    """ Tests the BaseAPIField class and its methods """

    @classmethod
    def setup_class(cls):
        """ Initialize the BaseAPIField that will be tested. """
        cls.field1 = BaseAPIField(DataType.STREET_ADDRESS, name="streetAddress")
        cls.faker = MilMoveData()

    def test_add_discriminator_value(self):
        """
        Tests a value is appended to the list of discriminator values.
        """
        testString = "test value"
        self.field1.add_discriminator_value(testString)
        assert testString in self.field1.discriminator_values

    def test_is_valid_discriminator(self):
        """
        Tests if a value is in the discriminator values list
        """
        self.field1.add_discriminator_value("test value 3")
        assert self.field1.is_valid_discriminator("test value 3") is True
        assert self.field1.is_valid_discriminator("second test value") is False

    def test_generate_fake_data(self):
        """
        Tests if a value generated is the correct type or the override value
        """
        faker = MilMoveData()
        assert self.field1.generate_fake_data(faker) in MilMoveProvider(Generator()).safe_data["addresses"]
        assert self.field1.generate_fake_data(faker, overrides={"streetAddress": "test address"}) == "test address"


class TestEnumField:
    @classmethod
    def setup_class(cls):
        """ Initialize the EnumField that will be tested. """
        cls.options = ["PERMANENT_CHANGE_OF_STATION", "RETIREMENT", "SEPARATION", "GHC", "NTS"]
        cls.enum_field = EnumField(name="ordersType", options=cls.options)
        cls.faker = MilMoveData()

    def test_generate_fake_data(self):
        assert self.enum_field.generate_fake_data(self.faker) in self.options
        assert self.enum_field.generate_fake_data(self.faker, overrides={"ordersType": "test"}) == "test"


class TestArrayField:
    @classmethod
    def setup_class(cls):
        """ Initialize the ArrayField that will be tested. """
        items_field = BaseAPIField(data_type=DataType.PHONE)
        cls.array_field = ArrayField(name="phoneNumbers", min_items=1, max_items=5, items_field=items_field)
        cls.faker = MilMoveData()

    def test_generate_fake_data(self):
        array1 = self.array_field.generate_fake_data(self.faker)
        assert re.match("^[2-9]\\d{2}-555-\\d{4}$", array1[0])

        overrides = {"phoneNumbers": ["test 1", "test 2", "test 3", "test 4"]}
        array2 = self.array_field.generate_fake_data(self.faker, overrides=overrides)
        assert array2[0] == overrides["phoneNumbers"][0]
