# ghc_client.UploadsApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_upload**](UploadsApi.md#create_upload) | **POST** /uploads | Create a new upload
[**delete_upload**](UploadsApi.md#delete_upload) | **DELETE** /uploads/{uploadID} | Deletes an upload


# **create_upload**
> Upload create_upload(file)

Create a new upload

Uploads represent a single digital file, such as a JPEG or PDF. Currently, office application uploads are only for Services Counselors to upload files for orders, but this may be expanded in the future.

### Example


```python
import time
import ghc_client
from ghc_client.api import uploads_api
from ghc_client.model.upload import Upload
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = uploads_api.UploadsApi(api_client)
    file = open('/path/to/file', 'rb') # file_type | The file to upload.
    document_id = "documentId_example" # str | UUID of the document to add an upload to (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new upload
        api_response = api_instance.create_upload(file)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling UploadsApi->create_upload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new upload
        api_response = api_instance.create_upload(file, document_id=document_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling UploadsApi->create_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**| The file to upload. |
 **document_id** | **str**| UUID of the document to add an upload to | [optional]

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

# **delete_upload**
> delete_upload(upload_id)

Deletes an upload

Uploads represent a single digital file, such as a JPEG or PDF.

### Example


```python
import time
import ghc_client
from ghc_client.api import uploads_api
from ghc_client.model.invalid_request_response_payload import InvalidRequestResponsePayload
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = uploads_api.UploadsApi(api_client)
    upload_id = "uploadID_example" # str | UUID of the upload to be deleted
    order_id = "orderID_example" # str | ID of the order that the upload belongs to (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes an upload
        api_instance.delete_upload(upload_id)
    except ghc_client.ApiException as e:
        print("Exception when calling UploadsApi->delete_upload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes an upload
        api_instance.delete_upload(upload_id, order_id=order_id)
    except ghc_client.ApiException as e:
        print("Exception when calling UploadsApi->delete_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| UUID of the upload to be deleted |
 **order_id** | **str**| ID of the order that the upload belongs to | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | deleted |  -  |
**400** | invalid request |  -  |
**403** | not authorized |  -  |
**404** | not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

