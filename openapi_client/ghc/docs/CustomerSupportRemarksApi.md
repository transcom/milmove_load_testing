# ghc_client.CustomerSupportRemarksApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_support_remark_for_move**](CustomerSupportRemarksApi.md#create_customer_support_remark_for_move) | **POST** /moves/{locator}/customer-support-remarks | Creates a customer support remark for a move
[**delete_customer_support_remark**](CustomerSupportRemarksApi.md#delete_customer_support_remark) | **DELETE** /customer-support-remarks/{customerSupportRemarkID} | Soft deletes a customer support remark by ID
[**get_customer_support_remarks_for_move**](CustomerSupportRemarksApi.md#get_customer_support_remarks_for_move) | **GET** /moves/{locator}/customer-support-remarks | Fetches customer support remarks using the move code (locator).
[**update_customer_support_remark_for_move**](CustomerSupportRemarksApi.md#update_customer_support_remark_for_move) | **PATCH** /customer-support-remarks/{customerSupportRemarkID} | Updates a customer support remark for a move


# **create_customer_support_remark_for_move**
> CustomerSupportRemark create_customer_support_remark_for_move(locator)

Creates a customer support remark for a move

Creates a customer support remark for a move

### Example


```python
import time
import ghc_client
from ghc_client.api import customer_support_remarks_api
from ghc_client.model.error import Error
from ghc_client.model.create_customer_support_remark import CreateCustomerSupportRemark
from ghc_client.model.customer_support_remark import CustomerSupportRemark
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
    api_instance = customer_support_remarks_api.CustomerSupportRemarksApi(api_client)
    locator = "locator_example" # str | move code to identify a move for customer support remarks
    body = CreateCustomerSupportRemark(
        content="This is a remark about a move.",
        office_user_id="1f2270c7-7166-40ae-981e-b200ebdf3054",
    ) # CreateCustomerSupportRemark |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a customer support remark for a move
        api_response = api_instance.create_customer_support_remark_for_move(locator)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling CustomerSupportRemarksApi->create_customer_support_remark_for_move: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a customer support remark for a move
        api_response = api_instance.create_customer_support_remark_for_move(locator, body=body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling CustomerSupportRemarksApi->create_customer_support_remark_for_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**| move code to identify a move for customer support remarks |
 **body** | [**CreateCustomerSupportRemark**](CreateCustomerSupportRemark.md)|  | [optional]

### Return type

[**CustomerSupportRemark**](CustomerSupportRemark.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created customer support remark |  -  |
**400** | The request payload is invalid |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_support_remark**
> delete_customer_support_remark(customer_support_remark_id)

Soft deletes a customer support remark by ID

Soft deletes a customer support remark by ID

### Example


```python
import time
import ghc_client
from ghc_client.api import customer_support_remarks_api
from ghc_client.model.error import Error
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
    api_instance = customer_support_remarks_api.CustomerSupportRemarksApi(api_client)
    customer_support_remark_id = "customerSupportRemarkID_example" # str | the customer support remark ID to be modified

    # example passing only required values which don't have defaults set
    try:
        # Soft deletes a customer support remark by ID
        api_instance.delete_customer_support_remark(customer_support_remark_id)
    except ghc_client.ApiException as e:
        print("Exception when calling CustomerSupportRemarksApi->delete_customer_support_remark: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_support_remark_id** | **str**| the customer support remark ID to be modified |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully soft deleted the shipment |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_support_remarks_for_move**
> CustomerSupportRemarks get_customer_support_remarks_for_move(locator)

Fetches customer support remarks using the move code (locator).

Fetches customer support remarks for a move

### Example


```python
import time
import ghc_client
from ghc_client.api import customer_support_remarks_api
from ghc_client.model.customer_support_remarks import CustomerSupportRemarks
from ghc_client.model.error import Error
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
    api_instance = customer_support_remarks_api.CustomerSupportRemarksApi(api_client)
    locator = "locator_example" # str | move code to identify a move for customer support remarks

    # example passing only required values which don't have defaults set
    try:
        # Fetches customer support remarks using the move code (locator).
        api_response = api_instance.get_customer_support_remarks_for_move(locator)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling CustomerSupportRemarksApi->get_customer_support_remarks_for_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**| move code to identify a move for customer support remarks |

### Return type

[**CustomerSupportRemarks**](CustomerSupportRemarks.md)

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

# **update_customer_support_remark_for_move**
> CustomerSupportRemark update_customer_support_remark_for_move(customer_support_remark_id, body)

Updates a customer support remark for a move

Updates a customer support remark for a move

### Example


```python
import time
import ghc_client
from ghc_client.api import customer_support_remarks_api
from ghc_client.model.error import Error
from ghc_client.model.update_customer_support_remark_payload import UpdateCustomerSupportRemarkPayload
from ghc_client.model.customer_support_remark import CustomerSupportRemark
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
    api_instance = customer_support_remarks_api.CustomerSupportRemarksApi(api_client)
    customer_support_remark_id = "customerSupportRemarkID_example" # str | the customer support remark ID to be modified
    body = UpdateCustomerSupportRemarkPayload(
        content="This is a remark about a move.",
    ) # UpdateCustomerSupportRemarkPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a customer support remark for a move
        api_response = api_instance.update_customer_support_remark_for_move(customer_support_remark_id, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling CustomerSupportRemarksApi->update_customer_support_remark_for_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_support_remark_id** | **str**| the customer support remark ID to be modified |
 **body** | [**UpdateCustomerSupportRemarkPayload**](UpdateCustomerSupportRemarkPayload.md)|  |

### Return type

[**CustomerSupportRemark**](CustomerSupportRemark.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated customer support remark |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

