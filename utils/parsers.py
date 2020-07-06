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
    """
    Parses a YAML Swagger file to isolate endpoint definitions.
    NOTE: This is stable for the Prime API yaml file, and may not handle all cases present in other APIs.
    """

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
        self.discriminated = False  # indicates if the parser is working with the data for a discriminator

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

    def get_definition(self, name):
        """
        Grabs a definition object from its name.
        :param name: str
        :return: dict
        """
        return self.parser.specification["definitions"].get(name)

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

    def _parse_all_of_data(self, all_defs, overrides=None, nested_overrides=None, require_all=False):
        """
        Loops through all of the objects defines in an "allOf" data section and puts them together into one object.
        :param all_defs:
        :param overrides:
        :param nested_overrides:
        :param require_all:
        :return:
        """
        data_types = {}
        overrides_copy = deepcopy(overrides) if overrides else {}

        for definition in all_defs:
            if definition.get("properties"):
                new_data, new_overrides = self._parse_object_data_types(
                    definition, overrides, nested_overrides, require_all
                )

                data_types.update(new_data)
                overrides_copy.update(new_overrides)
            else:  # We don't handle non-object types without distinct fields
                raise NotImplementedError("Cannot parse allOf with non-object members.")

        return data_types, overrides_copy

    def _parse_discriminator_data(self, object_def, overrides=None, nested_overrides=None, require_all=False):
        """
        Gets the discriminator value for an object definition, then grabs the possible values for the discriminator,
        picks one, and continues processing the rest of the object based on that value.

        :param object_def:
        :param overrides:
        :param nested_overrides:
        :param require_all:
        :return:
        """
        self.discriminated = True  # needed to prevent recursion error

        d = object_def["discriminator"]
        d_properties = object_def["properties"][d]  # for MTOServiceItems, this value is a field name
        d_data = {}

        # Get the field data type, use faker to pick a value, then parse all data based on that value:
        self._parse_field_properties(d, d_properties, d_data, overrides, nested_overrides)
        selection = self.milmove_data.populate_fake_data(d_data, overrides)[d]
        selection_def = self.get_definition(selection)["allOf"]
        overrides[d] = selection

        return_data = self._parse_all_of_data(selection_def, overrides, nested_overrides, require_all)
        self.discriminated = False

        return return_data

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
        if object_def.get("discriminator") and not self.discriminated:
            return self._parse_discriminator_data(object_def, overrides, nested_overrides, require_all)

        if object_def.get("allOf"):
            return self._parse_all_of_data(object_def["allOf"], overrides, nested_overrides, require_all)

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

            # NOTE: This function modifies data_types and overrides_copy directly
            self._parse_field_properties(field, properties, data_types, overrides_copy, nested_overrides, require_all)

        return data_types, overrides_copy

    def _parse_field_properties(self, field, properties, data, overrides, nested_overrides=None, require_all=False):
        """
        Parses the properties of a field in a swagger definition to determine what type of fake data to put into it.
        !!! NOTE: Modifies the data and overrides input dictionaries directly!!!

        :param field: str
        :param properties: dict
        :param data: dict, is modified directly!
        :param overrides: dict, is modified directly!
        :param nested_overrides: dict, optional
        :param require_all: bool, optional
        :return: None
        """
        field_type = properties.get("type", "")
        field_format = properties.get("format", "")

        if field_type == "array":
            min_items = properties.get("minItems", 1)
            max_items = properties.get("maxItems", 5)
            array_data = self._generate_fake_array_data(
                properties["items"], randint(min_items, max_items), nested_overrides, require_all
            )
            overrides[field] = array_data

        elif field_type == "object":
            sub_data, sub_overrides = self._parse_object_data_types(
                properties, nested_overrides, nested_overrides, require_all
            )
            overrides[field] = self.milmove_data.populate_fake_data(sub_data, sub_overrides)

        elif properties.get("enum"):
            data[field] = properties["enum"]

        elif DataType.validate(field_type):
            data[field] = DataType.match(field_type)

        elif DataType.validate(field):  # the field name itself indicates one of our handled data types
            data[field] = DataType.match(field)

        elif DataType.validate(field_format):  # the format might also tell us which type to use
            data[field] = DataType.match(field_format)

        elif field_type == "string":
            data[field] = self._approximate_str_type(field)

        # if the field doesn't fall into any of these cases, we just skip it because we have no rules for what data to
        # pass in
        return

    @staticmethod
    def _approximate_str_type(field):
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
    """ Parser class for the Prime API. Handles the polymorphism for MTO Service Items. """

    api_file = "https://raw.githubusercontent.com/transcom/mymove/master/swagger/prime.yaml"

    def generate_fake_request(self, path, method, overrides=None, nested_overrides=None, require_all=True):
        """ Overrides method so that require_all defaults to True. TODO remove when API discrepancies are fixed """
        return super().generate_fake_request(path, method, overrides, nested_overrides, require_all)


class SupportAPIParser(PrimeAPIParser):
    """ Parser class for the Support API. """

    api_file = "https://raw.githubusercontent.com/transcom/mymove/master/swagger/support.yaml"
