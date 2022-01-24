# PatchPersonallyProcuredMovePayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | [**TShirtSize**](TShirtSize.md) |  | [optional] 
**original_move_date** | **date, none_type** |  | [optional] 
**actual_move_date** | **date, none_type** |  | [optional] 
**pickup_postal_code** | **str, none_type** |  | [optional] 
**has_additional_postal_code** | **bool, none_type** |  | [optional] 
**additional_pickup_postal_code** | **str, none_type** |  | [optional] 
**destination_postal_code** | **str, none_type** |  | [optional] 
**has_sit** | **bool, none_type** |  | [optional] 
**days_in_storage** | **int, none_type** |  | [optional] 
**total_sit_cost** | **int, none_type** |  | [optional] 
**weight_estimate** | **int, none_type** |  | [optional] 
**net_weight** | **int, none_type** |  | [optional] 
**incentive_estimate_max** | **int, none_type** |  | [optional] 
**incentive_estimate_min** | **int, none_type** |  | [optional] 
**has_requested_advance** | **bool** |  | [optional]  if omitted the server will use the default value of False
**advance** | [**Reimbursement**](Reimbursement.md) |  | [optional] 
**advance_worksheet** | [**DocumentPayload**](DocumentPayload.md) |  | [optional] 
**has_pro_gear** | **str, none_type** |  | [optional] 
**has_pro_gear_over_thousand** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


