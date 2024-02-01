# prime_client.PaymentRequestApi

All URIs are relative to */prime/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_request**](PaymentRequestApi.md#create_payment_request) | **POST** /payment-requests | createPaymentRequest
[**create_upload**](PaymentRequestApi.md#create_upload) | **POST** /payment-requests/{paymentRequestID}/uploads | createUpload


# **create_payment_request**
> PaymentRequest create_payment_request()

createPaymentRequest

Creates a new instance of a paymentRequest and is assigned the status `PENDING`. A move task order can have multiple payment requests, and a final payment request can be marked using boolean `isFinal`.  If a `PENDING` payment request is recalculated, a new payment request is created and the original request is marked with the status `DEPRECATED`.  **NOTE**: In order to create a payment request for most service items, the shipment *must* be updated with the `PrimeActualWeight` value via [updateMTOShipment](#operation/updateMTOShipment).  **FSC - Fuel Surcharge** service items require `ActualPickupDate` to be updated on the shipment.  A service item can be on several payment requests in the case of partial payment requests and payments.  In the request, if no params are necessary, then just the `serviceItem` `id` is required. For example: ```json {   \"isFinal\": false,   \"moveTaskOrderID\": \"uuid\",   \"serviceItems\": [     {       \"id\": \"uuid\",     },     {       \"id\": \"uuid\",       \"params\": [         {           \"key\": \"Service Item Parameter Name\",           \"value\": \"Service Item Parameter Value\"         }       ]     }   ],   \"pointOfContact\": \"string\" } ```  SIT Service Items & Accepted Payment Request Parameters: --- If `WeightBilled` is not provided then the full shipment weight (`PrimeActualWeight`) will be considered in the calculation.  **NOTE**: Diversions have a unique calcuation for payment requests without a `WeightBilled` parameter.  If you created a payment request for a diversion and `WeightBilled` is not provided, then the following will be used in the calculation: - The lowest shipment weight (`PrimeActualWeight`) found in the diverted shipment chain. - The lowest reweigh weight found in the diverted shipment chain.  The diverted shipment chain is created by referencing the `diversion` boolean, `divertedFromShipmentId` UUID, and matching destination to pickup addresses. If the chain cannot be established it will fall back to the `PrimeActualWeight` of the current shipment. This is utilized because diverted shipments are all one single shipment, but going to different locations. The lowest weight found is the true shipment weight, and thus we search the chain of shipments for the lowest weight found.  **DOFSIT - Domestic origin 1st day SIT** ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     }   ] ```  **DOASIT - Domestic origin add'l SIT** *(SITPaymentRequestStart & SITPaymentRequestEnd are **REQUIRED**)* *To create a paymentRequest for this service item, the `SITPaymentRequestStart` and `SITPaymentRequestEnd` dates must not overlap previously requested SIT dates.* ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     },     {       \"key\": \"SITPaymentRequestStart\",       \"value\": \"date\"     },     {       \"key\": \"SITPaymentRequestEnd\",       \"value\": \"date\"     }   ] ```  **DOPSIT - Domestic origin SIT pickup** ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     }   ] ```  **DOSHUT - Domestic origin shuttle service** ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     }   ] ```  **DDFSIT - Domestic destination 1st day SIT** ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     }   ] ```  **DDASIT - Domestic destination add'l SIT** *(SITPaymentRequestStart & SITPaymentRequestEnd are **REQUIRED**)* *To create a paymentRequest for this service item, the `SITPaymentRequestStart` and `SITPaymentRequestEnd` dates must not overlap previously requested SIT dates.* ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     },     {       \"key\": \"SITPaymentRequestStart\",       \"value\": \"date\"     },     {       \"key\": \"SITPaymentRequestEnd\",       \"value\": \"date\"     }   ] ```  **DDDSIT - Domestic destination SIT delivery** *To create a paymentRequest for this service item, it must first have a final address set via [updateMTOServiceItem](#operation/updateMTOServiceItem).* ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     }   ] ```  **DDSHUT - Domestic destination shuttle service** ```json   \"params\": [     {       \"key\": \"WeightBilled\",       \"value\": \"integer\"     }   ] ``` --- 

### Example


```python
import time
import prime_client
from prime_client.api import payment_request_api
from prime_client.model.validation_error import ValidationError
from prime_client.model.payment_request import PaymentRequest
from prime_client.model.error import Error
from prime_client.model.create_payment_request import CreatePaymentRequest
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
    api_instance = payment_request_api.PaymentRequestApi(api_client)
    body = CreatePaymentRequest(
        is_final=False,
        move_task_order_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        service_items=[
            ServiceItem(
                id="c56a4180-65aa-42ec-a945-5fd21dec0538",
                params=[
                    ServiceItemParamsInner(
                        key="Service Item Parameter Name",
                        value="Service Item Parameter Value",
                    ),
                ],
            ),
        ],
        point_of_contact="point_of_contact_example",
    ) # CreatePaymentRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # createPaymentRequest
        api_response = api_instance.create_payment_request(body=body)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling PaymentRequestApi->create_payment_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePaymentRequest**](CreatePaymentRequest.md)|  | [optional]

### Return type

[**PaymentRequest**](PaymentRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a paymentRequest object. |  -  |
**400** | Request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**409** | The request could not be processed because of conflict in the current state of the resource. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload**
> UploadWithOmissions create_upload(payment_request_id, file)

createUpload

### Functionality This endpoint **uploads** a Proof of Service document for a PaymentRequest.  The PaymentRequest should already exist.  Optional key of **isWeightTicket** indicates if the document is a weight ticket or not. This will be used for partial and full deliveries and makes it easier for the Transportation Invoicing Officers to locate and review service item documents. If left empty, it will assume it is NOT a weight ticket.  The formdata in the body of the POST request that is sent should look like this if it IS a weight ticket being attached to an existing payment request:   ```json   {     \"file\": \"filePath\",     \"isWeightTicket\": true   }   ```   If the proof of service doc is NOT a weight ticket, it will look like this - or you can leave it empty:   ```json   {     \"file\": \"filePath\",     \"isWeightTicket\": false   }   ```   ```json   {     \"file\": \"filePath\",   }   ```  PaymentRequests are created with the [createPaymentRequest](#operation/createPaymentRequest) endpoint. 

### Example


```python
import time
import prime_client
from prime_client.api import payment_request_api
from prime_client.model.upload_with_omissions import UploadWithOmissions
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
    api_instance = payment_request_api.PaymentRequestApi(api_client)
    payment_request_id = "paymentRequestID_example" # str | UUID of payment request to use.
    file = open('/path/to/file', 'rb') # file_type | The file to upload.
    is_weight_ticket = True # bool | Indicates whether the file is a weight ticket. (optional)

    # example passing only required values which don't have defaults set
    try:
        # createUpload
        api_response = api_instance.create_upload(payment_request_id, file)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling PaymentRequestApi->create_upload: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # createUpload
        api_response = api_instance.create_upload(payment_request_id, file, is_weight_ticket=is_weight_ticket)
        pprint(api_response)
    except prime_client.ApiException as e:
        print("Exception when calling PaymentRequestApi->create_upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_request_id** | **str**| UUID of payment request to use. |
 **file** | **file_type**| The file to upload. |
 **is_weight_ticket** | **bool**| Indicates whether the file is a weight ticket. | [optional]

### Return type

[**UploadWithOmissions**](UploadWithOmissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created upload of digital file. |  -  |
**400** | The request payload is invalid. |  -  |
**401** | The request was denied. |  -  |
**403** | The request was denied. |  -  |
**404** | The requested resource wasn&#39;t found. |  -  |
**422** | The request was unprocessable, likely due to bad input from the requester. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

