# MovePayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**orders_id** | **str** |  | 
**locator** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**e_tag** | **str** |  | 
**service_member_id** | **str** |  | [optional] [readonly] 
**status** | [**MoveStatus**](MoveStatus.md) |  | [optional] 
**submitted_at** | **datetime, none_type** |  | [optional] 
**mto_shipments** | [**MTOShipments**](MTOShipments.md) |  | [optional] 
**closeout_office** | [**TransportationOffice**](TransportationOffice.md) |  | [optional] 
**cancel_reason** | **str, none_type** |  | [optional] 
**prime_counseling_completed_at** | **datetime** |  | [optional] [readonly] 
**additional_documents** | [**Document**](Document.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


