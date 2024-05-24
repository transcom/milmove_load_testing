# QueuePaymentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**move_id** | **str** |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**status** | [**QueuePaymentRequestStatus**](QueuePaymentRequestStatus.md) |  | [optional] 
**age** | **float** | Days since the payment request has been requested.  Decimal representation will allow more accurate sorting. | [optional] 
**submitted_at** | **datetime** |  | [optional] 
**locator** | **str** |  | [optional] 
**department_indicator** | [**DeptIndicator**](DeptIndicator.md) |  | [optional] 
**origin_gbloc** | [**GBLOC**](GBLOC.md) |  | [optional] 
**origin_duty_location** | [**DutyLocation**](DutyLocation.md) |  | [optional] 
**order_type** | **str, none_type** |  | [optional] 
**locked_by_office_user_id** | **str, none_type** |  | [optional] 
**lock_expires_at** | **datetime, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


