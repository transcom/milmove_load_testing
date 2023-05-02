# internal_client.MoveDocsApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_generic_move_document**](MoveDocsApi.md#create_generic_move_document) | **POST** /moves/{moveId}/move_documents | Creates a move document
[**create_weight_ticket_document**](MoveDocsApi.md#create_weight_ticket_document) | **POST** /moves/{moveId}/weight_ticket | Creates a weight ticket document
[**delete_move_document**](MoveDocsApi.md#delete_move_document) | **DELETE** /move_documents/{moveDocumentId} | Deletes a move document
[**index_move_documents**](MoveDocsApi.md#index_move_documents) | **GET** /moves/{moveId}/move_documents | Returns a list of all Move Documents associated with this move
[**update_move_document**](MoveDocsApi.md#update_move_document) | **PUT** /move_documents/{moveDocumentId} | Updates a move document


# **create_generic_move_document**
> MoveDocumentPayload create_generic_move_document(move_id, create_generic_move_document_payload)

Creates a move document

Created a move document with the given information

### Example


```python
import time
import internal_client
from internal_client.api import move_docs_api
from internal_client.model.move_document_payload import MoveDocumentPayload
from internal_client.model.create_generic_move_document_payload import CreateGenericMoveDocumentPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_docs_api.MoveDocsApi(api_client)
    move_id = "moveId_example" # str | UUID of the move
    create_generic_move_document_payload = CreateGenericMoveDocumentPayload(
        personally_procured_move_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        upload_ids=[
            "c56a4180-65aa-42ec-a945-5fd21dec0538",
        ],
        title="very_useful_document.pdf",
        move_document_type=MoveDocumentType("EXPENSE"),
        notes="This document is good to go!",
    ) # CreateGenericMoveDocumentPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a move document
        api_response = api_instance.create_generic_move_document(move_id, create_generic_move_document_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MoveDocsApi->create_generic_move_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |
 **create_generic_move_document_payload** | [**CreateGenericMoveDocumentPayload**](CreateGenericMoveDocumentPayload.md)|  |

### Return type

[**MoveDocumentPayload**](MoveDocumentPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns new move document object |  -  |
**400** | invalid request |  -  |
**401** | must be authenticated to use this endpoint |  -  |
**403** | not authorized to modify this move |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_weight_ticket_document**
> MoveDocumentPayload create_weight_ticket_document(move_id, create_weight_ticket_document)

Creates a weight ticket document

Created a weight ticket document with the given information

### Example


```python
import time
import internal_client
from internal_client.api import move_docs_api
from internal_client.model.create_weight_ticket_documents_payload import CreateWeightTicketDocumentsPayload
from internal_client.model.move_document_payload import MoveDocumentPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_docs_api.MoveDocsApi(api_client)
    move_id = "moveId_example" # str | UUID of the move
    create_weight_ticket_document = CreateWeightTicketDocumentsPayload(
        personally_procured_move_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        upload_ids=[
            "c56a4180-65aa-42ec-a945-5fd21dec0538",
        ],
        weight_ticket_set_type=WeightTicketSetType("CAR"),
        vehicle_nickname="vehicle_nickname_example",
        vehicle_make="vehicle_make_example",
        vehicle_model="vehicle_model_example",
        empty_weight_ticket_missing=True,
        empty_weight=0,
        full_weight_ticket_missing=True,
        full_weight=0,
        weight_ticket_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        trailer_ownership_missing=True,
    ) # CreateWeightTicketDocumentsPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a weight ticket document
        api_response = api_instance.create_weight_ticket_document(move_id, create_weight_ticket_document)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MoveDocsApi->create_weight_ticket_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |
 **create_weight_ticket_document** | [**CreateWeightTicketDocumentsPayload**](CreateWeightTicketDocumentsPayload.md)|  |

### Return type

[**MoveDocumentPayload**](MoveDocumentPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns new weight ticket document object |  -  |
**400** | invalid request |  -  |
**401** | must be authenticated to use this endpoint |  -  |
**403** | not authorized to modify this move |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_move_document**
> delete_move_document(move_document_id)

Deletes a move document

Deletes a move document with the given information

### Example


```python
import time
import internal_client
from internal_client.api import move_docs_api
from internal_client.model.invalid_request_response_payload import InvalidRequestResponsePayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_docs_api.MoveDocsApi(api_client)
    move_document_id = "moveDocumentId_example" # str | UUID of the move document model

    # example passing only required values which don't have defaults set
    try:
        # Deletes a move document
        api_instance.delete_move_document(move_document_id)
    except internal_client.ApiException as e:
        print("Exception when calling MoveDocsApi->delete_move_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_document_id** | **str**| UUID of the move document model |

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
**204** | deleted |  -  |
**400** | invalid request |  -  |
**403** | not authorized |  -  |
**404** | not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_move_documents**
> MoveDocuments index_move_documents(move_id)

Returns a list of all Move Documents associated with this move

Returns a list of all Move Documents associated with this move

### Example


```python
import time
import internal_client
from internal_client.api import move_docs_api
from internal_client.model.move_documents import MoveDocuments
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_docs_api.MoveDocsApi(api_client)
    move_id = "moveId_example" # str | UUID of the move

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of all Move Documents associated with this move
        api_response = api_instance.index_move_documents(move_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MoveDocsApi->index_move_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |

### Return type

[**MoveDocuments**](MoveDocuments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns list of move douments |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_move_document**
> MoveDocumentPayload update_move_document(move_document_id, update_move_document)

Updates a move document

Update a move document with the given information

### Example


```python
import time
import internal_client
from internal_client.api import move_docs_api
from internal_client.model.move_document_payload import MoveDocumentPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_docs_api.MoveDocsApi(api_client)
    move_document_id = "moveDocumentId_example" # str | UUID of the move document model
    update_move_document = MoveDocumentPayload(
        id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        move_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        personally_procured_move_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        document=Document(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            service_member_id="service_member_id_example",
            uploads=[
                Upload(
                ),
            ],
        ),
        title="very_useful_document.pdf",
        move_document_type=MoveDocumentType("EXPENSE"),
        status=MoveDocumentStatus("AWAITING_REVIEW"),
        notes="This document is good to go!",
        moving_expense_type=MovingExpenseType("CONTRACTED_EXPENSE"),
        requested_amount_cents=1,
        payment_method="OTHER",
        receipt_missing=True,
        weight_ticket_set_type=WeightTicketSetType("CAR"),
        vehicle_nickname="vehicle_nickname_example",
        vehicle_make="vehicle_make_example",
        vehicle_model="vehicle_model_example",
        empty_weight=0,
        empty_weight_ticket_missing=True,
        full_weight=0,
        full_weight_ticket_missing=True,
        weight_ticket_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        trailer_ownership_missing=True,
        storage_start_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        storage_end_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
    ) # MoveDocumentPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a move document
        api_response = api_instance.update_move_document(move_document_id, update_move_document)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MoveDocsApi->update_move_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_document_id** | **str**| UUID of the move document model |
 **update_move_document** | [**MoveDocumentPayload**](MoveDocumentPayload.md)|  |

### Return type

[**MoveDocumentPayload**](MoveDocumentPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of move document |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | move document not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

