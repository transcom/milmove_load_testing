# internal_client.AccesscodeApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claim_access_code**](AccesscodeApi.md#claim_access_code) | **PATCH** /access_codes/invalid | Updates access code as invalid by associating it with the current service member.
[**fetch_access_code**](AccesscodeApi.md#fetch_access_code) | **GET** /access_codes | Fetches an access code
[**validate_access_code**](AccesscodeApi.md#validate_access_code) | **GET** /access_codes/valid | Validate if an access code has been unused and associated with the correct move type.


# **claim_access_code**
> AccessCode claim_access_code(access_code)

Updates access code as invalid by associating it with the current service member.

Updates access code as invalid by associating it with the current service member.

### Example


```python
import time
import internal_client
from internal_client.api import accesscode_api
from internal_client.model.inline_object import InlineObject
from internal_client.model.access_code import AccessCode
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = accesscode_api.AccesscodeApi(api_client)
    access_code = InlineObject(
        code="code_example",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Updates access code as invalid by associating it with the current service member.
        api_response = api_instance.claim_access_code(access_code)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling AccesscodeApi->claim_access_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_code** | [**InlineObject**](InlineObject.md)|  |

### Return type

[**AccessCode**](AccessCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | access code is invalid or valid |  -  |
**400** | invalid request |  -  |
**401** | not authorized to validate access code |  -  |
**404** | access code not found in system |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_access_code**
> AccessCode fetch_access_code()

Fetches an access code

Fetches the access code for a service member.

### Example


```python
import time
import internal_client
from internal_client.api import accesscode_api
from internal_client.model.access_code import AccessCode
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = accesscode_api.AccesscodeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetches an access code
        api_response = api_instance.fetch_access_code()
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling AccesscodeApi->fetch_access_code: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessCode**](AccessCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | access code has been found in system |  -  |
**400** | invalid request |  -  |
**401** | not authorized to fetch access code |  -  |
**404** | access code not found in system |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_access_code**
> AccessCode validate_access_code()

Validate if an access code has been unused and associated with the correct move type.

Verifies if access code is both unused and correctly associated with a move type.

### Example


```python
import time
import internal_client
from internal_client.api import accesscode_api
from internal_client.model.access_code import AccessCode
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = accesscode_api.AccesscodeApi(api_client)
    code = "PPM-8Q6ZGC" # str | the code the access code represents and verifies if in use (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Validate if an access code has been unused and associated with the correct move type.
        api_response = api_instance.validate_access_code(code=code)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling AccesscodeApi->validate_access_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| the code the access code represents and verifies if in use | [optional]

### Return type

[**AccessCode**](AccessCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | access code is invalid or valid |  -  |
**400** | invalid request |  -  |
**401** | not authorized to validate access code |  -  |
**404** | access code not found in system |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

