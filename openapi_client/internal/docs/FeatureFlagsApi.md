# internal_client.FeatureFlagsApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boolean_feature_flag_for_user**](FeatureFlagsApi.md#boolean_feature_flag_for_user) | **POST** /feature-flags/user-boolean/{key} | Determines if a user has a feature flag enabled
[**variant_feature_flag_for_user**](FeatureFlagsApi.md#variant_feature_flag_for_user) | **POST** /feature-flags/user-variant/{key} | Determines if a user has a feature flag enabled


# **boolean_feature_flag_for_user**
> FeatureFlagBoolean boolean_feature_flag_for_user(key, flag_context)

Determines if a user has a feature flag enabled

Determines if a user has a feature flag enabled. The flagContext contains context used to determine if this flag applies to the logged in user.

### Example


```python
import time
import internal_client
from internal_client.api import feature_flags_api
from internal_client.model.feature_flag_boolean import FeatureFlagBoolean
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    key = "key_example" # str | Feature Flag Key
    flag_context = {
        "key": "key_example",
    } # {str: (str,)} | context for the feature flag request

    # example passing only required values which don't have defaults set
    try:
        # Determines if a user has a feature flag enabled
        api_response = api_instance.boolean_feature_flag_for_user(key, flag_context)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling FeatureFlagsApi->boolean_feature_flag_for_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Feature Flag Key |
 **flag_context** | **{str: (str,)}**| context for the feature flag request |

### Return type

[**FeatureFlagBoolean**](FeatureFlagBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean Feature Flag Status |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variant_feature_flag_for_user**
> FeatureFlagVariant variant_feature_flag_for_user(key, flag_context)

Determines if a user has a feature flag enabled

Determines if a user has a feature flag enabled. The flagContext contains context used to determine if this flag applies to the logged in user.

### Example


```python
import time
import internal_client
from internal_client.api import feature_flags_api
from internal_client.model.feature_flag_variant import FeatureFlagVariant
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    key = "key_example" # str | Feature Flag Key
    flag_context = {
        "key": "key_example",
    } # {str: (str,)} | context for the feature flag request

    # example passing only required values which don't have defaults set
    try:
        # Determines if a user has a feature flag enabled
        api_response = api_instance.variant_feature_flag_for_user(key, flag_context)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling FeatureFlagsApi->variant_feature_flag_for_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Feature Flag Key |
 **flag_context** | **{str: (str,)}**| context for the feature flag request |

### Return type

[**FeatureFlagVariant**](FeatureFlagVariant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Variant Feature Flag Status |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

