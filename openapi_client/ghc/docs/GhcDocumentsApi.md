# ghc_client.GhcDocumentsApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document**](GhcDocumentsApi.md#create_document) | **POST** /documents | Create a new document
[**get_document**](GhcDocumentsApi.md#get_document) | **GET** /documents/{documentId} | Returns a document


# **create_document**
> Document create_document(document_payload)

Create a new document

Documents represent a physical artifact such as a scanned document or a PDF file

### Example


```python
import time
import ghc_client
from ghc_client.api import ghc_documents_api
from ghc_client.model.error import Error
from ghc_client.model.document import Document
from ghc_client.model.post_document_payload import PostDocumentPayload
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ghc_documents_api.GhcDocumentsApi(api_client)
    document_payload = PostDocumentPayload(
        service_member_id="service_member_id_example",
    ) # PostDocumentPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new document
        api_response = api_instance.create_document(document_payload)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling GhcDocumentsApi->create_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_payload** | [**PostDocumentPayload**](PostDocumentPayload.md)|  |

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created document |  -  |
**400** | invalid request |  -  |
**403** | The request was denied |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> Document get_document(document_id)

Returns a document

Returns a document and its uploads

### Example


```python
import time
import ghc_client
from ghc_client.api import ghc_documents_api
from ghc_client.model.error import Error
from ghc_client.model.document import Document
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
    api_instance = ghc_documents_api.GhcDocumentsApi(api_client)
    document_id = "documentId_example" # str | UUID of the document to return

    # example passing only required values which don't have defaults set
    try:
        # Returns a document
        api_response = api_instance.get_document(document_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling GhcDocumentsApi->get_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| UUID of the document to return |

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the requested document |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

