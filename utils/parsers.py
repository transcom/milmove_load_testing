# -*- coding: utf-8 -*-
"""
This file is for helpers that parse an API and populate fake data for use in requests
"""
import logging
import random
from dataclasses import dataclass, field
from enum import Enum
from functools import lru_cache
from typing import Optional

from prance import ResolvingParser

from utils.base import ImplementationError
from utils.constants import ARRAY_MAX, ARRAY_MIN, DataType
from utils.fake_data import MilMoveData
from utils.fields import APIEndpointBody, ArrayField, BaseAPIField, EnumField, ObjectField
from utils.types import JSONType

logger = logging.getLogger(__name__)


class APIKey(Enum):
    """
    Define API keys that can be used to know which parser to use.
    """

    INTERNAL = "internal"
    OFFICE = "office"
    PRIME = "prime"
    SUPPORT = "support"


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
        self.processed_bodies = []  # list of APIEndpointBody objects

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
        except (KeyError, IndexError):
            # this means we either didn't even have a "parameters" or "in" key (no input at all),
            # or we got an empty list (the endpoint has parameters but no body),
            # and both cases are valid states for some endpoints
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

        return response

    def get_definition(self, name):
        """
        Grabs a definition object from its name.
        :param name: str
        :return: dict
        """
        return self.parser.specification["definitions"].get(name)

    def generate_fake_request(self, path, method, overrides=None, require_all=False):
        """
        Generates a request body filled with fake data to use with a specific endpoint in the API. Requires the endpoint
        path and method. Optionally takes in overrides and a bool indicating if all fields should be required or not.

        :param path: str
        :param method: str
        :param overrides: dict, optional
        :param require_all: bool, optional
        :return: dict
        """
        request_body = self._process_request_body(path, method)

        fake_request = request_body.generate_fake_data(self.milmove_data, overrides, require_all)
        # Hook method for custom post-data generation validation:
        self._custom_request_validation(path, method, fake_request)

        return fake_request

    def _get_processed_body(self, path, method):
        """
        Takes in a path and a method and searches for a pre-processed APIEndpointBody class for this endpoint's request
        body.

        :param path: str
        :param method: str
        :return: APIEndpointBody or None
        """
        for body in self.processed_bodies:
            if body.path == path and body.method == method:
                return body

        return None

    def _process_request_body(self, path, method):
        """
        Grabs the endpoint definition for a given path and method and processes it into a cohesive APIEndpointBody
        object that includes class representations of all request fields. Can be used for quick fake data generation.

        :param path: str
        :param method: str
        :return: APIEndpointBody
        """
        # Check first that we haven't already processed this request:
        if request_body := self._get_processed_body(path, method):
            return request_body

        request_def = self.get_request_body(path, method)
        request_body = APIEndpointBody(path, method)

        body_field = self._parse_definition(name="body", definition=request_def)
        request_body.body_field = body_field

        self.processed_bodies.append(request_body)
        # Hook method for custom validation/manipulation of the generated request body:
        self._custom_body_validation(request_body)

        return request_body

    def _parse_definition(self, name, definition):
        """
        Given an arbitrary API definition and the name for the definition, parses it into the appropriate BaseAPIField
        object and returns it.

        :param name: str
        :param definition: dict
        :return: BaseAPIField or None
        """
        parsed_field = None

        if not definition or definition.get("readOnly"):
            pass  # skip this field, maintain parsed_field = None

        elif definition.get(DataType.ENUM.value):
            parsed_field = EnumField(name=name, options=definition[DataType.ENUM.value])

        elif definition.get("type") and definition["type"] not in [DataType.ARRAY.value, DataType.OBJECT.value]:
            parsed_field = self._parse_typed_field(name, definition["type"], definition.get("format", ""), definition)

        elif definition.get("type") and definition["type"] == DataType.ARRAY.value:
            parsed_field = self._parse_array_field(name, definition)

        else:
            parsed_field = self._parse_object_field(name, definition)

        # Hook method for custom validation on a particular field:
        self._custom_field_validation(parsed_field, definition)

        return parsed_field

    def _parse_object_field(self, name, object_def):
        """
        Given a field name and definition, creates an ObjectField instance that captures the attributes of the field.
        Sets all sub-fields for this object.

        :param name: str
        :param object_def: dict
        :return: ObjectField
        """
        object_field = ObjectField(name=name)

        if object_def.get("discriminator") and not self.discriminated:
            # This function sets self.discriminated:
            object_field = self._parse_discriminator(object_field, object_def)

        elif object_def.get("properties"):
            for field_name, properties in object_def["properties"].items():
                api_field = self._parse_definition(field_name, properties)
                if api_field:
                    # NOTE: These are are all ALWAYS distinct fields in the object, NOT combined into the same
                    # object-level like allOf and oneOf:
                    object_field.add_field(api_field)

        # Separate if/elif statement because this can also happen for an object with a discriminator and/or properties:
        if object_def.get("allOf"):
            for definition in object_def["allOf"]:
                api_field = self._parse_definition(name, definition)
                if api_field:
                    object_field.combine_fields(api_field, unique=True)

        elif object_def.get("oneOf"):
            selection = random.choice(object_def["oneOf"])  # randomly select the object to use
            api_field = self._parse_definition(name, selection)
            if api_field:
                object_field.combine_fields(api_field)

        required_fields = object_def.get("required", [])
        object_field.update_required_fields(required_fields)

        return object_field

    def _parse_discriminator(self, object_field, object_def):
        """
        Takes in a pre-initialized ObjectField instance and the dict definition of that field, then parses this def
        using our custom discriminator logic.

        NOTE: This logic does not capture all possible ways in which a discriminator may be used in an API.

        :param object_field: ObjectField
        :param object_def: dict
        :return: ObjectField
        """
        if not object_def.get("discriminator"):
            raise ImplementationError("_parse_discriminator can only be used with API fields with a discriminator.")

        # We set this self.discriminated value to avoid infinite recursion loops:
        self.discriminated = True

        # This logic grabs the field definition and properties for the field named as the discriminator, then it parses
        # that field explicitly.
        object_field.discriminator = object_def["discriminator"]
        d_properties = object_def["properties"][object_field.discriminator]
        d_field = self._parse_definition(object_field.discriminator, d_properties)

        # We assume an EnumField for processing the discriminator:
        if not hasattr(d_field, "options"):
            raise NotImplementedError("This APIParser can only handle discriminators with enum options.")

        d_options = d_field.options
        # This means we are parsing one of the discriminator definitions now, so we don't need to parse all of the other
        # options now:
        if object_field.name in d_options:
            d_options = [object_field.name]

        # For each possible discriminator value, add the fields relevant to that value to the base ObjectField:
        for value in d_options:
            value_definition = self.get_definition(value)
            api_field = self._parse_definition(object_field.name, value_definition)

            if api_field:
                api_field.add_discriminator_value(value)
                # As we combine fields, we want it to NOT unique because different discriminator definitions could have
                # the same field names. We want to preserve both so that we can pick the right one when generating fake
                # data and validating discriminator values:
                object_field.combine_fields(api_field)

        self.discriminated = False
        return object_field

    def _parse_array_field(self, name, array_def):
        """
        Given a field name and definition, creates an ArrayField instance that captures the attributes of the field.

        :param name: str
        :param array_def: dict
        :return: ArrayField
        """
        if not array_def.get("type") == DataType.ARRAY.value:
            raise ImplementationError("_parse_array_field can only be used with API fields with type equal to 'array'.")

        array_field = ArrayField(
            name=name,
            min_items=array_def.get("minItems", ARRAY_MIN),
            max_items=array_def.get("maxItems", ARRAY_MAX),
        )
        items_field = self._parse_definition(name, array_def["items"])
        array_field.items_field = items_field

        return array_field

    def _parse_typed_field(self, name, field_type, field_format, definition):
        """
        Determines the data type and creates a BaseAPIField instance for a field, given its name, swagger type, and
        swagger format. May return None if the info cannot be parsed using the default rules.

        :param name: str
        :param field_type: str
        :param field_format: str
        :return: BaseAPIField or None
        """
        data_type = None

        # Try with field type first, then try other things. The field name itself indicates one
        # of our handled data types while the format might also tell us which type to use.
        for value_to_match in (field_type, name, field_format):
            try:
                data_type = DataType(value=value_to_match)
            except ValueError:
                continue
            else:
                break

        if data_type is None and field_type == "string":
            data_type = self._approximate_str_type(name)

        if data_type:
            return BaseAPIField(data_type=data_type, name=name, definition=definition)

        return None

    @staticmethod
    def _approximate_str_type(field_name):
        """
        Approximates the data type for a field with type "string" in the YAML based off the name of the field. Defaults
        to the SENTENCE data type.

        :param field_name: str, name of the field
        :return: DataType enum
        """
        field_name = field_name.lower()

        for data_type in DataType:
            value = data_type.value.lower()
            if (field_name in value) or (value in field_name):
                return data_type

        return DataType.SENTENCE

    def _custom_field_validation(self, api_field, object_def):
        """
        Hook for adding custom validation after a BaseAPIField object has been parsed. May apply whenever the field is
        used to generate data.

        :param api_field: BaseAPIField
        :param object_def: dict, original definition that was parsed into resultant field
        :return: field
        """
        pass

    def _custom_body_validation(self, body):
        """
        Hook for adding custom validation after a full APIEndpointBody has been parsed. May apply whenever the endpoint
        body is used to generate data.

        :param body: APIEndpointBody
        :return: body
        """
        pass

    def _custom_request_validation(self, path, method, request_data):
        """
        Hook for adding custom validation after fake data has been generated for an endpoint request. Takes in the path,
        method, and the dictionary of fake data. May be used for validation that requires that data already be populated
        in the field(s).

        :param path: str
        :param method: str
        :param request_data: dict
        :return: request_data dict
        """
        pass


