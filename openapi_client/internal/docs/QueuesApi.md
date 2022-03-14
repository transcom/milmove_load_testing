# internal_client.QueuesApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_queue**](QueuesApi.md#show_queue) | **GET** /queues/{queueType} | Show all moves in a queue


# **show_queue**
> [MoveQueueItem] show_queue(queue_type)

Show all moves in a queue

Show all moves in a queue

### Example


```python
import time
import internal_client
from internal_client.api import queues_api
from internal_client.model.move_queue_item import MoveQueueItem
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = queues_api.QueuesApi(api_client)
    queue_type = "new" # str | Queue type to show

    # example passing only required values which don't have defaults set
    try:
        # Show all moves in a queue
        api_response = api_instance.show_queue(queue_type)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling QueuesApi->show_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_type** | **str**| Queue type to show |

### Return type

[**[MoveQueueItem]**](MoveQueueItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list all moves in the specified queue |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized to access this queue |  -  |
**404** | move queue item is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

