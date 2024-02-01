# internal_client.PpmApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_moving_expense**](PpmApi.md#create_moving_expense) | **POST** /ppm-shipments/{ppmShipmentId}/moving-expenses | Creates moving expense document
[**create_ppm_upload**](PpmApi.md#create_ppm_upload) | **POST** /ppm-shipments/{ppmShipmentId}/uploads | Create a new upload for a PPM weight ticket, pro-gear, or moving expense document
[**create_pro_gear_weight_ticket**](PpmApi.md#create_pro_gear_weight_ticket) | **POST** /ppm-shipments/{ppmShipmentId}/pro-gear-weight-tickets | Creates a pro-gear weight ticket
[**create_weight_ticket**](PpmApi.md#create_weight_ticket) | **POST** /ppm-shipments/{ppmShipmentId}/weight-ticket | Creates a weight ticket document
[**delete_moving_expense**](PpmApi.md#delete_moving_expense) | **DELETE** /ppm-shipments/{ppmShipmentId}/moving-expenses/{movingExpenseId} | Soft deletes a moving expense by ID
[**delete_pro_gear_weight_ticket**](PpmApi.md#delete_pro_gear_weight_ticket) | **DELETE** /ppm-shipments/{ppmShipmentId}/pro-gear-weight-tickets/{proGearWeightTicketId} | Soft deletes a pro-gear weight line item by ID
[**delete_weight_ticket**](PpmApi.md#delete_weight_ticket) | **DELETE** /ppm-shipments/{ppmShipmentId}/weight-ticket/{weightTicketId} | Soft deletes a weight ticket by ID
[**patch_personally_procured_move**](PpmApi.md#patch_personally_procured_move) | **PATCH** /moves/{moveId}/personally_procured_move/{personallyProcuredMoveId} | Patches the PPM
[**request_ppm_payment**](PpmApi.md#request_ppm_payment) | **POST** /personally_procured_move/{personallyProcuredMoveId}/request_payment | Moves the PPM and the move into the PAYMENT_REQUESTED state
[**resubmit_ppm_shipment_documentation**](PpmApi.md#resubmit_ppm_shipment_documentation) | **PUT** /ppm-shipments/{ppmShipmentId}/resubmit-ppm-shipment-documentation/{signedCertificationId} | Updates signature and routes PPM shipment to service counselor
[**show_ppm_estimate**](PpmApi.md#show_ppm_estimate) | **GET** /estimates/ppm | Return a PPM cost estimate
[**show_ppm_incentive**](PpmApi.md#show_ppm_incentive) | **GET** /personally_procured_moves/incentive | Return a PPM incentive value
[**show_ppm_sit_estimate**](PpmApi.md#show_ppm_sit_estimate) | **GET** /estimates/ppm_sit | Return a PPM move&#39;s SIT cost estimate
[**submit_personally_procured_move**](PpmApi.md#submit_personally_procured_move) | **POST** /personally_procured_move/{personallyProcuredMoveId}/submit | Submits a PPM for approval
[**submit_ppm_shipment_documentation**](PpmApi.md#submit_ppm_shipment_documentation) | **POST** /ppm-shipments/{ppmShipmentId}/submit-ppm-shipment-documentation | Saves signature and routes PPM shipment to service counselor
[**update_moving_expense**](PpmApi.md#update_moving_expense) | **PATCH** /ppm-shipments/{ppmShipmentId}/moving-expenses/{movingExpenseId} | Updates the moving expense
[**update_pro_gear_weight_ticket**](PpmApi.md#update_pro_gear_weight_ticket) | **PATCH** /ppm-shipments/{ppmShipmentId}/pro-gear-weight-tickets/{proGearWeightTicketId} | Updates a pro-gear weight ticket
[**update_weight_ticket**](PpmApi.md#update_weight_ticket) | **PATCH** /ppm-shipments/{ppmShipmentId}/weight-ticket/{weightTicketId} | Updates a weight ticket document


# **create_moving_expense**
> MovingExpense create_moving_expense(ppm_shipment_id)

Creates moving expense document

Creates a moving expense document for the PPM shipment

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.moving_expense import MovingExpense
from internal_client.model.client_error import ClientError
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
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment

    # example passing only required values which don't have defaults set
    try:
        # Creates moving expense document
        api_response = api_instance.create_moving_expense(ppm_shipment_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->create_moving_expense: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |

### Return type

[**MovingExpense**](MovingExpense.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | returns new moving expense object |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ppm_upload**
> Upload create_ppm_upload(ppm_shipment_id, document_id, file)

Create a new upload for a PPM weight ticket, pro-gear, or moving expense document

Uploads represent a single digital file, such as a PNG, JPEG, PDF, or spreadsheet.

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.invalid_request_response_payload import InvalidRequestResponsePayload
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.upload import Upload
from internal_client.model.client_error import ClientError
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
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the ppm shipment
    document_id = "documentId_example" # str | UUID of the document to add an upload to
    file = open('/path/to/file', 'rb') # file_type | The file to upload.

    # example passing only required values which don't have defaults set
    try:
        # Create a new upload for a PPM weight ticket, pro-gear, or moving expense document
        api_response = api_instance.create_ppm_upload(ppm_shipment_id, document_id, file)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->create_ppm_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the ppm shipment |
 **document_id** | **str**| UUID of the document to add an upload to |
 **file** | **file_type**| The file to upload. |

### Return type

[**Upload**](Upload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created upload |  -  |
**400** | invalid request |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**413** | payload is too large |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pro_gear_weight_ticket**
> ProGearWeightTicket create_pro_gear_weight_ticket(ppm_shipment_id)

Creates a pro-gear weight ticket

Creates a PPM shipment's pro-gear weight ticket. This will only contain the minimum necessary fields for a pro-gear weight ticket. Data should be filled in using the patch endpoint. 

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.pro_gear_weight_ticket import ProGearWeightTicket
from internal_client.model.client_error import ClientError
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
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment

    # example passing only required values which don't have defaults set
    try:
        # Creates a pro-gear weight ticket
        api_response = api_instance.create_pro_gear_weight_ticket(ppm_shipment_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->create_pro_gear_weight_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |

### Return type

[**ProGearWeightTicket**](ProGearWeightTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | returns a new pro-gear weight ticket object |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_weight_ticket**
> WeightTicket create_weight_ticket(ppm_shipment_id)

Creates a weight ticket document

Created a weight ticket document with the given information

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.weight_ticket import WeightTicket
from internal_client.model.client_error import ClientError
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
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment

    # example passing only required values which don't have defaults set
    try:
        # Creates a weight ticket document
        api_response = api_instance.create_weight_ticket(ppm_shipment_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->create_weight_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |

### Return type

[**WeightTicket**](WeightTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns new weight ticket object |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_moving_expense**
> delete_moving_expense(ppm_shipment_id, moving_expense_id)

Soft deletes a moving expense by ID

Removes a single moving expense receipt from the closeout line items for a PPM shipment. Soft deleted records are not visible in milmove, but are kept in the database. 

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.client_error import ClientError
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
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    moving_expense_id = "movingExpenseId_example" # str | ID of the moving expense to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Soft deletes a moving expense by ID
        api_instance.delete_moving_expense(ppm_shipment_id, moving_expense_id)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->delete_moving_expense: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |
 **moving_expense_id** | **str**| ID of the moving expense to be deleted |

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
**204** | Successfully soft deleted the moving expense |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pro_gear_weight_ticket**
> delete_pro_gear_weight_ticket(ppm_shipment_id, pro_gear_weight_ticket_id)

Soft deletes a pro-gear weight line item by ID

Removes a single pro-gear weight ticket set from the closeout line items for a PPM shipment. Soft deleted records are not visible in milmove, but are kept in the database. 

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.client_error import ClientError
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
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    pro_gear_weight_ticket_id = "proGearWeightTicketId_example" # str | ID of the pro-gear weight ticket to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Soft deletes a pro-gear weight line item by ID
        api_instance.delete_pro_gear_weight_ticket(ppm_shipment_id, pro_gear_weight_ticket_id)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->delete_pro_gear_weight_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |
 **pro_gear_weight_ticket_id** | **str**| ID of the pro-gear weight ticket to be deleted |

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
**204** | Successfully soft deleted the pro-gear weight ticket |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_weight_ticket**
> delete_weight_ticket(ppm_shipment_id, weight_ticket_id)

Soft deletes a weight ticket by ID

Removes a single weight ticket from the closeout line items for a PPM shipment. Soft deleted records are not visible in milmove, but are kept in the database. This may change the PPM shipment's final incentive. 

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.client_error import ClientError
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
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    weight_ticket_id = "weightTicketId_example" # str | ID of the weight ticket to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Soft deletes a weight ticket by ID
        api_instance.delete_weight_ticket(ppm_shipment_id, weight_ticket_id)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->delete_weight_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |
 **weight_ticket_id** | **str**| ID of the weight ticket to be deleted |

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
**204** | Successfully soft deleted the weight ticket |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

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
        advance_worksheet=Document(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            service_member_id="service_member_id_example",
            uploads=[
                Upload(
                    is_weight_ticket=True,
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

# **resubmit_ppm_shipment_documentation**
> PPMShipment resubmit_ppm_shipment_documentation(ppm_shipment_id, signed_certification_id, if_match, save_ppm_shipment_signed_certification_payload)

Updates signature and routes PPM shipment to service counselor

Updates customer signature along with the text they agreed to, and then routes the PPM shipment to the service counselor queue for review. 

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.ppm_shipment import PPMShipment
from internal_client.model.save_ppm_shipment_signed_certification import SavePPMShipmentSignedCertification
from internal_client.model.client_error import ClientError
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
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    signed_certification_id = "signedCertificationId_example" # str | UUID of the signed certification
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    save_ppm_shipment_signed_certification_payload = SavePPMShipmentSignedCertification(
        certification_text="certification_text_example",
        signature="signature_example",
        date=dateutil_parser('1970-01-01').date(),
    ) # SavePPMShipmentSignedCertification | 

    # example passing only required values which don't have defaults set
    try:
        # Updates signature and routes PPM shipment to service counselor
        api_response = api_instance.resubmit_ppm_shipment_documentation(ppm_shipment_id, signed_certification_id, if_match, save_ppm_shipment_signed_certification_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->resubmit_ppm_shipment_documentation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |
 **signed_certification_id** | **str**| UUID of the signed certification |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **save_ppm_shipment_signed_certification_payload** | [**SavePPMShipmentSignedCertification**](SavePPMShipmentSignedCertification.md)|  |

### Return type

[**PPMShipment**](PPMShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated PPM shipment |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

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

# **submit_ppm_shipment_documentation**
> PPMShipment submit_ppm_shipment_documentation(ppm_shipment_id, save_ppm_shipment_signed_certification_payload)

Saves signature and routes PPM shipment to service counselor

Saves customer signature along with the text they agreed to, and then routes the PPM shipment to the service counselor queue for review. 

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.ppm_shipment import PPMShipment
from internal_client.model.save_ppm_shipment_signed_certification import SavePPMShipmentSignedCertification
from internal_client.model.client_error import ClientError
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
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    save_ppm_shipment_signed_certification_payload = SavePPMShipmentSignedCertification(
        certification_text="certification_text_example",
        signature="signature_example",
        date=dateutil_parser('1970-01-01').date(),
    ) # SavePPMShipmentSignedCertification | 

    # example passing only required values which don't have defaults set
    try:
        # Saves signature and routes PPM shipment to service counselor
        api_response = api_instance.submit_ppm_shipment_documentation(ppm_shipment_id, save_ppm_shipment_signed_certification_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->submit_ppm_shipment_documentation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |
 **save_ppm_shipment_signed_certification_payload** | [**SavePPMShipmentSignedCertification**](SavePPMShipmentSignedCertification.md)|  |

### Return type

[**PPMShipment**](PPMShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated PPM shipment |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_moving_expense**
> MovingExpense update_moving_expense(ppm_shipment_id, moving_expense_id, if_match, update_moving_expense)

Updates the moving expense

Any fields sent in this request will be set on the moving expense referenced

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.update_moving_expense import UpdateMovingExpense
from internal_client.model.moving_expense import MovingExpense
from internal_client.model.client_error import ClientError
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
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    moving_expense_id = "movingExpenseId_example" # str | UUID of the moving expense
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    update_moving_expense = UpdateMovingExpense(
        moving_expense_type=MovingExpenseType("CONTRACTED_EXPENSE"),
        description="description_example",
        paid_with_gtcc=True,
        amount=1,
        missing_receipt=True,
        sit_start_date=dateutil_parser('Tue Apr 26 00:00:00 UTC 2022').date(),
        sit_end_date=dateutil_parser('Sat May 26 00:00:00 UTC 2018').date(),
    ) # UpdateMovingExpense | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the moving expense
        api_response = api_instance.update_moving_expense(ppm_shipment_id, moving_expense_id, if_match, update_moving_expense)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->update_moving_expense: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |
 **moving_expense_id** | **str**| UUID of the moving expense |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **update_moving_expense** | [**UpdateMovingExpense**](UpdateMovingExpense.md)|  |

### Return type

[**MovingExpense**](MovingExpense.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns an updated moving expense object |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pro_gear_weight_ticket**
> ProGearWeightTicket update_pro_gear_weight_ticket(if_match, ppm_shipment_id, pro_gear_weight_ticket_id, update_pro_gear_weight_ticket)

Updates a pro-gear weight ticket

Updates a PPM shipment's pro-gear weight ticket with new information. Only some of the fields are editable because some have to be set by the customer, e.g. the description. 

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.pro_gear_weight_ticket import ProGearWeightTicket
from internal_client.model.update_pro_gear_weight_ticket import UpdateProGearWeightTicket
from internal_client.model.client_error import ClientError
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
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    pro_gear_weight_ticket_id = "proGearWeightTicketId_example" # str | UUID of the pro-gear weight ticket
    update_pro_gear_weight_ticket = UpdateProGearWeightTicket(
        belongs_to_self=True,
        description="description_example",
        has_weight_tickets=True,
        weight=0,
    ) # UpdateProGearWeightTicket | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a pro-gear weight ticket
        api_response = api_instance.update_pro_gear_weight_ticket(if_match, ppm_shipment_id, pro_gear_weight_ticket_id, update_pro_gear_weight_ticket)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->update_pro_gear_weight_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |
 **pro_gear_weight_ticket_id** | **str**| UUID of the pro-gear weight ticket |
 **update_pro_gear_weight_ticket** | [**UpdateProGearWeightTicket**](UpdateProGearWeightTicket.md)|  |

### Return type

[**ProGearWeightTicket**](ProGearWeightTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns an updated pro-gear weight ticket object |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_weight_ticket**
> WeightTicket update_weight_ticket(ppm_shipment_id, weight_ticket_id, if_match, update_weight_ticket_payload)

Updates a weight ticket document

Updates a weight ticket document with the new information

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
from internal_client.model.error import Error
from internal_client.model.update_weight_ticket import UpdateWeightTicket
from internal_client.model.validation_error import ValidationError
from internal_client.model.weight_ticket import WeightTicket
from internal_client.model.client_error import ClientError
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
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    weight_ticket_id = "weightTicketId_example" # str | UUID of the weight ticket
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    update_weight_ticket_payload = UpdateWeightTicket(
        vehicle_description="vehicle_description_example",
        empty_weight=0,
        missing_empty_weight_ticket=True,
        full_weight=0,
        missing_full_weight_ticket=True,
        owns_trailer=True,
        trailer_meets_criteria=True,
        adjusted_net_weight=0,
        net_weight_remarks="net_weight_remarks_example",
        allowable_weight=0,
    ) # UpdateWeightTicket | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a weight ticket document
        api_response = api_instance.update_weight_ticket(ppm_shipment_id, weight_ticket_id, if_match, update_weight_ticket_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->update_weight_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |
 **weight_ticket_id** | **str**| UUID of the weight ticket |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **update_weight_ticket_payload** | [**UpdateWeightTicket**](UpdateWeightTicket.md)|  |

### Return type

[**WeightTicket**](WeightTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns an updated weight ticket object |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

