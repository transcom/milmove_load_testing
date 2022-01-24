# internal_client.PpmApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_personally_procured_move**](PpmApi.md#create_personally_procured_move) | **POST** /moves/{moveId}/personally_procured_move | Creates a new PPM for the given move
[**create_ppm_attachments**](PpmApi.md#create_ppm_attachments) | **POST** /personally_procured_moves/{personallyProcuredMoveId}/create_ppm_attachments | Creates PPM attachments PDF
[**index_personally_procured_moves**](PpmApi.md#index_personally_procured_moves) | **GET** /moves/{moveId}/personally_procured_move | Returns a list of all PPMs associated with this move
[**patch_personally_procured_move**](PpmApi.md#patch_personally_procured_move) | **PATCH** /moves/{moveId}/personally_procured_move/{personallyProcuredMoveId} | Patches the PPM
[**request_ppm_expense_summary**](PpmApi.md#request_ppm_expense_summary) | **GET** /personally_procured_move/{personallyProcuredMoveId}/expense_summary | Returns an expense summary organized by expense type
[**request_ppm_payment**](PpmApi.md#request_ppm_payment) | **POST** /personally_procured_move/{personallyProcuredMoveId}/request_payment | Moves the PPM and the move into the PAYMENT_REQUESTED state
[**show_personally_procured_move**](PpmApi.md#show_personally_procured_move) | **GET** /moves/{moveId}/personally_procured_move/{personallyProcuredMoveId} | Returns the given PPM
[**show_ppm_estimate**](PpmApi.md#show_ppm_estimate) | **GET** /estimates/ppm | Return a PPM cost estimate
[**show_ppm_incentive**](PpmApi.md#show_ppm_incentive) | **GET** /personally_procured_moves/incentive | Return a PPM incentive value
[**show_ppm_sit_estimate**](PpmApi.md#show_ppm_sit_estimate) | **GET** /estimates/ppm_sit | Return a PPM move&#39;s SIT cost estimate
[**submit_personally_procured_move**](PpmApi.md#submit_personally_procured_move) | **POST** /personally_procured_move/{personallyProcuredMoveId}/submit | Submits a PPM for approval
[**update_personally_procured_move**](PpmApi.md#update_personally_procured_move) | **PUT** /moves/{moveId}/personally_procured_move/{personallyProcuredMoveId} | Updates the PPM
[**update_personally_procured_move_estimate**](PpmApi.md#update_personally_procured_move_estimate) | **PATCH** /moves/{moveId}/personally_procured_move/{personallyProcuredMoveId}/estimate | Calculates the estimated incentive of a PPM


# **create_personally_procured_move**
> PersonallyProcuredMovePayload create_personally_procured_move(move_id, create_personally_procured_move_payload)

Creates a new PPM for the given move

Create an instance of personally_procured_move tied to the move ID

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.personally_procured_move_payload import PersonallyProcuredMovePayload
from internal_client.model.create_personally_procured_move_payload import CreatePersonallyProcuredMovePayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    move_id = "moveId_example" # str | UUID of the move this PPM is associated with
    create_personally_procured_move_payload = CreatePersonallyProcuredMovePayload(
        size=TShirtSize("S"),
        original_move_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        pickup_postal_code="90210",
        has_additional_postal_code=True,
        additional_pickup_postal_code="90210",
        destination_postal_code="90210",
        has_sit=True,
        days_in_storage=0,
        estimated_storage_reimbursement="estimated_storage_reimbursement_example",
        weight_estimate=0,
        net_weight=1,
        has_requested_advance=True,
        advance=CreateReimbursement(
            requested_amount=1,
            method_of_receipt=MethodOfReceipt("MIL_PAY"),
        ),
        advance_worksheet=DocumentPayload(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            service_member_id="service_member_id_example",
            uploads=[
                UploadPayload(
                    id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                    url="https://uploads.domain.test/dir/c56a4180-65aa-42ec-a945-5fd21dec0538",
                    filename="filename.pdf",
                    content_type="application/pdf",
                    checksum="ImGQ2Ush0bDHsaQthV5BnQ==",
                    bytes=1,
                    status="INFECTED",
                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
        ),
        has_pro_gear="NOT SURE",
        has_pro_gear_over_thousand="NOT SURE",
    ) # CreatePersonallyProcuredMovePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new PPM for the given move
        api_response = api_instance.create_personally_procured_move(move_id, create_personally_procured_move_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->create_personally_procured_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move this PPM is associated with |
 **create_personally_procured_move_payload** | [**CreatePersonallyProcuredMovePayload**](CreatePersonallyProcuredMovePayload.md)|  |

### Return type

[**PersonallyProcuredMovePayload**](PersonallyProcuredMovePayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created instance of personally_procured_move |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | move not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ppm_attachments**
> UploadPayload create_ppm_attachments(personally_procured_move_id, doc_types)

Creates PPM attachments PDF

Creates a PPM attachments PDF

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.upload_payload import UploadPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    personally_procured_move_id = "personallyProcuredMoveId_example" # str | UUID of the PPM to create an attachments PDF for
    doc_types = [
        "OTHER",
    ] # [str] | Restrict the list to documents with matching docType.

    # example passing only required values which don't have defaults set
    try:
        # Creates PPM attachments PDF
        api_response = api_instance.create_ppm_attachments(personally_procured_move_id, doc_types)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->create_ppm_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personally_procured_move_id** | **str**| UUID of the PPM to create an attachments PDF for |
 **doc_types** | **[str]**| Restrict the list to documents with matching docType. |

### Return type

[**UploadPayload**](UploadPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns a PPM attachments upload |  -  |
**400** | invalid request |  -  |
**401** | must be authenticated to use this endpoint |  -  |
**403** | not authorized to perform this action |  -  |
**413** | payload is too large |  -  |
**422** | malformed PDF contained in uploads |  -  |
**424** | no files to be processed into attachments PDF |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_personally_procured_moves**
> IndexPersonallyProcuredMovePayload index_personally_procured_moves(move_id)

Returns a list of all PPMs associated with this move

Returns a list of all PPMs associated with this move

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.index_personally_procured_move_payload import IndexPersonallyProcuredMovePayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    move_id = "moveId_example" # str | UUID of the move these PPMs are associated with

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of all PPMs associated with this move
        api_response = api_instance.index_personally_procured_moves(move_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->index_personally_procured_moves: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move these PPMs are associated with |

### Return type

[**IndexPersonallyProcuredMovePayload**](IndexPersonallyProcuredMovePayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns list of personally_procured_move |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_personally_procured_move**
> PersonallyProcuredMovePayload patch_personally_procured_move(move_id, personally_procured_move_id, patch_personally_procured_move_payload)

Patches the PPM

Any fields sent in this request will be set on the PPM referenced

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.personally_procured_move_payload import PersonallyProcuredMovePayload
from internal_client.model.patch_personally_procured_move_payload import PatchPersonallyProcuredMovePayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    move_id = "moveId_example" # str | UUID of the move
    personally_procured_move_id = "personallyProcuredMoveId_example" # str | UUID of the PPM being patched
    patch_personally_procured_move_payload = PatchPersonallyProcuredMovePayload(
        size=TShirtSize("S"),
        original_move_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        actual_move_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        pickup_postal_code="90210",
        has_additional_postal_code=True,
        additional_pickup_postal_code="90210",
        destination_postal_code="90210",
        has_sit=True,
        days_in_storage=0,
        total_sit_cost=1,
        weight_estimate=0,
        net_weight=1,
        incentive_estimate_max=1,
        incentive_estimate_min=1,
        has_requested_advance=False,
        advance=Reimbursement(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            requested_amount=1,
            method_of_receipt=MethodOfReceipt("MIL_PAY"),
            status=ReimbursementStatus("DRAFT"),
            requested_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        ),
        advance_worksheet=DocumentPayload(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            service_member_id="service_member_id_example",
            uploads=[
                UploadPayload(
                    id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                    url="https://uploads.domain.test/dir/c56a4180-65aa-42ec-a945-5fd21dec0538",
                    filename="filename.pdf",
                    content_type="application/pdf",
                    checksum="ImGQ2Ush0bDHsaQthV5BnQ==",
                    bytes=1,
                    status="INFECTED",
                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
        ),
        has_pro_gear="NOT SURE",
        has_pro_gear_over_thousand="NOT SURE",
    ) # PatchPersonallyProcuredMovePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Patches the PPM
        api_response = api_instance.patch_personally_procured_move(move_id, personally_procured_move_id, patch_personally_procured_move_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->patch_personally_procured_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |
 **personally_procured_move_id** | **str**| UUID of the PPM being patched |
 **patch_personally_procured_move_payload** | [**PatchPersonallyProcuredMovePayload**](PatchPersonallyProcuredMovePayload.md)|  |

### Return type

[**PersonallyProcuredMovePayload**](PersonallyProcuredMovePayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of personally_procured_move |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | ppm is not found or ppm discount not found for provided postal codes and original move date |  -  |
**422** | cannot process request with given information |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_ppm_expense_summary**
> ExpenseSummaryPayload request_ppm_expense_summary(personally_procured_move_id)

Returns an expense summary organized by expense type

Calculates and returns an expense summary organized by expense type

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.expense_summary_payload import ExpenseSummaryPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    personally_procured_move_id = "personallyProcuredMoveId_example" # str | UUID of the PPM

    # example passing only required values which don't have defaults set
    try:
        # Returns an expense summary organized by expense type
        api_response = api_instance.request_ppm_expense_summary(personally_procured_move_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->request_ppm_expense_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personally_procured_move_id** | **str**| UUID of the PPM |

### Return type

[**ExpenseSummaryPayload**](ExpenseSummaryPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully calculated expense summary |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | personally procured move not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_ppm_payment**
> PersonallyProcuredMovePayload request_ppm_payment(personally_procured_move_id)

Moves the PPM and the move into the PAYMENT_REQUESTED state

Moves the PPM and the move into the PAYMENT_REQUESTED state

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.personally_procured_move_payload import PersonallyProcuredMovePayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    personally_procured_move_id = "personallyProcuredMoveId_example" # str | UUID of the PPM

    # example passing only required values which don't have defaults set
    try:
        # Moves the PPM and the move into the PAYMENT_REQUESTED state
        api_response = api_instance.request_ppm_payment(personally_procured_move_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->request_ppm_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personally_procured_move_id** | **str**| UUID of the PPM |

### Return type

[**PersonallyProcuredMovePayload**](PersonallyProcuredMovePayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucesssfully requested payment |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | move not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_personally_procured_move**
> IndexPersonallyProcuredMovePayload show_personally_procured_move(move_id, personally_procured_move_id)

Returns the given PPM

Returns the given PPM

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.index_personally_procured_move_payload import IndexPersonallyProcuredMovePayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    move_id = "moveId_example" # str | UUID of the move being signed for
    personally_procured_move_id = "personallyProcuredMoveId_example" # str | UUID of the PPM

    # example passing only required values which don't have defaults set
    try:
        # Returns the given PPM
        api_response = api_instance.show_personally_procured_move(move_id, personally_procured_move_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->show_personally_procured_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move being signed for |
 **personally_procured_move_id** | **str**| UUID of the PPM |

### Return type

[**IndexPersonallyProcuredMovePayload**](IndexPersonallyProcuredMovePayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the instance of personally_procured_move |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_ppm_estimate**
> PPMEstimateRange show_ppm_estimate(original_move_date, origin_zip, origin_duty_location_zip, orders_id, weight_estimate)

Return a PPM cost estimate

Calculates a reimbursement range for a PPM move (excluding SIT)

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.ppm_estimate_range import PPMEstimateRange
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    original_move_date = dateutil_parser('1970-01-01').date() # date | 
    origin_zip = "04807" # str | 
    origin_duty_location_zip = "04807" # str | 
    orders_id = "orders_id_example" # str | 
    weight_estimate = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Return a PPM cost estimate
        api_response = api_instance.show_ppm_estimate(original_move_date, origin_zip, origin_duty_location_zip, orders_id, weight_estimate)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->show_ppm_estimate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **original_move_date** | **date**|  |
 **origin_zip** | **str**|  |
 **origin_duty_location_zip** | **str**|  |
 **orders_id** | **str**|  |
 **weight_estimate** | **int**|  |

### Return type

[**PPMEstimateRange**](PPMEstimateRange.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Made estimate of PPM cost range |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | ppm discount not found for provided postal codes and original move date |  -  |
**409** | distance is less than 50 miles (no short haul moves) |  -  |
**422** | cannot process request with given information |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_ppm_incentive**
> PPMIncentive show_ppm_incentive(original_move_date, origin_zip, origin_duty_location_zip, orders_id, weight)

Return a PPM incentive value

Calculates incentive for a PPM move (excluding SIT)

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.ppm_incentive import PPMIncentive
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    original_move_date = dateutil_parser('1970-01-01').date() # date | 
    origin_zip = "04807" # str | 
    origin_duty_location_zip = "04807" # str | 
    orders_id = "orders_id_example" # str | 
    weight = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Return a PPM incentive value
        api_response = api_instance.show_ppm_incentive(original_move_date, origin_zip, origin_duty_location_zip, orders_id, weight)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->show_ppm_incentive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **original_move_date** | **date**|  |
 **origin_zip** | **str**|  |
 **origin_duty_location_zip** | **str**|  |
 **orders_id** | **str**|  |
 **weight** | **int**|  |

### Return type

[**PPMIncentive**](PPMIncentive.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Made calculation of PPM incentive |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**409** | distance is less than 50 miles (no short haul moves) |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_ppm_sit_estimate**
> PPMSitEstimate show_ppm_sit_estimate(personally_procured_move_id, original_move_date, days_in_storage, origin_zip, orders_id, weight_estimate)

Return a PPM move's SIT cost estimate

Calculates a reimbursment for a PPM move's SIT

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.ppm_sit_estimate import PPMSitEstimate
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    personally_procured_move_id = "personally_procured_move_id_example" # str | 
    original_move_date = dateutil_parser('1970-01-01').date() # date | 
    days_in_storage = 1 # int | 
    origin_zip = "04807" # str | 
    orders_id = "orders_id_example" # str | 
    weight_estimate = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Return a PPM move's SIT cost estimate
        api_response = api_instance.show_ppm_sit_estimate(personally_procured_move_id, original_move_date, days_in_storage, origin_zip, orders_id, weight_estimate)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->show_ppm_sit_estimate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personally_procured_move_id** | **str**|  |
 **original_move_date** | **date**|  |
 **days_in_storage** | **int**|  |
 **origin_zip** | **str**|  |
 **orders_id** | **str**|  |
 **weight_estimate** | **int**|  |

### Return type

[**PPMSitEstimate**](PPMSitEstimate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | show PPM SIT estimate |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**409** | distance is less than 50 miles (no short haul moves) |  -  |
**422** | the payload was unprocessable |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_personally_procured_move**
> PersonallyProcuredMovePayload submit_personally_procured_move(personally_procured_move_id, submit_personally_procured_move_payload)

Submits a PPM for approval

Submits a PPM for approval by the office. The status of the PPM will be updated to SUBMITTED

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.personally_procured_move_payload import PersonallyProcuredMovePayload
from internal_client.model.submit_personally_procured_move_payload import SubmitPersonallyProcuredMovePayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    personally_procured_move_id = "personallyProcuredMoveId_example" # str | UUID of the PPM being submitted
    submit_personally_procured_move_payload = SubmitPersonallyProcuredMovePayload(
        submit_date=dateutil_parser('2019-03-26T13:19:56-04:00'),
    ) # SubmitPersonallyProcuredMovePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Submits a PPM for approval
        api_response = api_instance.submit_personally_procured_move(personally_procured_move_id, submit_personally_procured_move_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->submit_personally_procured_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personally_procured_move_id** | **str**| UUID of the PPM being submitted |
 **submit_personally_procured_move_payload** | [**SubmitPersonallyProcuredMovePayload**](SubmitPersonallyProcuredMovePayload.md)|  |

### Return type

[**PersonallyProcuredMovePayload**](PersonallyProcuredMovePayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of personally_procured_move |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | ppm is not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_personally_procured_move**
> PersonallyProcuredMovePayload update_personally_procured_move(move_id, personally_procured_move_id, update_personally_procured_move_payload)

Updates the PPM

This replaces the current version of the PPM with the version sent.

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.update_personally_procured_move_payload import UpdatePersonallyProcuredMovePayload
from internal_client.model.personally_procured_move_payload import PersonallyProcuredMovePayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    move_id = "moveId_example" # str | UUID of the move
    personally_procured_move_id = "personallyProcuredMoveId_example" # str | UUID of the PPM being updated
    update_personally_procured_move_payload = UpdatePersonallyProcuredMovePayload(
        size=TShirtSize("S"),
        original_move_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        actual_move_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        pickup_postal_code="90210",
        has_additional_postal_code=True,
        additional_pickup_postal_code="90210",
        destination_postal_code="90210",
        has_sit=True,
        days_in_storage=0,
        total_sit_cost=0,
        estimated_storage_reimbursement="estimated_storage_reimbursement_example",
        weight_estimate=0,
        net_weight=1,
        has_requested_advance=False,
        advance=Reimbursement(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            requested_amount=1,
            method_of_receipt=MethodOfReceipt("MIL_PAY"),
            status=ReimbursementStatus("DRAFT"),
            requested_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        ),
        advance_worksheet=DocumentPayload(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            service_member_id="service_member_id_example",
            uploads=[
                UploadPayload(
                    id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                    url="https://uploads.domain.test/dir/c56a4180-65aa-42ec-a945-5fd21dec0538",
                    filename="filename.pdf",
                    content_type="application/pdf",
                    checksum="ImGQ2Ush0bDHsaQthV5BnQ==",
                    bytes=1,
                    status="INFECTED",
                    created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
        ),
        has_pro_gear="NOT SURE",
        has_pro_gear_over_thousand="NOT SURE",
    ) # UpdatePersonallyProcuredMovePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the PPM
        api_response = api_instance.update_personally_procured_move(move_id, personally_procured_move_id, update_personally_procured_move_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->update_personally_procured_move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |
 **personally_procured_move_id** | **str**| UUID of the PPM being updated |
 **update_personally_procured_move_payload** | [**UpdatePersonallyProcuredMovePayload**](UpdatePersonallyProcuredMovePayload.md)|  |

### Return type

[**PersonallyProcuredMovePayload**](PersonallyProcuredMovePayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of personally_procured_move |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_personally_procured_move_estimate**
> PersonallyProcuredMovePayload update_personally_procured_move_estimate(move_id, personally_procured_move_id)

Calculates the estimated incentive of a PPM

This request calculates the estimated incentive of a PPM and attaches this range to the PPM

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.personally_procured_move_payload import PersonallyProcuredMovePayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    move_id = "moveId_example" # str | UUID of the move
    personally_procured_move_id = "personallyProcuredMoveId_example" # str | UUID of the PPM being patched

    # example passing only required values which don't have defaults set
    try:
        # Calculates the estimated incentive of a PPM
        api_response = api_instance.update_personally_procured_move_estimate(move_id, personally_procured_move_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->update_personally_procured_move_estimate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move |
 **personally_procured_move_id** | **str**| UUID of the PPM being patched |

### Return type

[**PersonallyProcuredMovePayload**](PersonallyProcuredMovePayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of personally_procured_move |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | ppm is not found or ppm discount not found for provided postal codes and original move date |  -  |
**422** | cannot process request with given information |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

