# internal_client.DocumentsApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document**](DocumentsApi.md#create_document) | **POST** /documents | Create a new document
[**show_document**](DocumentsApi.md#show_document) | **GET** /documents/{documentId} | Returns a document


# **create_document**
> DocumentPayload create_document(document_payload)

Create a new document

Documents represent a physical artifact such as a scanned document or a PDF file

### Example


```python
import time
import internal_client
from internal_client.api import documents_api
from internal_client.model.post_document_payload import PostDocumentPayload
from internal_client.model.document_payload import DocumentPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    document_payload = PostDocumentPayload(
        service_member_id="service_member_id_example",
    ) # PostDocumentPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new document
        api_response = api_instance.create_document(document_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling DocumentsApi->create_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_payload** | [**PostDocumentPayload**](PostDocumentPayload.md)|  |

### Return type

[**DocumentPayload**](DocumentPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created document |  -  |
**400** | invalid request |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_document**
> DocumentPayload show_document(document_id)

Returns a document

Returns a document and its uploads

### Example


```python
import time
import internal_client
from internal_client.api import documents_api
from internal_client.model.invalid_request_response_payload import InvalidRequestResponsePayload
from internal_client.model.document_payload import DocumentPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    document_id = "documentId_example" # str | UUID of the document to return

    # example passing only required values which don't have defaults set
    try:
        # Returns a document
        api_response = api_instance.show_document(document_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling DocumentsApi->show_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| UUID of the document to return |

### Return type

[**DocumentPayload**](DocumentPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the requested document |  -  |
**400** | invalid request |  -  |
**403** | not authorized |  -  |
**404** | not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

