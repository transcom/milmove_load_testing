# internal_client.CalendarApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_available_move_dates**](CalendarApi.md#show_available_move_dates) | **GET** /calendar/available_move_dates | Returns available dates for the move calendar


# **show_available_move_dates**
> AvailableMoveDates show_available_move_dates(start_date)

Returns available dates for the move calendar

Returns available dates for the move calendar

### Example


```python
import time
import internal_client
from internal_client.api import calendar_api
from internal_client.model.available_move_dates import AvailableMoveDates
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = calendar_api.CalendarApi(api_client)
    start_date = dateutil_parser('1970-01-01').date() # date | Look for future available dates starting from (and including) this date

    # example passing only required values which don't have defaults set
    try:
        # Returns available dates for the move calendar
        api_response = api_instance.show_available_move_dates(start_date)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling CalendarApi->show_available_move_dates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Look for future available dates starting from (and including) this date |

### Return type

[**AvailableMoveDates**](AvailableMoveDates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available dates |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

