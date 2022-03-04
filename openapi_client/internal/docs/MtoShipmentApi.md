# internal_client.MtoShipmentApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mto_shipment**](MtoShipmentApi.md#create_mto_shipment) | **POST** /mto_shipments | createMTOShipment
[**list_mto_shipments**](MtoShipmentApi.md#list_mto_shipments) | **GET** /moves/{moveTaskOrderID}/mto_shipments | Gets all shipments for a move task order
[**update_mto_shipment**](MtoShipmentApi.md#update_mto_shipment) | **PATCH** /mto-shipments/{mtoShipmentId} | updateMTOShipment


# **create_mto_shipment**
> MTOShipment create_mto_shipment()

createMTOShipment

Creates a MTO shipment for the specified Move Task Order. Required fields include: * Shipment Type * Customer requested pick-up date * Pick-up Address * Delivery Address  Optional fields include: * Customer Remarks * Releasing / Receiving agents 

### Example


```python
import time
import internal_client
from internal_client.api import mto_shipment_api
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.mto_shipment import MTOShipment
from internal_client.model.create_shipment import CreateShipment
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
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    body = CreateShipment(
        move_task_order_id="1f2270c7-7166-40ae-981e-b200ebdf3054",
        shipment_type=MTOShipmentType("HHG"),
        ppm_shipment=CreatePPMShipment(
            expected_departure_date=dateutil_parser('1970-01-01').date(),
            pickup_postal_code="90210",
            secondary_pickup_postal_code="90210",
            destination_postal_code="90210",
            secondary_destination_postal_code="90210",
            sit_expected=True,
        ),
        requested_pickup_date=dateutil_parser('1970-01-01').date(),
        requested_delivery_date=dateutil_parser('1970-01-01').date(),
        customer_remarks="handle with care",
        pickup_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
        ),
        secondary_pickup_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
        ),
        destination_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
        ),
        secondary_delivery_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
        ),
        agents=MTOAgents([
            MTOAgent(
                id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                first_name="first_name_example",
                last_name="last_name_example",
                email="A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRddzXYdswQltRTtwKQzBuNJxBelKTmfIQcBkWgeAShmXXoTaDzlkczbtHjkljEhQVqeWYqqMQZlEQb",
                phone="748-072-8880",
                agent_type=MTOAgentType("RELEASING_AGENT"),
            ),
        ]),
    ) # CreateShipment |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # createMTOShipment
        api_response = api_instance.create_mto_shipment(body=body)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->create_mto_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateShipment**](CreateShipment.md)|  | [optional]

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
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mto_shipments**
> MTOShipments list_mto_shipments(move_task_order_id)

Gets all shipments for a move task order

Gets all MTO shipments for the specified Move Task Order. 

### Example


```python
import time
import internal_client
from internal_client.api import mto_shipment_api
from internal_client.model.error import Error
from internal_client.model.mto_shipments import MTOShipments
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
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move task order for mto shipment to use

    # example passing only required values which don't have defaults set
    try:
        # Gets all shipments for a move task order
        api_response = api_instance.list_mto_shipments(move_task_order_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->list_mto_shipments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move task order for mto shipment to use |

### Return type

[**MTOShipments**](MTOShipments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved all mto shipments for a move task order. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_shipment**
> MTOShipment update_mto_shipment(mto_shipment_id, if_match)

updateMTOShipment

Updates a specified MTO shipment.  Required fields include: * MTO Shipment ID required in path * If-Match required in headers * No fields required in body  Optional fields include: * New shipment status type * Shipment Type * Customer requested pick-up date * Pick-up Address * Delivery Address * Customer Remarks * Releasing / Receiving agents 

### Example


```python
import time
import internal_client
from internal_client.api import mto_shipment_api
from internal_client.model.error import Error
from internal_client.model.validation_error import ValidationError
from internal_client.model.mto_shipment import MTOShipment
from internal_client.model.client_error import ClientError
from internal_client.model.update_shipment import UpdateShipment
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    mto_shipment_id = "mtoShipmentId_example" # str | UUID of the MTO Shipment to update
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    body = UpdateShipment(
        status=MTOShipmentStatus("DRAFT"),
        shipment_type=MTOShipmentType("HHG"),
        ppm_shipment=UpdatePPMShipment(
            expected_departure_date=dateutil_parser('1970-01-01').date(),
            actual_move_date=dateutil_parser('1970-01-01').date(),
            pickup_postal_code="90210",
            secondary_pickup_postal_code="90210",
            destination_postal_code="90210",
            secondary_destination_postal_code="90210",
            sit_expected=True,
            estimated_weight=4200,
            net_weight=4300,
            has_pro_gear=True,
            pro_gear_weight=1,
            spouse_pro_gear_weight=1,
            estimated_incentive=1,
        ),
        requested_pickup_date=dateutil_parser('1970-01-01').date(),
        requested_delivery_date=dateutil_parser('1970-01-01').date(),
        customer_remarks="handle with care",
        pickup_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
        ),
        secondary_pickup_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
        ),
        destination_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
        ),
        secondary_delivery_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
        ),
        agents=MTOAgents([
            MTOAgent(
                id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                first_name="first_name_example",
                last_name="last_name_example",
                email="A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRddzXYdswQltRTtwKQzBuNJxBelKTmfIQcBkWgeAShmXXoTaDzlkczbtHjkljEhQVqeWYqqMQZlEQb",
                phone="748-072-8880",
                agent_type=MTOAgentType("RELEASING_AGENT"),
            ),
        ]),
    ) # UpdateShipment |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # updateMTOShipment
        api_response = api_instance.update_mto_shipment(mto_shipment_id, if_match)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->update_mto_shipment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # updateMTOShipment
        api_response = api_instance.update_mto_shipment(mto_shipment_id, if_match, body=body)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->update_mto_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_shipment_id** | **str**| UUID of the MTO Shipment to update |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **body** | [**UpdateShipment**](UpdateShipment.md)|  | [optional]

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
**200** | Successfully updated the specified MTO shipment. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**412** | Precondition failed, likely due to a stale eTag (If-Match). Fetch the request again to get the updated eTag value. |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

