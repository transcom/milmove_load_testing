# SitAddressUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**mto_service_item_id** | **str** |  | [optional] [readonly] 
**new_address_id** | **str** |  | [optional] [readonly] 
**new_address** | [**Address**](Address.md) |  | [optional] 
**old_address_id** | **str** |  | [optional] [readonly] 
**old_address** | [**Address**](Address.md) |  | [optional] 
**status** | [**SitAddressUpdateStatus**](SitAddressUpdateStatus.md) |  | [optional] 
**distance** | **int** |  | [optional] [readonly] 
**contractor_remarks** | **str, none_type** |  | [optional] 
**office_remarks** | **str, none_type** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**e_tag** | **str** | A hash unique to this shipment that should be used as the \&quot;If-Match\&quot; header for any updates. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


