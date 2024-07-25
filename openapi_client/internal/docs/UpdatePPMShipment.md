# UpdatePPMShipment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_departure_date** | **date, none_type** | Date the customer expects to move.  | [optional] 
**actual_move_date** | **date, none_type** |  | [optional] 
**pickup_address** | [**Address**](Address.md) |  | [optional] 
**secondary_pickup_address** | [**Address**](Address.md) |  | [optional] 
**has_secondary_pickup_address** | **bool, none_type** |  | [optional] 
**tertiary_pickup_address** | [**Address**](Address.md) |  | [optional] 
**has_tertiary_pickup_address** | **bool, none_type** |  | [optional] 
**actual_pickup_postal_code** | **str, none_type** | The actual postal code where the PPM shipment started. To be filled once the customer has moved the shipment.  | [optional] 
**destination_address** | [**Address**](Address.md) |  | [optional] 
**secondary_destination_address** | [**Address**](Address.md) |  | [optional] 
**has_secondary_destination_address** | **bool, none_type** |  | [optional] 
**tertiary_destination_address** | [**Address**](Address.md) |  | [optional] 
**has_tertiary_destination_address** | **bool, none_type** |  | [optional] 
**actual_destination_postal_code** | **str, none_type** | The actual postal code where the PPM shipment ended. To be filled once the customer has moved the shipment.  | [optional] 
**w2_address** | [**Address**](Address.md) |  | [optional] 
**final_incentive** | **int, none_type** | The final calculated incentive for the PPM shipment. This does not include **SIT** as it is a reimbursement.  | [optional] [readonly] 
**sit_expected** | **bool, none_type** |  | [optional] 
**estimated_weight** | **int, none_type** |  | [optional] 
**has_pro_gear** | **bool, none_type** | Indicates whether PPM shipment has pro gear.  | [optional] 
**pro_gear_weight** | **int, none_type** |  | [optional] 
**spouse_pro_gear_weight** | **int, none_type** |  | [optional] 
**has_requested_advance** | **bool, none_type** | Indicates whether an advance has been requested for the PPM shipment.  | [optional] 
**advance_amount_requested** | **int, none_type** | The amount requested for an advance, or null if no advance is requested  | [optional] 
**has_received_advance** | **bool, none_type** | Indicates whether an advance was received for the PPM shipment.  | [optional] 
**advance_amount_received** | **int, none_type** | The amount received for an advance, or null if no advance is received.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


