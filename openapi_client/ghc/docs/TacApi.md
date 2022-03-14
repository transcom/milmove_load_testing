# ghc_client.TacApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tac_validation**](TacApi.md#tac_validation) | **GET** /tac/valid | Validation of a TAC value


# **tac_validation**
> TacValid tac_validation(tac)

Validation of a TAC value

Returns a boolean based on whether a tac value is valid or not

### Example


```python
import time
import ghc_client
from ghc_client.api import tac_api
from ghc_client.model.error import Error
from ghc_client.model.tac_valid import TacValid
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tac_api.TacApi(api_client)
    tac = "tac_example" # str | The tac value to validate

    # example passing only required values which don't have defaults set
    try:
        # Validation of a TAC value
        api_response = api_instance.tac_validation(tac)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling TacApi->tac_validation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tac** | **str**| The tac value to validate |

### Return type

[**TacValid**](TacValid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved validation status |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

