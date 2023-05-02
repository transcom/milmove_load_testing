# ghc_client.MtoShipmentApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mto_shipment**](MtoShipmentApi.md#create_mto_shipment) | **POST** /mto-shipments | createMTOShipment
[**get_shipment**](MtoShipmentApi.md#get_shipment) | **GET** /shipments/{shipmentID} | fetches a shipment by ID
[**list_mto_shipments**](MtoShipmentApi.md#list_mto_shipments) | **GET** /move_task_orders/{moveTaskOrderID}/mto_shipments | Gets all shipments for a move task order
[**update_mto_shipment**](MtoShipmentApi.md#update_mto_shipment) | **PATCH** /move_task_orders/{moveTaskOrderID}/mto_shipments/{shipmentID} | updateMTOShipment


# **create_mto_shipment**
> MTOShipment create_mto_shipment()

createMTOShipment

Creates a MTO shipment for the specified Move Task Order. Required fields include: * Shipment Type * Customer requested pick-up date * Pick-up Address * Delivery Address * Releasing / Receiving agents Optional fields include: * Delivery Address Type * Customer Remarks * Releasing / Receiving agents * An array of optional accessorial service item codes 

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_shipment_api
from ghc_client.model.error import Error
from ghc_client.model.create_mto_shipment import CreateMTOShipment
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
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    body = CreateMTOShipment(
        move_task_order_id="1f2270c7-7166-40ae-981e-b200ebdf3054",
        requested_pickup_date=dateutil_parser('1970-01-01').date(),
        requested_delivery_date=dateutil_parser('1970-01-01').date(),
        customer_remarks="handle with care",
        counselor_remarks="handle with care",
        agents=MTOAgents([
            MTOAgent(
                id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                mto_shipment_id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                first_name="first_name_example",
                last_name="last_name_example",
                email="A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRddzXYdswQltRTtwKQzBuNJxBelKTmfIQcBkWgeAShmXXoTaDzlkczbtHjkljEhQVqeWYqqMQZlEQb",
                phone="748-072-8880",
                agent_type="RELEASING_AGENT",
                e_tag="e_tag_example",
            ),
        ]),
        mto_service_items=MTOServiceItems([
            MTOServiceItem(
                move_task_order_id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                mto_shipment_id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                re_service_id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                re_service_code="re_service_code_example",
                re_service_name="re_service_name_example",
                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                customer_contacts=MTOServiceItemCustomerContacts([
                    MTOServiceItemCustomerContact(
                        id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                        type=CustomerContactType("FIRST"),
                        time_military="0400Z",
                        first_available_delivery_date=dateutil_parser('Thu Dec 31 00:00:00 UTC 2020').date(),
                    ),
                ]),
                deleted_at=dateutil_parser('1970-01-01').date(),
                description="description_example",
                dimensions=MTOServiceItemDimensions([
                    MTOServiceItemDimension(
                        id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                        type=DimensionType("ITEM"),
                        length=1000,
                        width=1000,
                        height=1000,
                    ),
                ]),
                reason="reason_example",
                rejection_reason="rejection_reason_example",
                pickup_postal_code="pickup_postal_code_example",
                sit_entry_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                sit_departure_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                fee_type="COUNSELING",
                id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                quantity=1,
                rate=1,
                status=MTOServiceItemStatus("SUBMITTED"),
                submitted_at=dateutil_parser('1970-01-01').date(),
                total=1,
                estimated_weight=2500,
                updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                approved_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                rejected_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                e_tag="e_tag_example",
            ),
        ]),
        pickup_address={},
        destination_address={},
        destination_type=DestinationType("OTHER_THAN_AUTHORIZED"),
        shipment_type=MTOShipmentType("HHG"),
        tac_type={},
        sac_type={},
        uses_external_vendor=False,
        service_order_number="service_order_number_example",
        nts_recorded_weight=2000,
        storage_facility=StorageFacility(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            facility_name="facility_name_example",
            address=Address(
                id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                street_address1="123 Main Ave",
                street_address2="Apartment 9000",
                street_address3="Montmârtre",
                city="Anytown",
                state="AL",
                postal_code="90210",
                country="USA",
            ),
            lot_number="lot_number_example",
            phone="748-072-8880",
            email="A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRddzXYdswQltRTtwKQzBuNJxBelKTmfIQcBkWgeAShmXXoTaDzlkczbtHjkljEhQVqeWYqqMQZlEQb",
        ),
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
    except ghc_client.ApiException as e:
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
**400** | The request payload is invalid |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment**
> MTOShipment get_shipment(shipment_id)

fetches a shipment by ID

fetches a shipment by ID

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_shipment_api
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
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment to be fetched

    # example passing only required values which don't have defaults set
    try:
        # fetches a shipment by ID
        api_response = api_instance.get_shipment(shipment_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->get_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment to be fetched |

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
**200** | Successfully fetched the shipment |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mto_shipments**
> MTOShipments list_mto_shipments(move_task_order_id)

Gets all shipments for a move task order

Gets all shipments for a move task order

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_shipment_api
from ghc_client.model.error import Error
from ghc_client.model.mto_shipments import MTOShipments
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
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move task order for mto shipment to use

    # example passing only required values which don't have defaults set
    try:
        # Gets all shipments for a move task order
        api_response = api_instance.list_mto_shipments(move_task_order_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
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
**200** | Successfully retrieved all mto shipments for a move task order |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_shipment**
> MTOShipment update_mto_shipment(move_task_order_id, shipment_id, if_match)

updateMTOShipment

Updates a specified MTO shipment. Required fields include: * MTO Shipment ID required in path * If-Match required in headers * No fields required in body Optional fields include: * New shipment status type * Shipment Type * Customer requested pick-up date * Pick-up Address * Delivery Address * Secondary Pick-up Address * SecondaryDelivery Address * Delivery Address Type * Customer Remarks * Counselor Remarks * Releasing / Receiving agents 

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_shipment_api
from ghc_client.model.error import Error
from ghc_client.model.mto_shipment import MTOShipment
from ghc_client.model.update_shipment import UpdateShipment
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
    api_instance = mto_shipment_api.MtoShipmentApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move task order for mto shipment to use
    shipment_id = "shipmentID_example" # str | UUID of the MTO Shipment to update
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    body = UpdateShipment(
        shipment_type=MTOShipmentType("HHG"),
        requested_pickup_date=dateutil_parser('1970-01-01').date(),
        requested_delivery_date=dateutil_parser('1970-01-01').date(),
        customer_remarks="handle with care",
        counselor_remarks="counselor approved",
        billable_weight_cap=2500,
        billable_weight_justification="more weight than expected",
        pickup_address={},
        destination_address={},
        secondary_delivery_address={},
        secondary_pickup_address={},
        has_secondary_pickup_address=True,
        has_secondary_delivery_address=True,
        destination_type=DestinationType("OTHER_THAN_AUTHORIZED"),
        agents=MTOAgents([
            MTOAgent(
                id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                mto_shipment_id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                first_name="first_name_example",
                last_name="last_name_example",
                email="A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRddzXYdswQltRTtwKQzBuNJxBelKTmfIQcBkWgeAShmXXoTaDzlkczbtHjkljEhQVqeWYqqMQZlEQb",
                phone="748-072-8880",
                agent_type="RELEASING_AGENT",
                e_tag="e_tag_example",
            ),
        ]),
        tac_type=LOATypeNullable("HHG"),
        sac_type=LOATypeNullable("HHG"),
        uses_external_vendor=False,
        service_order_number="service_order_number_example",
        nts_recorded_weight=2000,
        storage_facility=StorageFacility(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            facility_name="facility_name_example",
            address=Address(
                id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                street_address1="123 Main Ave",
                street_address2="Apartment 9000",
                street_address3="Montmârtre",
                city="Anytown",
                state="AL",
                postal_code="90210",
                country="USA",
            ),
            lot_number="lot_number_example",
            phone="748-072-8880",
            email="A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRddzXYdswQltRTtwKQzBuNJxBelKTmfIQcBkWgeAShmXXoTaDzlkczbtHjkljEhQVqeWYqqMQZlEQb",
        ),
        ppm_shipment=UpdatePPMShipment(
            expected_departure_date=dateutil_parser('1970-01-01').date(),
            actual_move_date=dateutil_parser('1970-01-01').date(),
            pickup_postal_code="90210",
            secondary_pickup_postal_code="90210",
            destination_postal_code="90210",
            secondary_destination_postal_code="90210",
            w2_address=Address(
                id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                street_address1="123 Main Ave",
                street_address2="Apartment 9000",
                street_address3="Montmârtre",
                city="Anytown",
                state="AL",
                postal_code="90210",
                country="USA",
            ),
            sit_expected=True,
            sit_location={},
            sit_estimated_weight=2000,
            sit_estimated_entry_date=dateutil_parser('1970-01-01').date(),
            sit_estimated_departure_date=dateutil_parser('1970-01-01').date(),
            estimated_weight=4200,
            has_pro_gear=True,
            pro_gear_weight=1,
            spouse_pro_gear_weight=1,
            has_requested_advance=True,
            advance_amount_requested=1,
            advance_status=PPMAdvanceStatus("APPROVED"),
        ),
    ) # UpdateShipment |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # updateMTOShipment
        api_response = api_instance.update_mto_shipment(move_task_order_id, shipment_id, if_match)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->update_mto_shipment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # updateMTOShipment
        api_response = api_instance.update_mto_shipment(move_task_order_id, shipment_id, if_match, body=body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoShipmentApi->update_mto_shipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move task order for mto shipment to use |
 **shipment_id** | **str**| UUID of the MTO Shipment to update |
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
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

