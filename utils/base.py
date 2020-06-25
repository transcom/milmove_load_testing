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
    """
    """

    api_file = ""  # can be a relative path or a url

    def __init__(self, api_file=""):
        """
        :param api_file:
        """
        if self.api_file and api_file:
            pass  # todo raise exception can only use one

        if not self.api_file:
            self.api_file = api_file

        self.parser = ResolvingParser(api_file)

    def _get_endpoint(self, path, method):
        """
        :param path:
        :param method:
        :return:
        """
        try:
            return self.parser.specification["paths"][path][method]
        except KeyError:
            return  # todo raise exception and log for bad path, method
        except TypeError:
            return  # todo raise exception and log for bad parsing structure

    def get_request_body(self, path, method):
        """
        :param path:
        :param method:
        :return:
        """
        endpoint = self._get_endpoint(path, method)
        try:
            # grabbing the first body parameter in the endpoint to work with:
            body = [param for param in endpoint["parameters"] if param["in"] == "body"][0]
        except IndexError:  # this means we got an empty list - no body! Could be intended though
            return {}

        return body["schema"]

    def get_response_body(self, path, method, status="200"):
        """
        :param path:
        :param method:
        :param status:
        :return:
        """
        endpoint = self._get_endpoint(path, method)
        try:
            response = endpoint["responses"][status]
        except KeyError:  # no response body found for the given status code - could be intended
            return {}

        return response["schema"]
