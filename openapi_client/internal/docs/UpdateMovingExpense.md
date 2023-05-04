# UpdateMovingExpense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moving_expense_type** | [**MovingExpenseType**](MovingExpenseType.md) |  | 
**description** | **str** | A brief description of the expense | 
**paid_with_gtcc** | **bool** | Indicates if the service member used their government issued card to pay for the expense | 
**amount** | **int** | The total amount of the expense as indicated on the receipt | 
**missing_receipt** | **bool** | Indicates if the customer is missing the receipt for their expense. | 
**sit_start_date** | **date** | The date the shipment entered storage, applicable for the &#x60;STORAGE&#x60; movingExpenseType only | [optional] 
**sit_end_date** | **date** | The date the shipment exited storage, applicable for the &#x60;STORAGE&#x60; movingExpenseType only | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


