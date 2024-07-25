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
from prime_client.model.create_payment_request import CreatePaymentRequest
from prime_client.model.error import Error
from prime_client.model.payment_request import PaymentRequest
from prime_client.model.upload_with_omissions import UploadWithOmissions
from prime_client.model.validation_error import ValidationError


class PaymentRequestApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_payment_request_endpoint = _Endpoint(
            settings={
                'response_type': (PaymentRequest,),
                'auth': [],
                'endpoint_path': '/payment-requests',
                'operation_id': 'create_payment_request',
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
                        (CreatePaymentRequest,),
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
        self.create_upload_endpoint = _Endpoint(
            settings={
                'response_type': (UploadWithOmissions,),
                'auth': [],
                'endpoint_path': '/payment-requests/{paymentRequestID}/uploads',
                'operation_id': 'create_upload',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_request_id',
                    'file',
                    'is_weight_ticket',
                ],
                'required': [
                    'payment_request_id',
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
                    'payment_request_id':
                        (str,),
                    'file':
                        (file_type,),
                    'is_weight_ticket':
                        (bool,),
                },
                'attribute_map': {
                    'payment_request_id': 'paymentRequestID',
                    'file': 'file',
                    'is_weight_ticket': 'isWeightTicket',
                },
                'location_map': {
                    'payment_request_id': 'path',
                    'file': 'form',
                    'is_weight_ticket': 'form',
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

    def create_payment_request(
        self,
        **kwargs
    ):
        """createPaymentRequest  # noqa: E501

        Creates a new instance of a paymentRequest and is assigned the status `PENDING`. A move task order can have multiple payment requests, and a final payment request can be marked using boolean `isFinal`.  If a `PENDING` payment request is recalculated, a new payment request is created and the original request is marked with the status `DEPRECATED`.  **NOTE**: In order to create a payment request for most service items, the shipment *must* be updated with the `PrimeActualWeight` value via [updateMTOShipment](#operation/updateMTOShipment).  **FSC - Fuel Surcharge** service items require `ActualPickupDate` to be updated on the shipment.  A service item can be on several payment requests in the case of partial payment requests and payments.  In the request, if no params are necessary, then just the `serviceItem` `id` is required. For example: ```json {   \"isFinal\": false,   \"moveTaskOrderID\": \"uuid\",   \"serviceItems\": [     {       \"id\": \"uuid\",     },     {       \"id\": \"uuid\",       \"params\": [         {           \"key\": \"Service Item Parameter Name\",           \"value\": \"Service Item Parameter Value\"         }       ]     }   ],   \"pointOfContact\": \"string\" } ```  SIT Service Items & Accepted Payment Request Parameters: --- If `WeightBilled` is not provided then the full shipment weight (`PrimeActualWeight`) will be considered in the calculation.  **NOTE**: Diversions have a unique calcuation for payment requests without a `WeightBilled` parameter.  If you created a payment request for a diversion and `WeightBilled` is not provided, then the following will be used in the calculation: - The lowest shipment weight (`PrimeActualWeight`) found in the diverted shipment chain. - The lowest reweigh weight found in the diverted shipment chain.  The diverted shipment chain is created by referencing the `diversion` boolean, `divertedFromShipmentId` UUID, and matching destination to pickup addresses. If the chain cannot be established it will fall back to the `PrimeActualWeight` of the current shipment. This is utilized because diverted shipments are all one single shipment, but going to different locations. The lowest weight found is the true shipment weight, and thus we search the chain of shipments for the lowest weight found.  **DOFSIT - Domestic origin 1st day SIT** ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     }   ] ```  **DOASIT - Domestic origin add'l SIT** *(SITPaymentRequestStart & SITPaymentRequestEnd are **REQUIRED**)* *To create a paymentRequest for this service item, the `SITPaymentRequestStart` and `SITPaymentRequestEnd` dates must not overlap previously requested SIT dates.* ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     },     {       \"key\": \"SITPaymentRequestStart\",       \"value\": \"date\"     },     {       \"key\": \"SITPaymentRequestEnd\",       \"value\": \"date\"     }   ] ```  **DOPSIT - Domestic origin SIT pickup** ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     }   ] ```  **DOSHUT - Domestic origin shuttle service** ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     }   ] ```  **DDFSIT - Domestic destination 1st day SIT** ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     }   ] ```  **DDASIT - Domestic destination add'l SIT** *(SITPaymentRequestStart & SITPaymentRequestEnd are **REQUIRED**)* *To create a paymentRequest for this service item, the `SITPaymentRequestStart` and `SITPaymentRequestEnd` dates must not overlap previously requested SIT dates.* ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     },     {       \"key\": \"SITPaymentRequestStart\",       \"value\": \"date\"     },     {       \"key\": \"SITPaymentRequestEnd\",       \"value\": \"date\"     }   ] ```  **DDDSIT - Domestic destination SIT delivery** *To create a paymentRequest for this service item, it must first have a final address set via [updateMTOServiceItem](#operation/updateMTOServiceItem).* ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     }   ] ```  **DDSHUT - Domestic destination shuttle service** ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     }   ] ``` ---   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_payment_request(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            body (CreatePaymentRequest): [optional]
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
            PaymentRequest
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
        return self.create_payment_request_endpoint.call_with_http_info(**kwargs)

    def create_upload(
        self,
        payment_request_id,
        file,
        **kwargs
    ):
        """createUpload  # noqa: E501

        ### Functionality This endpoint **uploads** a Proof of Service document for a PaymentRequest.  The PaymentRequest should already exist.  Optional key of **isWeightTicket** indicates if the document is a weight ticket or not. This will be used for partial and full deliveries and makes it easier for the Task Invoicing Officers to locate and review service item documents. If left empty, it will assume it is NOT a weight ticket.  The formdata in the body of the POST request that is sent should look like this if it IS a weight ticket being attached to an existing payment request:   ```json   {     \"file\": \"filePath\",     \"isWeightTicket\": true   }   ```   If the proof of service doc is NOT a weight ticket, it will look like this - or you can leave it empty:   ```json   {     \"file\": \"filePath\",     \"isWeightTicket\": false   }   ```   ```json   {     \"file\": \"filePath\",   }   ```  PaymentRequests are created with the [createPaymentRequest](#operation/createPaymentRequest) endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_upload(payment_request_id, file, async_req=True)
        >>> result = thread.get()

        Args:
            payment_request_id (str): UUID of payment request to use.
            file (file_type): The file to upload.

        Keyword Args:
            is_weight_ticket (bool): Indicates whether the file is a weight ticket.. [optional]
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
            UploadWithOmissions
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
        kwargs['payment_request_id'] = \
            payment_request_id
        kwargs['file'] = \
            file
        return self.create_upload_endpoint.call_with_http_info(**kwargs)

