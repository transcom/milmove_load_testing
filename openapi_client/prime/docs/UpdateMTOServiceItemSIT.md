# UpdateMTOServiceItemSIT

Subtype used to provide the departure date for origin or destination SIT. This is not creating a new service item but rather updating and existing service item. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_type** | [**UpdateMTOServiceItemModelType**](UpdateMTOServiceItemModelType.md) |  | 
**re_service_code** | **str** | Service code allowed for this model type. | [optional] 
**sit_departure_date** | **date** | Departure date for SIT. This is the end date of the SIT at either origin or destination. | [optional] 
**sit_destination_final_address** | [**Address**](Address.md) |  | [optional] 
**time_military1** | **str, none_type** | Time of delivery corresponding to &#x60;firstAvailableDeliveryDate1&#x60;, in military format. | [optional] 
**first_available_delivery_date1** | **date, none_type** | First available date that Prime can deliver SIT service item. | [optional] 
**time_military2** | **str, none_type** | Time of delivery corresponding to &#x60;firstAvailableDeliveryDate2&#x60;, in military format. | [optional] 
**first_available_delivery_date2** | **date, none_type** | Second available date that Prime can deliver SIT service item. | [optional] 
**id** | **str** | ID of the service item. Must match path. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


