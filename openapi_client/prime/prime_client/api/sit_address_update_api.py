"""
    MilMove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from prime_client.api_client import ApiClient, Endpoint as _Endpoint
from prime_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from prime_client.model.client_error import ClientError
from prime_client.model.create_sit_address_update_request import CreateSITAddressUpdateRequest
from prime_client.model.error import Error
from prime_client.model.sit_address_update import SitAddressUpdate
from prime_client.model.validation_error import ValidationError


class SitAddressUpdateApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_sit_address_update_request_endpoint = _Endpoint(
            settings={
                'response_type': (SitAddressUpdate,),
                'auth': [],
                'endpoint_path': '/sit-address-updates',
                'operation_id': 'create_sit_address_update_request',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body':
                        (CreateSITAddressUpdateRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create_sit_address_update_request(
        self,
        **kwargs
    ):
        """createSITAddressUpdateRequest  # noqa: E501

        **Functionality:** Creates an update request for a SIT service item's final delivery address. A newly created update request is assigned the status 'REQUESTED'  if the change in address is > 50 miles and automatically approved otherwise.  **Limitations:** The update can be requested for APPROVED SIT service items only. Only ONE request is allowed per approved SIT service item.  **DEPRECATION ON AUGUST 5TH, 2024** Following deprecation, when updating a service item's final delivery address, you will need to update the shipment's destination address. This will update the destination SIT service items' final delivery address upon approval. For `APPROVED` shipments, you can use [updateShipmentDestinationAddress](#mtoShipment/updateShipmentDestinationAddress) For shipments in any other status, you can use [updateMTOShipmentAddress](#mtoShipment/updateMTOShipmentAddress)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_sit_address_update_request(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            body (CreateSITAddressUpdateRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            SitAddressUpdate
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.create_sit_address_update_request_endpoint.call_with_http_info(**kwargs)

