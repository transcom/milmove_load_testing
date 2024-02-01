# internal_client.OfficeApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_move**](OfficeApi.md#approve_move) | **POST** /moves/{moveId}/approve | Approves a move to proceed
[**approve_reimbursement**](OfficeApi.md#approve_reimbursement) | **POST** /reimbursement/{reimbursementId}/approve | Approves the reimbursement
[**cancel_move**](OfficeApi.md#cancel_move) | **POST** /moves/{moveId}/cancel | Cancels a move
[**show_office_orders**](OfficeApi.md#show_office_orders) | **GET** /moves/{moveId}/orders | Returns orders information for a move for office use


# **approve_move**
> MovePayload approve_move(move_id)

Approves a move to proceed

Approves the basic details of a move. The status of the move will be updated to APPROVED

### Example


```python
import time
import internal_client
from internal_client.api import office_api
from internal_client.model.move_payload import MovePayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = office_api.OfficeApi(api_client)
    move_id = "moveId_example" # str | UUID of the move

    # example passing only required values which don't have defaults set
    try:
        # Approves a move to proceed
        api_response = api_instance.approve_move(move_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling OfficeApi->approve_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |

### Return type

[**MovePayload**](MovePayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns updated (approved) move object |  -  |
**400** | invalid request |  -  |
**401** | must be authenticated to use this endpoint |  -  |
**403** | not authorized to approve this move |  -  |
**409** | the move is not in a state to be approved |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_reimbursement**
> Reimbursement approve_reimbursement(reimbursement_id)

Approves the reimbursement

Sets the status of the reimbursement to APPROVED.

### Example


```python
import time
import internal_client
from internal_client.api import office_api
from internal_client.model.reimbursement import Reimbursement
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = office_api.OfficeApi(api_client)
    reimbursement_id = "reimbursementId_example" # str | UUID of the reimbursement being approved

    # example passing only required values which don't have defaults set
    try:
        # Approves the reimbursement
        api_response = api_instance.approve_reimbursement(reimbursement_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling OfficeApi->approve_reimbursement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reimbursement_id** | **str**| UUID of the reimbursement being approved |

### Return type

[**Reimbursement**](Reimbursement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of reimbursement |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_move**
> MovePayload cancel_move(move_id, cancel_move)

Cancels a move

Cancels the basic details of a move. The status of the move will be updated to CANCELED

### Example


```python
import time
import internal_client
from internal_client.api import office_api
from internal_client.model.cancel_move import CancelMove
from internal_client.model.move_payload import MovePayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = office_api.OfficeApi(api_client)
    move_id = "moveId_example" # str | UUID of the move
    cancel_move = CancelMove(
        cancel_reason="Change of orders",
    ) # CancelMove | 

    # example passing only required values which don't have defaults set
    try:
        # Cancels a move
        api_response = api_instance.cancel_move(move_id, cancel_move)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling OfficeApi->cancel_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |
 **cancel_move** | [**CancelMove**](CancelMove.md)|  |

### Return type

[**MovePayload**](MovePayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns updated (canceled) move object |  -  |
**400** | invalid request |  -  |
**401** | must be authenticated to use this endpoint |  -  |
**403** | not authorized to cancel this move |  -  |
**409** | the move is not in a state to be canceled |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_office_orders**
> Orders show_office_orders(move_id)

Returns orders information for a move for office use

Returns orders information for a move for office use

### Example


```python
import time
import internal_client
from internal_client.api import office_api
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
    api_instance = office_api.OfficeApi(api_client)
    move_id = "moveId_example" # str | UUID of the move

    # example passing only required values which don't have defaults set
    try:
        # Returns orders information for a move for office use
        api_response = api_instance.show_office_orders(move_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling OfficeApi->show_office_orders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |

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
**200** | the orders information for a move for office use |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | move not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

