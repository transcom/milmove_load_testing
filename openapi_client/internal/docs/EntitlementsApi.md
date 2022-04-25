# internal_client.EntitlementsApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_entitlements**](EntitlementsApi.md#index_entitlements) | **GET** /entitlements | List weight weights allotted by entitlement


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

