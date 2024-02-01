# internal_client.OktaProfileApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_okta_info**](OktaProfileApi.md#show_okta_info) | **GET** /okta-profile | Returns Okta profile values from Okta&#39;s Users API
[**update_okta_info**](OktaProfileApi.md#update_okta_info) | **POST** /okta-profile | Update the user&#39;s okta profile with primary data, returns Okta profile values from the Okta&#39;s Users API reflecting updated values.


# **show_okta_info**
> OktaUserProfileData show_okta_info()

Returns Okta profile values from Okta's Users API

Calls a GET request to Okta's Users API and returns profile values that includes Okta data that the user provided upon registration or most recent profile update.

### Example


```python
import time
import internal_client
from internal_client.api import okta_profile_api
from internal_client.model.okta_user_profile_data import OktaUserProfileData
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = okta_profile_api.OktaProfileApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns Okta profile values from Okta's Users API
        api_response = api_instance.show_okta_info()
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling OktaProfileApi->show_okta_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OktaUserProfileData**](OktaUserProfileData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | okta profile for user |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | service member not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_okta_info**
> OktaUserProfileData update_okta_info(update_okta_user_profile_data)

Update the user's okta profile with primary data, returns Okta profile values from the Okta's Users API reflecting updated values.

Update the user's okta profile with primary data, returns Okta profile values from the Okta's Users API reflecting updated values.

### Example


```python
import time
import internal_client
from internal_client.api import okta_profile_api
from internal_client.model.okta_user_profile_data import OktaUserProfileData
from internal_client.model.update_okta_user_profile_data import UpdateOktaUserProfileData
from internal_client.model.errorunknown import ERRORUNKNOWN
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = okta_profile_api.OktaProfileApi(api_client)
    update_okta_user_profile_data = UpdateOktaUserProfileData(
        profile=OktaUserProfileData(
            sub="1duekdue9ekrjghf",
            login="user@email.com",
            email="user@email.com",
            first_name="John",
            last_name="Doe",
            cac_edipi="1234567890",
        ),
    ) # UpdateOktaUserProfileData | 

    # example passing only required values which don't have defaults set
    try:
        # Update the user's okta profile with primary data, returns Okta profile values from the Okta's Users API reflecting updated values.
        api_response = api_instance.update_okta_info(update_okta_user_profile_data)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling OktaProfileApi->update_okta_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_okta_user_profile_data** | [**UpdateOktaUserProfileData**](UpdateOktaUserProfileData.md)|  |

### Return type

[**OktaUserProfileData**](OktaUserProfileData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | okta profile for user |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**422** | validation error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

