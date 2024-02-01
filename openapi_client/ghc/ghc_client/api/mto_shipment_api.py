"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ghc_client.api_client import ApiClient, Endpoint as _Endpoint
from ghc_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ghc_client.model.create_mto_shipment import CreateMTOShipment
from ghc_client.model.error import Error
from ghc_client.model.mto_shipment import MTOShipment
from ghc_client.model.mto_shipments import MTOShipments
from ghc_client.model.update_shipment import UpdateShipment
from ghc_client.model.validation_error import ValidationError


class MtoShipmentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_mto_shipment_endpoint = _Endpoint(
            settings={
                'response_type': (MTOShipment,),
                'auth': [],
                'endpoint_path': '/mto-shipments',
                'operation_id': 'create_mto_shipment',
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
                        (CreateMTOShipment,),
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
        self.get_shipment_endpoint = _Endpoint(
            settings={
                'response_type': (MTOShipment,),
                'auth': [],
                'endpoint_path': '/shipments/{shipmentID}',
                'operation_id': 'get_shipment',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'shipment_id',
                ],
                'required': [
                    'shipment_id',
                ],
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
                    'shipment_id':
                        (str,),
                },
                'attribute_map': {
                    'shipment_id': 'shipmentID',
                },
                'location_map': {
                    'shipment_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_mto_shipments_endpoint = _Endpoint(
            settings={
                'response_type': (MTOShipments,),
                'auth': [],
                'endpoint_path': '/move_task_orders/{moveTaskOrderID}/mto_shipments',
                'operation_id': 'list_mto_shipments',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'move_task_order_id',
                ],
                'required': [
                    'move_task_order_id',
                ],
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
                    'move_task_order_id':
                        (str,),
                },
                'attribute_map': {
                    'move_task_order_id': 'moveTaskOrderID',
                },
                'location_map': {
                    'move_task_order_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_mto_shipment_endpoint = _Endpoint(
            settings={
                'response_type': (MTOShipment,),
                'auth': [],
                'endpoint_path': '/move_task_orders/{moveTaskOrderID}/mto_shipments/{shipmentID}',
                'operation_id': 'update_mto_shipment',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'move_task_order_id',
                    'shipment_id',
                    'if_match',
                    'body',
                ],
                'required': [
                    'move_task_order_id',
                    'shipment_id',
                    'if_match',
                ],
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
                    'move_task_order_id':
                        (str,),
                    'shipment_id':
                        (str,),
                    'if_match':
                        (str,),
                    'body':
                        (UpdateShipment,),
                },
                'attribute_map': {
                    'move_task_order_id': 'moveTaskOrderID',
                    'shipment_id': 'shipmentID',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'move_task_order_id': 'path',
                    'shipment_id': 'path',
                    'if_match': 'header',
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

    def create_mto_shipment(
        self,
        **kwargs
    ):
        """createMTOShipment  # noqa: E501

        Creates a MTO shipment for the specified Move Task Order. Required fields include: * Shipment Type * Customer requested pick-up date * Pick-up Address * Delivery Address * Releasing / Receiving agents Optional fields include: * Delivery Address Type * Customer Remarks * Releasing / Receiving agents * An array of optional accessorial service item codes   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_mto_shipment(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            body (CreateMTOShipment): [optional]
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
            MTOShipment
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
        return self.create_mto_shipment_endpoint.call_with_http_info(**kwargs)

    def get_shipment(
        self,
        shipment_id,
        **kwargs
    ):
        """fetches a shipment by ID  # noqa: E501

        fetches a shipment by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_shipment(shipment_id, async_req=True)
        >>> result = thread.get()

        Args:
            shipment_id (str): ID of the shipment to be fetched

        Keyword Args:
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
            MTOShipment
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
        kwargs['shipment_id'] = \
            shipment_id
        return self.get_shipment_endpoint.call_with_http_info(**kwargs)

    def list_mto_shipments(
        self,
        move_task_order_id,
        **kwargs
    ):
        """Gets all shipments for a move task order  # noqa: E501

        Gets all shipments for a move task order  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_mto_shipments(move_task_order_id, async_req=True)
        >>> result = thread.get()

        Args:
            move_task_order_id (str): ID of move task order for mto shipment to use

        Keyword Args:
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
            MTOShipments
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
        kwargs['move_task_order_id'] = \
            move_task_order_id
        return self.list_mto_shipments_endpoint.call_with_http_info(**kwargs)

    def update_mto_shipment(
        self,
        move_task_order_id,
        shipment_id,
        if_match,
        **kwargs
    ):
        """updateMTOShipment  # noqa: E501

        _[Deprecated: sunset on 2024-05-06]_ This endpoint is deprecated and will be removed in a future version. Please use the new endpoint at `/ghc/v2/updateMTOShipment` instead.  Updates a specified MTO shipment. Required fields include: * MTO Shipment ID required in path * If-Match required in headers * No fields required in body Optional fields include: * New shipment status type * Shipment Type * Customer requested pick-up date * Pick-up Address * Delivery Address * Secondary Pick-up Address * SecondaryDelivery Address * Delivery Address Type * Customer Remarks * Counselor Remarks * Releasing / Receiving agents   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_mto_shipment(move_task_order_id, shipment_id, if_match, async_req=True)
        >>> result = thread.get()

        Args:
            move_task_order_id (str): ID of move task order for mto shipment to use
            shipment_id (str): UUID of the MTO Shipment to update
            if_match (str): Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 

        Keyword Args:
            body (UpdateShipment): [optional]
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
            MTOShipment
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
        kwargs['move_task_order_id'] = \
            move_task_order_id
        kwargs['shipment_id'] = \
            shipment_id
        kwargs['if_match'] = \
            if_match
        return self.update_mto_shipment_endpoint.call_with_http_info(**kwargs)

