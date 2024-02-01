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
from prime_client.model.error import Error
from prime_client.model.excess_weight_record import ExcessWeightRecord
from prime_client.model.list_moves import ListMoves
from prime_client.model.move_task_order import MoveTaskOrder
from prime_client.model.validation_error import ValidationError


class MoveTaskOrderApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_excess_weight_record_endpoint = _Endpoint(
            settings={
                'response_type': (ExcessWeightRecord,),
                'auth': [],
                'endpoint_path': '/move-task-orders/{moveTaskOrderID}/excess-weight-record',
                'operation_id': 'create_excess_weight_record',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'move_task_order_id',
                    'file',
                ],
                'required': [
                    'move_task_order_id',
                    'file',
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
                    'file':
                        (file_type,),
                },
                'attribute_map': {
                    'move_task_order_id': 'moveTaskOrderID',
                    'file': 'file',
                },
                'location_map': {
                    'move_task_order_id': 'path',
                    'file': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )
        self.download_move_order_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [],
                'endpoint_path': '/moves/{locator}/order/download',
                'operation_id': 'download_move_order',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'locator',
                ],
                'required': [
                    'locator',
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
                    'locator':
                        (str,),
                },
                'attribute_map': {
                    'locator': 'locator',
                },
                'location_map': {
                    'locator': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/pdf'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_move_task_order_endpoint = _Endpoint(
            settings={
                'response_type': (MoveTaskOrder,),
                'auth': [],
                'endpoint_path': '/move-task-orders/{moveID}',
                'operation_id': 'get_move_task_order',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'move_id',
                ],
                'required': [
                    'move_id',
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
                    'move_id':
                        (str,),
                },
                'attribute_map': {
                    'move_id': 'moveID',
                },
                'location_map': {
                    'move_id': 'path',
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
        self.list_moves_endpoint = _Endpoint(
            settings={
                'response_type': (ListMoves,),
                'auth': [],
                'endpoint_path': '/moves',
                'operation_id': 'list_moves',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'since',
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
                    'since':
                        (datetime,),
                },
                'attribute_map': {
                    'since': 'since',
                },
                'location_map': {
                    'since': 'query',
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
        self.update_mto_post_counseling_information_endpoint = _Endpoint(
            settings={
                'response_type': (MoveTaskOrder,),
                'auth': [],
                'endpoint_path': '/move-task-orders/{moveTaskOrderID}/post-counseling-info',
                'operation_id': 'update_mto_post_counseling_information',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'move_task_order_id',
                    'if_match',
                ],
                'required': [
                    'move_task_order_id',
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
                    'if_match':
                        (str,),
                },
                'attribute_map': {
                    'move_task_order_id': 'moveTaskOrderID',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'move_task_order_id': 'path',
                    'if_match': 'header',
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

    def create_excess_weight_record(
        self,
        move_task_order_id,
        file,
        **kwargs
    ):
        """createExcessWeightRecord  # noqa: E501

        Uploads an excess weight record, which is a document that proves that the movers or contractors have counseled the customer about their excess weight. Excess weight counseling should occur after the sum of the shipments for the customer's move crosses the excess weight alert threshold.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_excess_weight_record(move_task_order_id, file, async_req=True)
        >>> result = thread.get()

        Args:
            move_task_order_id (str): UUID of the move being updated.
            file (file_type): The file to upload.

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
            ExcessWeightRecord
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
        kwargs['file'] = \
            file
        return self.create_excess_weight_record_endpoint.call_with_http_info(**kwargs)

    def download_move_order(
        self,
        locator,
        **kwargs
    ):
        """Downloads move order as a PDF  # noqa: E501

        ### Functionality This endpoint downloads all uploaded move order documentations into one download file by locator.  ### Errors * The move must be in need counseling state. * The move client's origin duty location must not currently have gov counseling.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_move_order(locator, async_req=True)
        >>> result = thread.get()

        Args:
            locator (str): the locator code for move order to be downloaded

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
            file_type
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
        kwargs['locator'] = \
            locator
        return self.download_move_order_endpoint.call_with_http_info(**kwargs)

    def get_move_task_order(
        self,
        move_id,
        **kwargs
    ):
        """getMoveTaskOrder  # noqa: E501

        ### Functionality This endpoint gets an individual MoveTaskOrder by ID.  It will provide information about the Customer and any associated MTOShipments, MTOServiceItems and PaymentRequests.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_move_task_order(move_id, async_req=True)
        >>> result = thread.get()

        Args:
            move_id (str): UUID or MoveCode of move task order to use.

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
            MoveTaskOrder
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
        kwargs['move_id'] = \
            move_id
        return self.get_move_task_order_endpoint.call_with_http_info(**kwargs)

    def list_moves(
        self,
        **kwargs
    ):
        """listMoves  # noqa: E501

        Gets all moves that have been reviewed and approved by the TOO. The `since` parameter can be used to filter this list down to only the moves that have been updated since the provided timestamp. A move will be considered updated if the `updatedAt` timestamp on the move or on its orders, shipments, service items, or payment requests, is later than the provided date and time.  **WIP**: Include what causes moves to leave this list. Currently, once the `availableToPrimeAt` timestamp has been set, that move will always appear in this list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_moves(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            since (datetime): Only return moves updated since this time. Formatted like \"2021-07-23T18:30:47.116Z\". [optional]
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
            ListMoves
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
        return self.list_moves_endpoint.call_with_http_info(**kwargs)

    def update_mto_post_counseling_information(
        self,
        move_task_order_id,
        if_match,
        **kwargs
    ):
        """updateMTOPostCounselingInformation  # noqa: E501

        ### Functionality This endpoint **updates** the MoveTaskOrder to indicate that the Prime has completed Counseling. This update uses the moveTaskOrderID provided in the path, updates the move status and marks child elements of the move to indicate the update. No body object is expected for this request.  **For Full/Partial PPMs**: This action is required so that the customer can start uploading their proof of service docs.  **For other move types**: This action is required for auditing reasons so that we have a record of when the Prime counseled the customer.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_mto_post_counseling_information(move_task_order_id, if_match, async_req=True)
        >>> result = thread.get()

        Args:
            move_task_order_id (str): ID of move task order to use.
            if_match (str): Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 

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
            MoveTaskOrder
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
        kwargs['if_match'] = \
            if_match
        return self.update_mto_post_counseling_information_endpoint.call_with_http_info(**kwargs)

