# prime_client.MoveTaskOrderApi

All URIs are relative to */prime/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_excess_weight_record**](MoveTaskOrderApi.md#create_excess_weight_record) | **POST** /move-task-orders/{moveTaskOrderID}/excess-weight-record | createExcessWeightRecord
[**download_move_order**](MoveTaskOrderApi.md#download_move_order) | **GET** /moves/{locator}/order/download | Downloads move order as a PDF
[**get_move_task_order**](MoveTaskOrderApi.md#get_move_task_order) | **GET** /move-task-orders/{moveID} | getMoveTaskOrder
[**list_moves**](MoveTaskOrderApi.md#list_moves) | **GET** /moves | listMoves
[**update_mto_post_counseling_information**](MoveTaskOrderApi.md#update_mto_post_counseling_information) | **PATCH** /move-task-orders/{moveTaskOrderID}/post-counseling-info | updateMTOPostCounselingInformation


# **create_excess_weight_record**
> ExcessWeightRecord create_excess_weight_record(move_task_order_id, file)

createExcessWeightRecord

Uploads an excess weight record, which is a document that proves that the movers or contractors have counseled the customer about their excess weight. Excess weight counseling should occur after the sum of the shipments for the customer's move crosses the excess weight alert threshold. 

### Example


```python
import time
import prime_client
from prime_client.api import move_task_order_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from prime_client.model.excess_weight_record import ExcessWeightRecord
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_task_order_api.MoveTaskOrderApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | UUID of the move being updated.
    file = open('/path/to/file', 'rb') # file_type | The file to upload.

    # example passing only required values which don't have defaults set
    try:
        # createExcessWeightRecord
        api_response = api_instance.create_excess_weight_record(move_task_order_id, file)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MoveTaskOrderApi->create_excess_weight_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| UUID of the move being updated. |
 **file** | **file_type**| The file to upload. |

### Return type

[**ExcessWeightRecord**](ExcessWeightRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully uploaded the excess weight record file. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_move_order**
> file_type download_move_order(locator)

Downloads move order as a PDF

### Functionality This endpoint downloads all uploaded move order documentations into one download file by locator.  ### Errors * The move must be in need counseling state. * The move client's origin duty location must not currently have gov counseling. 

### Example


```python
import time
import prime_client
from prime_client.api import move_task_order_api
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
    api_instance = move_task_order_api.MoveTaskOrderApi(api_client)
    locator = "locator_example" # str | the locator code for move order to be downloaded

    # example passing only required values which don't have defaults set
    try:
        # Downloads move order as a PDF
        api_response = api_instance.download_move_order(locator)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MoveTaskOrderApi->download_move_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**| the locator code for move order to be downloaded |

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Move Order PDF |  * Content-Disposition - File name to download <br>  |
**400** | The request payload is invalid. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_move_task_order**
> MoveTaskOrder get_move_task_order(move_id)

getMoveTaskOrder

### Functionality This endpoint gets an individual MoveTaskOrder by ID.  It will provide information about the Customer and any associated MTOShipments, MTOServiceItems and PaymentRequests. 

### Example


```python
import time
import prime_client
from prime_client.api import move_task_order_api
from prime_client.model.move_task_order import MoveTaskOrder
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
    api_instance = move_task_order_api.MoveTaskOrderApi(api_client)
    move_id = "moveID_example" # str | UUID or MoveCode of move task order to use.

    # example passing only required values which don't have defaults set
    try:
        # getMoveTaskOrder
        api_response = api_instance.get_move_task_order(move_id)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MoveTaskOrderApi->get_move_task_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID or MoveCode of move task order to use. |

### Return type

[**MoveTaskOrder**](MoveTaskOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieve an individual move task order. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_moves**
> ListMoves list_moves()

listMoves

Gets all moves that have been reviewed and approved by the TOO. The `since` parameter can be used to filter this list down to only the moves that have been updated since the provided timestamp. A move will be considered updated if the `updatedAt` timestamp on the move or on its orders, shipments, service items, or payment requests, is later than the provided date and time.  **WIP**: Include what causes moves to leave this list. Currently, once the `availableToPrimeAt` timestamp has been set, that move will always appear in this list. 

### Example


```python
import time
import prime_client
from prime_client.api import move_task_order_api
from prime_client.model.list_moves import ListMoves
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
    api_instance = move_task_order_api.MoveTaskOrderApi(api_client)
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only return moves updated since this time. Formatted like \"2021-07-23T18:30:47.116Z\" (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # listMoves
        api_response = api_instance.list_moves(since=since)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MoveTaskOrderApi->list_moves: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**| Only return moves updated since this time. Formatted like \&quot;2021-07-23T18:30:47.116Z\&quot; | [optional]

### Return type

[**ListMoves**](ListMoves.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved moves. A successful fetch might still return zero moves. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_post_counseling_information**
> MoveTaskOrder update_mto_post_counseling_information(move_task_order_id, if_match)

updateMTOPostCounselingInformation

### Functionality This endpoint **updates** the MoveTaskOrder to indicate that the Prime has completed Counseling. This update uses the moveTaskOrderID provided in the path, updates the move status and marks child elements of the move to indicate the update. No body object is expected for this request.  **For Full/Partial PPMs**: This action is required so that the customer can start uploading their proof of service docs.  **For other move types**: This action is required for auditing reasons so that we have a record of when the Prime counseled the customer. 

### Example


```python
import time
import prime_client
from prime_client.api import move_task_order_api
from prime_client.model.move_task_order import MoveTaskOrder
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
    api_instance = move_task_order_api.MoveTaskOrderApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move task order to use.
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 

    # example passing only required values which don't have defaults set
    try:
        # updateMTOPostCounselingInformation
        api_response = api_instance.update_mto_post_counseling_information(move_task_order_id, if_match)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MoveTaskOrderApi->update_mto_post_counseling_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move task order to use. |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |

### Return type

[**MoveTaskOrder**](MoveTaskOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated move task order with post counseling information. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