class PrimeAPIParser(APIParser):
    """Parser class for the Prime API."""

    api_file = "https://raw.githubusercontent.com/transcom/mymove/master/swagger/prime.yaml"

    def generate_fake_request(self, path, method, overrides=None, require_all=True):
        """
        Overrides method so that require_all defaults to True. TODO remove when API discrepancies are fixed
        """
        return super().generate_fake_request(path, method, overrides, True)

    def _custom_field_validation(self, api_field, object_def):
        """
        Custom validation for Prime API fields.
        """
        if api_field and api_field.name == "modelType" and ("MTOServiceItemBasic" in api_field.options):
            api_field.options.remove("MTOServiceItemBasic")

    def _custom_request_validation(self, path, method, request_data):
        """
        Custom post-data generation validation for the Prime API. Note that request_data is mutable and directly
        modified, and therefore doesn't need to be returned.
        """
        if path == "/mto-service-items" and method == "post":
            # Need to ensure that an 'item' is smaller than the crate it will be shipped in:
            if request_data["modelType"] == "MTOServiceItemDomesticCrating":
                item_details = request_data.get("item")
                crate_details = request_data.get("crate")
                if item_details and crate_details:
                    item_details["length"], crate_details["length"] = self.normalize_crate_dimensions(
                        item_details["length"], crate_details["length"]
                    )
                    item_details["width"], crate_details["width"] = self.normalize_crate_dimensions(
                        item_details["width"], crate_details["width"]
                    )
                    item_details["height"], crate_details["height"] = self.normalize_crate_dimensions(
                        item_details["height"], crate_details["height"]
                    )

    @staticmethod
    def normalize_crate_dimensions(item_dim: int, crate_dim: int) -> (int, int):
        """
        Check that the item dimensions are always smaller than the crate dimensions (since the item has to fit inside
        it). Additionally, ensure that both dimensions are greater than 0 so that we don't encounter any errors from
        MilMove attempting to manipulate zero or negative numbers. Returns the normalized versions of both values.

        :param item_dim: int
        :param crate_dim: int
        :return: tup(item_dim int, crate_dim int)
        """
        if item_dim <= 0:
            item_dim = 1
        if crate_dim <= item_dim:
            crate_dim = item_dim + 1
        return item_dim, crate_dim


