# CreatePPMShipment

A personally procured move is a type of shipment that a service members moves themselves.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_departure_date** | **date** | Date the customer expects to move.  | 
**pickup_address** | [**Address**](Address.md) |  | 
**destination_address** | [**Address**](Address.md) |  | 
**sit_expected** | **bool** |  | 
**secondary_pickup_address** | [**Address**](Address.md) |  | [optional] 
**secondary_destination_address** | [**Address**](Address.md) |  | [optional] 
**tertiary_destination_address** | [**Address**](Address.md) |  | [optional] 
**tertiary_pickup_address** | [**Address**](Address.md) |  | [optional] 
**has_tertiary_pickup_address** | **bool, none_type** |  | [optional] 
**has_tertiary_destination_address** | **bool, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


