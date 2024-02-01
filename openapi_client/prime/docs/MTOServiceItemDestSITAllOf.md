# MTOServiceItemDestSITAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**re_service_code** | **str** | Service code allowed for this model type. | 
**sit_entry_date** | **date** | Entry date for the SIT | 
**reason** | **str, none_type** | The reason item has been placed in SIT.  | 
**date_of_contact1** | **date, none_type** | Date of attempted contact by the prime corresponding to &#x60;timeMilitary1&#x60;. | [optional] 
**date_of_contact2** | **date, none_type** | Date of attempted contact by the prime corresponding to &#x60;timeMilitary2&#x60;. | [optional] 
**time_military1** | **str, none_type** | Time of attempted contact corresponding to &#x60;dateOfContact1&#x60;, in military format. | [optional] 
**time_military2** | **str, none_type** | Time of attempted contact corresponding to &#x60;dateOfContact2&#x60;, in military format. | [optional] 
**first_available_delivery_date1** | **date, none_type** | First available date that Prime can deliver SIT service item. | [optional] 
**first_available_delivery_date2** | **date, none_type** | Second available date that Prime can deliver SIT service item. | [optional] 
**sit_departure_date** | **date, none_type** | Departure date for SIT. This is the end date of the SIT at either origin or destination. This is optional as it can be updated using the UpdateMTOServiceItemSIT modelType at a later date. | [optional] 
**sit_destination_final_address** | [**Address**](Address.md) |  | [optional] 
**sit_address_updates** | [**SitAddressUpdates**](SitAddressUpdates.md) |  | [optional] 
**sit_requested_delivery** | **date, none_type** | Date when the customer has requested delivery out of SIT. | [optional] 
**sit_customer_contacted** | **date, none_type** | Date when the customer contacted the prime for a delivery out of SIT. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


