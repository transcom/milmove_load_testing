# SITAddressUpdate

An update to a SIT service item address.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**mto_service_item_id** | **str** |  | [optional] 
**distance** | **int** | The distance between the old address and the new address in miles. | [optional] 
**contractor_remarks** | **str, none_type** |  | [optional] 
**office_remarks** | **str, none_type** |  | [optional] 
**status** | **str** |  | [optional] 
**old_address** | [**Address**](Address.md) |  | [optional] 
**new_address** | [**Address**](Address.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**e_tag** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


