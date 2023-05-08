# MTOServiceItemDestSITAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**re_service_code** | **str** | Service code allowed for this model type. | 
**sit_entry_date** | **date** | Entry date for the SIT | 
**time_military1** | **str, none_type** | Time of delivery corresponding to &#x60;firstAvailableDeliveryDate1&#x60;, in military format. | [optional] 
**time_military2** | **str, none_type** | Time of delivery corresponding to &#x60;firstAvailableDeliveryDate2&#x60;, in military format. | [optional] 
**first_available_delivery_date1** | **date, none_type** | First available date that Prime can deliver SIT service item. | [optional] 
**first_available_delivery_date2** | **date, none_type** | Second available date that Prime can deliver SIT service item. | [optional] 
**sit_departure_date** | **date, none_type** | Departure date for SIT. This is the end date of the SIT at either origin or destination. This is optional as it can be updated using the UpdateMTOServiceItemSIT modelType at a later date. | [optional] 
**sit_destination_final_address** | [**Address**](Address.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


