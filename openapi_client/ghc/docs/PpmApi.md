# ghc_client.PpmApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finish_document_review**](PpmApi.md#finish_document_review) | **PATCH** /ppm-shipments/{ppmShipmentId}/finish-document-review | Updates a PPM shipment&#39;s status after document review
[**get_ppm_actual_weight**](PpmApi.md#get_ppm_actual_weight) | **GET** /ppm-shipments/{ppmShipmentId}/actual-weight | Get the actual weight for a PPM shipment
[**get_ppm_closeout**](PpmApi.md#get_ppm_closeout) | **GET** /ppm-shipments/{ppmShipmentId}/closeout | Get the closeout calcuations for the specified PPM shipment
[**get_ppm_documents**](PpmApi.md#get_ppm_documents) | **GET** /shipments/{shipmentID}/ppm-documents | Gets all the PPM documents for a PPM shipment
[**get_ppmsit_estimated_cost**](PpmApi.md#get_ppmsit_estimated_cost) | **GET** /ppm-shipments/{ppmShipmentId}/sit_location/{sitLocation}/sit-estimated-cost | Get the SIT estimated cost for a PPM shipment
[**show_aoa_packet**](PpmApi.md#show_aoa_packet) | **GET** /ppm-shipments/{ppmShipmentId}/aoa-packet | Downloads AOA Packet form PPMShipment as a PDF
[**show_payment_packet**](PpmApi.md#show_payment_packet) | **GET** /ppm-shipments/{ppmShipmentId}/payment-packet | Returns PPM payment packet
[**update_moving_expense**](PpmApi.md#update_moving_expense) | **PATCH** /ppm-shipments/{ppmShipmentId}/moving-expenses/{movingExpenseId} | Updates the moving expense
[**update_ppmsit**](PpmApi.md#update_ppmsit) | **PATCH** /ppm-shipments/{ppmShipmentId}/ppm-sit | Updates a PPM shipment&#39;s SIT values
[**update_pro_gear_weight_ticket**](PpmApi.md#update_pro_gear_weight_ticket) | **PATCH** /ppm-shipments/{ppmShipmentId}/pro-gear-weight-tickets/{proGearWeightTicketId} | Updates a pro-gear weight ticket
[**update_weight_ticket**](PpmApi.md#update_weight_ticket) | **PATCH** /ppm-shipments/{ppmShipmentId}/weight-ticket/{weightTicketId} | Updates a weight ticket document


# **finish_document_review**
> PPMShipment finish_document_review(ppm_shipment_id, if_match)

Updates a PPM shipment's status after document review

Updates a PPM shipment's status once documents have been reviewed. Status is updated depending on whether any documents have been rejected. 

### Example


```python
import time
import ghc_client
from ghc_client.api import ppm_api
from ghc_client.model.error import Error
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.ppm_shipment import PPMShipment
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    if_match = "If-Match_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a PPM shipment's status after document review
        api_response = api_instance.finish_document_review(ppm_shipment_id, if_match)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PpmApi->finish_document_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |
 **if_match** | **str**|  |

### Return type

[**PPMShipment**](PPMShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully finished document review |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ppm_actual_weight**
> PPMActualWeight get_ppm_actual_weight(ppm_shipment_id)

Get the actual weight for a PPM shipment

Retrieves the actual weight for the specified PPM shipment. 

### Example


```python
import time
import ghc_client
from ghc_client.api import ppm_api
from ghc_client.model.error import Error
from ghc_client.model.ppm_actual_weight import PPMActualWeight
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
    api_instance = ppm_api.PpmApi(api_client)
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment

    # example passing only required values which don't have defaults set
    try:
        # Get the actual weight for a PPM shipment
        api_response = api_instance.get_ppm_actual_weight(ppm_shipment_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PpmApi->get_ppm_actual_weight: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |

### Return type

[**PPMActualWeight**](PPMActualWeight.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns actual weight for the specified PPM shipment. |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ppm_closeout**
> PPMCloseout get_ppm_closeout(ppm_shipment_id)

Get the closeout calcuations for the specified PPM shipment

Retrieves the closeout calculations for the specified PPM shipment. 

### Example


```python
import time
import ghc_client
from ghc_client.api import ppm_api
from ghc_client.model.error import Error
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.ppm_closeout import PPMCloseout
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment

    # example passing only required values which don't have defaults set
    try:
        # Get the closeout calcuations for the specified PPM shipment
        api_response = api_instance.get_ppm_closeout(ppm_shipment_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PpmApi->get_ppm_closeout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |

### Return type

[**PPMCloseout**](PPMCloseout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns closeout for the specified PPM shipment. |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ppm_documents**
> PPMDocuments get_ppm_documents(shipment_id)

Gets all the PPM documents for a PPM shipment

Retrieves all of the documents and associated uploads for each ppm document type connected to a PPM shipment. This excludes any deleted PPM documents. 

### Example


```python
import time
import ghc_client
from ghc_client.api import ppm_api
from ghc_client.model.error import Error
from ghc_client.model.ppm_documents import PPMDocuments
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
    api_instance = ppm_api.PpmApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment

    # example passing only required values which don't have defaults set
    try:
        # Gets all the PPM documents for a PPM shipment
        api_response = api_instance.get_ppm_documents(shipment_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PpmApi->get_ppm_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |

### Return type

[**PPMDocuments**](PPMDocuments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All PPM documents and associated uploads for the specified PPM shipment. |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ppmsit_estimated_cost**
> PPMSITEstimatedCost get_ppmsit_estimated_cost(ppm_shipment_id, sit_location, sit_entry_date, sit_departure_date, weight_stored)

Get the SIT estimated cost for a PPM shipment

Calculates and returns the SIT estimated cost for the specified PPM shipment. 

### Example


```python
import time
import ghc_client
from ghc_client.api import ppm_api
from ghc_client.model.error import Error
from ghc_client.model.ppmsit_estimated_cost import PPMSITEstimatedCost
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
    api_instance = ppm_api.PpmApi(api_client)
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    sit_location = "ORIGIN" # str | location of sit
    sit_entry_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date entered into SIT
    sit_departure_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date departed SIT
    weight_stored = 0 # int | Weight stored in SIT

    # example passing only required values which don't have defaults set
    try:
        # Get the SIT estimated cost for a PPM shipment
        api_response = api_instance.get_ppmsit_estimated_cost(ppm_shipment_id, sit_location, sit_entry_date, sit_departure_date, weight_stored)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PpmApi->get_ppmsit_estimated_cost: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |
 **sit_location** | **str**| location of sit |
 **sit_entry_date** | **datetime**| Date entered into SIT |
 **sit_departure_date** | **datetime**| Date departed SIT |
 **weight_stored** | **int**| Weight stored in SIT |

### Return type

[**PPMSITEstimatedCost**](PPMSITEstimatedCost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Calculates and returns the SIT estimated cost for the specified PPM shipment. |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_aoa_packet**
> file_type show_aoa_packet(ppm_shipment_id)

Downloads AOA Packet form PPMShipment as a PDF

### Functionality This endpoint downloads all uploaded move order documentation combined with the Shipment Summary Worksheet into a single PDF. ### Errors * The PPMShipment must have requested an AOA. * The PPMShipment AOA Request must have been approved. 

### Example


```python
import time
import ghc_client
from ghc_client.api import ppm_api
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
    api_instance = ppm_api.PpmApi(api_client)
    ppm_shipment_id = "ppmShipmentId_example" # str | the id for the ppmshipment with aoa to be downloaded

    # example passing only required values which don't have defaults set
    try:
        # Downloads AOA Packet form PPMShipment as a PDF
        api_response = api_instance.show_aoa_packet(ppm_shipment_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PpmApi->show_aoa_packet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| the id for the ppmshipment with aoa to be downloaded |

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
**200** | AOA PDF |  * Content-Disposition - File name to download <br>  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_payment_packet**
> file_type show_payment_packet(ppm_shipment_id)

Returns PPM payment packet

Generates a PDF containing all user uploaded documentations for PPM. Contains SSW form, orders, weight and expense documentations.

### Example


```python
import time
import ghc_client
from ghc_client.api import ppm_api
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the ppmShipment

    # example passing only required values which don't have defaults set
    try:
        # Returns PPM payment packet
        api_response = api_instance.show_payment_packet(ppm_shipment_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PpmApi->show_payment_packet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the ppmShipment |

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
**200** | PPM Payment Packet PDF |  * Content-Disposition - File name to download <br>  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | ppm not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_moving_expense**
> MovingExpense update_moving_expense(ppm_shipment_id, moving_expense_id, if_match, update_moving_expense)

Updates the moving expense

Updates a PPM shipment's moving expense with new information. Only some of the moving expense's fields are editable because some have to be set by the customer, e.g. the description and the moving expense type. 

### Example


```python
import time
import ghc_client
from ghc_client.api import ppm_api
from ghc_client.model.error import Error
from ghc_client.model.moving_expense import MovingExpense
from ghc_client.model.update_moving_expense import UpdateMovingExpense
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
    api_instance = ppm_api.PpmApi(api_client)
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    moving_expense_id = "movingExpenseId_example" # str | UUID of the moving expense
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    update_moving_expense = UpdateMovingExpense(
        moving_expense_type=OmittableMovingExpenseType("CONTRACTED_EXPENSE"),
        description="description_example",
        amount=1,
        sit_start_date=dateutil_parser('1970-01-01').date(),
        sit_end_date=dateutil_parser('1970-01-01').date(),
        status=PPMDocumentStatus("APPROVED"),
        reason="reason_example",
        weight_stored=1,
        sit_location={},
        sit_estimated_cost=1,
        sit_reimburseable_amount=1,
    ) # UpdateMovingExpense | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the moving expense
        api_response = api_instance.update_moving_expense(ppm_shipment_id, moving_expense_id, if_match, update_moving_expense)
        pprint(api_response)
    except ghc_client.ApiException as e:
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
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ppmsit**
> PPMShipment update_ppmsit(ppm_shipment_id, if_match)

Updates a PPM shipment's SIT values

Updates a PPM shipment's SIT values 

### Example


```python
import time
import ghc_client
from ghc_client.api import ppm_api
from ghc_client.model.error import Error
from ghc_client.model.ppm_shipment_sit import PPMShipmentSIT
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.ppm_shipment import PPMShipment
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ppm_api.PpmApi(api_client)
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    if_match = "If-Match_example" # str | 
    body = PPMShipmentSIT(
        sit_location={},
    ) # PPMShipmentSIT |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a PPM shipment's SIT values
        api_response = api_instance.update_ppmsit(ppm_shipment_id, if_match)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PpmApi->update_ppmsit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a PPM shipment's SIT values
        api_response = api_instance.update_ppmsit(ppm_shipment_id, if_match, body=body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PpmApi->update_ppmsit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |
 **if_match** | **str**|  |
 **body** | [**PPMShipmentSIT**](PPMShipmentSIT.md)|  | [optional]

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
**200** | Successfully finished PPM SIT update |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pro_gear_weight_ticket**
> ProGearWeightTicket update_pro_gear_weight_ticket(ppm_shipment_id, pro_gear_weight_ticket_id, if_match, update_pro_gear_weight_ticket)

Updates a pro-gear weight ticket

Updates a PPM shipment's pro-gear weight ticket with new information. Only some of the fields are editable because some have to be set by the customer, e.g. the description. 

### Example


```python
import time
import ghc_client
from ghc_client.api import ppm_api
from ghc_client.model.pro_gear_weight_ticket import ProGearWeightTicket
from ghc_client.model.error import Error
from ghc_client.model.update_pro_gear_weight_ticket import UpdateProGearWeightTicket
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
    api_instance = ppm_api.PpmApi(api_client)
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    pro_gear_weight_ticket_id = "proGearWeightTicketId_example" # str | UUID of the pro-gear weight ticket
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    update_pro_gear_weight_ticket = UpdateProGearWeightTicket(
        belongs_to_self=True,
        has_weight_tickets=True,
        weight=0,
        status=PPMDocumentStatus("APPROVED"),
        reason="reason_example",
    ) # UpdateProGearWeightTicket | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a pro-gear weight ticket
        api_response = api_instance.update_pro_gear_weight_ticket(ppm_shipment_id, pro_gear_weight_ticket_id, if_match, update_pro_gear_weight_ticket)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PpmApi->update_pro_gear_weight_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the PPM shipment |
 **pro_gear_weight_ticket_id** | **str**| UUID of the pro-gear weight ticket |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
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
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_weight_ticket**
> WeightTicket update_weight_ticket(ppm_shipment_id, weight_ticket_id, if_match, update_weight_ticket_payload)

Updates a weight ticket document

Updates a PPM shipment's weight ticket document with new information. Only some of the weight ticket document's fields are editable because some have to be set by the customer, e.g. vehicle description. 

### Example


```python
import time
import ghc_client
from ghc_client.api import ppm_api
from ghc_client.model.weight_ticket import WeightTicket
from ghc_client.model.error import Error
from ghc_client.model.update_weight_ticket import UpdateWeightTicket
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
    api_instance = ppm_api.PpmApi(api_client)
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the PPM shipment
    weight_ticket_id = "weightTicketId_example" # str | UUID of the weight ticket
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    update_weight_ticket_payload = UpdateWeightTicket(
        empty_weight=0,
        full_weight=0,
        owns_trailer=True,
        trailer_meets_criteria=True,
        status=PPMDocumentStatus("APPROVED"),
        reason="reason_example",
        adjusted_net_weight=0,
        net_weight_remarks="net_weight_remarks_example",
        allowable_weight=0,
    ) # UpdateWeightTicket | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a weight ticket document
        api_response = api_instance.update_weight_ticket(ppm_shipment_id, weight_ticket_id, if_match, update_weight_ticket_payload)
        pprint(api_response)
    except ghc_client.ApiException as e:
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
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

