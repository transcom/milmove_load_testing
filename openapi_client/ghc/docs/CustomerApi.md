# ghc_client.CustomerApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_with_okta_option**](CustomerApi.md#create_customer_with_okta_option) | **POST** /customer | Creates a customer with Okta option
[**get_customer**](CustomerApi.md#get_customer) | **GET** /customer/{customerID} | Returns a given customer
[**search_customers**](CustomerApi.md#search_customers) | **POST** /customer/search | Search customers by DOD ID or customer name
[**update_customer**](CustomerApi.md#update_customer) | **PATCH** /customer/{customerID} | Updates customer info


# **create_customer_with_okta_option**
> CreatedCustomer create_customer_with_okta_option(body)

Creates a customer with Okta option

Creates a customer with option to create an Okta profile account

### Example


```python
import time
import ghc_client
from ghc_client.api import customer_api
from ghc_client.model.created_customer import CreatedCustomer
from ghc_client.model.error import Error
from ghc_client.model.create_customer_payload import CreateCustomerPayload
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
    body = CreateCustomerPayload(
        affiliation=Affiliation("ARMY"),
        edipi="John",
        first_name="John",
        middle_name="David",
        last_name="Doe",
        suffix="Jr.",
        telephone="748-072-8880",
        secondary_telephone="748-072-8880",
        personal_email="personalEmail@email.com",
        phone_is_preferred=True,
        email_is_preferred=True,
        residential_address=UpdateCustomerPayloadCurrentAddress(),
        backup_contact=BackupContact(
            name="name_example",
            email="backupContact@mail.com",
            phone="748-072-8880",
        ),
        backup_mailing_address=UpdateCustomerPayloadCurrentAddress(),
        create_okta_account=True,
        cac_user=True,
    ) # CreateCustomerPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a customer with Okta option
        api_response = api_instance.create_customer_with_okta_option(body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling CustomerApi->create_customer_with_okta_option: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomerPayload**](CreateCustomerPayload.md)|  |

### Return type

[**CreatedCustomer**](CreatedCustomer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully created the customer |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **search_customers**
> SearchCustomersResult search_customers()

Search customers by DOD ID or customer name

Search customers by DOD ID or customer name. Used by services counselors to locate profiles to update, find attached moves, and to create new moves. 

### Example


```python
import time
import ghc_client
from ghc_client.api import customer_api
from ghc_client.model.error import Error
from ghc_client.model.search_customers_result import SearchCustomersResult
from ghc_client.model.search_customers_request import SearchCustomersRequest
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
    body = SearchCustomersRequest(
        page=1,
        per_page=1,
        dod_id="dod_id_example",
        branch="branch_example",
        customer_name="customer_name_example",
        sort="customerName",
        order="asc",
    ) # SearchCustomersRequest | field that results should be sorted by (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search customers by DOD ID or customer name
        api_response = api_instance.search_customers(body=body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling CustomerApi->search_customers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchCustomersRequest**](SearchCustomersRequest.md)| field that results should be sorted by | [optional]

### Return type

[**SearchCustomersResult**](SearchCustomersResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned all customers matching the criteria |  -  |
**403** | The request was denied |  -  |
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
            email="backupContact@mail.com",
            phone="748-072-8880",
        ),
        phone_is_preferred=True,
        email_is_preferred=True,
        secondary_telephone="",
        backup_address=UpdateCustomerPayloadCurrentAddress(),
        cac_validated=True,
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

