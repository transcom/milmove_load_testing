# internal_client.DpsAuthApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cookie_url**](DpsAuthApi.md#get_cookie_url) | **POST** /dps_auth/cookie_url | Returns the URL to redirect to that begins DPS auth


# **get_cookie_url**
> DPSAuthCookieURLPayload get_cookie_url()

Returns the URL to redirect to that begins DPS auth

Returns the URL to redirect to that begins DPS auth

### Example


```python
import time
import internal_client
from internal_client.api import dps_auth_api
from internal_client.model.dps_auth_cookie_url_payload import DPSAuthCookieURLPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dps_auth_api.DpsAuthApi(api_client)
    cookie_name = "cookie_name_example" # str | The name of the cookie to set, DPS by default (optional)
    dps_redirect_url = "dps_redirect_url_example" # str | The DPS URL to redirec to (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the URL to redirect to that begins DPS auth
        api_response = api_instance.get_cookie_url(cookie_name=cookie_name, dps_redirect_url=dps_redirect_url)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling DpsAuthApi->get_cookie_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cookie_name** | **str**| The name of the cookie to set, DPS by default | [optional]
 **dps_redirect_url** | **str**| The DPS URL to redirec to | [optional]

### Return type

[**DPSAuthCookieURLPayload**](DPSAuthCookieURLPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | invalid request |  -  |
**403** | user is not authorized |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

