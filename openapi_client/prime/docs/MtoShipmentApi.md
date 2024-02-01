# prime_client.MtoShipmentApi

All URIs are relative to */prime/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mto_agent**](MtoShipmentApi.md#create_mto_agent) | **POST** /mto-shipments/{mtoShipmentID}/agents | createMTOAgent
[**create_mto_shipment**](MtoShipmentApi.md#create_mto_shipment) | **POST** /mto-shipments | createMTOShipment
[**create_sit_extension**](MtoShipmentApi.md#create_sit_extension) | **POST** /mto-shipments/{mtoShipmentID}/sit-extensions | createSITExtension
[**delete_mto_shipment**](MtoShipmentApi.md#delete_mto_shipment) | **DELETE** /mto-shipments/{mtoShipmentID} | deleteMTOShipment
[**update_mto_agent**](MtoShipmentApi.md#update_mto_agent) | **PUT** /mto-shipments/{mtoShipmentID}/agents/{agentID} | updateMTOAgent
[**update_mto_shipment**](MtoShipmentApi.md#update_mto_shipment) | **PATCH** /mto-shipments/{mtoShipmentID} | updateMTOShipment
[**update_mto_shipment_address**](MtoShipmentApi.md#update_mto_shipment_address) | **PUT** /mto-shipments/{mtoShipmentID}/addresses/{addressID} | updateMTOShipmentAddress
[**update_mto_shipment_status**](MtoShipmentApi.md#update_mto_shipment_status) | **PATCH** /mto-shipments/{mtoShipmentID}/status | updateMTOShipmentStatus
[**update_reweigh**](MtoShipmentApi.md#update_reweigh) | **PATCH** /mto-shipments/{mtoShipmentID}/reweighs/{reweighID} | updateReweigh
[**update_shipment_destination_address**](MtoShipmentApi.md#update_shipment_destination_address) | **POST** /mto-shipments/{mtoShipmentID}/shipment-address-updates | updateShipmentDestinationAddress


# **create_mto_agent**
> MTOAgent create_mto_agent(mto_shipment_id, body)

createMTOAgent

### Functionality This endpoint is used to **create** and add agents for an existing MTO Shipment. Only the fields being modified need to be sent in the request body.  ### Errors The agent must always have a name and at least one method of contact (either `email` or `phone`).  The agent must be associated with the MTO shipment passed in the url.  The shipment should be associated with an MTO that is available to the Pime. If the caller requests a new agent, and the shipment is not on an available MTO, the caller will receive a **NotFound** response. 

### Example


```python
import time
import prime_client
from prime_client.api import mto_shipment_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.mto_agent import MTOAgent
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    mto_shipment_id = "mtoShipmentID_example" # str | UUID of the shipment associated with the agent
    body = MTOAgent(
        first_name="first_name_example",
        last_name="last_name_example",
        email="WfRPS@v1C1ylmgd0.Y2TA5TkIRHRRA401iz.sCSLvdNTR",
        phone="980-728-8800",
        agent_type=MTOAgentType("RELEASING_AGENT"),
    ) # MTOAgent | 

    # example passing only required values which don't have defaults set
    try:
        # createMTOAgent
        api_response = api_instance.create_mto_agent(mto_shipment_id, body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->create_mto_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_shipment_id** | **str**| UUID of the shipment associated with the agent |
 **body** | [**MTOAgent**](MTOAgent.md)|  |

### Return type

[**MTOAgent**](MTOAgent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added the agent. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mto_shipment**
> MTOShipment create_mto_shipment()

createMTOShipment

_[Deprecated: sunset on 2024-04-08]_ This endpoint is deprecated and will be removed in a future version. Please use the new endpoint at `/prime/v2/createMTOShipment` instead.  Creates a new shipment within the specified move. This endpoint should be used whenever the movers identify a need for an additional shipment. The new shipment will be submitted to the TOO for review, and the TOO must approve it before the contractor can proceed with billing.  **WIP**: The Prime should be notified by a push notification whenever the TOO approves a shipment connected to one of their moves. Otherwise, the Prime can fetch the related move using the [getMoveTaskOrder](#operation/getMoveTaskOrder) endpoint and see if this shipment has the status `\"APPROVED\"`. 

### Example


```python
import time
import prime_client
from prime_client.api import mto_shipment_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.create_mto_shipment import CreateMTOShipment
from prime_client.model.mto_shipment import MTOShipment
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    body = CreateMTOShipment(
        move_task_order_id="1f2270c7-7166-40ae-981e-b200ebdf3054",
        requested_pickup_date=dateutil_parser('1970-01-01').date(),
        prime_estimated_weight=4500,
        customer_remarks="handle with care",
        agents=MTOAgents([
            MTOAgent(
                first_name="first_name_example",
                last_name="last_name_example",
                email="WfRPS@v1C1ylmgd0.Y2TA5TkIRHRRA401iz.sCSLvdNTR",
                phone="980-728-8800",
                agent_type=MTOAgentType("RELEASING_AGENT"),
            ),
        ]),
        mto_service_items=[
            MTOServiceItem(),
        ],
        pickup_address=CreateMTOShipmentPickupAddress(),
        destination_address=CreateMTOShipmentDestinationAddress(),
        shipment_type=MTOShipmentType("HHG"),
        diversion=True,
        point_of_contact="point_of_contact_example",
        counselor_remarks="counselor approved",
        ppm_shipment=CreatePPMShipment(
            expected_departure_date=dateutil_parser('1970-01-01').date(),
            pickup_postal_code="90210",
            secondary_pickup_postal_code="90210",
            destination_postal_code="90210",
            secondary_destination_postal_code="90210",
            sit_expected=True,
            sit_location={},
            sit_estimated_weight=2000,
            sit_estimated_entry_date=dateutil_parser('1970-01-01').date(),
            sit_estimated_departure_date=dateutil_parser('1970-01-01').date(),
            estimated_weight=4200,
            has_pro_gear=True,
            pro_gear_weight=1,
            spouse_pro_gear_weight=1,
        ),
    ) # CreateMTOShipment |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # createMTOShipment
        api_response = api_instance.create_mto_shipment(body=body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->create_mto_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMTOShipment**](CreateMTOShipment.md)|  | [optional]

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
**200** | Successfully created a MTO shipment. |  -  |
**400** | The request payload is invalid. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sit_extension**
> SITExtension create_sit_extension(mto_shipment_id, body)

createSITExtension

### Functionality This endpoint creates a storage in transit (SIT) extension request for a shipment. A SIT extension request is a request an increase in the shipment day allowance for the number of days a shipment is allowed to be in SIT. The total SIT day allowance includes time spent in both origin and destination SIT. 

### Example


```python
import time
import prime_client
from prime_client.api import mto_shipment_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.sit_extension import SITExtension
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from prime_client.model.create_sit_extension import CreateSITExtension
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    mto_shipment_id = "mtoShipmentID_example" # str | UUID of the shipment associated with the agent
    body = CreateSITExtension(
        request_reason="SERIOUS_ILLNESS_MEMBER",
        contractor_remarks="We need SIT additional days. The customer has not found a house yet.",
        requested_days=30,
    ) # CreateSITExtension | 

    # example passing only required values which don't have defaults set
    try:
        # createSITExtension
        api_response = api_instance.create_sit_extension(mto_shipment_id, body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->create_sit_extension: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_shipment_id** | **str**| UUID of the shipment associated with the agent |
 **body** | [**CreateSITExtension**](CreateSITExtension.md)|  |

### Return type

[**SITExtension**](SITExtension.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created the sit extension request. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mto_shipment**
> delete_mto_shipment(mto_shipment_id)

deleteMTOShipment

### Functionality This endpoint deletes an individual shipment by ID.  ### Errors * The mtoShipment should be associated with an MTO that is available to prime. * The mtoShipment must be a PPM shipment. * Counseling should not have already been completed for the associated MTO. 

### Example


```python
import time
import prime_client
from prime_client.api import mto_shipment_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    mto_shipment_id = "mtoShipmentID_example" # str | UUID of the shipment to be deleted

    # example passing only required values which don't have defaults set
    try:
        # deleteMTOShipment
        api_instance.delete_mto_shipment(mto_shipment_id)
    except prime_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->delete_mto_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_shipment_id** | **str**| UUID of the shipment to be deleted |

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
**204** | Successfully deleted the MTO shipment. |  -  |
**400** | The request payload is invalid. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_agent**
> MTOAgent update_mto_agent(mto_shipment_id, agent_id, if_match, body)

updateMTOAgent

### Functionality This endpoint is used to **update** the agents for an MTO Shipment. Only the fields being modified need to be sent in the request body.  ### Errors: The agent must always have a name and at least one method of contact (either `email` or `phone`).  The agent must be associated with the MTO shipment passed in the url.  The shipment should be associated with an MTO that is available to the Prime. If the caller requests an update to an agent, and the shipment is not on an available MTO, the caller will receive a **NotFound** response. 

### Example


```python
import time
import prime_client
from prime_client.api import mto_shipment_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.mto_agent import MTOAgent
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    mto_shipment_id = "mtoShipmentID_example" # str | UUID of the shipment associated with the agent
    agent_id = "agentID_example" # str | UUID of the agent being updated
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    body = MTOAgent(
        first_name="first_name_example",
        last_name="last_name_example",
        email="WfRPS@v1C1ylmgd0.Y2TA5TkIRHRRA401iz.sCSLvdNTR",
        phone="980-728-8800",
        agent_type=MTOAgentType("RELEASING_AGENT"),
    ) # MTOAgent | 

    # example passing only required values which don't have defaults set
    try:
        # updateMTOAgent
        api_response = api_instance.update_mto_agent(mto_shipment_id, agent_id, if_match, body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->update_mto_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_shipment_id** | **str**| UUID of the shipment associated with the agent |
 **agent_id** | **str**| UUID of the agent being updated |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **body** | [**MTOAgent**](MTOAgent.md)|  |

### Return type

[**MTOAgent**](MTOAgent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the agent. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_shipment**
> MTOShipment update_mto_shipment(mto_shipment_id, if_match, body)

updateMTOShipment

Updates an existing shipment for a move.  Note that there are some restrictions on nested objects:  * Service items: You cannot add or update service items using this endpoint. Please use [createMTOServiceItem](#operation/createMTOServiceItem) and [updateMTOServiceItem](#operation/updateMTOServiceItem) instead. * Agents: You cannot add or update agents using this endpoint. Please use [createMTOAgent](#operation/createMTOAgent) and [updateMTOAgent](#operation/updateMTOAgent) instead. * Addresses: You can add new addresses using this endpoint (and must use this endpoint to do so), but you cannot update existing ones. Please use [updateMTOShipmentAddress](#operation/updateMTOShipmentAddress) instead.  These restrictions are due to our [optimistic locking/concurrency control](https://transcom.github.io/mymove-docs/docs/dev/contributing/backend/use-optimistic-locking) mechanism.  Note that some fields cannot be manually changed but will still be updated automatically, such as `primeEstimatedWeightRecordedDate` and `requiredDeliveryDate`. 

### Example


```python
import time
import prime_client
from prime_client.api import mto_shipment_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.mto_shipment import MTOShipment
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from prime_client.model.update_mto_shipment import UpdateMTOShipment
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    mto_shipment_id = "mtoShipmentID_example" # str | UUID of the shipment being updated.
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    body = UpdateMTOShipment(
        scheduled_pickup_date=dateutil_parser('1970-01-01').date(),
        actual_pickup_date=dateutil_parser('1970-01-01').date(),
        first_available_delivery_date=dateutil_parser('1970-01-01').date(),
        scheduled_delivery_date=dateutil_parser('1970-01-01').date(),
        actual_delivery_date=dateutil_parser('1970-01-01').date(),
        prime_estimated_weight=4500,
        prime_actual_weight=4500,
        nts_recorded_weight=4500,
        pickup_address=UpdateMTOShipmentPickupAddress(),
        destination_address=UpdateMTOShipmentDestinationAddress(),
        destination_type=DestinationType("OTHER_THAN_AUTHORIZED"),
        secondary_pickup_address=UpdateMTOShipmentSecondaryPickupAddress(),
        secondary_delivery_address=UpdateMTOShipmentSecondaryDeliveryAddress(),
        storage_facility=UpdateMTOShipmentStorageFacility(),
        shipment_type=MTOShipmentType("HHG"),
        diversion=True,
        point_of_contact="point_of_contact_example",
        counselor_remarks="counselor approved",
        ppm_shipment=UpdatePPMShipment(
            expected_departure_date=dateutil_parser('1970-01-01').date(),
            pickup_postal_code="90210",
            secondary_pickup_postal_code="90210",
            destination_postal_code="90210",
            secondary_destination_postal_code="90210",
            sit_expected=True,
            sit_location={},
            sit_estimated_weight=2000,
            sit_estimated_entry_date=dateutil_parser('1970-01-01').date(),
            sit_estimated_departure_date=dateutil_parser('1970-01-01').date(),
            estimated_weight=4200,
            has_pro_gear=True,
            pro_gear_weight=1,
            spouse_pro_gear_weight=1,
        ),
    ) # UpdateMTOShipment | 

    # example passing only required values which don't have defaults set
    try:
        # updateMTOShipment
        api_response = api_instance.update_mto_shipment(mto_shipment_id, if_match, body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->update_mto_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_shipment_id** | **str**| UUID of the shipment being updated. |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **body** | [**UpdateMTOShipment**](UpdateMTOShipment.md)|  |

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
**200** | Successfully updated the MTO shipment. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_shipment_address**
> Address update_mto_shipment_address(mto_shipment_id, address_id, if_match, body)

updateMTOShipmentAddress

### Functionality This endpoint is used to **update** the pickup, secondary, and destination addresses on an MTO Shipment. mto-shipments/{mtoShipmentID}/shipment-address-updates is for updating a delivery address. The address details completely replace the original, except for the UUID. Therefore a complete address should be sent in the request. When a destination address on a shipment is updated, the destination SIT service items address ID will also be updated so that shipment and service item final destinations match.  This endpoint **cannot create** an address. To create an address on an MTO shipment, the caller must use [updateMTOShipment](#operation/updateMTOShipment) as the parent shipment has to be updated with the appropriate link to the address.  ### Errors The address must be associated with the mtoShipment passed in the url. In other words, it should be listed as pickupAddress, destinationAddress, secondaryPickupAddress or secondaryDeliveryAddress on the mtoShipment provided. If it is not, caller will receive a **Conflict** Error.  The mtoShipment should be associated with an MTO that is available to prime. If the caller requests an update to an address, and the shipment is not on an available MTO, the caller will receive a **NotFound** Error. 

### Example


```python
import time
import prime_client
from prime_client.api import mto_shipment_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.error import Error
from prime_client.model.address import Address
from prime_client.model.client_error import ClientError
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    mto_shipment_id = "mtoShipmentID_example" # str | UUID of the shipment associated with the address
    address_id = "addressID_example" # str | UUID of the address being updated
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    body = Address(
        id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        street_address1="123 Main Ave",
        street_address2="Apartment 9000",
        street_address3="Montmârtre",
        city="Anytown",
        state="AL",
        postal_code="90210",
        country="USA",
    ) # Address | 

    # example passing only required values which don't have defaults set
    try:
        # updateMTOShipmentAddress
        api_response = api_instance.update_mto_shipment_address(mto_shipment_id, address_id, if_match, body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->update_mto_shipment_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_shipment_id** | **str**| UUID of the shipment associated with the address |
 **address_id** | **str**| UUID of the address being updated |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **body** | [**Address**](Address.md)|  |

### Return type

[**Address**](Address.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the address. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_shipment_status**
> MTOShipment update_mto_shipment_status(mto_shipment_id, if_match, body)

updateMTOShipmentStatus

### Functionality This endpoint should be used by the Prime to confirm the cancellation of a shipment. It allows the shipment status to be changed to \"CANCELED.\" Currently, the Prime cannot update the shipment to any other status. 

### Example


```python
import time
import prime_client
from prime_client.api import mto_shipment_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.mto_shipment import MTOShipment
from prime_client.model.error import Error
from prime_client.model.update_mto_shipment_status import UpdateMTOShipmentStatus
from prime_client.model.client_error import ClientError
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    mto_shipment_id = "mtoShipmentID_example" # str | UUID of the shipment associated with the agent
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    body = UpdateMTOShipmentStatus(
        status="CANCELED",
    ) # UpdateMTOShipmentStatus | 

    # example passing only required values which don't have defaults set
    try:
        # updateMTOShipmentStatus
        api_response = api_instance.update_mto_shipment_status(mto_shipment_id, if_match, body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->update_mto_shipment_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_shipment_id** | **str**| UUID of the shipment associated with the agent |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **body** | [**UpdateMTOShipmentStatus**](UpdateMTOShipmentStatus.md)|  |

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
**200** | Successfully updated the shipment&#39;s status. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reweigh**
> Reweigh update_reweigh(mto_shipment_id, reweigh_id, if_match, body)

updateReweigh

### Functionality This endpoint can be used to update a reweigh with a new weight or to provide the reason why a reweigh did not occur. Only one of weight or verificationReason should be sent in the request body.  A reweigh is the second recorded weight for a shipment, as validated by certified weight tickets. Applies to one shipment. A reweigh can be triggered automatically, or requested by the customer or transportation office. Not all shipments are reweighed, so not all shipments will have a reweigh weight. 

### Example


```python
import time
import prime_client
from prime_client.api import mto_shipment_api
from prime_client.model.reweigh import Reweigh
from prime_client.model.validation_error import ValidationError
from prime_client.model.update_reweigh import UpdateReweigh
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    mto_shipment_id = "mtoShipmentID_example" # str | UUID of the shipment associated with the reweigh
    reweigh_id = "reweighID_example" # str | UUID of the reweigh being updated
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    body = UpdateReweigh(
        weight=2000,
        verification_reason="The reweigh was not performed because the shipment was already delivered",
    ) # UpdateReweigh | 

    # example passing only required values which don't have defaults set
    try:
        # updateReweigh
        api_response = api_instance.update_reweigh(mto_shipment_id, reweigh_id, if_match, body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->update_reweigh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_shipment_id** | **str**| UUID of the shipment associated with the reweigh |
 **reweigh_id** | **str**| UUID of the reweigh being updated |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **body** | [**UpdateReweigh**](UpdateReweigh.md)|  |

### Return type

[**Reweigh**](Reweigh.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the reweigh. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipment_destination_address**
> ShipmentAddressUpdate update_shipment_destination_address(mto_shipment_id, if_match, body)

updateShipmentDestinationAddress

### Functionality This endpoint is used so the Prime can request an **update** for the destination address on an MTO Shipment, after the destination address has already been approved. If automatically approved or TOO approves, this will update the final destination address values for destination SIT service items to be the same as the changed destination address that was approved. Address updates will be automatically approved unless they change:   - The service area   - Mileage bracket for direct delivery   - the address and the distance between the old and new address is > 50   - Domestic Short Haul to Domestic Line Haul or vice versa       - Shipments that start and end in one ZIP3 use Short Haul pricing       - Shipments that start and end in different ZIP3s use Line Haul pricing  For those, changes will require TOO approval. 

### Example


```python
import time
import prime_client
from prime_client.api import mto_shipment_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.update_shipment_destination_address import UpdateShipmentDestinationAddress
from prime_client.model.error import Error
from prime_client.model.client_error import ClientError
from prime_client.model.shipment_address_update import ShipmentAddressUpdate
from pprint import pprint
# Defining the host is optional and defaults to /prime/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = prime_client.Configuration(
    host = "/prime/v1"
)


# Enter a context with an instance of the API client
with prime_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    mto_shipment_id = "mtoShipmentID_example" # str | UUID of the shipment associated with the address
    if_match = "If-Match_example" # str | Needs to be the eTag of the mtoShipment. Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    body = UpdateShipmentDestinationAddress(
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
        contractor_remarks="Customer reached out to me this week and let me know they want to move somewhere else.",
    ) # UpdateShipmentDestinationAddress | 

    # example passing only required values which don't have defaults set
    try:
        # updateShipmentDestinationAddress
        api_response = api_instance.update_shipment_destination_address(mto_shipment_id, if_match, body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->update_shipment_destination_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_shipment_id** | **str**| UUID of the shipment associated with the address |
 **if_match** | **str**| Needs to be the eTag of the mtoShipment. Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **body** | [**UpdateShipmentDestinationAddress**](UpdateShipmentDestinationAddress.md)|  |

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
**201** | Successfully created the address update request. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

