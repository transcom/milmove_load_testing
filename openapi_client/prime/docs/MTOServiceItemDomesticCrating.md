# MTOServiceItemDomesticCrating

Describes a domestic crating/uncrating service item subtype of a MTOServiceItem.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**re_service_code** | **str** | A unique code for the service item. Indicates if the service is for crating (DCRT) or uncrating (DUCRT). | 
**item** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The dimensions of the item being crated. | 
**crate** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The dimensions for the crate the item will be shipped in. | 
**description** | **str** | A description of the item being crated. | 
**move_task_order_id** | **str** | The ID of the move for this service item. | 
**model_type** | [**MTOServiceItemModelType**](MTOServiceItemModelType.md) |  | 
**reason** | **str, none_type** | The contractor&#39;s explanation for why an item needed to be crated or uncrated. Used by the TOO while deciding to approve or reject the service item.  | [optional] 
**id** | **str** | The ID of the service item. | [optional] [readonly] 
**mto_shipment_id** | **str** | The ID of the shipment this service is for, if any. Optional. | [optional] 
**re_service_name** | **str** | The full descriptive name of the service. | [optional] [readonly] 
**status** | [**MTOServiceItemStatus**](MTOServiceItemStatus.md) |  | [optional] 
**rejection_reason** | **str, none_type** | The reason why this service item was rejected by the TOO. | [optional] [readonly] 
**e_tag** | **str** | A hash unique to this service item that should be used as the \&quot;If-Match\&quot; header for any updates. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


