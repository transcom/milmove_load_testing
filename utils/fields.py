# -*- coding: utf-8 -*-
""" utils/fields.py is for class representations of API fields """
import logging
from dataclasses import dataclass
from random import randint
from typing import List

from .constants import DataType, ARRAY_MIN, ARRAY_MAX

logger = logging.getLogger(__name__)


@dataclass
class BaseAPIField:
    data_type: DataType
    name: str = ""
    required: bool = False
    discriminator_values: list = None
    definition: dict = None

    def __post_init__(self):
        """
        If no value was passed in on __init__, initialize the discriminator_values instance attribute to an empty list
        after the default __init__ method executes.

        This is done to avoid setting a mutable datatype at the class-level, instead keeping it at the instance-level to
        ensure data integrity.
        """
        if not self.discriminator_values:
            self.discriminator_values = []

    def add_discriminator_value(self, value):
        """
        Adds a discriminator value to the current list of discriminator values on this field.
        :param value: str
        """
        self.discriminator_values.append(value)

    def is_valid_discriminator(self, value):
        """
        Checks if the value passed in is a valid discriminator value for this field. Assumes that if no value was
        provided, or if there are no discriminators on the field, that this field is NOT discriminated and is therefore
        valid.

        :param value: str
        :return: bool
        """
        if value and self.discriminator_values and value not in self.discriminator_values:
            return False

        return True  # default assumes the field is not discriminated

    def generate_fake_data(self, faker, **kwargs):
        """
        Gets fake data from the Faker class based on this fields data type.

        :param faker: MilMoveData
        :param kwargs:
        :return: any
        """
        if (overrides := kwargs.get("overrides")) and self.name in overrides:
            return overrides[self.name]

        params = (
            [self.definition.get("minimum", 0), self.definition.get("maximum", 9999)]
            if self.data_type == DataType.INTEGER
            else []
        )

        return faker.get_fake_data_for_type(self.data_type, params)


@dataclass
class EnumField(BaseAPIField):
    data_type: DataType = DataType.ENUM
    options: list = None

    def __post_init__(self):
        """
        If no value was passed in on __init__, initialize the options instance attribute to an empty list after the
        default __init__ method executes.

        This is done to avoid setting a mutable datatype at the class-level, instead keeping it at the instance-level to
        ensure data integrity.
        """
        super().__post_init__()
        if not self.options:
            self.options = []

    def generate_fake_data(self, faker, **kwargs):
        """
        Gets a random element from the options list and returns it.

        :param faker: MilMoveData
        :param kwargs:
        :return: str/int/element
        """
        if (overrides := kwargs.get("overrides")) and self.name in overrides:
            return overrides[self.name]

        return faker.get_random_choice(self.options)


@dataclass
class ArrayField(BaseAPIField):
    data_type: DataType = DataType.ARRAY
    min_items: int = ARRAY_MIN
    max_items: int = ARRAY_MAX
    items_field: BaseAPIField = None

    def generate_fake_data(self, faker, **kwargs):
        """
        Generate fake data for the array by generating X number of times for the base field for this array. X = a random
        number between the min and max values set for this ArrayField. Returns a list of the fake data.

        :param faker: MilMoveData
        :param kwargs:
        :return: list
        """
        fake_data = []

        if (overrides := kwargs.get("overrides")) and self.name in overrides:
            override_array = overrides[self.name]

            if isinstance(override_array, list):
                for item in override_array:
                    kwargs["overrides"] = item
                    fake_data.append(self.items_field.generate_fake_data(faker, **kwargs))

                return fake_data

            kwargs["overrides"] = override_array

        num_items = randint(self.min_items, self.max_items)

        for i in range(0, num_items):
            fake_data.append(self.items_field.generate_fake_data(faker, **kwargs))

        return fake_data


