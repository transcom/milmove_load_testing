# Reweigh

A reweigh  is when a shipment is weighed for a second time due to the request of a customer, the contractor, system or TOO.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**requested_at** | **datetime** |  | [optional] 
**requested_by** | [**ReweighRequester**](ReweighRequester.md) |  | [optional] 
**verification_provided_at** | **datetime, none_type** |  | [optional] 
**verification_reason** | **str, none_type** |  | [optional] 
**weight** | **int, none_type** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**e_tag** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


