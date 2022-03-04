# ghc_client.MoveApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_move**](MoveApi.md#get_move) | **GET** /move/{locator} | Returns a given move
[**get_move_history**](MoveApi.md#get_move_history) | **GET** /move/{locator}/history | Returns the history of an identified move
[**set_financial_review_flag**](MoveApi.md#set_financial_review_flag) | **POST** /moves/{moveID}/financial-review-flag | Flags a move for financial office review


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

# **get_move_history**
> MoveHistory get_move_history(locator)

Returns the history of an identified move

Returns the history for a given move for a unique alphanumeric locator string

### Example


```python
import time
import ghc_client
from ghc_client.api import move_api
from ghc_client.model.error import Error
from ghc_client.model.move_history import MoveHistory
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
        # Returns the history of an identified move
        api_response = api_instance.get_move_history(locator)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveApi->get_move_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**| Code used to identify a move in the system |

### Return type

[**MoveHistory**](MoveHistory.md)

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
from ghc_client.model.inline_object import InlineObject
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
    body = InlineObject(
        remarks="this address is way too far away",
        flag_for_review=False,
    ) # InlineObject |  (optional)

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
 **body** | [**InlineObject**](InlineObject.md)|  | [optional]

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

