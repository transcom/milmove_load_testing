# ghc_client.PaymentServiceItemApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_payment_service_item_status**](PaymentServiceItemApi.md#update_payment_service_item_status) | **PATCH** /move-task-orders/{moveTaskOrderID}/payment-service-items/{paymentServiceItemID}/status | Change the status of a payment service item for a move by ID


# **update_payment_service_item_status**
> PaymentServiceItem update_payment_service_item_status(move_task_order_id, payment_service_item_id, if_match, body)

Change the status of a payment service item for a move by ID

Changes the status of a line item for a move by ID

### Example


```python
import time
import ghc_client
from ghc_client.api import payment_service_item_api
from ghc_client.model.payment_service_item import PaymentServiceItem
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
    api_instance = payment_service_item_api.PaymentServiceItemApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move to use
    payment_service_item_id = "paymentServiceItemID_example" # str | ID of payment service item to use
    if_match = "If-Match_example" # str | 
    body = PaymentServiceItem(
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        payment_request_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        mto_service_item_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        mto_service_item_code="DLH",
        mto_service_item_name="Move management",
        mto_shipment_type=MTOShipmentType("HHG"),
        mto_shipment_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        status=PaymentServiceItemStatus("REQUESTED"),
        price_cents=1,
        rejection_reason="documentation was incomplete",
        payment_service_item_params=PaymentServiceItemParams([
            PaymentServiceItemParam(
                payment_service_item_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                key=ServiceItemParamName("ActualPickupDate"),
                value="3025",
                type=ServiceItemParamType("STRING"),
                origin=ServiceItemParamOrigin("PRIME"),
                e_tag="e_tag_example",
            ),
        ]),
        e_tag="e_tag_example",
    ) # PaymentServiceItem | 

    # example passing only required values which don't have defaults set
    try:
        # Change the status of a payment service item for a move by ID
        api_response = api_instance.update_payment_service_item_status(move_task_order_id, payment_service_item_id, if_match, body)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling PaymentServiceItemApi->update_payment_service_item_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move to use |
 **payment_service_item_id** | **str**| ID of payment service item to use |
 **if_match** | **str**|  |
 **body** | [**PaymentServiceItem**](PaymentServiceItem.md)|  |

### Return type

[**PaymentServiceItem**](PaymentServiceItem.md)

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

