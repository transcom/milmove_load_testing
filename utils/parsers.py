# -*- coding: utf-8 -*-
""" utils/parsers.py is for classes that parse an API and populate fake data for use in requests """
import logging
from copy import deepcopy
from random import randint

from prance import ResolvingParser

from .base import ImplementationError
from .constants import DataType
from .fake_data import MilMoveData

logger = logging.getLogger(__name__)


class APIParser:
    """ Parses a YAML Swagger file to isolate endpoint definitions. """

    api_file = ""  # can be a relative path or a url

    def __init__(self, api_file=""):
        """
        Sets the api_file and the parser attributes up for the class.
        :param api_file: str url, optional
        """
        if api_file:
            self.api_file = api_file

        if not self.api_file:
            raise ImplementationError("There must be an API file set to use the APIParser class.")

        self.parser = ResolvingParser(self.api_file)
        self.milmove_data = MilMoveData()  # for generating fake requests

    def _get_endpoint(self, path, method):
        """
        Given a relative endpoint path and method, returns the dictionary representation of the full swagger definition
        of the endpoint.

        :param path: str
        :param method: str
        :return: dict
        """
        try:
            return self.parser.specification["paths"][path][method]
        except KeyError:
            logger.debug(f"Bad path and/or method: {path} - {method}.")
            raise ImplementationError("Endpoint path or method not found in API.")
        except TypeError as e:
            logger.exception("Bad API structure, unable to get endpoint.")
            raise e

    def get_request_body(self, path, method):
        """
        Given a relative endpoint path and the HTTP/REST method for the endpoint, returns the dictionary representation
        of the request body.

        :param path: str
        :param method: str
        :return: dict
        """
        endpoint = self._get_endpoint(path, method)
        try:
            # grabbing the first body parameter in the endpoint to work with:
            body = [param for param in endpoint["parameters"] if param["in"] == "body"][0]
        except IndexError:  # this means we got an empty list - no body! Could be intended for this endpoint though
            return {}

        return body["schema"]

    def get_response_body(self, path, method, status="200"):
        """
        Given a relative endpoint path, the HTTP/REST method for the endpoint, and an optional status code, returns the
        dictionary representation of the response body.

        :param path: str
        :param method: str
        :param status: str, optional
        :return: dict
        """
        endpoint = self._get_endpoint(path, method)
        try:
            response = endpoint["responses"][status]
        except KeyError:  # no response body found for the given status code - could be intended
            return {}

        return response["schema"]

    def generate_fake_request(self, path, method, overrides=None, nested_overrides=None, require_all=False):
        """
        Generates a request body filled with fake data to use with a specific endpoint in the API. Requires the endpoint
        path and method. Optional takes top level overrides and nested overrides.

        :param path: str
        :param method: str
        :param overrides: dict, optional
        :param nested_overrides: dict, optional
        :param require_all: bool, optional
        :return: dict
        """
        request_def = self.get_request_body(path, method)
        if request_def.get("type") == "object":
            data, overrides = self._parse_object_data_types(request_def, overrides, nested_overrides, require_all)
            return self.milmove_data.populate_fake_data(data, overrides)
        else:
            raise NotImplementedError("This parser only handles request bodies with type 'object'.")

    def _generate_fake_array_data(self, items_def, num_items, nested_overrides=None, require_all=False):
        """
        Takes in a definition for the items in an array, the number of items to generate, and an optional dictionary of
        nested overrides to use with the data.

        :param items_def:
        :param num_items:
        :param nested_overrides:
        :param require_all:
        :return: list of items with fake data
        """
        items = []
        try:
            items_type = items_def["type"]
        except KeyError:
            raise NotImplementedError("This parser cannot handle arrays of arbitrary types.")

        if items_type == "object":
            data_types, overrides = self._parse_object_data_types(
                items_def, nested_overrides, nested_overrides, require_all
            )
            for _ in range(num_items):
                items.append(self.milmove_data.populate_fake_data(data_types, overrides))
        else:
            data_type = None

            if DataType.validate(items_type):
                data_type = DataType.match(items_type)
            elif data_type == "string":
                data_type = DataType.SENTENCE

            # If we were able to determine the data type above, populate some data. Otherwise we return the empty list
            if data_type:
                for _ in range(num_items):
                    items.append(self.milmove_data.data_types[data_type]())

        return items

    def _parse_object_data_types(self, object_def, overrides=None, nested_overrides=None, require_all=False):
        """
        Takes an object definition dictionary and figures out the data types for each of the fields. Takes in two
        optional override dictionaries:
            - overrides = general overrides for the base level of the object, not including fields in nested objects
            - nested_overrides = applies to ALL nested objects. e.g. if 'moveTaskOrderID' is in this override and this
              field appears in any of the sub-objects for this definition, ALL values will be overridden to the one
              passed in

        Can also vary which non-required fields get sent back, or the require_all field can be set to True and force all
        fields back. Returns the data type dictionary and the overrides (may be updated) to be passed into the fake data
        generator at will.

        :param object_def: dict, repr of yaml def
        :param overrides: dict, opt
        :param nested_overrides: dict, opt
        :param require_all: bool, opt
        :return: tuple(dict of data types, dict of overrides)
        """
        data_types = {}
        overrides_copy = deepcopy(overrides) if overrides else {}

        try:
            object_properties = object_def["properties"]
        except KeyError:
            raise TypeError("Cannot parse a free-form object to generate fake data.")
        required_fields = object_properties.keys() if require_all else object_def.get("required", [])

        for field, properties in object_properties.items():
            # Check if the field is going to be overridden or if it's readOnly; in both cases we don't need any data.
            # Also check if not required, and then we have a 1/4 chance to skip adding it entirely:
            if (
                field in overrides_copy.keys()
                or properties.get("readOnly")
                or (field not in required_fields and not randint(0, 3))
            ):
                continue

            field_type = properties.get("type", "")
            field_format = properties.get("format", "")

            if field_type == "array":
                min_items = properties.get("minItems", 1)
                max_items = properties.get("maxItems", 5)
                array_data = self._generate_fake_array_data(
                    properties["items"], randint(min_items, max_items), nested_overrides
                )
                overrides_copy[field] = array_data

            elif field_type == "object":
                sub_data, sub_overrides = self._parse_object_data_types(
                    properties, nested_overrides, nested_overrides, require_all
                )
                overrides_copy[field] = self.milmove_data.populate_fake_data(sub_data, sub_overrides)

            elif properties.get("enum"):
                data_types[field] = properties["enum"]

            elif DataType.validate(field_type):
                data_types[field] = DataType.match(field_type)

            elif DataType.validate(field):  # the field name itself indicates one of our handled data types
                data_types[field] = DataType.match(field)

            elif DataType.validate(field_format):  # the format might also tell us which type to use
                data_types[field] = DataType.match(field_format)

            elif field_type == "string":
                data_types[field] = self.approximate_str_type(field)

            # if the field doesn't fall into any of these cases, we just skip it because we have no rules for what data
            # to pass in

        return data_types, overrides_copy

    @staticmethod
    def approximate_str_type(field):
        """
        Approximates the data type for a field with type "string" in the YAML based off the name of the field. Defaults
        to the SENTENCE data type.

        :param field: str, name of the field
        :return: DataType enum
        """
        field = field.lower()

        for data_type in DataType:
            value = data_type.value.lower()
            if (field in value) or (value in field):
                return data_type

        return DataType.SENTENCE


class PrimeAPIParser(APIParser):
    """ Parser class for the Prime API. """

    api_file = "https://raw.githubusercontent.com/transcom/mymove/master/swagger/prime.yaml"


class SupportAPIParser(APIParser):
    """ Parser class for the Support API. """

    api_file = "https://raw.githubusercontent.com/transcom/mymove/master/swagger/support.yaml"
