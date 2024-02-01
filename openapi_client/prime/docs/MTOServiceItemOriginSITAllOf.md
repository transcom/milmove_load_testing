# MTOServiceItemOriginSITAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**re_service_code** | **str** | Service code allowed for this model type. | 
**reason** | **str** | Explanation of why Prime is picking up SIT item. | 
**sit_postal_code** | **str** |  | 
**sit_entry_date** | **date** | Entry date for the SIT | 
**sit_departure_date** | **date, none_type** | Departure date for SIT. This is the end date of the SIT at either origin or destination. This is optional as it can be updated using the UpdateMTOServiceItemSIT modelType at a later date. | [optional] 
**sit_hhg_actual_origin** | [**Address**](Address.md) |  | [optional] 
**sit_hhg_original_origin** | [**Address**](Address.md) |  | [optional] 
**request_approvals_requested_status** | **bool** |  | [optional] 
**sit_requested_delivery** | **date, none_type** | Date when the customer has requested delivery out of SIT. | [optional] 
**sit_customer_contacted** | **date, none_type** | Date when the customer contacted the prime for a delivery out of SIT. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


