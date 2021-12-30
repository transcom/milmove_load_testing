# -*- coding: utf-8 -*-
"""
Tests utils/parsers.py
"""
from unittest.mock import MagicMock

import pytest
from prance import ResolvingParser
from prance.util.url import ResolutionError

from utils.base import ImplementationError
from utils.constants import ARRAY_MAX, ARRAY_MIN, DataType, STATIC_FILES
from utils.fake_data import MilMoveData
from utils.fields import APIEndpointBody, ArrayField, BaseAPIField, EnumField, ObjectField
from utils.parsers import (
    APIFakeDataGenerator,
    APIKey,
    APIParser,
    GHCAPIParser,
    InternalAPIParser,
    PrimeAPIParser,
    SupportAPIParser,
    get_api_fake_data_generator,
    get_api_parsers,
)
from utils.tests.params_parsers import *


class TestAPIParser:
    """Tests the APIParser class and its methods."""

    TEST_API = str(STATIC_FILES / "test_api.yaml")

    @classmethod
    def setup_class(cls):
        """Initialize the APIParser that will be tested."""
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
        """Tests that _parse_definition returns the correct field type."""
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
        """Tests that an ObjectField with the correct properties is returned."""
        field = self.parser._parse_object_field(object_name, object_def)

        assert field.name == object_name
        assert field.discriminator == object_def.get("discriminator", "")
        assert len(field.object_fields) == num_fields_expected

    def test__parse_discriminator(self):
        """Tests that a polymorphic API definition is parsed correctly."""
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
        """Tests that the correct ArrayField object is returned from _parse_array_field."""
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
            (("firstName", "string", "", None), DataType.FIRST_NAME),
            (("postalCode", "string", "zip", None), DataType.POSTAL_CODE),
            (("contact", "string", "email", None), DataType.EMAIL),
            (("bestDateForDancing", "string", "date-time", None), DataType.DATE_TIME),
            (("randomThought", "string", "", None), DataType.SENTENCE),
            (("numRandomThoughts", "integer", "", None), DataType.INTEGER),
            (("numRandomThoughts", "integer", "", None), DataType.INTEGER),
            (("randomThing", "badType", "badFormat", None), None),
            (("", "", "", None), None),
        ],
    )
    def test__parse_typed_field(self, typed_field_args, expected_type):
        """Tests that the correct BaseAPIField is generated for a given field name, type, and format."""
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
        """Test that field names are being used to approximate the closest data type."""
        assert self.parser._approximate_str_type(field_name) == expected_type


class TestPrimeAPIParser:
    """Tests some of the custom methods on the PrimeAPIParser class"""

    @classmethod
    def setup_class(cls):
        """Initialize the APIParser that will be tested."""
        cls.parser = PrimeAPIParser()

    @pytest.mark.parametrize(
        "input_dimensions,expected_dimensions",
        [
            # (input=(item_dim, crate_dim), expected=(item_dim, crate_dim))
            ((0, 0), (1, 2)),
            ((-40, 5), (1, 5)),
            ((20, -15), (20, 21)),
            ((3, 3), (3, 4)),
            ((8, 16), (8, 16)),
        ],
    )
    def test_normalize_crate_dimensions(self, input_dimensions, expected_dimensions):
        """
        Tests that normalize_crate_dimensions always returns values that are greater than 0, and that the item is
        smaller than the crate.
        """
        output_dimensions = self.parser.normalize_crate_dimensions(*input_dimensions)
        assert output_dimensions == expected_dimensions


