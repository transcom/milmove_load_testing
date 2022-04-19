# ghc_client.OrderApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_excess_weight_risk**](OrderApi.md#acknowledge_excess_weight_risk) | **POST** /orders/{orderID}/acknowledge-excess-weight-risk | Saves the date and time a TOO acknowledged the excess weight risk by dismissing the alert
[**counseling_update_allowance**](OrderApi.md#counseling_update_allowance) | **PATCH** /counseling/orders/{orderID}/allowances | Updates an allowance (Orders with Entitlements)
[**counseling_update_order**](OrderApi.md#counseling_update_order) | **PATCH** /counseling/orders/{orderID} | Updates an order (performed by a services counselor)
[**get_order**](OrderApi.md#get_order) | **GET** /orders/{orderID} | Gets an order by ID
[**tac_validation**](OrderApi.md#tac_validation) | **GET** /tac/valid | Validation of a TAC value
[**update_allowance**](OrderApi.md#update_allowance) | **PATCH** /orders/{orderID}/allowances | Updates an allowance (Orders with Entitlements)
[**update_billable_weight**](OrderApi.md#update_billable_weight) | **PATCH** /orders/{orderID}/update-billable-weight | Updates the max billable weight
[**update_max_billable_weight_as_tio**](OrderApi.md#update_max_billable_weight_as_tio) | **PATCH** /orders/{orderID}/update-max-billable-weight/tio | Updates the max billable weight with TIO remarks
[**update_order**](OrderApi.md#update_order) | **PATCH** /orders/{orderID} | Updates an order


# **acknowledge_excess_weight_risk**
> Move acknowledge_excess_weight_risk(order_id, if_match)

Saves the date and time a TOO acknowledged the excess weight risk by dismissing the alert

Saves the date and time a TOO acknowledged the excess weight risk by dismissing the alert

### Example


```python
import time
import ghc_client
from ghc_client.api import order_api
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
    api_instance = order_api.OrderApi(api_client)
    order_id = "orderID_example" # str | ID of order to use
    if_match = "If-Match_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Saves the date and time a TOO acknowledged the excess weight risk by dismissing the alert
        api_response = api_instance.acknowledge_excess_weight_risk(order_id, if_match)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling OrderApi->acknowledge_excess_weight_risk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of order to use |
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
**200** | updated Move |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **counseling_update_allowance**
> Order counseling_update_allowance(order_id, if_match, body)

Updates an allowance (Orders with Entitlements)

All fields sent in this request will be set on the order referenced

### Example


```python
import time
import ghc_client
from ghc_client.api import order_api
from ghc_client.model.order import Order
from ghc_client.model.counseling_update_allowance_payload import CounselingUpdateAllowancePayload
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
    api_instance = order_api.OrderApi(api_client)
    order_id = "orderID_example" # str | ID of order to use
    if_match = "If-Match_example" # str | 
    body = CounselingUpdateAllowancePayload(
        grade=Grade("E_1"),
        dependents_authorized=True,
        agency=Affiliation("ARMY"),
        pro_gear_weight=2000,
        pro_gear_weight_spouse=2000,
        required_medical_equipment_weight=2000,
        organizational_clothing_and_individual_equipment=True,
        storage_in_transit=0,
    ) # CounselingUpdateAllowancePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an allowance (Orders with Entitlements)
        api_response = api_instance.counseling_update_allowance(order_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling OrderApi->counseling_update_allowance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of order to use |
 **if_match** | **str**|  |
 **body** | [**CounselingUpdateAllowancePayload**](CounselingUpdateAllowancePayload.md)|  |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of allowance |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **counseling_update_order**
> Order counseling_update_order(order_id, if_match, body)

Updates an order (performed by a services counselor)

All fields sent in this request will be set on the order referenced

### Example


```python
import time
import ghc_client
from ghc_client.api import order_api
from ghc_client.model.order import Order
from ghc_client.model.counseling_update_order_payload import CounselingUpdateOrderPayload
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
    api_instance = order_api.OrderApi(api_client)
    order_id = "orderID_example" # str | ID of order to update
    if_match = "If-Match_example" # str | 
    body = CounselingUpdateOrderPayload(
        issue_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        report_by_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        orders_type=OrdersType("PERMANENT_CHANGE_OF_STATION"),
        origin_duty_location_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        new_duty_location_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        tac="F8J1",
        sac="sac_example",
        nts_tac="nts_tac_example",
        nts_sac="nts_sac_example",
    ) # CounselingUpdateOrderPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an order (performed by a services counselor)
        api_response = api_instance.counseling_update_order(order_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling OrderApi->counseling_update_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of order to update |
 **if_match** | **str**|  |
 **body** | [**CounselingUpdateOrderPayload**](CounselingUpdateOrderPayload.md)|  |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of orders |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> Order get_order(order_id)

Gets an order by ID

Gets an order

### Example


```python
import time
import ghc_client
from ghc_client.api import order_api
from ghc_client.model.order import Order
from ghc_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = order_api.OrderApi(api_client)
    order_id = "orderID_example" # str | ID of order to use

    # example passing only required values which don't have defaults set
    try:
        # Gets an order by ID
        api_response = api_instance.get_order(order_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling OrderApi->get_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of order to use |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved order |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tac_validation**
> TacValid tac_validation(tac)

Validation of a TAC value

Returns a boolean based on whether a tac value is valid or not

### Example


```python
import time
import ghc_client
from ghc_client.api import order_api
from ghc_client.model.error import Error
from ghc_client.model.tac_valid import TacValid
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = order_api.OrderApi(api_client)
    tac = "tac_example" # str | The tac value to validate

    # example passing only required values which don't have defaults set
    try:
        # Validation of a TAC value
        api_response = api_instance.tac_validation(tac)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling OrderApi->tac_validation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tac** | **str**| The tac value to validate |

### Return type

[**TacValid**](TacValid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved validation status |  -  |
**400** | The request payload is invalid |  -  |
**401** | The request was denied |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_allowance**
> Order update_allowance(order_id, if_match, body)

Updates an allowance (Orders with Entitlements)

All fields sent in this request will be set on the order referenced

### Example


```python
import time
import ghc_client
from ghc_client.api import order_api
from ghc_client.model.order import Order
from ghc_client.model.error import Error
from ghc_client.model.update_allowance_payload import UpdateAllowancePayload
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
    api_instance = order_api.OrderApi(api_client)
    order_id = "orderID_example" # str | ID of order to use
    if_match = "If-Match_example" # str | 
    body = UpdateAllowancePayload(
        authorized_weight=2000,
        grade=Grade("E_1"),
        dependents_authorized=True,
        agency=Affiliation("ARMY"),
        pro_gear_weight=2000,
        pro_gear_weight_spouse=500,
        required_medical_equipment_weight=2000,
        organizational_clothing_and_individual_equipment=True,
        storage_in_transit=0,
    ) # UpdateAllowancePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an allowance (Orders with Entitlements)
        api_response = api_instance.update_allowance(order_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling OrderApi->update_allowance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of order to use |
 **if_match** | **str**|  |
 **body** | [**UpdateAllowancePayload**](UpdateAllowancePayload.md)|  |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of allowance |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billable_weight**
> Order update_billable_weight(order_id, if_match, body)

Updates the max billable weight

Updates the DBAuthorizedWeight attribute for the Order Entitlements=

### Example


```python
import time
import ghc_client
from ghc_client.api import order_api
from ghc_client.model.order import Order
from ghc_client.model.error import Error
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.update_billable_weight_payload import UpdateBillableWeightPayload
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = order_api.OrderApi(api_client)
    order_id = "orderID_example" # str | ID of order to use
    if_match = "If-Match_example" # str | 
    body = UpdateBillableWeightPayload(
        authorized_weight=2000,
    ) # UpdateBillableWeightPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the max billable weight
        api_response = api_instance.update_billable_weight(order_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling OrderApi->update_billable_weight: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of order to use |
 **if_match** | **str**|  |
 **body** | [**UpdateBillableWeightPayload**](UpdateBillableWeightPayload.md)|  |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated Order |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_max_billable_weight_as_tio**
> Order update_max_billable_weight_as_tio(order_id, if_match, body)

Updates the max billable weight with TIO remarks

Updates the DBAuthorizedWeight attribute for the Order Entitlements and move TIO remarks

### Example


```python
import time
import ghc_client
from ghc_client.api import order_api
from ghc_client.model.order import Order
from ghc_client.model.error import Error
from ghc_client.model.validation_error import ValidationError
from ghc_client.model.update_max_billable_weight_as_tio_payload import UpdateMaxBillableWeightAsTIOPayload
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = order_api.OrderApi(api_client)
    order_id = "orderID_example" # str | ID of order to use
    if_match = "If-Match_example" # str | Optimistic locking is implemented via the `If-Match` header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a `412 Precondition Failed` error. 
    body = UpdateMaxBillableWeightAsTIOPayload(
        authorized_weight=2000,
        tio_remarks="Increasing max billable weight",
    ) # UpdateMaxBillableWeightAsTIOPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the max billable weight with TIO remarks
        api_response = api_instance.update_max_billable_weight_as_tio(order_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling OrderApi->update_max_billable_weight_as_tio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of order to use |
 **if_match** | **str**| Optimistic locking is implemented via the &#x60;If-Match&#x60; header. If the ETag header does not match the value of the resource on the server, the server rejects the change with a &#x60;412 Precondition Failed&#x60; error.  |
 **body** | [**UpdateMaxBillableWeightAsTIOPayload**](UpdateMaxBillableWeightAsTIOPayload.md)|  |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated Order |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order**
> Order update_order(order_id, if_match, body)

Updates an order

All fields sent in this request will be set on the order referenced

### Example


```python
import time
import ghc_client
from ghc_client.api import order_api
from ghc_client.model.order import Order
from ghc_client.model.error import Error
from ghc_client.model.update_order_payload import UpdateOrderPayload
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
    api_instance = order_api.OrderApi(api_client)
    order_id = "orderID_example" # str | ID of order to use
    if_match = "If-Match_example" # str | 
    body = UpdateOrderPayload(
        issue_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        report_by_date=dateutil_parser('Thu Apr 26 00:00:00 UTC 2018').date(),
        orders_type=OrdersType("PERMANENT_CHANGE_OF_STATION"),
        orders_type_detail=OrdersTypeDetail("HHG_PERMITTED"),
        origin_duty_location_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        new_duty_location_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        orders_number="030-00362",
        tac="F8J1",
        sac="sac_example",
        nts_tac="nts_tac_example",
        nts_sac="nts_sac_example",
        department_indicator=DeptIndicator("NAVY_AND_MARINES"),
        orders_acknowledgement=True,
    ) # UpdateOrderPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an order
        api_response = api_instance.update_order(order_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling OrderApi->update_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID of order to use |
 **if_match** | **str**|  |
 **body** | [**UpdateOrderPayload**](UpdateOrderPayload.md)|  |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of orders |  -  |
**400** | The request payload is invalid |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

