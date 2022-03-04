# PPMShipment

A personally procured move is a type of shipment that a service members moves themselves.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**shipment_id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**status** | [**PPMShipmentStatus**](PPMShipmentStatus.md) |  | 
**expected_departure_date** | **date** | Date the customer expects to move.  | 
**pickup_postal_code** | **str** | zip code | 
**destination_postal_code** | **str** |  | 
**sit_expected** | **bool** |  | 
**e_tag** | **str** | A hash unique to this shipment that should be used as the \&quot;If-Match\&quot; header for any updates. | [readonly] 
**actual_move_date** | **date, none_type** |  | [optional] 
**submitted_at** | **datetime, none_type** |  | [optional] 
**reviewed_at** | **datetime, none_type** |  | [optional] 
**approved_at** | **datetime, none_type** |  | [optional] 
**secondary_pickup_postal_code** | **str, none_type** |  | [optional] 
**secondary_destination_postal_code** | **str, none_type** |  | [optional] 
**estimated_weight** | **int, none_type** |  | [optional] 
**net_weight** | **int, none_type** | The net weight of the shipment once it has been weight  | [optional] 
**has_pro_gear** | **bool, none_type** | Indicates whether PPM shipment has pro gear.  | [optional] 
**pro_gear_weight** | **int, none_type** |  | [optional] 
**spouse_pro_gear_weight** | **int, none_type** |  | [optional] 
**estimated_incentive** | **int, none_type** |  | [optional] 
**advance_requested** | **bool, none_type** |  | [optional] 
**advance_id** | **str, none_type** |  | [optional] [readonly] 
**advance_worksheet_id** | **str, none_type** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


