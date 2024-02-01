# ServiceItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**params** | [**[ServiceItemParamsInner]**](ServiceItemParamsInner.md) | This should be populated for the following service items:   * DOASIT(Domestic origin Additional day SIT)   * DDASIT(Domestic destination Additional day SIT)  Both take in the following param keys:   * &#x60;SITPaymentRequestStart&#x60;   * &#x60;SITPaymentRequestEnd&#x60;  The value of each is a date string in the format \&quot;YYYY-MM-DD\&quot; (e.g. \&quot;2023-01-15\&quot;)  | [optional] 
**e_tag** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


