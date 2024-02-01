# UpdateMTOServiceItemSIT

Subtype used to provide the departure date for origin or destination SIT. This is not creating a new service item but rather updating and existing service item. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_type** | [**UpdateMTOServiceItemModelType**](UpdateMTOServiceItemModelType.md) |  | 
**re_service_code** | **str** | Service code allowed for this model type. | [optional] 
**sit_departure_date** | **date** | Departure date for SIT. This is the end date of the SIT at either origin or destination. | [optional] 
**sit_destination_final_address** | [**Address**](Address.md) |  | [optional] 
**date_of_contact1** | **date, none_type** | Date of attempted contact by the prime corresponding to &#39;timeMilitary1&#39;. | [optional] 
**time_military1** | **str, none_type** | Time of attempted contact by the prime corresponding to &#39;dateOfContact1&#39;, in military format. | [optional] 
**first_available_delivery_date1** | **date, none_type** | First available date that Prime can deliver SIT service item. | [optional] 
**date_of_contact2** | **date, none_type** | Date of attempted contact by the prime corresponding to &#39;timeMilitary2&#39;. | [optional] 
**time_military2** | **str, none_type** | Time of attempted contact by the prime corresponding to &#39;dateOfContact2&#39;, in military format. | [optional] 
**first_available_delivery_date2** | **date, none_type** | Second available date that Prime can deliver SIT service item. | [optional] 
**sit_requested_delivery** | **date, none_type** | Date when the customer has requested delivery out of SIT. | [optional] 
**sit_customer_contacted** | **date, none_type** | Date when the customer contacted the prime for a delivery out of SIT. | [optional] 
**update_reason** | **str, none_type** | Reason for updating service item. | [optional] 
**sit_postal_code** | **str, none_type** |  | [optional] 
**sit_entry_date** | **date, none_type** | Entry date for the SIT. | [optional] 
**request_approvals_requested_status** | **bool, none_type** | Indicates if \&quot;Approvals Requested\&quot; status is being requested. | [optional] 
**id** | **str** | ID of the service item. Must match path. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


