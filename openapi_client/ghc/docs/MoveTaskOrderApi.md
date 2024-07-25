# ghc_client.MoveTaskOrderApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entitlements**](MoveTaskOrderApi.md#get_entitlements) | **GET** /move-task-orders/{moveTaskOrderID}/entitlements | Gets entitlements for a move by ID
[**get_move_task_order**](MoveTaskOrderApi.md#get_move_task_order) | **GET** /move-task-orders/{moveTaskOrderID} | Gets a move by ID
[**update_move_task_order_status**](MoveTaskOrderApi.md#update_move_task_order_status) | **PATCH** /move-task-orders/{moveTaskOrderID}/status | Change the status of a move task order to make it available to prime
[**update_move_tio_remarks**](MoveTaskOrderApi.md#update_move_tio_remarks) | **PATCH** /move-task-orders/{moveTaskOrderID}/tio-remarks | 
[**update_mto_reviewed_billable_weights_at**](MoveTaskOrderApi.md#update_mto_reviewed_billable_weights_at) | **PATCH** /move-task-orders/{moveTaskOrderID}/billable-weights-reviewed-at | 
[**update_mto_status_service_counseling_completed**](MoveTaskOrderApi.md#update_mto_status_service_counseling_completed) | **PATCH** /move-task-orders/{moveTaskOrderID}/status/service-counseling-completed | Changes move (move task order) status to service counseling completed


# **get_entitlements**
> Entitlements get_entitlements(move_task_order_id)

Gets entitlements for a move by ID

Gets entitlements

### Example


```python
import time
import ghc_client
from ghc_client.api import move_task_order_api
from ghc_client.model.error import Error
from ghc_client.model.entitlements import Entitlements
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_task_order_api.MoveTaskOrderApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move to use

    # example passing only required values which don't have defaults set
    try:
        # Gets entitlements for a move by ID
        api_response = api_instance.get_entitlements(move_task_order_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveTaskOrderApi->get_entitlements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move to use |

### Return type

[**Entitlements**](Entitlements.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved entitlements |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_move_task_order**
> MoveTaskOrder get_move_task_order(move_task_order_id)

Gets a move by ID

Gets a move

### Example


```python
import time
import ghc_client
from ghc_client.api import move_task_order_api
from ghc_client.model.error import Error
from ghc_client.model.move_task_order import MoveTaskOrder
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_task_order_api.MoveTaskOrderApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move to use

    # example passing only required values which don't have defaults set
    try:
        # Gets a move by ID
        api_response = api_instance.get_move_task_order(move_task_order_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveTaskOrderApi->get_move_task_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move to use |

### Return type

[**MoveTaskOrder**](MoveTaskOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved move task order |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_move_task_order_status**
> Move update_move_task_order_status(move_task_order_id, if_match, service_item_codes)

Change the status of a move task order to make it available to prime

Changes move task order status to make it available to prime

### Example


```python
import time
import ghc_client
from ghc_client.api import move_task_order_api
from ghc_client.model.error import Error
from ghc_client.model.mto_approval_service_item_codes import MTOApprovalServiceItemCodes
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.move import Move
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_task_order_api.MoveTaskOrderApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move to use
    if_match = "If-Match_example" # str | 
    service_item_codes = MTOApprovalServiceItemCodes(
        service_code_cs=True,
        service_code_ms=True,
    ) # MTOApprovalServiceItemCodes | 

    # example passing only required values which don't have defaults set
    try:
        # Change the status of a move task order to make it available to prime
        api_response = api_instance.update_move_task_order_status(move_task_order_id, if_match, service_item_codes)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveTaskOrderApi->update_move_task_order_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move to use |
 **if_match** | **str**|  |
 **service_item_codes** | [**MTOApprovalServiceItemCodes**](MTOApprovalServiceItemCodes.md)|  |

### Return type

[**Move**](Move.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated move task order status |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_move_tio_remarks**
> Move update_move_tio_remarks(move_task_order_id, if_match, body)



Changes move (move task order) billableWeightsReviewedAt field to a timestamp

### Example


```python
import time
import ghc_client
from ghc_client.api import move_task_order_api
from ghc_client.model.error import Error
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.move import Move
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_task_order_api.MoveTaskOrderApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move to use
    if_match = "If-Match_example" # str | 
    body = Move(
        id="1f2270c7-7166-40ae-981e-b200ebdf3054",
        service_counseling_completed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        available_to_prime_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        billable_weights_reviewed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        contractor_id="contractor_id_example",
        contractor=Contractor(
            contract_number="contract_number_example",
            id="id_example",
            name="name_example",
            type="type_example",
        ),
        locator="1K43AR",
        orders_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        orders=Order(
            id="1f2270c7-7166-40ae-981e-b200ebdf3054",
            customer_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            customer=Customer(
                agency="agency_example",
                first_name="John",
                last_name="Doe",
                phone="748-072-8880",
                email="A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRddzXYdswQltRTtwKQzBuNJxBelKTmfIQcBkWgeAShmXXoTaDzlkczbtHjkljEhQVqeWYqqMQZlEQb",
                suffix="Jr.",
                middle_name="David",
                current_address=Address(
                    id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                    street_address1="123 Main Ave",
                    street_address2="Apartment 9000",
                    street_address3="Montmârtre",
                    city="Anytown",
                    state="AL",
                    postal_code="90210",
                    country="USA",
                    county="LOS ANGELES",
                ),
                backup_contact=BackupContact(
                    name="name_example",
                    email="backupContact@mail.com",
                    phone="748-072-8880",
                ),
                id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                dod_id="dod_id_example",
                emplid="emplid_example",
                user_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                e_tag="e_tag_example",
                phone_is_preferred=True,
                email_is_preferred=True,
                secondary_telephone="",
                backup_address=Address(
                    id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                    street_address1="123 Main Ave",
                    street_address2="Apartment 9000",
                    street_address3="Montmârtre",
                    city="Anytown",
                    state="AL",
                    postal_code="90210",
                    country="USA",
                    county="LOS ANGELES",
                ),
                cac_validated=True,
            ),
            move_code="H2XFJF",
            grade=Grade("E_1"),
            agency=Affiliation("ARMY"),
            entitlement=Entitlements(
                id="571008b1-b0de-454d-b843-d71be9f02c04",
                authorized_weight=2000,
                dependents_authorized=True,
                gun_safe=False,
                non_temporary_storage=False,
                privately_owned_vehicle=False,
                pro_gear_weight=2000,
                pro_gear_weight_spouse=500,
                storage_in_transit=90,
                total_weight=500,
                total_dependents=2,
                required_medical_equipment_weight=500,
                organizational_clothing_and_individual_equipment=True,
                e_tag="e_tag_example",
            ),
            destination_duty_location=DutyLocation(
                id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                name="Fort Bragg North Station",
                address_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                address=Address(
                    id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                    street_address1="123 Main Ave",
                    street_address2="Apartment 9000",
                    street_address3="Montmârtre",
                    city="Anytown",
                    state="AL",
                    postal_code="90210",
                    country="USA",
                    county="LOS ANGELES",
                ),
                e_tag="e_tag_example",
            ),
            destination_duty_location_gbloc=GBLOC("AGFM"),
            origin_duty_location=DutyLocation(
                id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                name="Fort Bragg North Station",
                address_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                address=Address(
                    id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                    street_address1="123 Main Ave",
                    street_address2="Apartment 9000",
                    street_address3="Montmârtre",
                    city="Anytown",
                    state="AL",
                    postal_code="90210",
                    country="USA",
                    county="LOS ANGELES",
                ),
                e_tag="e_tag_example",
            ),
            origin_duty_location_gbloc=GBLOC("AGFM"),
            move_task_order_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            uploaded_order_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            uploaded_amended_order_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            amended_orders_acknowledged_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
            order_number="030-00362",
            order_type=OrdersType("PERMANENT_CHANGE_OF_STATION"),
            order_type_detail=OrdersTypeDetail("HHG_PERMITTED"),
            date_issued=dateutil_parser('Wed Jan 01 00:00:00 UTC 2020').date(),
            report_by_date=dateutil_parser('Wed Jan 01 00:00:00 UTC 2020').date(),
            department_indicator=DeptIndicator("NAVY_AND_MARINES"),
            tac="F8J1",
            sac="N002214CSW32Y9",
            nts_tac="F8J1",
            nts_sac="N002214CSW32Y9",
            has_dependents=False,
            spouse_has_pro_gear=False,
            supply_and_services_cost_estimate="supply_and_services_cost_estimate_example",
            packing_and_shipping_instructions="packing_and_shipping_instructions_example",
            method_of_payment="method_of_payment_example",
            naics="naics_example",
            orders_type=OrdersType("PERMANENT_CHANGE_OF_STATION"),
            e_tag="e_tag_example",
        ),
        reference_id="1001-3456",
        status=MoveStatus("DRAFT"),
        excess_weight_qualified_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        excess_weight_acknowledged_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        tio_remarks="approved additional weight",
        closeout_office=TransportationOffice(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            name="Fort Bragg North Station",
            address=Address(
                id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                street_address1="123 Main Ave",
                street_address2="Apartment 9000",
                street_address3="Montmârtre",
                city="Anytown",
                state="AL",
                postal_code="90210",
                country="USA",
                county="LOS ANGELES",
            ),
            phone_lines=[
                "212-555-5555",
            ],
            gbloc="JENQ",
            latitude=29.382973,
            longitude=-98.62759,
            created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
            updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        closeout_office_id="closeout_office_id_example",
        approvals_requested_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        submitted_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        e_tag="e_tag_example",
        shipment_gbloc=GBLOC("AGFM"),
        locked_by_office_user_id="locked_by_office_user_id_example",
        locked_by_office_user=LockedOfficeUser(
            first_name="first_name_example",
            last_name="last_name_example",
            transportation_office_id="transportation_office_id_example",
            transportation_office=TransportationOffice(
                id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                name="Fort Bragg North Station",
                address=Address(
                    id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                    street_address1="123 Main Ave",
                    street_address2="Apartment 9000",
                    street_address3="Montmârtre",
                    city="Anytown",
                    state="AL",
                    postal_code="90210",
                    country="USA",
                    county="LOS ANGELES",
                ),
                phone_lines=[
                    "212-555-5555",
                ],
                gbloc="JENQ",
                latitude=29.382973,
                longitude=-98.62759,
                created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ),
        lock_expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        additional_documents=Document(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            service_member_id="service_member_id_example",
            uploads=[
                Upload(
                    is_weight_ticket=True,
                ),
            ],
        ),
    ) # Move | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_move_tio_remarks(move_task_order_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveTaskOrderApi->update_move_tio_remarks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move to use |
 **if_match** | **str**|  |
 **body** | [**Move**](Move.md)|  |

### Return type

[**Move**](Move.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated move task order tioRemarks field |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_reviewed_billable_weights_at**
> Move update_mto_reviewed_billable_weights_at(move_task_order_id, if_match)



Changes move (move task order) billableWeightsReviewedAt field to a timestamp

### Example


```python
import time
import ghc_client
from ghc_client.api import move_task_order_api
from ghc_client.model.error import Error
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.move import Move
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_task_order_api.MoveTaskOrderApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move to use
    if_match = "If-Match_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_mto_reviewed_billable_weights_at(move_task_order_id, if_match)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveTaskOrderApi->update_mto_reviewed_billable_weights_at: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move to use |
 **if_match** | **str**|  |

### Return type

[**Move**](Move.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated move task order billableWeightsReviewedAt field |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_status_service_counseling_completed**
> Move update_mto_status_service_counseling_completed(move_task_order_id, if_match)

Changes move (move task order) status to service counseling completed

Changes move (move task order) status to service counseling completed

### Example


```python
import time
import ghc_client
from ghc_client.api import move_task_order_api
from ghc_client.model.error import Error
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.move import Move
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = move_task_order_api.MoveTaskOrderApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move to use
    if_match = "If-Match_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Changes move (move task order) status to service counseling completed
        api_response = api_instance.update_mto_status_service_counseling_completed(move_task_order_id, if_match)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MoveTaskOrderApi->update_mto_status_service_counseling_completed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move to use |
 **if_match** | **str**|  |

### Return type

[**Move**](Move.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated move task order status |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

