# UpdatePPMShipment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_departure_date** | **date, none_type** | Date the customer expects to move.  | [optional] 
**actual_move_date** | **date, none_type** |  | [optional] 
**pickup_address** | [**UpdateCustomerPayloadCurrentAddress**](UpdateCustomerPayloadCurrentAddress.md) |  | [optional] 
**secondary_pickup_address** | [**UpdateCustomerPayloadCurrentAddress**](UpdateCustomerPayloadCurrentAddress.md) |  | [optional] 
**destination_address** | [**UpdateCustomerPayloadCurrentAddress**](UpdateCustomerPayloadCurrentAddress.md) |  | [optional] 
**secondary_destination_address** | [**UpdateCustomerPayloadCurrentAddress**](UpdateCustomerPayloadCurrentAddress.md) |  | [optional] 
**has_secondary_pickup_address** | **bool, none_type** |  | [optional] 
**has_secondary_destination_address** | **bool, none_type** |  | [optional] 
**w2_address** | [**Address**](Address.md) |  | [optional] 
**sit_expected** | **bool, none_type** |  | [optional] 
**sit_location** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**sit_estimated_weight** | **int, none_type** |  | [optional] 
**sit_estimated_entry_date** | **date, none_type** |  | [optional] 
**sit_estimated_departure_date** | **date, none_type** |  | [optional] 
**estimated_weight** | **int, none_type** |  | [optional] 
**has_pro_gear** | **bool, none_type** | Indicates whether PPM shipment has pro gear.  | [optional] 
**pro_gear_weight** | **int, none_type** |  | [optional] 
**spouse_pro_gear_weight** | **int, none_type** |  | [optional] 
**has_requested_advance** | **bool, none_type** | Indicates whether an advance has been requested for the PPM shipment.  | [optional] 
**has_received_advance** | **bool, none_type** | Indicates whether an advance was received for the PPM shipment.  | [optional] 
**advance_amount_requested** | **int, none_type** | The amount request for an advance, or null if no advance is requested  | [optional] 
**advance_amount_received** | **int, none_type** | The amount received for an advance, or null if no advance is received  | [optional] 
**advance_status** | [**PPMAdvanceStatus**](PPMAdvanceStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