@dataclass
class ObjectField(BaseAPIField):
    data_type: DataType = DataType.OBJECT
    object_fields: List[BaseAPIField] = None  # list of the sub-fields in this object
    discriminator: str = ""  # name of the discriminator field, if one exists

    def __post_init__(self):
        """
        If no value was passed in on __init__, initialize the object_fields instance attribute to an empty list after
        the default __init__ method executes.

        This is done to avoid setting a mutable datatype at the class-level, instead keeping it at the instance-level to
        ensure data integrity.
        """
        super().__post_init__()
        if not self.object_fields:
            self.object_fields = []

    def has_field(self, field_name: str):
        """ Checks if this object contains a field with the provided name in its object_fields property. """
        return field_name in [f.name for f in self.object_fields]

    def add_field(self, field, unique=False):
        # We don't want to add duplicate fields if unique is True, so we check for existing fields with this name:
        if unique and field.name in [existing_field.name for existing_field in self.object_fields]:
            return
        self.object_fields.append(field)

    def add_fields(self, fields_list, unique=False):
        for field in fields_list:
            self.add_field(field, unique)

    def combine_fields(self, field: BaseAPIField, unique=False):
        """
        Combines the fields into this ObjectField. If combining with another ObjectField, all fields are added to the
        same list. If it is another field type, simply adds the field to this object's list of fields.

        :param field: BaseAPIField
        :param unique: boolean, indicates if the fields should be uniquely combined or if duplicates are fine
        """
        if not isinstance(field, BaseAPIField):
            logger.error(f"Unexpected object type passed into combine_fields: {type(field)}, {field}")
            raise TypeError("ObjectField instances can only be combined with other BaseAPIField instances.")

        if isinstance(field, ObjectField):
            self.add_fields(field.object_fields, unique)
        else:
            self.add_field(field, unique)

    def get_field(self, field_name):
        """
        Searches the object_fields list for a field matching the specific name passed in. Returns the BaseAPIField
        object if found; otherwise, returns None.

        :param field_name: str
        :return: BaseAPIField or None
        """
        for field in self.object_fields:
            if field.name == field_name:
                return field

        return None

    def update_required_fields(self, required_fields):
        """
        Takes in a list of required fields for the object and updates the `required` attribute for each of them.
        :param required_fields: list
        """
        for field in self.object_fields:
            field.required = field.name in required_fields

    def add_discriminator_value(self, value):
        """
        Adds a discriminator value for all of the fields currently in the object.
        :param value: str
        """
        for field in self.object_fields:
            field.add_discriminator_value(value)

        super().add_discriminator_value(value)

    def generate_discriminator_value(self, faker, overrides=None):
        """
        If the class has a discriminator, this function finds the field for the discriminator and generates data for
        that field (for the purpose of knowing what data to generate for the rest of the object fields).

        :param faker: MilMoveData
        :param overrides: dict, optional
        :return: str
        """
        if self.discriminator:
            if overrides and self.discriminator in overrides:
                return overrides[self.discriminator]  # if the user passed in an explicit discriminator value, use it

            discriminator_field = self.get_field(self.discriminator)
            if discriminator_field:
                return discriminator_field.generate_fake_data(faker)

        return ""  # return an empty string if we can't determine a value

    def generate_fake_data(self, faker, overrides=None, require_all=False):
        """
        Generates fake data for this field by looping through the fields in self.object_fields and generating data for
        those fields as well. Returns a dictionary formatted with [field_name]: field_data.

        :param faker: MilMoveData
        :param overrides: dict, optional
        :param require_all: bool, optional
        :return: dict
        """
        fake_data = {}
        overrides = {} if not overrides else overrides

        if self.name in overrides:
            overrides = overrides[self.name] or {}

        d_value = self.generate_discriminator_value(faker, overrides)
        if self.discriminator and d_value:
            overrides[self.discriminator] = d_value

        for field in self.object_fields:
            if self.skip_field(field, discriminator_value=d_value, overrides=overrides, require_all=require_all):
                continue

            fake_data[field.name] = field.generate_fake_data(faker, overrides=overrides, require_all=require_all)

        for field_name in overrides:
            if field_name not in fake_data and self.has_field(field_name):
                fake_data[field_name] = overrides[field_name]

        return fake_data

    @staticmethod
    def skip_field(field, **kwargs):
        """ Evaluate whether or not we should skip this field while generating fake data. """
        # Check the discriminator above all (for polymorphic API data):
        if (d_value := kwargs.get("discriminator_value")) and not field.is_valid_discriminator(d_value):
            return True

        # Check if the field is in the overrides, which indicates that the caller wants to see this field in the output
        # data:
        if field.name in kwargs.get("overrides", {}):
            return False

        # Otherwise, check if we're requiring all fields, if this field is required, and if we passed the random chance
        # to add a non-required field:
        return not (field.required or kwargs.get("require_all") or randint(0, 3))


@dataclass
class APIEndpointBody:
    path: str
    method: str
    body_field: BaseAPIField = None

    def generate_fake_data(self, faker, overrides=None, require_all=False):
        """
        Generates a dictionary (JSON-valid) representation of the endpoint body filled with fake data. Must have a Faker
        data generator passed in, and can optionally accept overrides and a switch indicating if all fields should be
        required or not (regardless of their actual required value).

        :param faker: MilMoveData
        :param overrides: dict, optional
        :param require_all: bool, optional
        :return: dict
        """
        fake_data = self.body_field.generate_fake_data(faker, overrides=overrides, require_all=require_all)

        return fake_data
