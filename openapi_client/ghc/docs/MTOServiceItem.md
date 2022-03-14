# MTOServiceItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_task_order_id** | **str** |  | 
**mto_shipment_id** | **str** |  | 
**re_service_id** | **str** |  | 
**re_service_code** | **str** |  | 
**re_service_name** | **str** |  | 
**description** | **str** |  | 
**reason** | **str** |  | 
**pickup_postal_code** | **str** |  | 
**id** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**customer_contacts** | [**MTOServiceItemCustomerContacts**](MTOServiceItemCustomerContacts.md) |  | [optional] 
**deleted_at** | **date** |  | [optional] 
**dimensions** | [**MTOServiceItemDimensions**](MTOServiceItemDimensions.md) |  | [optional] 
**rejection_reason** | **str, none_type** |  | [optional] 
**sit_postal_code** | **str, none_type** |  | [optional] [readonly] 
**sit_entry_date** | **datetime, none_type** |  | [optional] 
**sit_departure_date** | **datetime, none_type** |  | [optional] 
**fee_type** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**rate** | **int** |  | [optional] 
**status** | [**MTOServiceItemStatus**](MTOServiceItemStatus.md) |  | [optional] 
**submitted_at** | **date** |  | [optional] 
**total** | **int** |  | [optional] 
**estimated_weight** | **int, none_type** | estimated weight of the shuttle service item provided by the prime | [optional] 
**updated_at** | **datetime** |  | [optional] 
**approved_at** | **datetime, none_type** |  | [optional] 
**rejected_at** | **datetime, none_type** |  | [optional] 
**e_tag** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


