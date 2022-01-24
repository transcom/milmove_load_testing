# internal_client.AddressesApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_address**](AddressesApi.md#show_address) | **GET** /addresses/{addressId} | Returns an address


# **show_address**
> Address show_address(address_id)

Returns an address

Returns an address

### Example


```python
import time
import internal_client
from internal_client.api import addresses_api
from internal_client.model.address import Address
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    address_id = "addressId_example" # str | UUID of the address to return

    # example passing only required values which don't have defaults set
    try:
        # Returns an address
        api_response = api_instance.show_address(address_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling AddressesApi->show_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **str**| UUID of the address to return |

### Return type

[**Address**](Address.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the requested address |  -  |
**400** | invalid request |  -  |
**403** | not authorized |  -  |
**404** | not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

