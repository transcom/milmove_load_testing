# UpdateMovingExpense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moving_expense_type** | [**OmittableMovingExpenseType**](OmittableMovingExpenseType.md) |  | [optional] 
**description** | **str, none_type** | A brief description of the expense. | [optional] 
**amount** | **int** | The total amount of the expense as indicated on the receipt | [optional] 
**sit_start_date** | **date** | The date the shipment entered storage, applicable for the &#x60;STORAGE&#x60; movingExpenseType only | [optional] 
**sit_end_date** | **date** | The date the shipment exited storage, applicable for the &#x60;STORAGE&#x60; movingExpenseType only | [optional] 
**status** | [**PPMDocumentStatus**](PPMDocumentStatus.md) |  | [optional] 
**reason** | **str** | The reason the services counselor has excluded or rejected the item. | [optional] 
**weight_stored** | **int** | The total weight stored in PPM SIT | [optional] 
**sit_location** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**sit_estimated_cost** | **int, none_type** | The estimated amount that the government will pay the service member to put their goods into storage. This estimated storage cost is separate from the estimated incentive. | [optional] 
**sit_reimburseable_amount** | **int, none_type** | The amount of SIT that will be reimbursed | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


