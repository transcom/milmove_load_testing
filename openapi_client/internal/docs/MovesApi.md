# internal_client.MovesApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_move**](MovesApi.md#patch_move) | **PATCH** /moves/{moveId} | Patches the move
[**show_move**](MovesApi.md#show_move) | **GET** /moves/{moveId} | Returns the given move
[**show_move_dates_summary**](MovesApi.md#show_move_dates_summary) | **GET** /moves/{moveId}/move_dates_summary | Returns projected move-related dates for a given move date
[**show_shipment_summary_worksheet**](MovesApi.md#show_shipment_summary_worksheet) | **GET** /moves/{moveId}/shipment_summary_worksheet | Returns Shipment Summary Worksheet
[**submit_amended_orders**](MovesApi.md#submit_amended_orders) | **POST** /moves/{moveId}/submit_amended_orders | Submits amended orders for review
[**submit_move_for_approval**](MovesApi.md#submit_move_for_approval) | **POST** /moves/{moveId}/submit | Submits a move for approval


# **patch_move**
> MovePayload patch_move(move_id, patch_move_payload)

Patches the move

Any fields sent in this request will be set on the move referenced

### Example


```python
import time
import internal_client
from internal_client.api import moves_api
from internal_client.model.patch_move_payload import PatchMovePayload
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
    api_instance = moves_api.MovesApi(api_client)
    move_id = "moveId_example" # str | UUID of the move
    patch_move_payload = PatchMovePayload(
        selected_move_type=SelectedMoveType("HHG"),
    ) # PatchMovePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Patches the move
        api_response = api_instance.patch_move(move_id, patch_move_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MovesApi->patch_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |
 **patch_move_payload** | [**PatchMovePayload**](PatchMovePayload.md)|  |

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
**201** | updated instance of move |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | move is not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_move**
> MovePayload show_move(move_id)

Returns the given move

Returns the given move

### Example


```python
import time
import internal_client
from internal_client.api import moves_api
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
    api_instance = moves_api.MovesApi(api_client)
    move_id = "moveId_example" # str | UUID of the move

    # example passing only required values which don't have defaults set
    try:
        # Returns the given move
        api_response = api_instance.show_move(move_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MovesApi->show_move: %s\n" % e)
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
**200** | the instance of the move |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | move is not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_move_dates_summary**
> MoveDatesSummary show_move_dates_summary(move_id, move_date)

Returns projected move-related dates for a given move date

Returns projected move-related dates for a given move date

### Example


```python
import time
import internal_client
from internal_client.api import moves_api
from internal_client.model.move_dates_summary import MoveDatesSummary
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moves_api.MovesApi(api_client)
    move_id = "moveId_example" # str | UUID of the move
    move_date = dateutil_parser('1970-01-01').date() # date | The chosen move date

    # example passing only required values which don't have defaults set
    try:
        # Returns projected move-related dates for a given move date
        api_response = api_instance.show_move_dates_summary(move_id, move_date)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MovesApi->show_move_dates_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |
 **move_date** | **date**| The chosen move date |

### Return type

[**MoveDatesSummary**](MoveDatesSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of projected move-related dates |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_shipment_summary_worksheet**
> file_type show_shipment_summary_worksheet(move_id, preparation_date)

Returns Shipment Summary Worksheet

Generates pre-filled PDF using data already collected

### Example


```python
import time
import internal_client
from internal_client.api import moves_api
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = moves_api.MovesApi(api_client)
    move_id = "moveId_example" # str | UUID of the move
    preparation_date = dateutil_parser('1970-01-01').date() # date | The preparationDate of PDF

    # example passing only required values which don't have defaults set
    try:
        # Returns Shipment Summary Worksheet
        api_response = api_instance.show_shipment_summary_worksheet(move_id, preparation_date)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MovesApi->show_shipment_summary_worksheet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |
 **preparation_date** | **date**| The preparationDate of PDF |

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
**200** | Pre-filled worksheet PDF |  * Content-Disposition - File name to download <br>  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_amended_orders**
> MovePayload submit_amended_orders(move_id)

Submits amended orders for review

Submits amended orders for review by the office. The status of the move will be updated to an appropriate status depending on whether it needs services counseling or not.

### Example


```python
import time
import internal_client
from internal_client.api import moves_api
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
    api_instance = moves_api.MovesApi(api_client)
    move_id = "moveId_example" # str | UUID of the move

    # example passing only required values which don't have defaults set
    try:
        # Submits amended orders for review
        api_response = api_instance.submit_amended_orders(move_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MovesApi->submit_amended_orders: %s\n" % e)
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
**200** | returns updated (submitted) move object |  -  |
**400** | invalid request |  -  |
**401** | must be authenticated to use this endpoint |  -  |
**403** | not authorized to approve this move |  -  |
**409** | the move is not in a state to be approved |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_move_for_approval**
> MovePayload submit_move_for_approval(move_id, submit_move_for_approval_payload)

Submits a move for approval

Submits a move for approval by the office. The status of the move will be updated to SUBMITTED

### Example


```python
import time
import internal_client
from internal_client.api import moves_api
from internal_client.model.submit_move_for_approval_payload import SubmitMoveForApprovalPayload
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
    api_instance = moves_api.MovesApi(api_client)
    move_id = "moveId_example" # str | UUID of the move
    submit_move_for_approval_payload = SubmitMoveForApprovalPayload(
        certificate=CreateSignedCertificationPayload(
            date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            signature="signature_example",
            certification_text="certification_text_example",
            personally_procured_move_id="personally_procured_move_id_example",
            certification_type=SignedCertificationTypeCreate("PPM_PAYMENT"),
        ),
    ) # SubmitMoveForApprovalPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Submits a move for approval
        api_response = api_instance.submit_move_for_approval(move_id, submit_move_for_approval_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MovesApi->submit_move_for_approval: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |
 **submit_move_for_approval_payload** | [**SubmitMoveForApprovalPayload**](SubmitMoveForApprovalPayload.md)|  |

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
**200** | returns updated (submitted) move object |  -  |
**400** | invalid request |  -  |
**401** | must be authenticated to use this endpoint |  -  |
**403** | not authorized to approve this move |  -  |
**409** | the move is not in a state to be approved |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

