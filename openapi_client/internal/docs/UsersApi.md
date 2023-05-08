# internal_client.UsersApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**is_logged_in_user**](UsersApi.md#is_logged_in_user) | **GET** /users/is_logged_in | Returns boolean as to whether the user is logged in
[**show_logged_in_user**](UsersApi.md#show_logged_in_user) | **GET** /users/logged_in | Returns the user info for the currently logged in user


# **is_logged_in_user**
> IsLoggedInUser200Response is_logged_in_user()

Returns boolean as to whether the user is logged in

Returns boolean as to whether the user is logged in

### Example


```python
import time
import internal_client
from internal_client.api import users_api
from internal_client.model.is_logged_in_user200_response import IsLoggedInUser200Response
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns boolean as to whether the user is logged in
        api_response = api_instance.is_logged_in_user()
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling UsersApi->is_logged_in_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**IsLoggedInUser200Response**](IsLoggedInUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currently logged in user |  -  |
**400** | invalid request |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_logged_in_user**
> LoggedInUserPayload show_logged_in_user()

Returns the user info for the currently logged in user

Returns the user info for the currently logged in user

### Example


```python
import time
import internal_client
from internal_client.api import users_api
from internal_client.model.logged_in_user_payload import LoggedInUserPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the user info for the currently logged in user
        api_response = api_instance.show_logged_in_user()
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling UsersApi->show_logged_in_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LoggedInUserPayload**](LoggedInUserPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currently logged in user |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

