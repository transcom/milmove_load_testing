# MTOShipment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_task_order_id** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**requested_pickup_date** | **date, none_type** |  | [optional] [readonly] 
**requested_delivery_date** | **date, none_type** |  | [optional] [readonly] 
**agents** | [**MTOAgents**](MTOAgents.md) |  | [optional] 
**customer_remarks** | **str, none_type** |  | [optional] [readonly] 
**ppm_shipment** | [**PPMShipment**](PPMShipment.md) |  | [optional] 
**shipment_type** | [**MTOShipmentType**](MTOShipmentType.md) |  | [optional] 
**status** | [**MTOShipmentStatus**](MTOShipmentStatus.md) |  | [optional] 
**pickup_address** | [**Address**](Address.md) |  | [optional] 
**destination_address** | [**Address**](Address.md) |  | [optional] 
**secondary_pickup_address** | [**Address**](Address.md) |  | [optional] 
**has_secondary_pickup_address** | **bool, none_type** |  | [optional] 
**secondary_delivery_address** | [**Address**](Address.md) |  | [optional] 
**has_secondary_delivery_address** | **bool, none_type** |  | [optional] 
**actual_pro_gear_weight** | **int, none_type** |  | [optional] 
**actual_spouse_pro_gear_weight** | **int, none_type** |  | [optional] 
**e_tag** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


