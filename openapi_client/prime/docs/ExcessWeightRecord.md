# ExcessWeightRecord

A document uploaded by the movers proving that the customer has been counseled about excess weight.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**content_type** | **str** |  | 
**bytes** | **int** |  | 
**move_id** | **str** | The UUID of the move this excess weight record belongs to. | 
**id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**move_excess_weight_qualified_at** | **datetime, none_type** | The date and time when the sum of all the move&#39;s shipments met the excess weight qualification threshold. The system monitors these weights and will update this field automatically.  | [optional] [readonly] 
**move_excess_weight_acknowledged_at** | **datetime, none_type** | The date and time when the TOO acknowledged the excess weight alert, either by dismissing the risk or updating the max billable weight. This will occur after the excess weight record has been uploaded.  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


