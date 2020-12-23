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
from .assertions import MTO_SHIPMENT_DEFINITION, CREATE_MTO_SHIPMENT_DEFINITION, UPDATE_MTO_ENDPOINT


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
            (
                "/mto-shipments",
                "post",
                {
                    "summary": "createMTOShipment",
                    "description": "Creates a MTO shipment for the specified Move Task Order.\nRequired fields include:"
                    "\n* Shipment Type\n* Customer requested pick-up date\n* Pick-up Address\n* "
                    "Delivery Address\n* Releasing / Receiving agents\n\nOptional fields include:\n* "
                    "Customer Remarks\n* Releasing / Receiving agents\n* An array of optional "
                    "accessorial service item codes\n",
                    "consumes": ["application/json"],
                    "produces": ["application/json"],
                    "operationId": "createMTOShipment",
                    "tags": ["mtoShipment"],
                    "parameters": [{"in": "body", "name": "body", "schema": CREATE_MTO_SHIPMENT_DEFINITION}],
                    "responses": {
                        "200": {
                            "description": "Successfully created a MTO shipment.",
                            "schema": MTO_SHIPMENT_DEFINITION,
                        },
                        "400": {
                            "description": "The request payload is invalid.",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "title": {"type": "string"},
                                    "detail": {"type": "string"},
                                    "instance": {"type": "string", "format": "uuid"},
                                },
                                "required": ["title", "detail", "instance"],
                            },
                        },
                        "404": {
                            "description": "The requested resource wasn't found.",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "title": {"type": "string"},
                                    "detail": {"type": "string"},
                                    "instance": {"type": "string", "format": "uuid"},
                                },
                                "required": ["title", "detail", "instance"],
                            },
                        },
                        "422": {
                            "description": "The payload was unprocessable.",
                            "schema": {
                                "allOf": [
                                    {
                                        "type": "object",
                                        "properties": {
                                            "title": {"type": "string"},
                                            "detail": {"type": "string"},
                                            "instance": {"type": "string", "format": "uuid"},
                                        },
                                        "required": ["title", "detail", "instance"],
                                    },
                                    {"type": "object"},
                                ],
                                "properties": {
                                    "invalidFields": {
                                        "type": "object",
                                        "additionalProperties": {
                                            "description": "List of errors for the field",
                                            "type": "array",
                                            "items": {"type": "string"},
                                        },
                                    }
                                },
                                "required": ["invalidFields"],
                            },
                        },
                        "500": {
                            "description": "A server error occurred.",
                            "schema": {
                                "properties": {
                                    "title": {"type": "string"},
                                    "detail": {"type": "string"},
                                    "instance": {"type": "string", "format": "uuid"},
                                },
                                "required": ["title", "detail"],
                                "type": "object",
                            },
                        },
                    },
                },
            ),
            ("/move-task-orders/{moveTaskOrderID}/post-counseling-info", "patch", UPDATE_MTO_ENDPOINT),
        ],
    )
    def test_get_endpoint(self, path, method, endpoint):
        """
        Tests getting a parsed endpoint definition from the Prance API resolver.
        """
        assert self.parser._get_endpoint(path, method) == endpoint

    @pytest.mark.parametrize(
        "path,method,request_body",
        [("/mto-shipments", "post", CREATE_MTO_SHIPMENT_DEFINITION), ("/move-task-orders", "get", {})],
    )
    def test_get_request_body(self, path, method, request_body):
        """
        Tests getting a parsed request body for an endpoint in the Prance API resolver.
        """
        assert self.parser.get_request_body(path, method) == request_body

    @pytest.mark.parametrize(
        "path,method,status,response_body",
        [
            ("/mto-shipments", "post", "200", MTO_SHIPMENT_DEFINITION),
            (
                "/mto-shipments",
                "post",
                "422",
                {
                    "allOf": [
                        {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "detail": {"type": "string"},
                                "instance": {"type": "string", "format": "uuid"},
                            },
                            "required": ["title", "detail", "instance"],
                        },
                        {"type": "object"},
                    ],
                    "properties": {
                        "invalidFields": {
                            "type": "object",
                            "additionalProperties": {
                                "description": "List of errors for the field",
                                "type": "array",
                                "items": {"type": "string"},
                            },
                        }
                    },
                    "required": ["invalidFields"],
                },
            ),
        ],
    )
    def test_get_response_body(self, path, method, status, response_body):
        """
        Tests getting a parsed response body for an endpoint in the Prance API resolver.
        """
        assert self.parser.get_response_body(path, method, status) == response_body

    @pytest.mark.parametrize(
        "name,definition",
        [
            (
                "ClientError",
                {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "detail": {"type": "string"},
                        "instance": {"type": "string", "format": "uuid"},
                    },
                    "required": ["title", "detail", "instance"],
                },
            ),
            ("MTOShipment", MTO_SHIPMENT_DEFINITION),
        ],
    )
    def test_get_definition(self, name, definition):
        """
        Tests getting a parsed definition from the Prance API resolver.
        """
        assert self.parser.get_definition(name) == definition

    @pytest.mark.parametrize("path,method", [("/mto-shipments", "post")])
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
