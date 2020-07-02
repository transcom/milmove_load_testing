# -*- coding: utf-8 -*-
""" utils/fake_data.py is for Faker classes and functions to set up test data """
from typing import Optional
from copy import deepcopy

from faker import Faker
from faker.providers import BaseProvider
from prance import ResolvingParser

from .constants import DataType
from .base import ImplementationError


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
            DataType.FIRST_NAME: self.fake.first_name,  # TODO: replace with data from milmove fake address spreadsheet
            DataType.LAST_NAME: self.fake.last_name,  # TODO: same ^
            DataType.PHONE: self.fake.safe_phone_number,
            DataType.EMAIL: self.fake.safe_email,
            DataType.STREET_ADDRESS: self.fake.street_address,  # TODO: same ^^
            DataType.CITY: self.fake.city,
            DataType.STATE: self.fake.state_abbr,
            DataType.POSTAL_CODE: self.fake.postalcode,
            DataType.COUNTRY: self.fake.country,
            DataType.DATE: self.fake.date,
            DataType.SENTENCE: self.fake.sentence,
            DataType.BOOLEAN: self.fake.boolean,
            DataType.INTEGER: self.fake.random_number,
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
            # todo log
            raise ImplementationError("Endpoint path or method not found in API.")
        except TypeError as e:
            # todo log exception "Bad API structure, unable to get endpoint."
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

    #
    # def generate_fake_request(self, request_def):
    #     """
    #
    #     """
    #     fake_data = {}
    #
    #     if request_def.get("type") == "object":
    #         required_fields = request_def.get("required", [])
    #         try:
    #             request_properties = request_def["properties"]
    #         except KeyError:
    #             raise TypeError("Bad API structure, unable to get properties for request body.")
    #
    #         for field, properties in request_properties.items():
    #             field_type = properties["type"]
    #
    #             if field_type == "array":
    #                 pass  # todo handle
    #             elif DataType.validate(field_type):
    #                 fake_data[field] = DataType.match(field_type)
    #
    #             print(field)
    #             print(properties)
    #     else:
    #         raise NotImplementedError("This parser only handles request bodies with type 'object'.")
    #
    #     return fake_data
