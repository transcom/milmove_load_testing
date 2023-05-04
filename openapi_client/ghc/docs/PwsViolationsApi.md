# ghc_client.PwsViolationsApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pws_violations**](PwsViolationsApi.md#get_pws_violations) | **GET** /pws-violations | Fetch the possible PWS violations for an evaluation report


# **get_pws_violations**
> PWSViolations get_pws_violations()

Fetch the possible PWS violations for an evaluation report

Fetch the possible PWS violations for an evaluation report

### Example


```python
import time
import ghc_client
from ghc_client.api import pws_violations_api
from ghc_client.model.error import Error
from ghc_client.model.pws_violations import PWSViolations
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pws_violations_api.PwsViolationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch the possible PWS violations for an evaluation report
        api_response = api_instance.get_pws_violations()
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PwsViolationsApi->get_pws_violations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PWSViolations**](PWSViolations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the PWS violations |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

