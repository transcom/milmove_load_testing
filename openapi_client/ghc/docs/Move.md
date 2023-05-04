# Move


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**service_counseling_completed_at** | **datetime, none_type** |  | [optional] 
**available_to_prime_at** | **datetime, none_type** |  | [optional] 
**billable_weights_reviewed_at** | **datetime, none_type** |  | [optional] 
**contractor_id** | **str, none_type** |  | [optional] 
**contractor** | [**Contractor**](Contractor.md) |  | [optional] 
**locator** | **str** |  | [optional] 
**orders_id** | **str** |  | [optional] 
**orders** | [**Order**](Order.md) |  | [optional] 
**reference_id** | **str, none_type** |  | [optional] 
**status** | [**MoveStatus**](MoveStatus.md) |  | [optional] 
**excess_weight_qualified_at** | **datetime, none_type** | Timestamp of when the estimated shipment weights of the move reached 90% of the weight allowance | [optional] 
**excess_weight_acknowledged_at** | **datetime, none_type** | Timestamp of when the TOO acknowledged the excess weight risk by either dismissing the alert or updating the max billable weight | [optional] 
**tio_remarks** | **str, none_type** |  | [optional] 
**financial_review_flag** | **bool** | This flag is set by office users if a move should be reviewed by a Financial Office | [optional] [readonly] 
**financial_review_remarks** | **str, none_type** |  | [optional] [readonly] 
**closeout_office** | [**TransportationOffice**](TransportationOffice.md) |  | [optional] 
**closeout_office_id** | **str, none_type** | The transportation office that will handle reviewing PPM Closeout documentation for Army and Air Force service members | [optional] 
**approvals_requested_at** | **datetime, none_type** | The time at which a move is sent back to the TOO becuase the prime added a new service item for approval | [optional] 
**created_at** | **datetime** |  | [optional] 
**submitted_at** | **datetime, none_type** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**e_tag** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


