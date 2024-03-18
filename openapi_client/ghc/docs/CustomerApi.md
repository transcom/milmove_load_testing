# ghc_client.CustomerApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer**](CustomerApi.md#get_customer) | **GET** /customer/{customerID} | Returns a given customer
[**update_customer**](CustomerApi.md#update_customer) | **PATCH** /customer/{customerID} | Updates customer info


# **get_customer**
> Customer get_customer(customer_id)

Returns a given customer

Returns a given customer

### Example


```python
import time
import ghc_client
from ghc_client.api import customer_api
from ghc_client.model.error import Error
from ghc_client.model.customer import Customer
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = customer_api.CustomerApi(api_client)
    customer_id = "customerID_example" # str | ID of customer to use

    # example passing only required values which don't have defaults set
    try:
        # Returns a given customer
        api_response = api_instance.get_customer(customer_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling CustomerApi->get_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| ID of customer to use |

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved information on an individual customer |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> Customer update_customer(customer_id, if_match, body)

Updates customer info

Updates customer info by ID

### Example


```python
import time
import ghc_client
from ghc_client.api import customer_api
from ghc_client.model.error import Error
from ghc_client.model.customer import Customer
from ghc_client.model.update_customer_payload import UpdateCustomerPayload
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
    api_instance = customer_api.CustomerApi(api_client)
    customer_id = "customerID_example" # str | ID of customer to use
    if_match = "If-Match_example" # str | 
    body = UpdateCustomerPayload(
        first_name="John",
        last_name="Doe",
        phone="748-072-8880",
        email="A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRddzXYdswQltRTtwKQzBuNJxBelKTmfIQcBkWgeAShmXXoTaDzlkczbtHjkljEhQVqeWYqqMQZlEQb",
        suffix="Jr.",
        middle_name="David",
        current_address=UpdateCustomerPayloadCurrentAddress(),
        backup_contact=BackupContact(
            name="name_example",
            email="A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRddzXYdswQltRTtwKQzBuNJxBelKTmfIQcBkWgeAShmXXoTaDzlkczbtHjkljEhQVqeWYqqMQZlEQb",
            phone="748-072-8880",
        ),
        phone_is_preferred=True,
        email_is_preferred=True,
        secondary_telephone="748-072-8880",
        backup_address=UpdateCustomerPayloadCurrentAddress(),
    ) # UpdateCustomerPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Updates customer info
        api_response = api_instance.update_customer(customer_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling CustomerApi->update_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| ID of customer to use |
 **if_match** | **str**|  |
 **body** | [**UpdateCustomerPayload**](UpdateCustomerPayload.md)|  |

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of orders |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

