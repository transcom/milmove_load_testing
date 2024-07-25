# ghc_client.ApplicationParametersApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_param**](ApplicationParametersApi.md#get_param) | **GET** /application_parameters/{parameterName} | Searches for an application parameter by name, returns nil if not found


# **get_param**
> ApplicationParameters get_param(parameter_name)

Searches for an application parameter by name, returns nil if not found

Searches for an application parameter by name, returns nil if not found

### Example


```python
import time
import ghc_client
from ghc_client.api import application_parameters_api
from ghc_client.model.application_parameters import ApplicationParameters
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_parameters_api.ApplicationParametersApi(api_client)
    parameter_name = "parameterName_example" # str | Parameter Name

    # example passing only required values which don't have defaults set
    try:
        # Searches for an application parameter by name, returns nil if not found
        api_response = api_instance.get_param(parameter_name)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ApplicationParametersApi->get_param: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_name** | **str**| Parameter Name |

### Return type

[**ApplicationParameters**](ApplicationParameters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application Parameters |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

