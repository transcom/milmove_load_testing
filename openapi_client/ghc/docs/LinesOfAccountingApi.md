# ghc_client.LinesOfAccountingApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_line_of_accounting**](LinesOfAccountingApi.md#request_line_of_accounting) | **POST** /lines-of-accounting | Fetch line of accounting


# **request_line_of_accounting**
> LineOfAccounting request_line_of_accounting(body)

Fetch line of accounting

Fetches a line of accounting based on provided service member affiliation, order issue date, and Transportation Accounting Code (TAC).

### Example


```python
import time
import ghc_client
from ghc_client.api import lines_of_accounting_api
from ghc_client.model.line_of_accounting import LineOfAccounting
from ghc_client.model.error import Error
from ghc_client.model.fetch_line_of_accounting_payload import FetchLineOfAccountingPayload
from ghc_client.model.validation_error import ValidationError
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lines_of_accounting_api.LinesOfAccountingApi(api_client)
    body = FetchLineOfAccountingPayload(
        service_member_affiliation=Affiliation("ARMY"),
        orders_issue_date=dateutil_parser('Sun Jan 01 00:00:00 UTC 2023').date(),
        tac_code="F8J1",
    ) # FetchLineOfAccountingPayload | Service member affiliation, order issue date, and TAC code.

    # example passing only required values which don't have defaults set
    try:
        # Fetch line of accounting
        api_response = api_instance.request_line_of_accounting(body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling LinesOfAccountingApi->request_line_of_accounting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FetchLineOfAccountingPayload**](FetchLineOfAccountingPayload.md)| Service member affiliation, order issue date, and TAC code. |

### Return type

[**LineOfAccounting**](LineOfAccounting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved line of accounting |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

