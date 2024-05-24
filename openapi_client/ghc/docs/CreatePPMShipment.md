# CreatePPMShipment

A personally procured move is a type of shipment that a service members moves themselves.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_departure_date** | **date** | Date the customer expects to move.  | 
**pickup_address** | [**UpdateCustomerPayloadCurrentAddress**](UpdateCustomerPayloadCurrentAddress.md) |  | 
**destination_address** | [**UpdateCustomerPayloadCurrentAddress**](UpdateCustomerPayloadCurrentAddress.md) |  | 
**sit_expected** | **bool** |  | 
**estimated_weight** | **int** |  | 
**has_pro_gear** | **bool** | Indicates whether PPM shipment has pro gear.  | 
**secondary_destination_address** | [**UpdateCustomerPayloadCurrentAddress**](UpdateCustomerPayloadCurrentAddress.md) |  | [optional] 
**secondary_pickup_address** | [**UpdateCustomerPayloadCurrentAddress**](UpdateCustomerPayloadCurrentAddress.md) |  | [optional] 
**has_secondary_pickup_address** | **bool, none_type** |  | [optional] 
**has_secondary_destination_address** | **bool, none_type** |  | [optional] 
**sit_location** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**sit_estimated_weight** | **int, none_type** |  | [optional] 
**sit_estimated_entry_date** | **date, none_type** |  | [optional] 
**sit_estimated_departure_date** | **date, none_type** |  | [optional] 
**pro_gear_weight** | **int, none_type** |  | [optional] 
**spouse_pro_gear_weight** | **int, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


