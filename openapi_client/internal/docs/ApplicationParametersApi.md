# internal_client.ApplicationParametersApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate**](ApplicationParametersApi.md#validate) | **POST** /application_parameters | Searches for an application parameter by name and value, returns nil if not found


# **validate**
> ApplicationParameters validate(body)

Searches for an application parameter by name and value, returns nil if not found

Searches for an application parameter by name and value, returns nil if not found

### Example


```python
import time
import internal_client
from internal_client.api import application_parameters_api
from internal_client.model.application_parameters import ApplicationParameters
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = application_parameters_api.ApplicationParametersApi(api_client)
    body = ApplicationParameters(
        validation_code="validation_code_example",
        parameter_name="parameter_name_example",
        parameter_value="parameter_value_example",
    ) # ApplicationParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Searches for an application parameter by name and value, returns nil if not found
        api_response = api_instance.validate(body)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling ApplicationParametersApi->validate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationParameters**](ApplicationParameters.md)|  |

### Return type

[**ApplicationParameters**](ApplicationParameters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application Parameters |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

