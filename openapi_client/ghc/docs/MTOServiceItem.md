# MTOServiceItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_task_order_id** | **str** |  | 
**re_service_id** | **str** |  | 
**re_service_code** | **str** |  | 
**re_service_name** | **str** |  | 
**id** | **str** |  | 
**mto_shipment_id** | **str, none_type** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**convert_to_customer_expense** | **bool** |  | [optional] 
**customer_expense_reason** | **str, none_type** |  | [optional] 
**customer_contacts** | [**MTOServiceItemCustomerContacts**](MTOServiceItemCustomerContacts.md) |  | [optional] 
**deleted_at** | **date** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**dimensions** | [**MTOServiceItemDimensions**](MTOServiceItemDimensions.md) |  | [optional] 
**reason** | **str, none_type** |  | [optional] 
**rejection_reason** | **str, none_type** |  | [optional] 
**pickup_postal_code** | **str, none_type** |  | [optional] 
**sit_postal_code** | **str, none_type** |  | [optional] [readonly] 
**sit_entry_date** | **datetime, none_type** |  | [optional] 
**sit_departure_date** | **datetime, none_type** |  | [optional] 
**sit_customer_contacted** | **date, none_type** |  | [optional] 
**sit_requested_delivery** | **date, none_type** |  | [optional] 
**sit_destination_original_address** | [**Address**](Address.md) |  | [optional] 
**sit_origin_hhg_original_address** | [**Address**](Address.md) |  | [optional] 
**sit_origin_hhg_actual_address** | [**Address**](Address.md) |  | [optional] 
**sit_destination_final_address** | [**Address**](Address.md) |  | [optional] 
**sit_address_updates** | [**SITAddressUpdates**](SITAddressUpdates.md) |  | [optional] 
**sit_delivery_miles** | **int, none_type** |  | [optional] 
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
**update_reason** | **str, none_type** | Reason for updating service item. | [optional] 
**standalone_crate** | **bool, none_type** |  | [optional] 
**service_request_documents** | [**ServiceRequestDocuments**](ServiceRequestDocuments.md) |  | [optional] 
**estimated_price** | **int, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


