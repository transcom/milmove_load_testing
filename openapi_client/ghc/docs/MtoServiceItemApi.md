# ghc_client.MtoServiceItemApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_sit_address_update**](MtoServiceItemApi.md#approve_sit_address_update) | **PATCH** /sit-address-update/{sitAddressUpdateID}/approve | Approves a SIT Address Update
[**create_sit_address_update**](MtoServiceItemApi.md#create_sit_address_update) | **POST** /service-items/{mtoServiceItemID}/sit-address-update | Create an approved SIT Address Update
[**get_mto_service_item**](MtoServiceItemApi.md#get_mto_service_item) | **GET** /move-task-orders/{moveTaskOrderID}/service-items/{mtoServiceItemID} | Gets a line item by ID for a move by ID
[**list_mto_service_items**](MtoServiceItemApi.md#list_mto_service_items) | **GET** /move_task_orders/{moveTaskOrderID}/mto_service_items | Gets all line items for a move
[**reject_sit_address_update**](MtoServiceItemApi.md#reject_sit_address_update) | **PATCH** /sit-address-update/{sitAddressUpdateID}/reject | Rejects a SIT Address Update
[**update_mto_service_item**](MtoServiceItemApi.md#update_mto_service_item) | **PATCH** /move-task-orders/{moveTaskOrderID}/service-items/{mtoServiceItemID} | Updates a service item by ID for a move by ID
[**update_mto_service_item_status**](MtoServiceItemApi.md#update_mto_service_item_status) | **PATCH** /move-task-orders/{moveTaskOrderID}/service-items/{mtoServiceItemID}/status | Change the status of a line item for a move by ID


# **approve_sit_address_update**
> MTOServiceItem approve_sit_address_update(sit_address_update_id, if_match, body)

Approves a SIT Address Update

This endpoint is used to approve a SIT address update. Office remarks are required. Approving the SIT address update will update the SIT Destination Final Address of the associated service item

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_service_item_api
from ghc_client.model.error import Error
from ghc_client.model.mto_service_item import MTOServiceItem
from ghc_client.model.patch_sit_address_update_status import PatchSITAddressUpdateStatus
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
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    sit_address_update_id = "sitAddressUpdateID_example" # str | ID of the sit address update
    if_match = "If-Match_example" # str | 
    body = PatchSITAddressUpdateStatus(
        office_remarks="Insufficient details provided",
    ) # PatchSITAddressUpdateStatus | 

    # example passing only required values which don't have defaults set
    try:
        # Approves a SIT Address Update
        api_response = api_instance.approve_sit_address_update(sit_address_update_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->approve_sit_address_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sit_address_update_id** | **str**| ID of the sit address update |
 **if_match** | **str**|  |
 **body** | [**PatchSITAddressUpdateStatus**](PatchSITAddressUpdateStatus.md)|  |

### Return type

[**MTOServiceItem**](MTOServiceItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully approved a SIT address update |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sit_address_update**
> MTOServiceItem create_sit_address_update(mto_service_item_id, body)

Create an approved SIT Address Update

TOO can create an already-approved SIT Address Update on behalf of a customer

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_service_item_api
from ghc_client.model.error import Error
from ghc_client.model.mto_service_item import MTOServiceItem
from ghc_client.model.create_sit_address_update import CreateSITAddressUpdate
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
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    mto_service_item_id = "mtoServiceItemID_example" # str | ID of line item to use
    body = CreateSITAddressUpdate(
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
        office_remarks="office_remarks_example",
    ) # CreateSITAddressUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Create an approved SIT Address Update
        api_response = api_instance.create_sit_address_update(mto_service_item_id, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->create_sit_address_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mto_service_item_id** | **str**| ID of line item to use |
 **body** | [**CreateSITAddressUpdate**](CreateSITAddressUpdate.md)|  |

### Return type

[**MTOServiceItem**](MTOServiceItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a SIT Address Update. |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mto_service_item**
> MTOServiceItem get_mto_service_item(move_task_order_id, mto_service_item_id)

Gets a line item by ID for a move by ID

Gets a line item by ID for a move by ID

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_service_item_api
from ghc_client.model.error import Error
from ghc_client.model.mto_service_item import MTOServiceItem
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move to use
    mto_service_item_id = "mtoServiceItemID_example" # str | ID of line item to use

    # example passing only required values which don't have defaults set
    try:
        # Gets a line item by ID for a move by ID
        api_response = api_instance.get_mto_service_item(move_task_order_id, mto_service_item_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->get_mto_service_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move to use |
 **mto_service_item_id** | **str**| ID of line item to use |

### Return type

[**MTOServiceItem**](MTOServiceItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved a line item for a move task order by ID |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mto_service_items**
> MTOServiceItems list_mto_service_items(move_task_order_id)

Gets all line items for a move

Gets all line items for a move

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_service_item_api
from ghc_client.model.error import Error
from ghc_client.model.mto_service_items import MTOServiceItems
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
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move for mto service item to use

    # example passing only required values which don't have defaults set
    try:
        # Gets all line items for a move
        api_response = api_instance.list_mto_service_items(move_task_order_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->list_mto_service_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move for mto service item to use |

### Return type

[**MTOServiceItems**](MTOServiceItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved all line items for a move task order |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_sit_address_update**
> MTOServiceItem reject_sit_address_update(sit_address_update_id, if_match, body)

Rejects a SIT Address Update

This endpoint is used to reject a requested SIT address update. Office remarks are required. Rejecting the SIT address update will not update the SIT Destination Final Address.

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_service_item_api
from ghc_client.model.error import Error
from ghc_client.model.mto_service_item import MTOServiceItem
from ghc_client.model.patch_sit_address_update_status import PatchSITAddressUpdateStatus
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
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    sit_address_update_id = "sitAddressUpdateID_example" # str | ID of the sit address update
    if_match = "If-Match_example" # str | 
    body = PatchSITAddressUpdateStatus(
        office_remarks="Insufficient details provided",
    ) # PatchSITAddressUpdateStatus | 

    # example passing only required values which don't have defaults set
    try:
        # Rejects a SIT Address Update
        api_response = api_instance.reject_sit_address_update(sit_address_update_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->reject_sit_address_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sit_address_update_id** | **str**| ID of the sit address update |
 **if_match** | **str**|  |
 **body** | [**PatchSITAddressUpdateStatus**](PatchSITAddressUpdateStatus.md)|  |

### Return type

[**MTOServiceItem**](MTOServiceItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully rejected a SIT address update |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_service_item**
> MoveTaskOrder update_mto_service_item(move_task_order_id, mto_service_item_id, if_match, body)

Updates a service item by ID for a move by ID

Updates a service item by ID for a move by ID

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_service_item_api
from ghc_client.model.error import Error
from ghc_client.model.move_task_order import MoveTaskOrder
from ghc_client.model.mto_service_item import MTOServiceItem
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move to use
    mto_service_item_id = "mtoServiceItemID_example" # str | ID of line item to use
    if_match = "If-Match_example" # str | 
    body = MTOServiceItem(
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
        sit_destination_original_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
        ),
        sit_destination_final_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
        ),
        sit_address_updates=SITAddressUpdates([
            SITAddressUpdate(
                id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                mto_service_item_id="1f2270c7-7166-40ae-981e-b200ebdf3054",
                distance=54,
                contractor_remarks="The customer has found a new house closer to base.",
                office_remarks="The customer has found a new house closer to base.",
                status="REQUESTED",
                old_address=Address(
                    id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                    street_address1="123 Main Ave",
                    street_address2="Apartment 9000",
                    street_address3="Montmârtre",
                    city="Anytown",
                    state="AL",
                    postal_code="90210",
                    country="USA",
                ),
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
            ),
        ]),
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
    ) # MTOServiceItem | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a service item by ID for a move by ID
        api_response = api_instance.update_mto_service_item(move_task_order_id, mto_service_item_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->update_mto_service_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move to use |
 **mto_service_item_id** | **str**| ID of line item to use |
 **if_match** | **str**|  |
 **body** | [**MTOServiceItem**](MTOServiceItem.md)|  |

### Return type

[**MoveTaskOrder**](MoveTaskOrder.md)

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
**412** | Precondition failed |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mto_service_item_status**
> MTOServiceItem update_mto_service_item_status(move_task_order_id, mto_service_item_id, if_match, body)

Change the status of a line item for a move by ID

Changes the status of a line item for a move by ID

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_service_item_api
from ghc_client.model.error import Error
from ghc_client.model.mto_service_item import MTOServiceItem
from ghc_client.model.patch_mto_service_item_status_payload import PatchMTOServiceItemStatusPayload
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
    api_instance = mto_service_item_api.MtoServiceItemApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move to use
    mto_service_item_id = "mtoServiceItemID_example" # str | ID of line item to use
    if_match = "If-Match_example" # str | 
    body = PatchMTOServiceItemStatusPayload(
        status="SUBMITTED",
        rejection_reason="Insufficent details provided",
    ) # PatchMTOServiceItemStatusPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Change the status of a line item for a move by ID
        api_response = api_instance.update_mto_service_item_status(move_task_order_id, mto_service_item_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoServiceItemApi->update_mto_service_item_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move to use |
 **mto_service_item_id** | **str**| ID of line item to use |
 **if_match** | **str**|  |
 **body** | [**PatchMTOServiceItemStatusPayload**](PatchMTOServiceItemStatusPayload.md)|  |

### Return type

[**MTOServiceItem**](MTOServiceItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated status for a line item for a move task order by ID |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

