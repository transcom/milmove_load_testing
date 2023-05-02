# prime_client.PaymentRequestApi

All URIs are relative to */prime/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_request**](PaymentRequestApi.md#create_payment_request) | **POST** /payment-requests | createPaymentRequest
[**create_upload**](PaymentRequestApi.md#create_upload) | **POST** /payment-requests/{paymentRequestID}/uploads | createUpload


# **create_payment_request**
> PaymentRequest create_payment_request()

createPaymentRequest

Creates a new instance of a paymentRequest. A newly created payment request is assigned the status `PENDING`. A move task order can have multiple payment requests, and a final payment request can be marked using boolean `isFinal`.  If a `PENDING` payment request is recalculated, a new payment request is created and the original request is marked with the status `DEPRECATED`.  **NOTE**: In order to create a payment request for most service items, the shipment *must* be updated with the `PrimeActualWeight` value via [updateMTOShipment](#operation/updateMTOShipment). **Fuel Surcharge** service items require `ActualPickupDate` to be updated on the shipment.  To create a paymentRequest for a SIT Delivery mtoServiceItem, the item must first have a final address set via [updateMTOServiceItem](#operation/updateMTOServiceItem). 

### Example


```python
import time
import prime_client
from prime_client.api import payment_request_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.payment_request import PaymentRequest
from prime_client.model.error import Error
from prime_client.model.create_payment_request import CreatePaymentRequest
from prime_client.model.client_error import ClientError
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_request_api.PaymentRequestApi(api_client)
    body = CreatePaymentRequest(
        is_final=False,
        move_task_order_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        service_items=[
            ServiceItem(
                id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                params=[
                    ServiceItemParams(
                        key="Service Item Parameter Name",
                        value="Service Item Parameter Value",
                    ),
                ],
            ),
        ],
        point_of_contact="point_of_contact_example",
    ) # CreatePaymentRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # createPaymentRequest
        api_response = api_instance.create_payment_request(body=body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling PaymentRequestApi->create_payment_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePaymentRequest**](CreatePaymentRequest.md)|  | [optional]

### Return type

[**PaymentRequest**](PaymentRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a paymentRequest object. |  -  |
**400** | Request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload**
> UploadWithOmissions create_upload(payment_request_id, file)

createUpload

### Functionality This endpoint **uploads** a Proof of Service document for a PaymentRequest.  The PaymentRequest should already exist.  PaymentRequests are created with the [createPaymentRequest](#operation/createPaymentRequest) endpoint. 

### Example


```python
import time
import prime_client
from prime_client.api import payment_request_api
from prime_client.model.upload_with_omissions import UploadWithOmissions
from prime_client.model.validation_error import ValidationError
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_request_api.PaymentRequestApi(api_client)
    payment_request_id = "paymentRequestID_example" # str | UUID of payment request to use.
    file = open('/path/to/file', 'rb') # file_type | The file to upload.

    # example passing only required values which don't have defaults set
    try:
        # createUpload
        api_response = api_instance.create_upload(payment_request_id, file)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling PaymentRequestApi->create_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**| UUID of payment request to use. |
 **file** | **file_type**| The file to upload. |

### Return type

[**UploadWithOmissions**](UploadWithOmissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created upload of digital file. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

