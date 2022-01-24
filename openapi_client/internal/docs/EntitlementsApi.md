# internal_client.EntitlementsApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_entitlements**](EntitlementsApi.md#index_entitlements) | **GET** /entitlements | List weight weights allotted by entitlement
[**validate_entitlement**](EntitlementsApi.md#validate_entitlement) | **GET** /entitlements/{moveId} | Validates that the stored weight estimate is below the allotted entitlement range for a service member


# **index_entitlements**
> IndexEntitlements index_entitlements()

List weight weights allotted by entitlement

List weight weights allotted by entitlement

### Example


```python
import time
import internal_client
from internal_client.api import entitlements_api
from internal_client.model.index_entitlements import IndexEntitlements
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entitlements_api.EntitlementsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List weight weights allotted by entitlement
        api_response = api_instance.index_entitlements()
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling EntitlementsApi->index_entitlements: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**IndexEntitlements**](IndexEntitlements.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of weights allotted entitlement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_entitlement**
> validate_entitlement(move_id)

Validates that the stored weight estimate is below the allotted entitlement range for a service member

Determine whether weight estimate is below entitlement

### Example


```python
import time
import internal_client
from internal_client.api import entitlements_api
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entitlements_api.EntitlementsApi(api_client)
    move_id = "moveId_example" # str | UUID of the move

    # example passing only required values which don't have defaults set
    try:
        # Validates that the stored weight estimate is below the allotted entitlement range for a service member
        api_instance.validate_entitlement(move_id)
    except internal_client.ApiException as e:
        print("Exception when calling EntitlementsApi->validate_entitlement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | weight estimate is below allotted entitlement |  -  |
**404** | personally procured move not found |  -  |
**409** | Requested weight estimate is above allotted entitlement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

