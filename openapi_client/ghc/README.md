# ghc-client
The API for move.mil

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import ghc_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ghc_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import ghc_client
from pprint import pprint
from ghc_client.api import customer_api
from ghc_client.model.customer import Customer
from ghc_client.model.error import Error
from ghc_client.model.update_customer_payload import UpdateCustomerPayload
from ghc_client.model.validation_error import ValidationError
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)



# Enter a context with an instance of the API client
with ghc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = customer_api.CustomerApi(api_client)
    customer_id = "customerID_example" # str | ID of customer to use

    try:
        # Returns a given customer
        api_response = api_instance.get_customer(customer_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling CustomerApi->get_customer: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */ghc/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CustomerApi* | [**get_customer**](docs/CustomerApi.md#get_customer) | **GET** /customer/{customerID} | Returns a given customer
*CustomerApi* | [**update_customer**](docs/CustomerApi.md#update_customer) | **PATCH** /customer/{customerID} | Updates customer info
*GhcDocumentsApi* | [**get_document**](docs/GhcDocumentsApi.md#get_document) | **GET** /documents/{documentId} | Returns a document
*MoveApi* | [**get_move**](docs/MoveApi.md#get_move) | **GET** /move/{locator} | Returns a given move
*MoveApi* | [**set_financial_review_flag**](docs/MoveApi.md#set_financial_review_flag) | **POST** /moves/{moveID}/financial-review-flag | Flags a move for financial office review
*MoveTaskOrderApi* | [**get_entitlements**](docs/MoveTaskOrderApi.md#get_entitlements) | **GET** /move-task-orders/{moveTaskOrderID}/entitlements | Gets entitlements for a move by ID
*MoveTaskOrderApi* | [**get_move_task_order**](docs/MoveTaskOrderApi.md#get_move_task_order) | **GET** /move-task-orders/{moveTaskOrderID} | Gets a move by ID
*MoveTaskOrderApi* | [**update_move_task_order**](docs/MoveTaskOrderApi.md#update_move_task_order) | **PATCH** /move-task-orders/{moveTaskOrderID} | Updates a move by ID
*MoveTaskOrderApi* | [**update_move_task_order_status**](docs/MoveTaskOrderApi.md#update_move_task_order_status) | **PATCH** /move-task-orders/{moveTaskOrderID}/status | Change the status of a move task order to make it available to prime
*MoveTaskOrderApi* | [**update_move_tio_remarks**](docs/MoveTaskOrderApi.md#update_move_tio_remarks) | **PATCH** /move-task-orders/{moveTaskOrderID}/tio-remarks | 
*MoveTaskOrderApi* | [**update_mto_reviewed_billable_weights_at**](docs/MoveTaskOrderApi.md#update_mto_reviewed_billable_weights_at) | **PATCH** /move-task-orders/{moveTaskOrderID}/billable-weights-reviewed-at | 
*MoveTaskOrderApi* | [**update_mto_status_service_counseling_completed**](docs/MoveTaskOrderApi.md#update_mto_status_service_counseling_completed) | **PATCH** /move-task-orders/{moveTaskOrderID}/status/service-counseling-completed | Changes move (move task order) status to service counseling completed
*MtoAgentApi* | [**fetch_mto_agent_list**](docs/MtoAgentApi.md#fetch_mto_agent_list) | **GET** /move_task_orders/{moveTaskOrderID}/mto_shipments/{shipmentID}/mto-agents | Fetch move task order agents.
*MtoServiceItemApi* | [**get_mto_service_item**](docs/MtoServiceItemApi.md#get_mto_service_item) | **GET** /move-task-orders/{moveTaskOrderID}/service-items/{mtoServiceItemID} | Gets a line item by ID for a move by ID
*MtoServiceItemApi* | [**list_mto_service_items**](docs/MtoServiceItemApi.md#list_mto_service_items) | **GET** /move_task_orders/{moveTaskOrderID}/mto_service_items | Gets all line items for a move
*MtoServiceItemApi* | [**update_mto_service_item**](docs/MtoServiceItemApi.md#update_mto_service_item) | **PATCH** /move-task-orders/{moveTaskOrderID}/service-items/{mtoServiceItemID} | Updates a service item by ID for a move by ID
*MtoServiceItemApi* | [**update_mto_service_item_status**](docs/MtoServiceItemApi.md#update_mto_service_item_status) | **PATCH** /move-task-orders/{moveTaskOrderID}/service-items/{mtoServiceItemID}/status | Change the status of a line item for a move by ID
*MtoShipmentApi* | [**create_mto_shipment**](docs/MtoShipmentApi.md#create_mto_shipment) | **POST** /mto-shipments | createMTOShipment
*MtoShipmentApi* | [**list_mto_shipments**](docs/MtoShipmentApi.md#list_mto_shipments) | **GET** /move_task_orders/{moveTaskOrderID}/mto_shipments | Gets all shipments for a move task order
*MtoShipmentApi* | [**update_mto_shipment**](docs/MtoShipmentApi.md#update_mto_shipment) | **PATCH** /move_task_orders/{moveTaskOrderID}/mto_shipments/{shipmentID} | updateMTOShipment
*OrderApi* | [**acknowledge_excess_weight_risk**](docs/OrderApi.md#acknowledge_excess_weight_risk) | **POST** /orders/{orderID}/acknowledge-excess-weight-risk | Saves the date and time a TOO acknowledged the excess weight risk by dismissing the alert
*OrderApi* | [**counseling_update_allowance**](docs/OrderApi.md#counseling_update_allowance) | **PATCH** /counseling/orders/{orderID}/allowances | Updates an allowance (Orders with Entitlements)
*OrderApi* | [**counseling_update_order**](docs/OrderApi.md#counseling_update_order) | **PATCH** /counseling/orders/{orderID} | Updates an order (performed by a services counselor)
*OrderApi* | [**get_order**](docs/OrderApi.md#get_order) | **GET** /orders/{orderID} | Gets an order by ID
*OrderApi* | [**tac_validation**](docs/OrderApi.md#tac_validation) | **GET** /tac/valid | Validation of a TAC value
*OrderApi* | [**update_allowance**](docs/OrderApi.md#update_allowance) | **PATCH** /orders/{orderID}/allowances | Updates an allowance (Orders with Entitlements)
*OrderApi* | [**update_billable_weight**](docs/OrderApi.md#update_billable_weight) | **PATCH** /orders/{orderID}/update-billable-weight | Updates the max billable weight
*OrderApi* | [**update_max_billable_weight_as_tio**](docs/OrderApi.md#update_max_billable_weight_as_tio) | **PATCH** /orders/{orderID}/update-max-billable-weight/tio | Updates the max billable weight with TIO remarks
*OrderApi* | [**update_order**](docs/OrderApi.md#update_order) | **PATCH** /orders/{orderID} | Updates an order
*PaymentRequestsApi* | [**get_payment_request**](docs/PaymentRequestsApi.md#get_payment_request) | **GET** /payment-requests/{paymentRequestID} | Fetches a payment request by id
*PaymentRequestsApi* | [**get_payment_requests_for_move**](docs/PaymentRequestsApi.md#get_payment_requests_for_move) | **GET** /moves/{locator}/payment-requests | Fetches payment requests using the move code (locator).
*PaymentRequestsApi* | [**get_shipments_payment_sit_balance**](docs/PaymentRequestsApi.md#get_shipments_payment_sit_balance) | **GET** /payment-requests/{paymentRequestID}/shipments-payment-sit-balance | Returns all shipment payment request SIT usage to support partial SIT invoicing
*PaymentRequestsApi* | [**update_payment_request_status**](docs/PaymentRequestsApi.md#update_payment_request_status) | **PATCH** /payment-requests/{paymentRequestID}/status | Updates status of a payment request by id
*PaymentServiceItemApi* | [**update_payment_service_item_status**](docs/PaymentServiceItemApi.md#update_payment_service_item_status) | **PATCH** /move-task-orders/{moveTaskOrderID}/payment-service-items/{paymentServiceItemID}/status | Change the status of a payment service item for a move by ID
*QueuesApi* | [**get_moves_queue**](docs/QueuesApi.md#get_moves_queue) | **GET** /queues/moves | Gets queued list of all customer moves by GBLOC origin
*QueuesApi* | [**get_payment_requests_queue**](docs/QueuesApi.md#get_payment_requests_queue) | **GET** /queues/payment-requests | Gets queued list of all payment requests by GBLOC origin
*QueuesApi* | [**get_services_counseling_queue**](docs/QueuesApi.md#get_services_counseling_queue) | **GET** /queues/counseling | Gets queued list of all customer moves needing services counseling by GBLOC origin
*ReweighApi* | [**request_shipment_reweigh**](docs/ReweighApi.md#request_shipment_reweigh) | **POST** /shipments/{shipmentID}/request-reweigh | Requests a shipment reweigh
*ShipmentApi* | [**approve_shipment**](docs/ShipmentApi.md#approve_shipment) | **POST** /shipments/{shipmentID}/approve | Approves a shipment
*ShipmentApi* | [**approve_shipment_diversion**](docs/ShipmentApi.md#approve_shipment_diversion) | **POST** /shipments/{shipmentID}/approve-diversion | Approves a shipment diversion
*ShipmentApi* | [**approve_sit_extension**](docs/ShipmentApi.md#approve_sit_extension) | **PATCH** /shipments/{shipmentID}/sit-extensions/{sitExtensionID}/approve | Approves a SIT extension
*ShipmentApi* | [**create_sit_extension_as_too**](docs/ShipmentApi.md#create_sit_extension_as_too) | **POST** /shipments/{shipmentID}/sit-extensions/ | Create an approved SIT extension
*ShipmentApi* | [**delete_shipment**](docs/ShipmentApi.md#delete_shipment) | **DELETE** /shipments/{shipmentID} | Soft deletes a shipment by ID
*ShipmentApi* | [**deny_sit_extension**](docs/ShipmentApi.md#deny_sit_extension) | **PATCH** /shipments/{shipmentID}/sit-extensions/{sitExtensionID}/deny | Denies a SIT extension
*ShipmentApi* | [**reject_shipment**](docs/ShipmentApi.md#reject_shipment) | **POST** /shipments/{shipmentID}/reject | rejects a shipment
*ShipmentApi* | [**request_shipment_cancellation**](docs/ShipmentApi.md#request_shipment_cancellation) | **POST** /shipments/{shipmentID}/request-cancellation | Requests a shipment cancellation
*ShipmentApi* | [**request_shipment_diversion**](docs/ShipmentApi.md#request_shipment_diversion) | **POST** /shipments/{shipmentID}/request-diversion | Requests a shipment diversion
*ShipmentApi* | [**request_shipment_reweigh**](docs/ShipmentApi.md#request_shipment_reweigh) | **POST** /shipments/{shipmentID}/request-reweigh | Requests a shipment reweigh
*SitExtensionApi* | [**approve_sit_extension**](docs/SitExtensionApi.md#approve_sit_extension) | **PATCH** /shipments/{shipmentID}/sit-extensions/{sitExtensionID}/approve | Approves a SIT extension
*SitExtensionApi* | [**create_sit_extension_as_too**](docs/SitExtensionApi.md#create_sit_extension_as_too) | **POST** /shipments/{shipmentID}/sit-extensions/ | Create an approved SIT extension
*SitExtensionApi* | [**deny_sit_extension**](docs/SitExtensionApi.md#deny_sit_extension) | **PATCH** /shipments/{shipmentID}/sit-extensions/{sitExtensionID}/deny | Denies a SIT extension
*TacApi* | [**tac_validation**](docs/TacApi.md#tac_validation) | **GET** /tac/valid | Validation of a TAC value


## Documentation For Models

 - [Address](docs/Address.md)
 - [ApproveSITExtension](docs/ApproveSITExtension.md)
 - [BackupContact](docs/BackupContact.md)
 - [Branch](docs/Branch.md)
 - [ClientError](docs/ClientError.md)
 - [Contractor](docs/Contractor.md)
 - [CounselingUpdateAllowancePayload](docs/CounselingUpdateAllowancePayload.md)
 - [CounselingUpdateOrderPayload](docs/CounselingUpdateOrderPayload.md)
 - [CreateMTOShipment](docs/CreateMTOShipment.md)
 - [CreateSITExtensionAsTOO](docs/CreateSITExtensionAsTOO.md)
 - [Customer](docs/Customer.md)
 - [CustomerContactType](docs/CustomerContactType.md)
 - [DenySITExtension](docs/DenySITExtension.md)
 - [DeptIndicator](docs/DeptIndicator.md)
 - [DestinationType](docs/DestinationType.md)
 - [DimensionType](docs/DimensionType.md)
 - [DocumentPayload](docs/DocumentPayload.md)
 - [DutyLocation](docs/DutyLocation.md)
 - [Entitlements](docs/Entitlements.md)
 - [Error](docs/Error.md)
 - [GBLOC](docs/GBLOC.md)
 - [Grade](docs/Grade.md)
 - [InlineObject](docs/InlineObject.md)
 - [LOAType](docs/LOAType.md)
 - [MTOAgent](docs/MTOAgent.md)
 - [MTOAgents](docs/MTOAgents.md)
 - [MTOApprovalServiceItemCodes](docs/MTOApprovalServiceItemCodes.md)
 - [MTOServiceItem](docs/MTOServiceItem.md)
 - [MTOServiceItemCustomerContact](docs/MTOServiceItemCustomerContact.md)
 - [MTOServiceItemCustomerContacts](docs/MTOServiceItemCustomerContacts.md)
 - [MTOServiceItemDimension](docs/MTOServiceItemDimension.md)
 - [MTOServiceItemDimensions](docs/MTOServiceItemDimensions.md)
 - [MTOServiceItemStatus](docs/MTOServiceItemStatus.md)
 - [MTOServiceItems](docs/MTOServiceItems.md)
 - [MTOShipment](docs/MTOShipment.md)
 - [MTOShipmentStatus](docs/MTOShipmentStatus.md)
 - [MTOShipmentType](docs/MTOShipmentType.md)
 - [MTOShipments](docs/MTOShipments.md)
 - [Move](docs/Move.md)
 - [MoveStatus](docs/MoveStatus.md)
 - [MoveTaskOrder](docs/MoveTaskOrder.md)
 - [MoveTaskOrders](docs/MoveTaskOrders.md)
 - [Order](docs/Order.md)
 - [OrdersType](docs/OrdersType.md)
 - [OrdersTypeDetail](docs/OrdersTypeDetail.md)
 - [PatchMTOServiceItemStatusPayload](docs/PatchMTOServiceItemStatusPayload.md)
 - [PaymentRequest](docs/PaymentRequest.md)
 - [PaymentRequestStatus](docs/PaymentRequestStatus.md)
 - [PaymentRequests](docs/PaymentRequests.md)
 - [PaymentServiceItem](docs/PaymentServiceItem.md)
 - [PaymentServiceItemParam](docs/PaymentServiceItemParam.md)
 - [PaymentServiceItemParams](docs/PaymentServiceItemParams.md)
 - [PaymentServiceItemStatus](docs/PaymentServiceItemStatus.md)
 - [PaymentServiceItems](docs/PaymentServiceItems.md)
 - [ProofOfServiceDoc](docs/ProofOfServiceDoc.md)
 - [ProofOfServiceDocs](docs/ProofOfServiceDocs.md)
 - [QueueMove](docs/QueueMove.md)
 - [QueueMoves](docs/QueueMoves.md)
 - [QueueMovesResult](docs/QueueMovesResult.md)
 - [QueuePaymentRequest](docs/QueuePaymentRequest.md)
 - [QueuePaymentRequests](docs/QueuePaymentRequests.md)
 - [QueuePaymentRequestsResult](docs/QueuePaymentRequestsResult.md)
 - [RejectShipment](docs/RejectShipment.md)
 - [Reweigh](docs/Reweigh.md)
 - [ReweighRequester](docs/ReweighRequester.md)
 - [SITExtension](docs/SITExtension.md)
 - [SITExtensions](docs/SITExtensions.md)
 - [SITStatus](docs/SITStatus.md)
 - [ServiceItemParamName](docs/ServiceItemParamName.md)
 - [ServiceItemParamOrigin](docs/ServiceItemParamOrigin.md)
 - [ServiceItemParamType](docs/ServiceItemParamType.md)
 - [ShipmentPaymentSITBalance](docs/ShipmentPaymentSITBalance.md)
 - [ShipmentsPaymentSITBalance](docs/ShipmentsPaymentSITBalance.md)
 - [StorageFacility](docs/StorageFacility.md)
 - [TacValid](docs/TacValid.md)
 - [UpdateAllowancePayload](docs/UpdateAllowancePayload.md)
 - [UpdateBillableWeightPayload](docs/UpdateBillableWeightPayload.md)
 - [UpdateCustomerPayload](docs/UpdateCustomerPayload.md)
 - [UpdateMaxBillableWeightAsTIOPayload](docs/UpdateMaxBillableWeightAsTIOPayload.md)
 - [UpdateOrderPayload](docs/UpdateOrderPayload.md)
 - [UpdatePaymentRequestStatusPayload](docs/UpdatePaymentRequestStatusPayload.md)
 - [UpdateShipment](docs/UpdateShipment.md)
 - [Upload](docs/Upload.md)
 - [ValidationError](docs/ValidationError.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

dp3@truss.works


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in ghc_client.apis and ghc_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from ghc_client.api.default_api import DefaultApi`
- `from ghc_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import ghc_client
from ghc_client.apis import *
from ghc_client.models import *
```
