# ghc_client.ReportViolationsApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associate_report_violations**](ReportViolationsApi.md#associate_report_violations) | **POST** /report-violations/{reportID} | Associate violations with an evaluation report
[**get_report_violations_by_report_id**](ReportViolationsApi.md#get_report_violations_by_report_id) | **GET** /report-violations/{reportID} | Fetch the report violations for an evaluation report


# **associate_report_violations**
> associate_report_violations(report_id)

Associate violations with an evaluation report

Associate violations with an evaluation report. This will overwrite any existing report-violations associations for the report and replace them with the newly provided ones.  An empty array will remove all violation associations for a given report.

### Example


```python
import time
import ghc_client
from ghc_client.api import report_violations_api
from ghc_client.model.error import Error
from ghc_client.model.associate_report_violations import AssociateReportViolations
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
    api_instance = report_violations_api.ReportViolationsApi(api_client)
    report_id = "reportID_example" # str | the evaluation report ID that has associated violations
    body = AssociateReportViolations(
        violations=[
            "violations_example",
        ],
    ) # AssociateReportViolations |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Associate violations with an evaluation report
        api_instance.associate_report_violations(report_id)
    except ghc_client.ApiException as e:
        print("Exception when calling ReportViolationsApi->associate_report_violations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Associate violations with an evaluation report
        api_instance.associate_report_violations(report_id, body=body)
    except ghc_client.ApiException as e:
        print("Exception when calling ReportViolationsApi->associate_report_violations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| the evaluation report ID that has associated violations |
 **body** | [**AssociateReportViolations**](AssociateReportViolations.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully saved the report violations |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_violations_by_report_id**
> ReportViolations get_report_violations_by_report_id(report_id)

Fetch the report violations for an evaluation report

Fetch the report violations for an evaluation report

### Example


```python
import time
import ghc_client
from ghc_client.api import report_violations_api
from ghc_client.model.report_violations import ReportViolations
from ghc_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = report_violations_api.ReportViolationsApi(api_client)
    report_id = "reportID_example" # str | the evaluation report ID that has associated violations

    # example passing only required values which don't have defaults set
    try:
        # Fetch the report violations for an evaluation report
        api_response = api_instance.get_report_violations_by_report_id(report_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ReportViolationsApi->get_report_violations_by_report_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| the evaluation report ID that has associated violations |

### Return type

[**ReportViolations**](ReportViolations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the report violations |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

