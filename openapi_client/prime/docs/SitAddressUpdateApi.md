# prime_client.SitAddressUpdateApi

All URIs are relative to */prime/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sit_address_update_request**](SitAddressUpdateApi.md#create_sit_address_update_request) | **POST** /sit-address-updates | createSITAddressUpdateRequest


# **create_sit_address_update_request**
> SitAddressUpdate create_sit_address_update_request()

createSITAddressUpdateRequest

**Functionality:** Creates an update request for a SIT service item's final delivery address. A newly created update request is assigned the status 'REQUESTED'  if the change in address is > 50 miles and automatically approved otherwise.  **Limitations:** The update can be requested for APPROVED SIT service items only. Only ONE request is allowed per approved SIT service item.  **DEPRECATION ON AUGUST 5TH, 2024** Following deprecation, when updating a service item's final delivery address, you will need to update the shipment's destination address. This will update the destination SIT service items' final delivery address upon approval. For `APPROVED` shipments, you can use [updateShipmentDestinationAddress](#mtoShipment/updateShipmentDestinationAddress) For shipments in any other status, you can use [updateMTOShipmentAddress](#mtoShipment/updateMTOShipmentAddress) 

### Example


```python
import time
import prime_client
from prime_client.api import sit_address_update_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from prime_client.model.sit_address_update import SitAddressUpdate
from prime_client.model.create_sit_address_update_request import CreateSITAddressUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sit_address_update_api.SitAddressUpdateApi(api_client)
    body = CreateSITAddressUpdateRequest(
        new_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
        ),
        contractor_remarks="Customer reached out to me this week & let me know they want to move closer to family.",
        mto_service_item_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
    ) # CreateSITAddressUpdateRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # createSITAddressUpdateRequest
        api_response = api_instance.create_sit_address_update_request(body=body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling SitAddressUpdateApi->create_sit_address_update_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSITAddressUpdateRequest**](CreateSITAddressUpdateRequest.md)|  | [optional]

### Return type

[**SitAddressUpdate**](SitAddressUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Succesfully created a SIT address update request. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

