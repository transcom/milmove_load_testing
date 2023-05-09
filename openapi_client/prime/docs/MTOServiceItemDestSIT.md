# MTOServiceItemDestSIT

Describes a domestic destination SIT service item. Subtype of a MTOServiceItem.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**re_service_code** | **str** | Service code allowed for this model type. | 
**sit_entry_date** | **date** | Entry date for the SIT | 
**move_task_order_id** | **str** | The ID of the move for this service item. | 
**model_type** | [**MTOServiceItemModelType**](MTOServiceItemModelType.md) |  | 
**time_military1** | **str, none_type** | Time of delivery corresponding to &#x60;firstAvailableDeliveryDate1&#x60;, in military format. | [optional] 
**time_military2** | **str, none_type** | Time of delivery corresponding to &#x60;firstAvailableDeliveryDate2&#x60;, in military format. | [optional] 
**first_available_delivery_date1** | **date, none_type** | First available date that Prime can deliver SIT service item. | [optional] 
**first_available_delivery_date2** | **date, none_type** | Second available date that Prime can deliver SIT service item. | [optional] 
**sit_departure_date** | **date, none_type** | Departure date for SIT. This is the end date of the SIT at either origin or destination. This is optional as it can be updated using the UpdateMTOServiceItemSIT modelType at a later date. | [optional] 
**sit_destination_final_address** | [**Address**](Address.md) |  | [optional] 
**id** | **str** | The ID of the service item. | [optional] [readonly] 
**mto_shipment_id** | **str** | The ID of the shipment this service is for, if any. Optional. | [optional] 
**re_service_name** | **str** | The full descriptive name of the service. | [optional] [readonly] 
**status** | [**MTOServiceItemStatus**](MTOServiceItemStatus.md) |  | [optional] 
**rejection_reason** | **str, none_type** | The reason why this service item was rejected by the TOO. | [optional] [readonly] 
**e_tag** | **str** | A hash unique to this service item that should be used as the \&quot;If-Match\&quot; header for any updates. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


