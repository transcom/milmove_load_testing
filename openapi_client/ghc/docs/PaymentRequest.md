# PaymentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proof_of_service_docs** | [**ProofOfServiceDocs**](ProofOfServiceDocs.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**is_final** | **bool** |  | [optional]  if omitted the server will use the default value of False
**move_task_order** | [**Move**](Move.md) |  | [optional] 
**move_task_order_id** | **str** |  | [optional] 
**rejection_reason** | **str, none_type** |  | [optional] 
**service_items** | [**PaymentServiceItems**](PaymentServiceItems.md) |  | [optional] 
**status** | [**PaymentRequestStatus**](PaymentRequestStatus.md) |  | [optional] 
**payment_request_number** | **str** |  | [optional] [readonly] 
**recalculation_of_payment_request_id** | **str, none_type** |  | [optional] [readonly] 
**e_tag** | **str** |  | [optional] 
**reviewed_at** | **datetime, none_type** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


