# MTOServiceItemShuttle

Describes a shuttle service item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**re_service_code** | **str** | A unique code for the service item. Indicates if shuttling is requested for the shipment origin (&#x60;DOSHUT&#x60;) or destination (&#x60;DDSHUT&#x60;).  | 
**reason** | **str** | The contractor&#39;s explanation for why a shuttle service is requested. Used by the TOO while deciding to approve or reject the service item.  | 
**move_task_order_id** | **str** | The ID of the move for this service item. | 
**model_type** | [**MTOServiceItemModelType**](MTOServiceItemModelType.md) |  | 
**estimated_weight** | **int, none_type** | An estimate of how much weight from a shipment will be included in the shuttling service. | [optional] 
**actual_weight** | **int, none_type** | A record of the actual weight that was shuttled. Provided by the movers, based on weight tickets. | [optional] 
**id** | **str** | The ID of the service item. | [optional] [readonly] 
**mto_shipment_id** | **str** | The ID of the shipment this service is for, if any. Optional. | [optional] 
**re_service_name** | **str** | The full descriptive name of the service. | [optional] [readonly] 
**status** | [**MTOServiceItemStatus**](MTOServiceItemStatus.md) |  | [optional] 
**rejection_reason** | **str, none_type** | The reason why this service item was rejected by the TOO. | [optional] [readonly] 
**service_request_documents** | [**ServiceRequestDocuments**](ServiceRequestDocuments.md) |  | [optional] 
**e_tag** | **str** | A hash unique to this service item that should be used as the \&quot;If-Match\&quot; header for any updates. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


