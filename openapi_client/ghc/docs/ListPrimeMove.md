# ListPrimeMove

An abbreviated definition for a move, without all the nested information (shipments, service items, etc). Used to fetch a list of moves more efficiently. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**move_code** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**order_id** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**available_to_prime_at** | **datetime, none_type** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**ppm_type** | **str** |  | [optional] 
**e_tag** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


