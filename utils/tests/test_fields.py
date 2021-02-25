# -*- coding: utf-8 -*-
""" Tests utils/fields.py """
import re

import pytest
from faker.generator import Generator

from utils.fields import BaseAPIField, ArrayField, EnumField, ObjectField
from utils.constants import DataType
from utils.fake_data import MilMoveProvider, MilMoveData


class TestBaseAPIField:
    """ Tests the BaseAPIField class and its methods """

    @classmethod
    def setup_class(cls):
        """ Initialize the BaseAPIField that will be tested. """
        cls.field = BaseAPIField(DataType.STREET_ADDRESS, name="streetAddress")
        cls.faker = MilMoveData()

    def test_add_discriminator_value(self):
        """
        Tests a value is appended to the list of discriminator values.
        """
        test_string = "test value"
        self.field.add_discriminator_value(test_string)
        assert test_string in self.field.discriminator_values

    def test_is_valid_discriminator(self):
        """
        Tests if a value is in the discriminator values list
        """
        self.field.add_discriminator_value("test value 3")
        assert self.field.is_valid_discriminator("test value 3") is True
        assert self.field.is_valid_discriminator("second test value") is False

    def test_generate_fake_data(self):
        """
        Tests if a value generated is the correct type or the override value
        """
        assert self.field.generate_fake_data(self.faker) in MilMoveProvider(Generator()).safe_data["addresses"]
        assert self.field.generate_fake_data(self.faker, overrides={"streetAddress": "test address"}) == "test address"


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
        items_field = BaseAPIField(data_type=DataType.PHONE, name="phoneNumber")
        cls.array_field = ArrayField(name="phoneNumbers", min_items=1, max_items=5, items_field=items_field)
        cls.faker = MilMoveData()

    def test_generate_fake_data(self):
        array1 = self.array_field.generate_fake_data(self.faker)
        assert re.match("^[2-9]\\d{2}-555-\\d{4}$", array1[0])

        overrides = {"phoneNumbers": [{"phoneNumber": "test 1"}, {"phoneNumber": "test 2"}]}
        array2 = self.array_field.generate_fake_data(self.faker, overrides=overrides)
        assert array2[0] == "test 1" and array2[1] == "test 2"


class TestObjectField:
    """ Tests the ObjectField class and its methods. """

    @classmethod
    def setup_class(cls):
        """ Initialize the ObjectField that will be tested. """
        cls.object_field = ObjectField()
        cls.faker = MilMoveData()

    def test_init(self):
        """
        Tests that the ObjectField was initialized with the right values, including the logic from the __post_init__
        method.
        """
        assert self.object_field.object_fields == []
        assert self.object_field.data_type == DataType.OBJECT
        assert self.object_field.name == ""
        assert self.object_field.discriminator == ""
        assert self.object_field.discriminator_values == []
        assert self.object_field.required is False

    def test_add_field(self):
        """ Tests adding one field to the ObjectField instance's list of sub-fields. """
        self.object_field.object_fields = []

        test_field = BaseAPIField(name="baseField", data_type=DataType.INTEGER)
        self.object_field.add_field(test_field)
        assert test_field in self.object_field.object_fields

        # Testing that we can add another ObjectField to this ObjectField's list of subfields,
        # and that the subfields of the two Objects do not merge:
        test_object = ObjectField(name="testObject")
        test_object_subfield = BaseAPIField(name="testSentence", data_type=DataType.SENTENCE)
        test_object.add_field(test_object_subfield)
        self.object_field.add_field(test_object)
        assert test_object in self.object_field.object_fields
        assert test_object_subfield in test_object.object_fields
        assert test_object_subfield not in self.object_field.object_fields

        test_field_duplicate = BaseAPIField(name="baseField", data_type=DataType.DATE)
        self.object_field.add_field(test_field_duplicate)  # unique=False, so duplicates should be allowed
        assert test_field_duplicate in self.object_field.object_fields
        assert test_field in self.object_field.object_fields  # make sure the original is still in the list
        assert test_field.name == test_field_duplicate.name

        test_object_duplicate = BaseAPIField(name="testObject", data_type=DataType.SENTENCE)
        self.object_field.add_field(test_object_duplicate, unique=True)
        assert test_object_duplicate not in self.object_field.object_fields
        assert test_object in self.object_field.object_fields

    def test_add_fields(self):
        """ Tests adding multiple fields at once to the the ObjectField's list of sub-fields. Calls add_field. """
        self.object_field.object_fields = []

        field_list = [
            BaseAPIField(name="baseField", data_type=DataType.INTEGER),
            BaseAPIField(name="testSentence", data_type=DataType.SENTENCE),
        ]
        self.object_field.add_fields(field_list)
        assert all([field in self.object_field.object_fields for field in field_list])

        duplicate_field_list = [BaseAPIField(name="baseField", data_type=DataType.PHONE)]
        self.object_field.add_fields(duplicate_field_list)  # unique=False
        assert all([field in self.object_field.object_fields for field in duplicate_field_list])
        assert all([field in self.object_field.object_fields for field in field_list])
        assert len([field for field in self.object_field.object_fields if field.name == "baseField"]) == 2

        unique_field = BaseAPIField(name="uniqueField", data_type=DataType.COUNTRY)
        unique_field_list = [BaseAPIField(name="testSentence", data_type=DataType.EMAIL), unique_field]
        self.object_field.add_fields(unique_field_list, unique=True)
        assert len([field for field in self.object_field.object_fields if field.name == "testSentence"]) == 1
        assert unique_field in self.object_field.object_fields

    def test_combine_fields(self):
        """
        Tests combining fields with this ObjectField.
        Expected behavior:
         - If the field is a subclass of BaseAPIField, but not another ObjectField, it should simply add the field to
           this ObjectField's list of sub-fields.
         - If the field is another ObjectField instance, it should add all of the sub-fields of the ObjectField to this
           ObjectField's list of sub-fields.
        """
        self.object_field.object_fields = []

        array_field = ArrayField(name="arrayField")
        self.object_field.combine_fields(array_field)
        assert array_field in self.object_field.object_fields

        self.object_field.combine_fields(array_field, unique=True)
        assert len([field for field in self.object_field.object_fields if field.name == "arrayField"]) == 1

        test_object = ObjectField(name="testObject")
        test_object_subfield = BaseAPIField(name="testSentence", data_type=DataType.SENTENCE)
        test_object.add_field(test_object_subfield)

        self.object_field.combine_fields(test_object)
        assert test_object not in self.object_field.object_fields
        assert all([test_field in self.object_field.object_fields for test_field in test_object.object_fields])

        with pytest.raises(TypeError):
            self.object_field.combine_fields("field string")
