# -*- coding: utf-8 -*-
from prance import ResolvingParser

parser = ResolvingParser("https://github.com/transcom/mymove/blob/master/swagger/prime.yaml")


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