class TestGetAPIParsers:
    """
    Tests for get_api_parsers
    """

    def test_returns_expected_parsers_already_initialized(self) -> None:
        api_parsers = get_api_parsers()

        assert list(api_parsers.keys()) == [
            APIKey.INTERNAL,
            APIKey.OFFICE,
            APIKey.PRIME,
            APIKey.SUPPORT,
        ]

        assert isinstance(api_parsers[APIKey.INTERNAL], InternalAPIParser)
        assert isinstance(api_parsers[APIKey.OFFICE], GHCAPIParser)
        assert isinstance(api_parsers[APIKey.PRIME], PrimeAPIParser)
        assert isinstance(api_parsers[APIKey.SUPPORT], SupportAPIParser)

    def test_returns_cached_parsers(self) -> None:
        # Cache is shared across tests so to be sure this is correct, we'll calculate the values
        # we expect. We could clear the cache instead, but that would make the tests slower
        # because the api parsing is slow.
        previous_cache_misses = get_api_parsers.cache_info().misses

        if previous_cache_misses == 0:
            expected_misses = 1
            expected_hits = 1
        else:
            expected_misses = 1
            expected_hits = get_api_parsers.cache_info().hits + 2

        get_api_parsers()
        get_api_parsers()

        # Misses the first time since it's the first time it's called, but should get it the second
        # time
        assert get_api_parsers.cache_info().misses == expected_misses
        assert get_api_parsers.cache_info().hits == expected_hits


class TestAPIFakeDataGenerator:
    """
    Tests for APIFakeDataGenerator
    """

    def test_api_parsers_defaults_to_all_parsers(self) -> None:
        fake_data_generator = APIFakeDataGenerator()

        assert list(fake_data_generator.api_parsers.keys()) == [
            APIKey.INTERNAL,
            APIKey.OFFICE,
            APIKey.PRIME,
            APIKey.SUPPORT,
        ]

        assert isinstance(fake_data_generator.api_parsers[APIKey.INTERNAL], InternalAPIParser)
        assert isinstance(fake_data_generator.api_parsers[APIKey.OFFICE], GHCAPIParser)
        assert isinstance(fake_data_generator.api_parsers[APIKey.PRIME], PrimeAPIParser)
        assert isinstance(fake_data_generator.api_parsers[APIKey.SUPPORT], SupportAPIParser)

    def test_generate_fake_request_data_gives_back_expected_payload(self) -> None:
        mock_internal_api_parser = MagicMock()

        fake_data_generator = APIFakeDataGenerator(
            api_parsers={
                APIKey.INTERNAL: mock_internal_api_parser.return_value,
            }
        )

        payload = fake_data_generator.generate_fake_request_data(
            api_key=APIKey.INTERNAL,
            path="/moves",
            method="POST",
            overrides={"thing": None},
            require_all=True,
        )

        assert payload == mock_internal_api_parser.return_value.generate_fake_request.return_value

    def test_generate_fake_request_data_calls_fake_request_with_expected_values(self) -> None:
        mock_internal_api_parser = MagicMock()

        fake_data_generator = APIFakeDataGenerator(
            api_parsers={
                APIKey.INTERNAL: mock_internal_api_parser.return_value,
            }
        )

        fake_path = "/moves"
        method = "POST"
        overrides = {"thing": None}
        require_all = True

        fake_data_generator.generate_fake_request_data(
            api_key=APIKey.INTERNAL,
            path=fake_path,
            method=method,
            overrides=overrides,
            require_all=require_all,
        )

        mock_internal_api_parser.return_value.generate_fake_request.assert_called_once_with(
            path=fake_path,
            method=method.lower(),
            overrides=overrides,
            require_all=require_all,
        )


class TestGetAPIFakeDataGenerator:
    """
    Tests for get_api_fake_data_generator
    """

    def test_returns_initialized_api_fake_data_generator(self) -> None:
        fake_data_generator = get_api_fake_data_generator()

        assert isinstance(fake_data_generator, APIFakeDataGenerator)

    def test_returns_cached_parsers(self) -> None:
        # Cache is shared across tests so to be sure this is correct, we'll calculate the values
        # we expect. We could clear the cache instead, but that would make the tests slower
        # because the api parsing is slow.
        previous_cache_misses = get_api_fake_data_generator.cache_info().misses

        if previous_cache_misses == 0:
            expected_misses = 1
            expected_hits = 1
        else:
            expected_misses = 1
            expected_hits = get_api_fake_data_generator.cache_info().hits + 2

        get_api_fake_data_generator()
        get_api_fake_data_generator()

        # Misses the first time since it's the first time it's called, but should get it the second
        # time
        assert get_api_fake_data_generator.cache_info().misses == expected_misses
        assert get_api_fake_data_generator.cache_info().hits == expected_hits
