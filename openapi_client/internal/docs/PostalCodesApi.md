# internal_client.PostalCodesApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_postal_code_with_rate_data**](PostalCodesApi.md#validate_postal_code_with_rate_data) | **GET** /rate_engine_postal_codes/{postal_code} | Validate if a zipcode is valid for origin or destination location for a move.


# **validate_postal_code_with_rate_data**
> RateEnginePostalCodePayload validate_postal_code_with_rate_data(postal_code, postal_code_type)

Validate if a zipcode is valid for origin or destination location for a move.

Verifies if a zipcode is valid for origin or destination location for a move.

### Example


```python
import time
import internal_client
from internal_client.api import postal_codes_api
from internal_client.model.rate_engine_postal_code_payload import RateEnginePostalCodePayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = postal_codes_api.PostalCodesApi(api_client)
    postal_code = "48072" # str | 
    postal_code_type = "origin" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Validate if a zipcode is valid for origin or destination location for a move.
        api_response = api_instance.validate_postal_code_with_rate_data(postal_code, postal_code_type)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PostalCodesApi->validate_postal_code_with_rate_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postal_code** | **str**|  |
 **postal_code_type** | **str**|  |

### Return type

[**RateEnginePostalCodePayload**](RateEnginePostalCodePayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | postal_code is valid or invalid |  -  |
**400** | invalid request |  -  |
**401** | must be authenticated to use this endpoint |  -  |
**403** | user is not authorized |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

