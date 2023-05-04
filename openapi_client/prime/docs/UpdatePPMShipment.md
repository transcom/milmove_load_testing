# UpdatePPMShipment

The PPM specific fields of the shipment with values being changed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_departure_date** | **date, none_type** | Date the customer expects to begin moving from their origin.  | [optional] 
**pickup_postal_code** | **str, none_type** | The postal code of the origin location where goods are being moved from. | [optional] 
**secondary_pickup_postal_code** | **str, none_type** | An optional secondary pickup location near the origin where additional goods exist. | [optional] 
**destination_postal_code** | **str, none_type** | The postal code of the destination location where goods are being delivered to. | [optional] 
**secondary_destination_postal_code** | **str, none_type** | An optional secondary location near the destination where goods will be dropped off. | [optional] 
**sit_expected** | **bool, none_type** | Captures whether some or all of the PPM shipment will require temporary storage at the origin or destination.  Must be set to &#x60;true&#x60; when providing &#x60;sitLocation&#x60;, &#x60;sitEstimatedWeight&#x60;, &#x60;sitEstimatedEntryDate&#x60;, and &#x60;sitEstimatedDepartureDate&#x60; values to calculate the &#x60;sitEstimatedCost&#x60;.  | [optional] 
**sit_location** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**sit_estimated_weight** | **int, none_type** | The estimated weight of the goods being put into storage. | [optional] 
**sit_estimated_entry_date** | **date, none_type** | The date that goods will first enter the storage location. | [optional] 
**sit_estimated_departure_date** | **date, none_type** | The date that goods will exit the storage location. | [optional] 
**estimated_weight** | **int, none_type** | The estimated weight of the PPM shipment goods being moved. | [optional] 
**has_pro_gear** | **bool, none_type** | Indicates whether PPM shipment has pro gear for themselves or their spouse.  | [optional] 
**pro_gear_weight** | **int, none_type** | The estimated weight of the pro-gear being moved belonging to the service member. | [optional] 
**spouse_pro_gear_weight** | **int, none_type** | The estimated weight of the pro-gear being moved belonging to a spouse. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


