# ghc_client.MoveApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_move**](MoveApi.md#get_move) | **GET** /move/{locator} | Returns a given move
[**get_move_counseling_evaluation_reports_list**](MoveApi.md#get_move_counseling_evaluation_reports_list) | **GET** /moves/{moveID}/counseling-evaluation-reports-list | Returns counseling evaluation reports for the specified move that are visible to the current office user
[**get_move_history**](MoveApi.md#get_move_history) | **GET** /move/{locator}/history | Returns the history of an identified move
[**get_move_shipment_evaluation_reports_list**](MoveApi.md#get_move_shipment_evaluation_reports_list) | **GET** /moves/{moveID}/shipment-evaluation-reports-list | Returns shipment evaluation reports for the specified move that are visible to the current office user
[**search_moves**](MoveApi.md#search_moves) | **POST** /moves/search | Search moves by locator, DOD ID, or customer name
[**set_financial_review_flag**](MoveApi.md#set_financial_review_flag) | **POST** /moves/{moveID}/financial-review-flag | Flags a move for financial office review
[**update_closeout_office**](MoveApi.md#update_closeout_office) | **PATCH** /moves/{locator}/closeout-office | Updates a Move&#39;s PPM closeout office for Army and Air Force customers


# **get_move**
> Move get_move(locator)

Returns a given move

Returns a given move for a unique alphanumeric locator string

### Example


```python
import time
import ghc_client
from ghc_client.api import move_api
from ghc_client.model.error import Error
from ghc_client.model.move import Move
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_api.MoveApi(api_client)
    locator = "locator_example" # str | Code used to identify a move in the system

    # example passing only required values which don't have defaults set
    try:
        # Returns a given move
        api_response = api_instance.get_move(locator)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveApi->get_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**| Code used to identify a move in the system |

### Return type

[**Move**](Move.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the individual move |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_move_counseling_evaluation_reports_list**
> EvaluationReportList get_move_counseling_evaluation_reports_list(move_id)

Returns counseling evaluation reports for the specified move that are visible to the current office user

Returns counseling evaluation reports for the specified move that are visible to the current office user

### Example


```python
import time
import ghc_client
from ghc_client.api import move_api
from ghc_client.model.error import Error
from ghc_client.model.evaluation_report_list import EvaluationReportList
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_api.MoveApi(api_client)
    move_id = "moveID_example" # str | Code used to identify a move in the system

    # example passing only required values which don't have defaults set
    try:
        # Returns counseling evaluation reports for the specified move that are visible to the current office user
        api_response = api_instance.get_move_counseling_evaluation_reports_list(move_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveApi->get_move_counseling_evaluation_reports_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| Code used to identify a move in the system |

### Return type

[**EvaluationReportList**](EvaluationReportList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the move&#39;s evaluation reports |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_move_history**
> MoveHistoryResult get_move_history(locator)

Returns the history of an identified move

Returns the history for a given move for a unique alphanumeric locator string

### Example


```python
import time
import ghc_client
from ghc_client.api import move_api
from ghc_client.model.error import Error
from ghc_client.model.move_history_result import MoveHistoryResult
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_api.MoveApi(api_client)
    locator = "locator_example" # str | Code used to identify a move in the system
    page = 1 # int | requested page of results (optional)
    per_page = 1 # int | results per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns the history of an identified move
        api_response = api_instance.get_move_history(locator)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveApi->get_move_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the history of an identified move
        api_response = api_instance.get_move_history(locator, page=page, per_page=per_page)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveApi->get_move_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**| Code used to identify a move in the system |
 **page** | **int**| requested page of results | [optional]
 **per_page** | **int**| results per page | [optional]

### Return type

[**MoveHistoryResult**](MoveHistoryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the individual move history |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_move_shipment_evaluation_reports_list**
> EvaluationReportList get_move_shipment_evaluation_reports_list(move_id)

Returns shipment evaluation reports for the specified move that are visible to the current office user

Returns shipment evaluation reports for the specified move that are visible to the current office user

### Example


```python
import time
import ghc_client
from ghc_client.api import move_api
from ghc_client.model.error import Error
from ghc_client.model.evaluation_report_list import EvaluationReportList
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_api.MoveApi(api_client)
    move_id = "moveID_example" # str | Code used to identify a move in the system

    # example passing only required values which don't have defaults set
    try:
        # Returns shipment evaluation reports for the specified move that are visible to the current office user
        api_response = api_instance.get_move_shipment_evaluation_reports_list(move_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveApi->get_move_shipment_evaluation_reports_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| Code used to identify a move in the system |

### Return type

[**EvaluationReportList**](EvaluationReportList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the move&#39;s evaluation reports |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_moves**
> SearchMovesResult search_moves()

Search moves by locator, DOD ID, or customer name

Search moves by locator, DOD ID, or customer name. Used by QAE and CSR users. 

### Example


```python
import time
import ghc_client
from ghc_client.api import move_api
from ghc_client.model.search_moves_result import SearchMovesResult
from ghc_client.model.error import Error
from ghc_client.model.search_moves_request import SearchMovesRequest
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_api.MoveApi(api_client)
    body = SearchMovesRequest(
        page=1,
        per_page=1,
        locator="locator_example",
        dod_id="dod_id_example",
        customer_name="customer_name_example",
        status=[
            "SUBMITTED",
        ],
        origin_postal_code="origin_postal_code_example",
        destination_postal_code="destination_postal_code_example",
        branch="branch_example",
        shipments_count=1,
        sort="customerName",
        order="asc",
    ) # SearchMovesRequest | field that results should be sorted by (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search moves by locator, DOD ID, or customer name
        api_response = api_instance.search_moves(body=body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveApi->search_moves: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchMovesRequest**](SearchMovesRequest.md)| field that results should be sorted by | [optional]

### Return type

[**SearchMovesResult**](SearchMovesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned all moves matching the criteria |  -  |
**403** | The request was denied |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_financial_review_flag**
> Move set_financial_review_flag(move_id)

Flags a move for financial office review

This sets a flag which indicates that the move should be reviewed by a fincancial office. For example, if the origin or destination address of a shipment is far from the duty location and may incur excess costs to the customer.

### Example


```python
import time
import ghc_client
from ghc_client.api import move_api
from ghc_client.model.error import Error
from ghc_client.model.set_financial_review_flag_request import SetFinancialReviewFlagRequest
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.move import Move
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_api.MoveApi(api_client)
    move_id = "moveID_example" # str | ID of move to flag
    if_match = "If-Match_example" # str |  (optional)
    body = SetFinancialReviewFlagRequest(
        remarks="this address is way too far away",
        flag_for_review=False,
    ) # SetFinancialReviewFlagRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Flags a move for financial office review
        api_response = api_instance.set_financial_review_flag(move_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveApi->set_financial_review_flag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Flags a move for financial office review
        api_response = api_instance.set_financial_review_flag(move_id, if_match=if_match, body=body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveApi->set_financial_review_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| ID of move to flag |
 **if_match** | **str**|  | [optional]
 **body** | [**SetFinancialReviewFlagRequest**](SetFinancialReviewFlagRequest.md)|  | [optional]

### Return type

[**Move**](Move.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated Move |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_closeout_office**
> Move update_closeout_office(locator, if_match)

Updates a Move's PPM closeout office for Army and Air Force customers

Sets the transportation office closeout location for where the Move's PPM Shipment documentation will be reviewed by

### Example


```python
import time
import ghc_client
from ghc_client.api import move_api
from ghc_client.model.error import Error
from ghc_client.model.update_closeout_office_request import UpdateCloseoutOfficeRequest
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.move import Move
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_api.MoveApi(api_client)
    locator = "locator_example" # str | move code to identify a move to update the PPM shipment's closeout office for Army and Air Force service members
    if_match = "If-Match_example" # str | 
    body = UpdateCloseoutOfficeRequest(
        closeout_office_id="closeout_office_id_example",
    ) # UpdateCloseoutOfficeRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a Move's PPM closeout office for Army and Air Force customers
        api_response = api_instance.update_closeout_office(locator, if_match)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveApi->update_closeout_office: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a Move's PPM closeout office for Army and Air Force customers
        api_response = api_instance.update_closeout_office(locator, if_match, body=body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveApi->update_closeout_office: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**| move code to identify a move to update the PPM shipment&#39;s closeout office for Army and Air Force service members |
 **if_match** | **str**|  |
 **body** | [**UpdateCloseoutOfficeRequest**](UpdateCloseoutOfficeRequest.md)|  | [optional]

### Return type

[**Move**](Move.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully set the closeout office for the move |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

