# internal_client.OrdersApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_orders**](OrdersApi.md#create_orders) | **POST** /orders | Creates an orders model for a logged-in user
[**show_orders**](OrdersApi.md#show_orders) | **GET** /orders/{ordersId} | Returns the given order
[**update_orders**](OrdersApi.md#update_orders) | **PUT** /orders/{ordersId} | Updates orders
[**upload_amended_orders**](OrdersApi.md#upload_amended_orders) | **PATCH** /orders/{ordersId}/upload_amended_orders | Patch the amended orders for a given order


# **create_orders**
> Orders create_orders(create_orders)

Creates an orders model for a logged-in user

Creates an instance of orders tied to a service member

### Example


```python
import time
import internal_client
from internal_client.api import orders_api
from internal_client.model.orders import Orders
from internal_client.model.create_update_orders import CreateUpdateOrders
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    create_orders = CreateUpdateOrders(
        service_member_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        issue_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        report_by_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        orders_type=OrdersType("PERMANENT_CHANGE_OF_STATION"),
        orders_type_detail=OrdersTypeDetail("HHG_PERMITTED"),
        has_dependents=True,
        spouse_has_pro_gear=True,
        new_duty_station_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        orders_number="030-00362",
        tac="F8J1",
        sac="N002214CSW32Y9",
        department_indicator=DeptIndicator("NAVY_AND_MARINES"),
    ) # CreateUpdateOrders | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an orders model for a logged-in user
        api_response = api_instance.create_orders(create_orders)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling OrdersApi->create_orders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_orders** | [**CreateUpdateOrders**](CreateUpdateOrders.md)|  |

### Return type

[**Orders**](Orders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created instance of orders |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_orders**
> Orders show_orders(orders_id)

Returns the given order

Returns the given order

### Example


```python
import time
import internal_client
from internal_client.api import orders_api
from internal_client.model.orders import Orders
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    orders_id = "ordersId_example" # str | UUID of the order

    # example passing only required values which don't have defaults set
    try:
        # Returns the given order
        api_response = api_instance.show_orders(orders_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling OrdersApi->show_orders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_id** | **str**| UUID of the order |

### Return type

[**Orders**](Orders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the instance of the order |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | order is not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_orders**
> Orders update_orders(orders_id, update_orders)

Updates orders

All fields sent in this request will be set on the orders referenced

### Example


```python
import time
import internal_client
from internal_client.api import orders_api
from internal_client.model.orders import Orders
from internal_client.model.create_update_orders import CreateUpdateOrders
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    orders_id = "ordersId_example" # str | UUID of the orders model
    update_orders = CreateUpdateOrders(
        service_member_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        issue_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        report_by_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        orders_type=OrdersType("PERMANENT_CHANGE_OF_STATION"),
        orders_type_detail=OrdersTypeDetail("HHG_PERMITTED"),
        has_dependents=True,
        spouse_has_pro_gear=True,
        new_duty_station_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        orders_number="030-00362",
        tac="F8J1",
        sac="N002214CSW32Y9",
        department_indicator=DeptIndicator("NAVY_AND_MARINES"),
    ) # CreateUpdateOrders | 

    # example passing only required values which don't have defaults set
    try:
        # Updates orders
        api_response = api_instance.update_orders(orders_id, update_orders)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling OrdersApi->update_orders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_id** | **str**| UUID of the orders model |
 **update_orders** | [**CreateUpdateOrders**](CreateUpdateOrders.md)|  |

### Return type

[**Orders**](Orders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of orders |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | orders not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_amended_orders**
> UploadPayload upload_amended_orders(orders_id, file)

Patch the amended orders for a given order

Patch the amended orders for a given order

### Example


```python
import time
import internal_client
from internal_client.api import orders_api
from internal_client.model.invalid_request_response_payload import InvalidRequestResponsePayload
from internal_client.model.upload_payload import UploadPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = orders_api.OrdersApi(api_client)
    orders_id = "ordersId_example" # str | UUID of the order
    file = open('/path/to/file', 'rb') # file_type | The file to upload.

    # example passing only required values which don't have defaults set
    try:
        # Patch the amended orders for a given order
        api_response = api_instance.upload_amended_orders(orders_id, file)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling OrdersApi->upload_amended_orders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_id** | **str**| UUID of the order |
 **file** | **file_type**| The file to upload. |

### Return type

[**UploadPayload**](UploadPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created upload |  -  |
**400** | invalid request |  -  |
**403** | not authorized |  -  |
**404** | not found |  -  |
**413** | payload is too large |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

