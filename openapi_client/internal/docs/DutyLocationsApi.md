# internal_client.DutyLocationsApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_duty_locations**](DutyLocationsApi.md#search_duty_locations) | **GET** /duty_locations | Returns the duty locations matching the search query


# **search_duty_locations**
> DutyLocationsPayload search_duty_locations(search)

Returns the duty locations matching the search query

Returns the duty locations matching the search query

### Example


```python
import time
import internal_client
from internal_client.api import duty_locations_api
from internal_client.model.duty_locations_payload import DutyLocationsPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = duty_locations_api.DutyLocationsApi(api_client)
    search = "search_example" # str | Search string for duty locations

    # example passing only required values which don't have defaults set
    try:
        # Returns the duty locations matching the search query
        api_response = api_instance.search_duty_locations(search)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling DutyLocationsApi->search_duty_locations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search string for duty locations |

### Return type

[**DutyLocationsPayload**](DutyLocationsPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the instance of the duty location |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | matching duty location not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

