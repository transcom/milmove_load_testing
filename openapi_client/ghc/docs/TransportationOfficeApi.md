# ghc_client.TransportationOfficeApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transportation_offices**](TransportationOfficeApi.md#get_transportation_offices) | **GET** /transportation-offices | Returns the transportation offices matching the search query


# **get_transportation_offices**
> TransportationOffices get_transportation_offices(search)

Returns the transportation offices matching the search query

Returns the transportation offices matching the search query

### Example


```python
import time
import ghc_client
from ghc_client.api import transportation_office_api
from ghc_client.model.transportation_offices import TransportationOffices
from ghc_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transportation_office_api.TransportationOfficeApi(api_client)
    search = "search_example" # str | Search string for transportation offices

    # example passing only required values which don't have defaults set
    try:
        # Returns the transportation offices matching the search query
        api_response = api_instance.get_transportation_offices(search)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling TransportationOfficeApi->get_transportation_offices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search string for transportation offices |

### Return type

[**TransportationOffices**](TransportationOffices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved transportation offices |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
