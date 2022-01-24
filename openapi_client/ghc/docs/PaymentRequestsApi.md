# ghc_client.PaymentRequestsApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_request**](PaymentRequestsApi.md#get_payment_request) | **GET** /payment-requests/{paymentRequestID} | Fetches a payment request by id
[**get_payment_requests_for_move**](PaymentRequestsApi.md#get_payment_requests_for_move) | **GET** /moves/{locator}/payment-requests | Fetches payment requests using the move code (locator).
[**get_shipments_payment_sit_balance**](PaymentRequestsApi.md#get_shipments_payment_sit_balance) | **GET** /payment-requests/{paymentRequestID}/shipments-payment-sit-balance | Returns all shipment payment request SIT usage to support partial SIT invoicing
[**update_payment_request_status**](PaymentRequestsApi.md#update_payment_request_status) | **PATCH** /payment-requests/{paymentRequestID}/status | Updates status of a payment request by id


# **get_payment_request**
> PaymentRequest get_payment_request(payment_request_id)

Fetches a payment request by id

Fetches an instance of a payment request by id

### Example


```python
import time
import ghc_client
from ghc_client.api import payment_requests_api
from ghc_client.model.payment_request import PaymentRequest
from ghc_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_requests_api.PaymentRequestsApi(api_client)
    payment_request_id = "paymentRequestID_example" # str | UUID of payment request

    # example passing only required values which don't have defaults set
    try:
        # Fetches a payment request by id
        api_response = api_instance.get_payment_request(payment_request_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PaymentRequestsApi->get_payment_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**| UUID of payment request |

### Return type

[**PaymentRequest**](PaymentRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | fetched instance of payment request |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_requests_for_move**
> PaymentRequests get_payment_requests_for_move(locator)

Fetches payment requests using the move code (locator).

Fetches payment requests for a move

### Example


```python
import time
import ghc_client
from ghc_client.api import payment_requests_api
from ghc_client.model.error import Error
from ghc_client.model.payment_requests import PaymentRequests
from ghc_client.model.validation_error import ValidationError
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_requests_api.PaymentRequestsApi(api_client)
    locator = "locator_example" # str | move code to identify a move for payment requests

    # example passing only required values which don't have defaults set
    try:
        # Fetches payment requests using the move code (locator).
        api_response = api_instance.get_payment_requests_for_move(locator)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PaymentRequestsApi->get_payment_requests_for_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**| move code to identify a move for payment requests |

### Return type

[**PaymentRequests**](PaymentRequests.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved all line items for a move task order |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipments_payment_sit_balance**
> ShipmentsPaymentSITBalance get_shipments_payment_sit_balance(payment_request_id)

Returns all shipment payment request SIT usage to support partial SIT invoicing

Returns all shipment payment request SIT usage to support partial SIT invoicing

### Example


```python
import time
import ghc_client
from ghc_client.api import payment_requests_api
from ghc_client.model.error import Error
from ghc_client.model.shipments_payment_sit_balance import ShipmentsPaymentSITBalance
from ghc_client.model.validation_error import ValidationError
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_requests_api.PaymentRequestsApi(api_client)
    payment_request_id = "paymentRequestID_example" # str | payment request ID of the payment request with SIT service items being reviewed

    # example passing only required values which don't have defaults set
    try:
        # Returns all shipment payment request SIT usage to support partial SIT invoicing
        api_response = api_instance.get_shipments_payment_sit_balance(payment_request_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PaymentRequestsApi->get_shipments_payment_sit_balance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**| payment request ID of the payment request with SIT service items being reviewed |

### Return type

[**ShipmentsPaymentSITBalance**](ShipmentsPaymentSITBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved shipments and their SIT days balance from all payment requests on the move |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_request_status**
> PaymentRequest update_payment_request_status(payment_request_id, if_match, body)

Updates status of a payment request by id

Updates status of a payment request by id

### Example


```python
import time
import ghc_client
from ghc_client.api import payment_requests_api
from ghc_client.model.payment_request import PaymentRequest
from ghc_client.model.error import Error
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.update_payment_request_status_payload import UpdatePaymentRequestStatusPayload
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_requests_api.PaymentRequestsApi(api_client)
    payment_request_id = "paymentRequestID_example" # str | UUID of payment request
    if_match = "If-Match_example" # str | 
    body = UpdatePaymentRequestStatusPayload(
        rejection_reason="documentation was incomplete",
        status=PaymentRequestStatus("PENDING"),
        e_tag="e_tag_example",
    ) # UpdatePaymentRequestStatusPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Updates status of a payment request by id
        api_response = api_instance.update_payment_request_status(payment_request_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PaymentRequestsApi->update_payment_request_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**| UUID of payment request |
 **if_match** | **str**|  |
 **body** | [**UpdatePaymentRequestStatusPayload**](UpdatePaymentRequestStatusPayload.md)|  |

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
**200** | updated payment request |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

