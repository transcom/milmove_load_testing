# ghc_client.SitExtensionApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_sit_extension**](SitExtensionApi.md#approve_sit_extension) | **PATCH** /shipments/{shipmentID}/sit-extensions/{sitExtensionID}/approve | Approves a SIT extension
[**create_approved_sit_duration_update**](SitExtensionApi.md#create_approved_sit_duration_update) | **POST** /shipments/{shipmentID}/sit-extensions/ | Create an approved SIT Duration Update
[**deny_sit_extension**](SitExtensionApi.md#deny_sit_extension) | **PATCH** /shipments/{shipmentID}/sit-extensions/{sitExtensionID}/deny | Denies a SIT extension


# **approve_sit_extension**
> MTOShipment approve_sit_extension(shipment_id, sit_extension_id, if_match, body)

Approves a SIT extension

Approves a SIT extension

### Example


```python
import time
import ghc_client
from ghc_client.api import sit_extension_api
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
    api_instance = sit_extension_api.SitExtensionApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    sit_extension_id = "sitExtensionID_example" # str | ID of the SIT extension
    if_match = "If-Match_example" # str | We want the shipment's eTag rather than the SIT extension eTag as the SIT extension is always associated with a shipment
    body = ApproveSITExtension(
        approved_days=21,
        office_remarks="Approved for three weeks rather than requested 45 days",
    ) # ApproveSITExtension | 

    # example passing only required values which don't have defaults set
    try:
        # Approves a SIT extension
        api_response = api_instance.approve_sit_extension(shipment_id, sit_extension_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling SitExtensionApi->approve_sit_extension: %s\n" % e)
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
from ghc_client.api import sit_extension_api
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
    api_instance = sit_extension_api.SitExtensionApi(api_client)
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
        print("Exception when calling SitExtensionApi->create_approved_sit_duration_update: %s\n" % e)
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

# **deny_sit_extension**
> MTOShipment deny_sit_extension(shipment_id, sit_extension_id, if_match, body)

Denies a SIT extension

Denies a SIT extension

### Example


```python
import time
import ghc_client
from ghc_client.api import sit_extension_api
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
    api_instance = sit_extension_api.SitExtensionApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment
    sit_extension_id = "sitExtensionID_example" # str | ID of the SIT extension
    if_match = "If-Match_example" # str | 
    body = DenySITExtension(
        office_remarks="Denied this extension as it does not match the criteria",
    ) # DenySITExtension | 

    # example passing only required values which don't have defaults set
    try:
        # Denies a SIT extension
        api_response = api_instance.deny_sit_extension(shipment_id, sit_extension_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling SitExtensionApi->deny_sit_extension: %s\n" % e)
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