class SupportAPIParser(PrimeAPIParser):
    """Parser class for the Support API."""

    api_file = "https://raw.githubusercontent.com/transcom/mymove/master/swagger/support.yaml"

    def _custom_request_validation(self, path, method, request_data):
        """
        Custom post-data generation validation for the Support API. Note that request_data is mutable and directly
        modified, and therefore doesn't need to be returned.
        """
        if path == "/move-task-orders" and method == "post":
            move_task_order = request_data
            move_orders = request_data["order"]
            customer = move_orders["customer"]
            entitlement = move_orders["entitlement"]

            # createMoveTaskOrders cannot create certain nested objects, none are passed in.
            move_task_order.pop("mtoShipments", None)
            move_task_order.pop("paymentRequests", None)
            move_task_order.pop("mtoServiceItems", None)

            move_task_order.pop("orderID", None)  # orderID will be returned on creation

            # Cannot create certain nested objects with this endpoint, instead the caller should pass in an ID
            # (in overrides)
            move_orders.pop("uploadedOrders", None)
            move_orders.pop("originDutyStation", None)
            move_orders.pop("destinationDutyStation", None)

            move_orders.pop("id", None)  # id will be returned on creation
            move_orders.pop("customerID", None)  # customerID will be returned on creation

            customer.pop("currentAddress", None)  # Cannot create currentAddress with this endpoint
            entitlement.pop("id", None)  # id will be returned on creation


