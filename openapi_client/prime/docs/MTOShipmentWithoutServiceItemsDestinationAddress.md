# MTOShipmentWithoutServiceItemsDestinationAddress

Where the movers should deliver this shipment. Often provided by the customer when they enter shipment details during onboarding, if they know their new address already.  May be blank when entered by the customer, required when entered by the Prime. May not represent the true final destination due to the shipment being diverted or placed in SIT. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_address1** | **str** |  | 
**city** | **str** |  | 
**state** | **str** |  | 
**postal_code** | **str** |  | 
**id** | **str** |  | [optional] 
**street_address2** | **str, none_type** |  | [optional] 
**street_address3** | **str, none_type** |  | [optional] 
**e_tag** | **str** |  | [optional] [readonly] 
**country** | **str, none_type** |  | [optional]  if omitted the server will use the default value of "USA"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


