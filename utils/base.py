# -*- coding: utf-8 -*-
""" utils/base.py is for generic utilities that don't deserve their own file and may only be used in utils. """
from enum import Enum

from prance import ResolvingParser


class ImplementationError(Exception):
    """ Base exception when a util hasn't been implemented correctly. """


class ListEnum(Enum):
    @classmethod
    def values(cls):
        return [c.value for c in cls]

    @classmethod
    def names(cls):
        return [c.name for c in cls]

    @classmethod
    def validate(cls, value):
        return isinstance(value, cls) or value in cls.values()

    @classmethod
    def match(cls, value):
        """ Returns the first literal that matches the value - throws an IndexError if not found. """
        return [c for c in cls if c == value or c.value == value][0]


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
        except TypeError:
            # todo log
            raise ImplementationError("Bad API structure, unable to get endpoint.")

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
