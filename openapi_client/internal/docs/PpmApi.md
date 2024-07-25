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
[**resubmit_ppm_shipment_documentation**](PpmApi.md#resubmit_ppm_shipment_documentation) | **PUT** /ppm-shipments/{ppmShipmentId}/resubmit-ppm-shipment-documentation/{signedCertificationId} | Updates signature and routes PPM shipment to service counselor
[**show_aoa_packet**](PpmApi.md#show_aoa_packet) | **GET** /ppm-shipments/{ppmShipmentId}/aoa-packet | Downloads AOA Packet form PPMShipment as a PDF
[**show_payment_packet**](PpmApi.md#show_payment_packet) | **GET** /ppm-shipments/{ppmShipmentId}/payment-packet | Returns PPM payment packet
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
> Upload create_ppm_upload(ppm_shipment_id, document_id, weight_receipt, file)

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
    weight_receipt = True # bool | If the upload is a Weight Receipt
    file = open('/path/to/file', 'rb') # file_type | The file to upload.

    # example passing only required values which don't have defaults set
    try:
        # Create a new upload for a PPM weight ticket, pro-gear, or moving expense document
        api_response = api_instance.create_ppm_upload(ppm_shipment_id, document_id, weight_receipt, file)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling PpmApi->create_ppm_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm_shipment_id** | **str**| UUID of the ppm shipment |
 **document_id** | **str**| UUID of the document to add an upload to |
 **weight_receipt** | **bool**| If the upload is a Weight Receipt |
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

# **show_aoa_packet**
> file_type show_aoa_packet(ppm_shipment_id)

Downloads AOA Packet form PPMShipment as a PDF

### Functionality This endpoint downloads all uploaded move order documentation combined with the Shipment Summary Worksheet into a single PDF. ### Errors * The PPMShipment must have requested an AOA. * The PPMShipment AOA Request must have been approved. 

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
    ppm_shipment_id = "ppmShipmentId_example" # str | the id for the ppmshipment with aoa to be downloaded

    # example passing only required values which don't have defaults set
    try:
        # Downloads AOA Packet form PPMShipment as a PDF
        api_response = api_instance.show_aoa_packet(ppm_shipment_id)
        pprint(api_response)
    except internal_client.ApiException as e:
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
**400** | The request payload is invalid. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_payment_packet**
> file_type show_payment_packet(ppm_shipment_id)

Returns PPM payment packet

Generates a PDF containing all user uploaded documentations for PPM. Contains SSW form, orders, weight and expense documentations.

### Example


```python
import time
import internal_client
from internal_client.api import ppm_api
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
    ppm_shipment_id = "ppmShipmentId_example" # str | UUID of the ppmShipment

    # example passing only required values which don't have defaults set
    try:
        # Returns PPM payment packet
        api_response = api_instance.show_payment_packet(ppm_shipment_id)
        pprint(api_response)
    except internal_client.ApiException as e:
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
        sit_start_date=dateutil_parser('1970-01-01').date(),
        sit_end_date=dateutil_parser('1970-01-01').date(),
        weight_stored=1,
        sit_location={},
        sit_reimburseable_amount=1,
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

