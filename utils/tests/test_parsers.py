# -*- coding: utf-8 -*-
""" Tests utils/parsers.py """
import os
import pytest

from prance import ResolvingParser
from prance.util.url import ResolutionError

from utils.base import ImplementationError
from utils.constants import STATIC_FILES, DataType, ARRAY_MIN, ARRAY_MAX
from utils.fake_data import MilMoveData
from utils.fields import APIEndpointBody, ObjectField, BaseAPIField, ArrayField, EnumField
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
    def test__get_endpoint(self, path, method, endpoint):
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
    def test__process_request_body(self, path, method):
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

    @pytest.mark.parametrize("path,method", [("/orchards", "post")])
    def test__get_processed_body(self, path, method):
        """
        Tests that we can retrieve an already processed request body from the processed_bodies attribute of APIParser.

        :param path: str, endpoint path in the yaml file
        :param method: str, endpoint HTTP method
        """
        body = self.parser._process_request_body(path, method)
        stored_body = self.parser._get_processed_body(path, method)

        assert stored_body is not None
        assert stored_body == body

    @pytest.mark.parametrize(
        "name,definition,expected_type",
        [
            ("AppleTrees", APPLE_TREES_DEF, ArrayField),
            ("Farmer", FARMER_DEF, ObjectField),
            ("Apple", APPLE_DEF, EnumField),
            ("size", {"type": "integer"}, BaseAPIField),
        ],
    )
    def test__parse_definition(self, name, definition, expected_type):
        """ Tests that _parse_definition returns the correct field type. """
        field = self.parser._parse_definition(name, definition)

        assert field is not None
        assert type(field) is expected_type
        assert field.name == name

    @pytest.mark.parametrize(
        "object_name,object_def,num_fields_expected",
        [
            ("AppleTree", APPLE_TREE_DEF, 4),  # num_fields_expected = Tree properties + AppleTree properties - readOnly
            ("Farmer", FARMER_DEF, 6),  # num_fields_expected = Farmer properties - readOnly
            ("Orchard", ORCHARD_DEF, 3),  # num_fields_expected = Orchard properties - readOnly
        ],
    )
    def test__parse_object_field(self, object_name, object_def, num_fields_expected):
        """ Tests that an ObjectField with the correct properties is returned. """
        field = self.parser._parse_object_field(object_name, object_def)

        assert field.name == object_name
        assert field.discriminator == object_def.get("discriminator", "")
        assert len(field.object_fields) == num_fields_expected

    def test__parse_discriminator(self):
        """ Tests that a polymorphic API definition is parsed correctly. """
        object_field = ObjectField(name="trees")
        object_field = self.parser._parse_discriminator(object_field, TREE_DEF)

        assert object_field.discriminator == TREE_DEF["discriminator"]
        assert object_field.object_fields is not None

        field_names = [field.name for field in object_field.object_fields]
        assert "treeType" in field_names  # from base Tree
        assert "datePlanted" in field_names  # from base Tree
        assert "apples" in field_names  # from AppleTree
        assert "cherryBunchSize" in field_names  # from CherryTree
        assert "goodForLemonade" in field_names  # from LemonTree
        assert "peaches" in field_names  # from PeachTree

        apples = object_field.get_field("apples")
        assert apples.discriminator_values is not None
        assert "AppleTree" in apples.discriminator_values
        assert "CherryTree" not in apples.discriminator_values
        assert "LemonTree" not in apples.discriminator_values
        assert "PeachTree" not in apples.discriminator_values

    @pytest.mark.parametrize(
        "array_name,array_def", [("AppleTrees", APPLE_TREES_DEF), ("trees", ORCHARD_DEF["properties"]["trees"])]
    )
    def test__parse_array_field(self, array_name, array_def):
        """ Tests that the correct ArrayField object is returned from _parse_array_field. """
        array_field = self.parser._parse_array_field(array_name, array_def)

        assert array_field is not None
        assert type(array_field) is ArrayField
        assert array_field.name == array_name
        assert array_field.items_field is not None
        assert array_field.min_items == array_def.get("minItems", ARRAY_MIN)
        assert array_field.max_items == array_def.get("maxItems", ARRAY_MAX)

    @pytest.mark.parametrize(
        "typed_field_args,expected_type",
        [
            (("firstName", "string", ""), DataType.FIRST_NAME),
            (("postalCode", "string", "zip"), DataType.POSTAL_CODE),
            (("contact", "string", "email"), DataType.EMAIL),
            (("bestDateForDancing", "string", "date-time"), DataType.DATE_TIME),
            (("randomThought", "string", ""), DataType.SENTENCE),
            (("numRandomThoughts", "integer", ""), DataType.INTEGER),
            (("numRandomThoughts", "integer", ""), DataType.INTEGER),
            (("randomThing", "badType", "badFormat"), None),
            (("", "", ""), None),
        ],
    )
    def test__parse_typed_field(self, typed_field_args, expected_type):
        """ Tests that the correct BaseAPIField is generated for a given field name, type, and format. """
        if not expected_type:
            assert self.parser._parse_typed_field(*typed_field_args) is None
            return  # done with this test

        api_field = self.parser._parse_typed_field(*typed_field_args)
        field_name, *_ = typed_field_args

        assert api_field is not None
        assert type(api_field) is BaseAPIField
        assert api_field.data_type == expected_type
        assert api_field.name == field_name

    @pytest.mark.parametrize(
        "field_name,expected_type",
        [
            ("firstName", DataType.FIRST_NAME),
            ("streetAddress2", DataType.STREET_ADDRESS),
            ("favoriteCity", DataType.CITY),
            ("bestDateForDancing", DataType.DATE),
            ("randomThought", DataType.SENTENCE),
        ],
    )
    def test__approximate_str_type(self, field_name, expected_type):
        """ Test that field names are being used to approximate the closest data type. """
        assert self.parser._approximate_str_type(field_name) == expected_type
