# internal_client.MovesApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_moves**](MovesApi.md#get_all_moves) | **GET** /allmoves/{serviceMemberId} | Return the current and previous moves of a service member
[**patch_move**](MovesApi.md#patch_move) | **PATCH** /moves/{moveId} | Patches the move
[**show_move**](MovesApi.md#show_move) | **GET** /moves/{moveId} | Returns the given move
[**submit_amended_orders**](MovesApi.md#submit_amended_orders) | **POST** /moves/{moveId}/submit_amended_orders | Submits amended orders for review
[**submit_move_for_approval**](MovesApi.md#submit_move_for_approval) | **POST** /moves/{moveId}/submit | Submits a move for approval
[**upload_additional_documents**](MovesApi.md#upload_additional_documents) | **PATCH** /moves/{moveId}/uploadAdditionalDocuments | Patch the additional documents for a given move


# **get_all_moves**
> MovesList get_all_moves(service_member_id)

Return the current and previous moves of a service member

This endpoint gets all moves that belongs to the serviceMember by using the service members id. In a previous moves array and the current move in the current move array. The current move is the move with the latest CreatedAt date. All other moves will go into the previous move array. 

### Example


```python
import time
import internal_client
from internal_client.api import moves_api
from internal_client.model.error import Error
from internal_client.model.moves_list import MovesList
from internal_client.model.client_error import ClientError
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
    service_member_id = "serviceMemberId_example" # str | UUID of the service member

    # example passing only required values which don't have defaults set
    try:
        # Return the current and previous moves of a service member
        api_response = api_instance.get_all_moves(service_member_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MovesApi->get_all_moves: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_member_id** | **str**| UUID of the service member |

### Return type

[**MovesList**](MovesList.md)

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

# **patch_move**
> MovePayload patch_move(move_id, if_match, patch_move_payload)

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
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    patch_move_payload = PatchMovePayload(
        closeout_office_id="closeout_office_id_example",
    ) # PatchMovePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Patches the move
        api_response = api_instance.patch_move(move_id, if_match, patch_move_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MovesApi->patch_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
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
**200** | updated instance of move |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | move or closeout office is not found |  -  |
**412** | precondition failed |  -  |
**422** | unprocessable entity |  -  |
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
            ppm_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
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

# **upload_additional_documents**
> Upload upload_additional_documents(move_id, file)

Patch the additional documents for a given move

Customers will on occaision need the ability to upload additional supporting documents, for a variety of reasons. This does not include amended order.

### Example


```python
import time
import internal_client
from internal_client.api import moves_api
from internal_client.model.invalid_request_response_payload import InvalidRequestResponsePayload
from internal_client.model.upload import Upload
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
    move_id = "moveId_example" # str | UUID of the order
    file = open('/path/to/file', 'rb') # file_type | The file to upload.

    # example passing only required values which don't have defaults set
    try:
        # Patch the additional documents for a given move
        api_response = api_instance.upload_additional_documents(move_id, file)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MovesApi->upload_additional_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the order |
 **file** | **file_type**| The file to upload. |

### Return type

[**Upload**](Upload.md)

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

