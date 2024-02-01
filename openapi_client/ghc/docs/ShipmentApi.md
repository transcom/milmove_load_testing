# ghc_client.ShipmentApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_shipment**](ShipmentApi.md#approve_shipment) | **POST** /shipments/{shipmentID}/approve | Approves a shipment
[**approve_shipment_diversion**](ShipmentApi.md#approve_shipment_diversion) | **POST** /shipments/{shipmentID}/approve-diversion | Approves a shipment diversion
[**approve_sit_extension**](ShipmentApi.md#approve_sit_extension) | **PATCH** /shipments/{shipmentID}/sit-extensions/{sitExtensionID}/approve | Approves a SIT extension
[**create_approved_sit_duration_update**](ShipmentApi.md#create_approved_sit_duration_update) | **POST** /shipments/{shipmentID}/sit-extensions | Create an approved SIT Duration Update
[**delete_shipment**](ShipmentApi.md#delete_shipment) | **DELETE** /shipments/{shipmentID} | Soft deletes a shipment by ID
[**deny_sit_extension**](ShipmentApi.md#deny_sit_extension) | **PATCH** /shipments/{shipmentID}/sit-extensions/{sitExtensionID}/deny | Denies a SIT extension
[**reject_shipment**](ShipmentApi.md#reject_shipment) | **POST** /shipments/{shipmentID}/reject | rejects a shipment
[**request_shipment_cancellation**](ShipmentApi.md#request_shipment_cancellation) | **POST** /shipments/{shipmentID}/request-cancellation | Requests a shipment cancellation
[**request_shipment_diversion**](ShipmentApi.md#request_shipment_diversion) | **POST** /shipments/{shipmentID}/request-diversion | Requests a shipment diversion
[**request_shipment_reweigh**](ShipmentApi.md#request_shipment_reweigh) | **POST** /shipments/{shipmentID}/request-reweigh | Requests a shipment reweigh
[**review_shipment_address_update**](ShipmentApi.md#review_shipment_address_update) | **PATCH** /shipments/{shipmentID}/review-shipment-address-update | Allows TOO to review a shipment address update
[**update_sit_service_item_customer_expense**](ShipmentApi.md#update_sit_service_item_customer_expense) | **PATCH** /shipments/{shipmentID}/sit-service-item/convert-to-customer-expense | Converts a SIT to customer expense


# **approve_shipment**
> MTOShipment approve_shipment(shipment_id, if_match)

Approves a shipment

Approves a shipment

### Example


```python
import time
import ghc_client
from ghc_client.api import shipment_api
from ghc_client.model.error import Error
from ghc_client.model.mto_shipment import MTOShipment
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
    api_instance = shipment_api.ShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    if_match = "If-Match_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Approves a shipment
        api_response = api_instance.approve_shipment(shipment_id, if_match)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ShipmentApi->approve_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |
 **if_match** | **str**|  |

### Return type

[**MTOShipment**](MTOShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully approved the shipment |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_shipment_diversion**
> MTOShipment approve_shipment_diversion(shipment_id, if_match)

Approves a shipment diversion

Approves a shipment diversion

### Example


```python
import time
import ghc_client
from ghc_client.api import shipment_api
from ghc_client.model.error import Error
from ghc_client.model.mto_shipment import MTOShipment
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
    api_instance = shipment_api.ShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    if_match = "If-Match_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Approves a shipment diversion
        api_response = api_instance.approve_shipment_diversion(shipment_id, if_match)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ShipmentApi->approve_shipment_diversion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |
 **if_match** | **str**|  |

### Return type

[**MTOShipment**](MTOShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully approved the shipment diversion |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_sit_extension**
> MTOShipment approve_sit_extension(shipment_id, sit_extension_id, if_match, body)

Approves a SIT extension

Approves a SIT extension

### Example


```python
import time
import ghc_client
from ghc_client.api import shipment_api
from ghc_client.model.error import Error
from ghc_client.model.approve_sit_extension import ApproveSITExtension
from ghc_client.model.mto_shipment import MTOShipment
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
    api_instance = shipment_api.ShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    sit_extension_id = "sitExtensionID_example" # str | ID of the SIT extension
    if_match = "If-Match_example" # str | We want the shipment's eTag rather than the SIT extension eTag as the SIT extension is always associated with a shipment
    body = ApproveSITExtension(
        approved_days=21,
        request_reason="AWAITING_COMPLETION_OF_RESIDENCE",
        office_remarks="Approved for three weeks rather than requested 45 days",
    ) # ApproveSITExtension | 

    # example passing only required values which don't have defaults set
    try:
        # Approves a SIT extension
        api_response = api_instance.approve_sit_extension(shipment_id, sit_extension_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ShipmentApi->approve_sit_extension: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |
 **sit_extension_id** | **str**| ID of the SIT extension |
 **if_match** | **str**| We want the shipment&#39;s eTag rather than the SIT extension eTag as the SIT extension is always associated with a shipment |
 **body** | [**ApproveSITExtension**](ApproveSITExtension.md)|  |

### Return type

[**MTOShipment**](MTOShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully approved a SIT extension |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_approved_sit_duration_update**
> MTOShipment create_approved_sit_duration_update(shipment_id, if_match, body)

Create an approved SIT Duration Update

TOO can creates an already-approved SIT Duration Update on behalf of a customer

### Example


```python
import time
import ghc_client
from ghc_client.api import shipment_api
from ghc_client.model.error import Error
from ghc_client.model.create_approved_sit_duration_update import CreateApprovedSITDurationUpdate
from ghc_client.model.mto_shipment import MTOShipment
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
    api_instance = shipment_api.ShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    if_match = "If-Match_example" # str | We want the shipment's eTag rather than the SIT Duration Update eTag as the SIT Duration Update is always associated with a shipment
    body = CreateApprovedSITDurationUpdate(
        request_reason="AWAITING_COMPLETION_OF_RESIDENCE",
        approved_days=21,
        office_remarks="Customer needs additional storage time as their new place of residence is not yet ready",
    ) # CreateApprovedSITDurationUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Create an approved SIT Duration Update
        api_response = api_instance.create_approved_sit_duration_update(shipment_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ShipmentApi->create_approved_sit_duration_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |
 **if_match** | **str**| We want the shipment&#39;s eTag rather than the SIT Duration Update eTag as the SIT Duration Update is always associated with a shipment |
 **body** | [**CreateApprovedSITDurationUpdate**](CreateApprovedSITDurationUpdate.md)|  |

### Return type

[**MTOShipment**](MTOShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a SIT Extension. |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shipment**
> delete_shipment(shipment_id)

Soft deletes a shipment by ID

Soft deletes a shipment by ID

### Example


```python
import time
import ghc_client
from ghc_client.api import shipment_api
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
    api_instance = shipment_api.ShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Soft deletes a shipment by ID
        api_instance.delete_shipment(shipment_id)
    except ghc_client.ApiException as e:
        print("Exception when calling ShipmentApi->delete_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment to be deleted |

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
**204** | Successfully soft deleted the shipment |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deny_sit_extension**
> MTOShipment deny_sit_extension(shipment_id, sit_extension_id, if_match, body)

Denies a SIT extension

Denies a SIT extension

### Example


```python
import time
import ghc_client
from ghc_client.api import shipment_api
from ghc_client.model.error import Error
from ghc_client.model.mto_shipment import MTOShipment
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.deny_sit_extension import DenySITExtension
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = shipment_api.ShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    sit_extension_id = "sitExtensionID_example" # str | ID of the SIT extension
    if_match = "If-Match_example" # str | 
    body = DenySITExtension(
        office_remarks="Denied this extension as it does not match the criteria",
        convert_to_customer_expense=False,
    ) # DenySITExtension | 

    # example passing only required values which don't have defaults set
    try:
        # Denies a SIT extension
        api_response = api_instance.deny_sit_extension(shipment_id, sit_extension_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ShipmentApi->deny_sit_extension: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |
 **sit_extension_id** | **str**| ID of the SIT extension |
 **if_match** | **str**|  |
 **body** | [**DenySITExtension**](DenySITExtension.md)|  |

### Return type

[**MTOShipment**](MTOShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully denied a SIT extension |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_shipment**
> MTOShipment reject_shipment(shipment_id, if_match, body)

rejects a shipment

rejects a shipment

### Example


```python
import time
import ghc_client
from ghc_client.api import shipment_api
from ghc_client.model.error import Error
from ghc_client.model.reject_shipment import RejectShipment
from ghc_client.model.mto_shipment import MTOShipment
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
    api_instance = shipment_api.ShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    if_match = "If-Match_example" # str | 
    body = RejectShipment(
        rejection_reason="MTO Shipment not good enough",
    ) # RejectShipment | 

    # example passing only required values which don't have defaults set
    try:
        # rejects a shipment
        api_response = api_instance.reject_shipment(shipment_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ShipmentApi->reject_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |
 **if_match** | **str**|  |
 **body** | [**RejectShipment**](RejectShipment.md)|  |

### Return type

[**MTOShipment**](MTOShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully rejected the shipment |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_shipment_cancellation**
> MTOShipment request_shipment_cancellation(shipment_id, if_match)

Requests a shipment cancellation

Requests a shipment cancellation

### Example


```python
import time
import ghc_client
from ghc_client.api import shipment_api
from ghc_client.model.error import Error
from ghc_client.model.mto_shipment import MTOShipment
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
    api_instance = shipment_api.ShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    if_match = "If-Match_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Requests a shipment cancellation
        api_response = api_instance.request_shipment_cancellation(shipment_id, if_match)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ShipmentApi->request_shipment_cancellation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |
 **if_match** | **str**|  |

### Return type

[**MTOShipment**](MTOShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully requested the shipment cancellation |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_shipment_diversion**
> MTOShipment request_shipment_diversion(shipment_id, if_match)

Requests a shipment diversion

Requests a shipment diversion

### Example


```python
import time
import ghc_client
from ghc_client.api import shipment_api
from ghc_client.model.error import Error
from ghc_client.model.mto_shipment import MTOShipment
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
    api_instance = shipment_api.ShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    if_match = "If-Match_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Requests a shipment diversion
        api_response = api_instance.request_shipment_diversion(shipment_id, if_match)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ShipmentApi->request_shipment_diversion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |
 **if_match** | **str**|  |

### Return type

[**MTOShipment**](MTOShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully requested the shipment diversion |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_shipment_reweigh**
> Reweigh request_shipment_reweigh(shipment_id)

Requests a shipment reweigh

Requests a shipment reweigh

### Example


```python
import time
import ghc_client
from ghc_client.api import shipment_api
from ghc_client.model.reweigh import Reweigh
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
    api_instance = shipment_api.ShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment

    # example passing only required values which don't have defaults set
    try:
        # Requests a shipment reweigh
        api_response = api_instance.request_shipment_reweigh(shipment_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ShipmentApi->request_shipment_reweigh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |

### Return type

[**Reweigh**](Reweigh.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully requested a reweigh of the shipment |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review_shipment_address_update**
> ShipmentAddressUpdate review_shipment_address_update(shipment_id, if_match, body)

Allows TOO to review a shipment address update

This endpoint is used to approve a address update request. Office remarks are required. Approving the address update will update the Destination Final Address of the associated service item

### Example


```python
import time
import ghc_client
from ghc_client.api import shipment_api
from ghc_client.model.shipment_address_update import ShipmentAddressUpdate
from ghc_client.model.error import Error
from ghc_client.model.review_shipment_address_update_request import ReviewShipmentAddressUpdateRequest
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
    api_instance = shipment_api.ShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    if_match = "If-Match_example" # str | 
    body = ReviewShipmentAddressUpdateRequest(
        status="REJECTED",
        office_remarks="office_remarks_example",
    ) # ReviewShipmentAddressUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Allows TOO to review a shipment address update
        api_response = api_instance.review_shipment_address_update(shipment_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ShipmentApi->review_shipment_address_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |
 **if_match** | **str**|  |
 **body** | [**ReviewShipmentAddressUpdateRequest**](ReviewShipmentAddressUpdateRequest.md)|  |

### Return type

[**ShipmentAddressUpdate**](ShipmentAddressUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully requested a shipment address update |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sit_service_item_customer_expense**
> MTOShipment update_sit_service_item_customer_expense(shipment_id, if_match, body)

Converts a SIT to customer expense

Converts a SIT to customer expense

### Example


```python
import time
import ghc_client
from ghc_client.api import shipment_api
from ghc_client.model.error import Error
from ghc_client.model.update_sit_service_item_customer_expense import UpdateSITServiceItemCustomerExpense
from ghc_client.model.mto_shipment import MTOShipment
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
    api_instance = shipment_api.ShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    if_match = "If-Match_example" # str | 
    body = UpdateSITServiceItemCustomerExpense(
        convert_to_customer_expense=True,
        customer_expense_reason="Insufficent details provided",
    ) # UpdateSITServiceItemCustomerExpense | 

    # example passing only required values which don't have defaults set
    try:
        # Converts a SIT to customer expense
        api_response = api_instance.update_sit_service_item_customer_expense(shipment_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ShipmentApi->update_sit_service_item_customer_expense: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |
 **if_match** | **str**|  |
 **body** | [**UpdateSITServiceItemCustomerExpense**](UpdateSITServiceItemCustomerExpense.md)|  |

### Return type

[**MTOShipment**](MTOShipment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully converted to customer expense |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

