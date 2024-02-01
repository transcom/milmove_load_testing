# ghc_client.MtoServiceItemApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mto_service_item**](MtoServiceItemApi.md#get_mto_service_item) | **GET** /move-task-orders/{moveTaskOrderID}/service-items/{mtoServiceItemID} | Gets a line item by ID for a move by ID
[**list_mto_service_items**](MtoServiceItemApi.md#list_mto_service_items) | **GET** /move_task_orders/{moveTaskOrderID}/mto_service_items | Gets all line items for a move
[**update_mto_service_item_status**](MtoServiceItemApi.md#update_mto_service_item_status) | **PATCH** /move-task-orders/{moveTaskOrderID}/service-items/{mtoServiceItemID}/status | Change the status of a line item for a move by ID
[**update_service_item_sit_entry_date**](MtoServiceItemApi.md#update_service_item_sit_entry_date) | **PATCH** /service-item/{mtoServiceItemID}/entry-date-update | Updates a service item&#39;s SIT entry date by ID
[**update_sit_service_item_customer_expense**](MtoServiceItemApi.md#update_sit_service_item_customer_expense) | **PATCH** /shipments/{shipmentID}/sit-service-item/convert-to-customer-expense | Converts a SIT to customer expense


# **get_mto_service_item**
> MTOServiceItemSingle get_mto_service_item(move_task_order_id, mto_service_item_id)

Gets a line item by ID for a move by ID

Gets a line item by ID for a move by ID

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_service_item_api
from ghc_client.model.error import Error
from ghc_client.model.mto_service_item_single import MTOServiceItemSingle
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move to use
    mto_service_item_id = "mtoServiceItemID_example" # str | ID of line item to use

    # example passing only required values which don't have defaults set
    try:
        # Gets a line item by ID for a move by ID
        api_response = api_instance.get_mto_service_item(move_task_order_id, mto_service_item_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->get_mto_service_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move to use |
 **mto_service_item_id** | **str**| ID of line item to use |

### Return type

[**MTOServiceItemSingle**](MTOServiceItemSingle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved a line item for a move task order by ID |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mto_service_items**
> MTOServiceItems list_mto_service_items(move_task_order_id)

Gets all line items for a move

Gets all line items for a move

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_service_item_api
from ghc_client.model.error import Error
from ghc_client.model.mto_service_items import MTOServiceItems
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
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move for mto service item to use

    # example passing only required values which don't have defaults set
    try:
        # Gets all line items for a move
        api_response = api_instance.list_mto_service_items(move_task_order_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->list_mto_service_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move for mto service item to use |

### Return type

[**MTOServiceItems**](MTOServiceItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved all line items for a move task order |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_service_item_status**
> MTOServiceItem update_mto_service_item_status(move_task_order_id, mto_service_item_id, if_match, body)

Change the status of a line item for a move by ID

Changes the status of a line item for a move by ID

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_service_item_api
from ghc_client.model.error import Error
from ghc_client.model.mto_service_item import MTOServiceItem
from ghc_client.model.patch_mto_service_item_status_payload import PatchMTOServiceItemStatusPayload
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
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move to use
    mto_service_item_id = "mtoServiceItemID_example" # str | ID of line item to use
    if_match = "If-Match_example" # str | 
    body = PatchMTOServiceItemStatusPayload(
        status="SUBMITTED",
        rejection_reason="Insufficent details provided",
    ) # PatchMTOServiceItemStatusPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Change the status of a line item for a move by ID
        api_response = api_instance.update_mto_service_item_status(move_task_order_id, mto_service_item_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->update_mto_service_item_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move to use |
 **mto_service_item_id** | **str**| ID of line item to use |
 **if_match** | **str**|  |
 **body** | [**PatchMTOServiceItemStatusPayload**](PatchMTOServiceItemStatusPayload.md)|  |

### Return type

[**MTOServiceItem**](MTOServiceItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated status for a line item for a move task order by ID |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_item_sit_entry_date**
> MTOServiceItemSingle update_service_item_sit_entry_date(mto_service_item_id, body)

Updates a service item's SIT entry date by ID

Locates the service item in the database and updates the SIT entry date for the selected service item and returns the service item

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_service_item_api
from ghc_client.model.service_item_sit_entry_date import ServiceItemSitEntryDate
from ghc_client.model.error import Error
from ghc_client.model.mto_service_item_single import MTOServiceItemSingle
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
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    mto_service_item_id = "mtoServiceItemID_example" # str | ID of the service item
    body = ServiceItemSitEntryDate(
        id="1f2270c7-7166-40ae-981e-b200ebdf3054",
        sit_entry_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # ServiceItemSitEntryDate | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a service item's SIT entry date by ID
        api_response = api_instance.update_service_item_sit_entry_date(mto_service_item_id, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->update_service_item_sit_entry_date: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_service_item_id** | **str**| ID of the service item |
 **body** | [**ServiceItemSitEntryDate**](ServiceItemSitEntryDate.md)|  |

### Return type

[**MTOServiceItemSingle**](MTOServiceItemSingle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated SIT entry date |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sit_service_item_customer_expense**
> MTOShipment update_sit_service_item_customer_expense(shipment_id, if_match, body)

Converts a SIT to customer expense

Converts a SIT to customer expense

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_service_item_api
from ghc_client.model.error import Error
from ghc_client.model.update_sit_service_item_customer_expense import UpdateSITServiceItemCustomerExpense
from ghc_client.model.mto_shipment import MTOShipment
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
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    if_match = "If-Match_example" # str | 
    body = UpdateSITServiceItemCustomerExpense(
        convert_to_customer_expense=True,
        customer_expense_reason="Insufficent details provided",
    ) # UpdateSITServiceItemCustomerExpense | 

    # example passing only required values which don't have defaults set
    try:
        # Converts a SIT to customer expense
        api_response = api_instance.update_sit_service_item_customer_expense(shipment_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->update_sit_service_item_customer_expense: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |
 **if_match** | **str**|  |
 **body** | [**UpdateSITServiceItemCustomerExpense**](UpdateSITServiceItemCustomerExpense.md)|  |

### Return type

[**MTOShipment**](MTOShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully converted to customer expense |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

