# internal_client.TransportationOfficesApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_duty_location_transportation_office**](TransportationOfficesApi.md#show_duty_location_transportation_office) | **GET** /duty_locations/{dutyLocationId}/transportation_office | Returns the transportation office for a given duty location


# **show_duty_location_transportation_office**
> TransportationOffice show_duty_location_transportation_office(duty_location_id)

Returns the transportation office for a given duty location

Returns the given duty location's transportation office

### Example


```python
import time
import internal_client
from internal_client.api import transportation_offices_api
from internal_client.model.transportation_office import TransportationOffice
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transportation_offices_api.TransportationOfficesApi(api_client)
    duty_location_id = "dutyLocationId_example" # str | UUID of the duty location

    # example passing only required values which don't have defaults set
    try:
        # Returns the transportation office for a given duty location
        api_response = api_instance.show_duty_location_transportation_office(duty_location_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling TransportationOfficesApi->show_duty_location_transportation_office: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duty_location_id** | **str**| UUID of the duty location |

### Return type

[**TransportationOffice**](TransportationOffice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the instance of the transportation office for a duty location |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | transportation office not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

