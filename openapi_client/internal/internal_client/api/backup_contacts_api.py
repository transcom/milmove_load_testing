"""
    MilMove Internal API

    The Internal API is a RESTful API that enables the Customer application for MilMove.  All endpoints are located under `/internal`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from internal_client.api_client import ApiClient, Endpoint as _Endpoint
from internal_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from internal_client.model.create_service_member_backup_contact_payload import CreateServiceMemberBackupContactPayload
from internal_client.model.index_service_member_backup_contacts_payload import IndexServiceMemberBackupContactsPayload
from internal_client.model.service_member_backup_contact_payload import ServiceMemberBackupContactPayload
from internal_client.model.update_service_member_backup_contact_payload import UpdateServiceMemberBackupContactPayload


class BackupContactsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_service_member_backup_contact_endpoint = _Endpoint(
            settings={
                'response_type': (ServiceMemberBackupContactPayload,),
                'auth': [],
                'endpoint_path': '/service_members/{serviceMemberId}/backup_contacts',
                'operation_id': 'create_service_member_backup_contact',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_member_id',
                    'create_backup_contact_payload',
                ],
                'required': [
                    'service_member_id',
                    'create_backup_contact_payload',
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
                    'service_member_id':
                        (str,),
                    'create_backup_contact_payload':
                        (CreateServiceMemberBackupContactPayload,),
                },
                'attribute_map': {
                    'service_member_id': 'serviceMemberId',
                },
                'location_map': {
                    'service_member_id': 'path',
                    'create_backup_contact_payload': 'body',
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
        self.index_service_member_backup_contacts_endpoint = _Endpoint(
            settings={
                'response_type': (IndexServiceMemberBackupContactsPayload,),
                'auth': [],
                'endpoint_path': '/service_members/{serviceMemberId}/backup_contacts',
                'operation_id': 'index_service_member_backup_contacts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_member_id',
                ],
                'required': [
                    'service_member_id',
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
                    'service_member_id':
                        (str,),
                },
                'attribute_map': {
                    'service_member_id': 'serviceMemberId',
                },
                'location_map': {
                    'service_member_id': 'path',
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
        self.show_service_member_backup_contact_endpoint = _Endpoint(
            settings={
                'response_type': (ServiceMemberBackupContactPayload,),
                'auth': [],
                'endpoint_path': '/backup_contacts/{backupContactId}',
                'operation_id': 'show_service_member_backup_contact',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'backup_contact_id',
                ],
                'required': [
                    'backup_contact_id',
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
                    'backup_contact_id':
                        (str,),
                },
                'attribute_map': {
                    'backup_contact_id': 'backupContactId',
                },
                'location_map': {
                    'backup_contact_id': 'path',
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
        self.update_service_member_backup_contact_endpoint = _Endpoint(
            settings={
                'response_type': (ServiceMemberBackupContactPayload,),
                'auth': [],
                'endpoint_path': '/backup_contacts/{backupContactId}',
                'operation_id': 'update_service_member_backup_contact',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'backup_contact_id',
                    'update_service_member_backup_contact_payload',
                ],
                'required': [
                    'backup_contact_id',
                    'update_service_member_backup_contact_payload',
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
                    'backup_contact_id':
                        (str,),
                    'update_service_member_backup_contact_payload':
                        (UpdateServiceMemberBackupContactPayload,),
                },
                'attribute_map': {
                    'backup_contact_id': 'backupContactId',
                },
                'location_map': {
                    'backup_contact_id': 'path',
                    'update_service_member_backup_contact_payload': 'body',
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

    def create_service_member_backup_contact(
        self,
        service_member_id,
        create_backup_contact_payload,
        **kwargs
    ):
        """Submits backup contact for a logged-in user  # noqa: E501

        Creates an instance of a backup contact tied to a service member user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_service_member_backup_contact(service_member_id, create_backup_contact_payload, async_req=True)
        >>> result = thread.get()

        Args:
            service_member_id (str): UUID of the service member
            create_backup_contact_payload (CreateServiceMemberBackupContactPayload):

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
            ServiceMemberBackupContactPayload
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
        kwargs['service_member_id'] = \
            service_member_id
        kwargs['create_backup_contact_payload'] = \
            create_backup_contact_payload
        return self.create_service_member_backup_contact_endpoint.call_with_http_info(**kwargs)

    def index_service_member_backup_contacts(
        self,
        service_member_id,
        **kwargs
    ):
        """List all service member backup contacts  # noqa: E501

        List all service member backup contacts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.index_service_member_backup_contacts(service_member_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_member_id (str): UUID of the service member

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
            IndexServiceMemberBackupContactsPayload
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
        kwargs['service_member_id'] = \
            service_member_id
        return self.index_service_member_backup_contacts_endpoint.call_with_http_info(**kwargs)

    def show_service_member_backup_contact(
        self,
        backup_contact_id,
        **kwargs
    ):
        """Returns the given service member backup contact  # noqa: E501

        Returns the given service member backup contact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.show_service_member_backup_contact(backup_contact_id, async_req=True)
        >>> result = thread.get()

        Args:
            backup_contact_id (str): UUID of the service member backup contact

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
            ServiceMemberBackupContactPayload
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
        kwargs['backup_contact_id'] = \
            backup_contact_id
        return self.show_service_member_backup_contact_endpoint.call_with_http_info(**kwargs)

    def update_service_member_backup_contact(
        self,
        backup_contact_id,
        update_service_member_backup_contact_payload,
        **kwargs
    ):
        """Updates a service member backup contact  # noqa: E501

        Any fields sent in this request will be set on the backup contact referenced  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_service_member_backup_contact(backup_contact_id, update_service_member_backup_contact_payload, async_req=True)
        >>> result = thread.get()

        Args:
            backup_contact_id (str): UUID of the service member backup contact
            update_service_member_backup_contact_payload (UpdateServiceMemberBackupContactPayload):

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
            ServiceMemberBackupContactPayload
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
        kwargs['backup_contact_id'] = \
            backup_contact_id
        kwargs['update_service_member_backup_contact_payload'] = \
            update_service_member_backup_contact_payload
        return self.update_service_member_backup_contact_endpoint.call_with_http_info(**kwargs)

