# -*- coding: utf-8 -*-
""" Tests utils/parsers.py """
import os
import pytest

from prance import ResolvingParser
from prance.util.url import ResolutionError

from utils.base import ImplementationError
from utils.constants import STATIC_FILES
from utils.fake_data import MilMoveData
from utils.fields import APIEndpointBody, ObjectField
from utils.parsers import APIParser
from .test_parsers_params import *


class TestAPIParser:
    """ Tests the APIParser class and its methods. """

    TEST_API = os.path.join(STATIC_FILES, "test_api.yaml")

    @classmethod
    def setup_class(cls):
        """ Initialize the APIParser that will be tested. """
        cls.parser = APIParser(api_file=cls.TEST_API)

    def test_init(self):
        """
        Tests that the __init__ from the setup_class method worked correctly.
        """
        assert self.parser.api_file == self.TEST_API
        assert type(self.parser.parser) is ResolvingParser
        assert type(self.parser.milmove_data) is MilMoveData
        assert self.parser.processed_bodies == []
        assert not self.parser.discriminated

    def test_empty_init(self):
        """
        Tests an __init__ of APIParser with no API file indicated.
        """
        with pytest.raises(ImplementationError):
            APIParser()

    def test_file_not_found_init(self):
        """
        Tests an __init__ of APIParser with a bad path for the API file.
        """
        with pytest.raises(ResolutionError):
            APIParser(api_file="non_existent.yaml")

    @pytest.mark.parametrize(
        "path,method,endpoint",
        [
            ("/apple-trees/{appleTreeID}", "get", APPLE_TREE_GET),
            ("/apple-trees/{appleTreeID}", "delete", APPLE_TREE_DELETE),
            ("/orchards", "post", ORCHARDS_POST),
        ],
    )
    def test_get_endpoint(self, path, method, endpoint):
        """
        Tests getting a parsed endpoint definition from the Prance API resolver.
        """
        assert self.parser._get_endpoint(path, method) == endpoint

    @pytest.mark.parametrize(
        "path,method,request_body",
        [
            ("/apples", "get", {}),  # this endpoint has no input
            ("/farmers/{farmerID}", "put", FARMER_DEF),
            ("/orchards/{orchardID}", "patch", TREE_DEF),
        ],
    )
    def test_get_request_body(self, path, method, request_body):
        """
        Tests getting a parsed request body for an endpoint in the Prance API resolver.
        """
        assert self.parser.get_request_body(path, method) == request_body

    @pytest.mark.parametrize(
        "path,method,status,response_body",
        [
            ("/apple-trees/{appleTreeID}", "get", None, APPLE_TREE_GET_200),  # should be the 200 response
            ("/apple-trees/{appleTreeID}", "get", "404", APPLE_TREE_GET_404),
            ("/apple-trees/{appleTreeID}", "delete", "200", APPLE_TREE_DELETE_200),
            ("/farmers", "post", "201", FARMERS_POST_201),
            ("/farmers/{farmerID}", "put", "422", FARMER_PUT_422),
        ],
    )
    def test_get_response_body(self, path, method, status, response_body):
        """
        Tests getting a parsed response body for an endpoint in the Prance API resolver.
        """
        if status:
            assert self.parser.get_response_body(path, method, status) == response_body
        else:
            assert self.parser.get_response_body(path, method) == response_body

    @pytest.mark.parametrize(
        "name,definition",
        [("Apple", APPLE_DEF), ("Tree", TREE_DEF), ("CherryTree", CHERRY_TREE_DEF), ("Orchard", ORCHARD_DEF)],
    )
    def test_get_definition(self, name, definition):
        """
        Tests getting a parsed definition from the Prance API resolver.
        """
        assert self.parser.get_definition(name) == definition

    @pytest.mark.parametrize("path,method", [("/orchards", "post")])
    def test_process_request_body(self, path, method):
        """
        Tests the function that processes an endpoint request body from the Prance API resolver and turns it into an
        APIEndpointBody class, which will be used for populating fake data later on.

        :param path: str, endpoint path in the yaml file
        :param method: str, endpoint HTTP method
        """
        body = self.parser._process_request_body(path, method)

        assert type(body) is APIEndpointBody
        assert body.path == path
        assert body.method == method
        assert type(body.body_field) is ObjectField
