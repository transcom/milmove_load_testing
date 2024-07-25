# MovingExpense

Expense information and receipts of costs incurred that can be reimbursed while moving a PPM shipment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique primary identifier of the Moving Expense object | [readonly] 
**ppm_shipment_id** | **str** | The PPM Shipment id that this moving expense belongs to | [readonly] 
**document_id** | **str** | The id of the Document that contains all file uploads for this expense | [readonly] 
**document** | [**MovingExpenseDocument**](MovingExpenseDocument.md) |  | 
**created_at** | **datetime** | Timestamp the moving expense object was initially created in the system (UTC) | [readonly] 
**updated_at** | **datetime** | Timestamp when a property of this moving expense object was last modified (UTC) | [readonly] 
**moving_expense_type** | [**OmittableMovingExpenseType**](OmittableMovingExpenseType.md) |  | [optional] 
**submitted_moving_expense_type** | [**SubmittedMovingExpenseType**](SubmittedMovingExpenseType.md) |  | [optional] 
**description** | **str, none_type** | A brief description of the expense | [optional] 
**submitted_description** | **str, none_type** | Customer submitted description of the expense | [optional] 
**paid_with_gtcc** | **bool, none_type** | Indicates if the service member used their government issued card to pay for the expense | [optional] 
**amount** | **int, none_type** | The total amount of the expense as indicated on the receipt | [optional] 
**submitted_amount** | **int, none_type** | Customer submitted total amount of the expense as indicated on the receipt | [optional] 
**missing_receipt** | **bool, none_type** | Indicates if the service member is missing the receipt with the proof of expense amount | [optional] 
**status** | [**OmittablePPMDocumentStatus**](OmittablePPMDocumentStatus.md) |  | [optional] 
**reason** | **str, none_type** | The reason the services counselor has excluded or rejected the item. | [optional] 
**sit_start_date** | **date, none_type** | The date the shipment entered storage, applicable for the &#x60;STORAGE&#x60; movingExpenseType only | [optional] 
**submitted_sit_start_date** | **date, none_type** | Customer submitted date the shipment entered storage, applicable for the &#x60;STORAGE&#x60; movingExpenseType only | [optional] 
**sit_end_date** | **date, none_type** | The date the shipment exited storage, applicable for the &#x60;STORAGE&#x60; movingExpenseType only | [optional] 
**submitted_sit_end_date** | **date, none_type** | Customer submitted date the shipment exited storage, applicable for the &#x60;STORAGE&#x60; movingExpenseType only | [optional] 
**e_tag** | **str** | A hash that should be used as the \&quot;If-Match\&quot; header for any updates. | [optional] [readonly] 
**weight_stored** | **int, none_type** | The total weight stored in PPM SIT | [optional] 
**sit_location** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**sit_estimated_cost** | **int, none_type** | The estimated amount that the government will pay the service member to put their goods into storage. This estimated storage cost is separate from the estimated incentive. | [optional] 
**sit_reimburseable_amount** | **int, none_type** | The amount of SIT that will be reimbursed | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