class GHCAPIParser(APIParser):
    """Parser class for the GHC API."""

    api_file = "https://raw.githubusercontent.com/transcom/mymove/master/swagger/ghc.yaml"


class InternalAPIParser(APIParser):
    """Parser class for the Internal API."""

    api_file = "https://raw.githubusercontent.com/transcom/mymove/master/swagger/internal.yaml"


@lru_cache()
def get_api_parsers() -> dict[APIKey, APIParser]:
    """
    Initialize parsers and returnMapping with string as keys, and JSONValue as values them for easy
    use.

    :return: dict with APIKey types as keys and the corresponding initialized parser as the value.
    """
    parser_classes = {
        APIKey.INTERNAL: InternalAPIParser,
        APIKey.OFFICE: GHCAPIParser,
        APIKey.PRIME: PrimeAPIParser,
        APIKey.SUPPORT: SupportAPIParser,
    }

    initialized_parsers = {}

    for parser_key, parser_class in parser_classes.items():
        initialized_parsers[parser_key] = parser_class()

    return initialized_parsers


@dataclass
class APIFakeDataGenerator:
    """
    Helper class to generate fake data for different API endpoints.
    """

    api_parsers: dict[APIKey, APIParser] = field(default_factory=get_api_parsers)

    def generate_fake_request_data(
        self,
        api_key: APIKey,
        path: str,
        method: str,
        overrides: Optional[dict[str, JSONType]] = None,
        require_all: bool = False,
    ) -> JSONType:
        """
        Generates fake data for the given api and method. You can pass overrides for fields and
        indicate if all fields in an object should be required.

        :param api_key: APIKey to indicate which API you want to target, e.g. APIKey.PRIME
        :param path: path to use in the api, e.g. "/mto-shipments"
        :param method: method for the request, e.g. "get"
        :param overrides: Optional overrides for fields if you need specific values set.
        :param require_all: Indicates that all fields of an object should be filled in, whether they
            are required per the API spec or not.
        :return: a payload to use in a request
        """
        return self.api_parsers[api_key].generate_fake_request(
            path=path,
            method=method.lower(),  # This needs to be lowercase later so make sure it's correct
            overrides=overrides,
            require_all=require_all,
        )


@lru_cache
def get_api_fake_data_generator() -> APIFakeDataGenerator:
    """
    Initializes and returns a fake data generator. Uses cache to avoid re-parsing apis.

    :return: API fake data generator ready for use
    """
    return APIFakeDataGenerator()
