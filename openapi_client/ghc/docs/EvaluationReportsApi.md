# ghc_client.EvaluationReportsApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_evaluation_report**](EvaluationReportsApi.md#create_evaluation_report) | **POST** /moves/{locator}/evaluation-reports | Creates an evaluation report
[**delete_evaluation_report**](EvaluationReportsApi.md#delete_evaluation_report) | **DELETE** /evaluation-reports/{reportID} | Deletes an evaluation report by ID
[**download_evaluation_report**](EvaluationReportsApi.md#download_evaluation_report) | **GET** /evaluation-reports/{reportID}/download | Downloads an evaluation report as a PDF
[**get_evaluation_report**](EvaluationReportsApi.md#get_evaluation_report) | **GET** /evaluation-reports/{reportID} | Gets an evaluation report by ID
[**save_evaluation_report**](EvaluationReportsApi.md#save_evaluation_report) | **PUT** /evaluation-reports/{reportID} | Saves an evaluation report as a draft
[**submit_evaluation_report**](EvaluationReportsApi.md#submit_evaluation_report) | **POST** /evaluation-reports/{reportID}/submit | Submits an evaluation report


# **create_evaluation_report**
> EvaluationReport create_evaluation_report(locator)

Creates an evaluation report

Creates an evaluation report

### Example


```python
import time
import ghc_client
from ghc_client.api import evaluation_reports_api
from ghc_client.model.error import Error
from ghc_client.model.create_evaluation_report import CreateEvaluationReport
from ghc_client.model.evaluation_report import EvaluationReport
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
    api_instance = evaluation_reports_api.EvaluationReportsApi(api_client)
    locator = "locator_example" # str | 
    body = CreateEvaluationReport(
        shipment_id="01b9671e-b268-4906-967b-ba661a1d3933",
    ) # CreateEvaluationReport |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates an evaluation report
        api_response = api_instance.create_evaluation_report(locator)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling EvaluationReportsApi->create_evaluation_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates an evaluation report
        api_response = api_instance.create_evaluation_report(locator, body=body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling EvaluationReportsApi->create_evaluation_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  |
 **body** | [**CreateEvaluationReport**](CreateEvaluationReport.md)|  | [optional]

### Return type

[**EvaluationReport**](EvaluationReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created evaluation report |  -  |
**400** | The request payload is invalid |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_evaluation_report**
> delete_evaluation_report(report_id)

Deletes an evaluation report by ID

Deletes an evaluation report by ID

### Example


```python
import time
import ghc_client
from ghc_client.api import evaluation_reports_api
from ghc_client.model.error import Error
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
    api_instance = evaluation_reports_api.EvaluationReportsApi(api_client)
    report_id = "reportID_example" # str | the evaluation report ID to be modified

    # example passing only required values which don't have defaults set
    try:
        # Deletes an evaluation report by ID
        api_instance.delete_evaluation_report(report_id)
    except ghc_client.ApiException as e:
        print("Exception when calling EvaluationReportsApi->delete_evaluation_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| the evaluation report ID to be modified |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted the report |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_evaluation_report**
> file_type download_evaluation_report(report_id)

Downloads an evaluation report as a PDF

Downloads an evaluation report as a PDF

### Example


```python
import time
import ghc_client
from ghc_client.api import evaluation_reports_api
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
    api_instance = evaluation_reports_api.EvaluationReportsApi(api_client)
    report_id = "reportID_example" # str | the evaluation report ID to be downloaded

    # example passing only required values which don't have defaults set
    try:
        # Downloads an evaluation report as a PDF
        api_response = api_instance.download_evaluation_report(report_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling EvaluationReportsApi->download_evaluation_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| the evaluation report ID to be downloaded |

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Evaluation report PDF |  * Content-Disposition - File name to download <br>  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluation_report**
> EvaluationReport get_evaluation_report(report_id)

Gets an evaluation report by ID

Gets an evaluation report by ID

### Example


```python
import time
import ghc_client
from ghc_client.api import evaluation_reports_api
from ghc_client.model.error import Error
from ghc_client.model.evaluation_report import EvaluationReport
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = evaluation_reports_api.EvaluationReportsApi(api_client)
    report_id = "reportID_example" # str | the evaluation report ID to be modified

    # example passing only required values which don't have defaults set
    try:
        # Gets an evaluation report by ID
        api_response = api_instance.get_evaluation_report(report_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling EvaluationReportsApi->get_evaluation_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| the evaluation report ID to be modified |

### Return type

[**EvaluationReport**](EvaluationReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully got the report |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_evaluation_report**
> save_evaluation_report(report_id, if_match)

Saves an evaluation report as a draft

Saves an evaluation report as a draft

### Example


```python
import time
import ghc_client
from ghc_client.api import evaluation_reports_api
from ghc_client.model.error import Error
from ghc_client.model.evaluation_report import EvaluationReport
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
    api_instance = evaluation_reports_api.EvaluationReportsApi(api_client)
    report_id = "reportID_example" # str | the evaluation report ID to be modified
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    body = EvaluationReport(
        type=EvaluationReportType("SHIPMENT"),
        inspection_type=EvaluationReportInspectionType("DATA_REVIEW"),
        inspection_date=dateutil_parser('1970-01-01').date(),
        office_user=EvaluationReportOfficeUser(
            id="1f2270c7-7166-40ae-981e-b200ebdf3054",
            first_name="first_name_example",
            last_name="last_name_example",
            email="A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRddzXYdswQltRTtwKQzBuNJxBelKTmfIQcBkWgeAShmXXoTaDzlkczbtHjkljEhQVqeWYqqMQZlEQb",
            phone="748-072-8880",
        ),
        location=EvaluationReportLocation("ORIGIN"),
        report_violations=ReportViolations([
            ReportViolation(
                id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                report_id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                violation_id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                violation=PWSViolation(
                    id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                    display_order=3,
                    paragraph_number="1.2.3.4.5",
                    title="Customer Support",
                    category="Pre-Move Services",
                    sub_category="Weight Estimate",
                    requirement_summary="Provide a single point of contact (POC)",
                    requirement_statement="The contractor shall prepare and load property going into NTS in containers at residence for shipment to NTS.",
                    is_kpi=False,
                    additional_data_elem="QAE Observed Delivery Date",
                ),
            ),
        ]),
        location_description="Route 66 at crash inspection site 3",
        observed_shipment_delivery_date=dateutil_parser('1970-01-01').date(),
        observed_shipment_physical_pickup_date=dateutil_parser('1970-01-01').date(),
        time_depart="14:30",
        eval_start="15:00",
        eval_end="18:00",
        violations_observed=True,
        remarks="remarks_example",
        serious_incident=True,
        serious_incident_desc="serious_incident_desc_example",
        observed_claims_response_date=dateutil_parser('1970-01-01').date(),
        observed_pickup_date=dateutil_parser('1970-01-01').date(),
        observed_pickup_spread_start_date=dateutil_parser('1970-01-01').date(),
        observed_pickup_spread_end_date=dateutil_parser('1970-01-01').date(),
        observed_delivery_date=dateutil_parser('1970-01-01').date(),
        e_tag="e_tag_example",
        submitted_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # EvaluationReport |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Saves an evaluation report as a draft
        api_instance.save_evaluation_report(report_id, if_match)
    except ghc_client.ApiException as e:
        print("Exception when calling EvaluationReportsApi->save_evaluation_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Saves an evaluation report as a draft
        api_instance.save_evaluation_report(report_id, if_match, body=body)
    except ghc_client.ApiException as e:
        print("Exception when calling EvaluationReportsApi->save_evaluation_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| the evaluation report ID to be modified |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **body** | [**EvaluationReport**](EvaluationReport.md)|  | [optional]

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
**204** | Successfully saved the report |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_evaluation_report**
> submit_evaluation_report(report_id, if_match)

Submits an evaluation report

Submits an evaluation report

### Example


```python
import time
import ghc_client
from ghc_client.api import evaluation_reports_api
from ghc_client.model.error import Error
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
    api_instance = evaluation_reports_api.EvaluationReportsApi(api_client)
    report_id = "reportID_example" # str | the evaluation report ID to be modified
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 

    # example passing only required values which don't have defaults set
    try:
        # Submits an evaluation report
        api_instance.submit_evaluation_report(report_id, if_match)
    except ghc_client.ApiException as e:
        print("Exception when calling EvaluationReportsApi->submit_evaluation_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| the evaluation report ID to be modified |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully submitted an evaluation report with the provided ID |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

