# ghc_client.QueuesApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_moves_queue**](QueuesApi.md#get_moves_queue) | **GET** /queues/moves | Gets queued list of all customer moves by GBLOC origin
[**get_payment_requests_queue**](QueuesApi.md#get_payment_requests_queue) | **GET** /queues/payment-requests | Gets queued list of all payment requests by GBLOC origin
[**get_services_counseling_queue**](QueuesApi.md#get_services_counseling_queue) | **GET** /queues/counseling | Gets queued list of all customer moves needing services counseling by GBLOC origin
[**list_prime_moves**](QueuesApi.md#list_prime_moves) | **GET** /queues/prime-moves | getPrimeMovesQueue


# **get_moves_queue**
> QueueMovesResult get_moves_queue()

Gets queued list of all customer moves by GBLOC origin

An office TOO user will be assigned a transportation office that will determine which moves are displayed in their queue based on the origin duty location.  GHC moves will show up here onced they have reached the submitted status sent by the customer and have move task orders, shipments, and service items to approve. 

### Example


```python
import time
import ghc_client
from ghc_client.api import queues_api
from ghc_client.model.error import Error
from ghc_client.model.queue_moves_result import QueueMovesResult
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = queues_api.QueuesApi(api_client)
    page = 1 # int | requested page of results (optional)
    per_page = 1 # int | results per page (optional)
    sort = "lastName" # str | field that results should be sorted by (optional)
    order = "asc" # str | direction of sort order if applied (optional)
    branch = "branch_example" # str |  (optional)
    locator = "locator_example" # str |  (optional)
    last_name = "lastName_example" # str |  (optional)
    dod_id = "dodID_example" # str |  (optional)
    origin_duty_location = "originDutyLocation_example" # str |  (optional)
    destination_duty_location = "destinationDutyLocation_example" # str |  (optional)
    appeared_in_too_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    requested_move_date = "requestedMoveDate_example" # str | filters the requested pickup date of a shipment on the move (optional)
    status = [
        "SUBMITTED",
    ] # [str] | Filtering for the status. (optional)
    order_type = "orderType_example" # str | order type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets queued list of all customer moves by GBLOC origin
        api_response = api_instance.get_moves_queue(page=page, per_page=per_page, sort=sort, order=order, branch=branch, locator=locator, last_name=last_name, dod_id=dod_id, origin_duty_location=origin_duty_location, destination_duty_location=destination_duty_location, appeared_in_too_at=appeared_in_too_at, requested_move_date=requested_move_date, status=status, order_type=order_type)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling QueuesApi->get_moves_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| requested page of results | [optional]
 **per_page** | **int**| results per page | [optional]
 **sort** | **str**| field that results should be sorted by | [optional]
 **order** | **str**| direction of sort order if applied | [optional]
 **branch** | **str**|  | [optional]
 **locator** | **str**|  | [optional]
 **last_name** | **str**|  | [optional]
 **dod_id** | **str**|  | [optional]
 **origin_duty_location** | **str**|  | [optional]
 **destination_duty_location** | **str**|  | [optional]
 **appeared_in_too_at** | **datetime**|  | [optional]
 **requested_move_date** | **str**| filters the requested pickup date of a shipment on the move | [optional]
 **status** | **[str]**| Filtering for the status. | [optional]
 **order_type** | **str**| order type | [optional]

### Return type

[**QueueMovesResult**](QueueMovesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned all moves matching the criteria |  -  |
**403** | The request was denied |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_requests_queue**
> QueuePaymentRequestsResult get_payment_requests_queue()

Gets queued list of all payment requests by GBLOC origin

An office TIO user will be assigned a transportation office that will determine which payment requests are displayed in their queue based on the origin duty location. 

### Example


```python
import time
import ghc_client
from ghc_client.api import queues_api
from ghc_client.model.error import Error
from ghc_client.model.queue_payment_requests_result import QueuePaymentRequestsResult
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = queues_api.QueuesApi(api_client)
    sort = "lastName" # str | field that results should be sorted by (optional)
    order = "asc" # str | direction of sort order if applied (optional)
    page = 1 # int | requested page of results (optional)
    per_page = 1 # int | number of records to include per page (optional)
    submitted_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Start of the submitted at date in the user's local time zone converted to UTC (optional)
    branch = "branch_example" # str |  (optional)
    locator = "locator_example" # str |  (optional)
    last_name = "lastName_example" # str |  (optional)
    dod_id = "dodID_example" # str |  (optional)
    destination_duty_location = "destinationDutyLocation_example" # str |  (optional)
    origin_duty_location = "originDutyLocation_example" # str |  (optional)
    status = [
        "PENDING",
    ] # [str] | Filtering for the status. (optional)
    order_type = "orderType_example" # str | order type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets queued list of all payment requests by GBLOC origin
        api_response = api_instance.get_payment_requests_queue(sort=sort, order=order, page=page, per_page=per_page, submitted_at=submitted_at, branch=branch, locator=locator, last_name=last_name, dod_id=dod_id, destination_duty_location=destination_duty_location, origin_duty_location=origin_duty_location, status=status, order_type=order_type)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling QueuesApi->get_payment_requests_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| field that results should be sorted by | [optional]
 **order** | **str**| direction of sort order if applied | [optional]
 **page** | **int**| requested page of results | [optional]
 **per_page** | **int**| number of records to include per page | [optional]
 **submitted_at** | **datetime**| Start of the submitted at date in the user&#39;s local time zone converted to UTC | [optional]
 **branch** | **str**|  | [optional]
 **locator** | **str**|  | [optional]
 **last_name** | **str**|  | [optional]
 **dod_id** | **str**|  | [optional]
 **destination_duty_location** | **str**|  | [optional]
 **origin_duty_location** | **str**|  | [optional]
 **status** | **[str]**| Filtering for the status. | [optional]
 **order_type** | **str**| order type | [optional]

### Return type

[**QueuePaymentRequestsResult**](QueuePaymentRequestsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned all moves matching the criteria |  -  |
**403** | The request was denied |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_counseling_queue**
> QueueMovesResult get_services_counseling_queue()

Gets queued list of all customer moves needing services counseling by GBLOC origin

An office services counselor user will be assigned a transportation office that will determine which moves are displayed in their queue based on the origin duty location.  GHC moves will show up here onced they have reached the NEEDS SERVICE COUNSELING status after submission from a customer or created on a customer's behalf. 

### Example


```python
import time
import ghc_client
from ghc_client.api import queues_api
from ghc_client.model.error import Error
from ghc_client.model.queue_moves_result import QueueMovesResult
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = queues_api.QueuesApi(api_client)
    page = 1 # int | requested page number of paginated move results (optional)
    per_page = 1 # int | maximum number of moves to show on each page of paginated results (optional)
    sort = "lastName" # str | field that results should be sorted by (optional)
    order = "asc" # str | direction of sort order if applied (optional)
    branch = "branch_example" # str | filters by the branch of the move's service member (optional)
    locator = "locator_example" # str | filters to match the unique move code locator (optional)
    last_name = "lastName_example" # str | filters using a prefix match on the service member's last name (optional)
    dod_id = "dodID_example" # str | filters to match the unique service member's DoD ID (optional)
    requested_move_date = "requestedMoveDate_example" # str | filters the requested pickup date of a shipment on the move (optional)
    submitted_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Start of the submitted at date in the user's local time zone converted to UTC (optional)
    origin_gbloc = "originGBLOC_example" # str | filters the GBLOC of the service member's origin duty location (optional)
    origin_duty_location = "originDutyLocation_example" # str | filters the name of the origin duty location on the orders (optional)
    destination_duty_location = "destinationDutyLocation_example" # str | filters the name of the destination duty location on the orders (optional)
    status = [
        "NEEDS SERVICE COUNSELING",
    ] # [str] | filters the status of the move (optional)
    needs_ppm_closeout = True # bool | Only used for Services Counseling queue. If true, show PPM moves that are ready for closeout. Otherwise, show all other moves. (optional)
    ppm_type = "FULL" # str | filters PPM type (optional)
    closeout_initiated = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Latest date that closeout was initiated on a PPM on the move (optional)
    closeout_location = "closeoutLocation_example" # str | closeout location (optional)
    order_type = "orderType_example" # str | order type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets queued list of all customer moves needing services counseling by GBLOC origin
        api_response = api_instance.get_services_counseling_queue(page=page, per_page=per_page, sort=sort, order=order, branch=branch, locator=locator, last_name=last_name, dod_id=dod_id, requested_move_date=requested_move_date, submitted_at=submitted_at, origin_gbloc=origin_gbloc, origin_duty_location=origin_duty_location, destination_duty_location=destination_duty_location, status=status, needs_ppm_closeout=needs_ppm_closeout, ppm_type=ppm_type, closeout_initiated=closeout_initiated, closeout_location=closeout_location, order_type=order_type)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling QueuesApi->get_services_counseling_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| requested page number of paginated move results | [optional]
 **per_page** | **int**| maximum number of moves to show on each page of paginated results | [optional]
 **sort** | **str**| field that results should be sorted by | [optional]
 **order** | **str**| direction of sort order if applied | [optional]
 **branch** | **str**| filters by the branch of the move&#39;s service member | [optional]
 **locator** | **str**| filters to match the unique move code locator | [optional]
 **last_name** | **str**| filters using a prefix match on the service member&#39;s last name | [optional]
 **dod_id** | **str**| filters to match the unique service member&#39;s DoD ID | [optional]
 **requested_move_date** | **str**| filters the requested pickup date of a shipment on the move | [optional]
 **submitted_at** | **datetime**| Start of the submitted at date in the user&#39;s local time zone converted to UTC | [optional]
 **origin_gbloc** | **str**| filters the GBLOC of the service member&#39;s origin duty location | [optional]
 **origin_duty_location** | **str**| filters the name of the origin duty location on the orders | [optional]
 **destination_duty_location** | **str**| filters the name of the destination duty location on the orders | [optional]
 **status** | **[str]**| filters the status of the move | [optional]
 **needs_ppm_closeout** | **bool**| Only used for Services Counseling queue. If true, show PPM moves that are ready for closeout. Otherwise, show all other moves. | [optional]
 **ppm_type** | **str**| filters PPM type | [optional]
 **closeout_initiated** | **datetime**| Latest date that closeout was initiated on a PPM on the move | [optional]
 **closeout_location** | **str**| closeout location | [optional]
 **order_type** | **str**| order type | [optional]

### Return type

[**QueueMovesResult**](QueueMovesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned all moves matching the criteria |  -  |
**403** | The request was denied |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_prime_moves**
> ListPrimeMovesResult list_prime_moves()

getPrimeMovesQueue

Gets all moves that have been reviewed and approved by the TOO. The `since` parameter can be used to filter this list down to only the moves that have been updated since the provided timestamp. A move will be considered updated if the `updatedAt` timestamp on the move or on its orders, shipments, service items, or payment requests, is later than the provided date and time.  **WIP**: Include what causes moves to leave this list. Currently, once the `availableToPrimeAt` timestamp has been set, that move will always appear in this list. 

### Example


```python
import time
import ghc_client
from ghc_client.api import queues_api
from ghc_client.model.list_prime_moves_result import ListPrimeMovesResult
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
    api_instance = queues_api.QueuesApi(api_client)
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only return moves updated since this time. Formatted like \"2021-07-23T18:30:47.116Z\" (optional)
    page = 1 # int | requested page of results (optional)
    per_page = 1 # int | results per page (optional)
    id = "id_example" # str |  (optional)
    move_code = "moveCode_example" # str |  (optional)
    order_type = "orderType_example" # str | order type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getPrimeMovesQueue
        api_response = api_instance.list_prime_moves(since=since, page=page, per_page=per_page, id=id, move_code=move_code, order_type=order_type)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling QueuesApi->list_prime_moves: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**| Only return moves updated since this time. Formatted like \&quot;2021-07-23T18:30:47.116Z\&quot; | [optional]
 **page** | **int**| requested page of results | [optional]
 **per_page** | **int**| results per page | [optional]
 **id** | **str**|  | [optional]
 **move_code** | **str**|  | [optional]
 **order_type** | **str**| order type | [optional]

### Return type

[**ListPrimeMovesResult**](ListPrimeMovesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved moves. A successful fetch might still return zero moves. |  -  |
**403** | The request was denied |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

