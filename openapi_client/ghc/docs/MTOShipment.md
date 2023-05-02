# MTOShipment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_task_order_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime, none_type** |  | [optional] 
**prime_estimated_weight** | **int, none_type** |  | [optional] 
**prime_actual_weight** | **int, none_type** |  | [optional] 
**calculated_billable_weight** | **int, none_type** |  | [optional] [readonly] 
**nts_recorded_weight** | **int, none_type** | The previously recorded weight for the NTS Shipment. Used for NTS Release to know what the previous primeActualWeight or billable weight was. | [optional] 
**scheduled_pickup_date** | **date, none_type** |  | [optional] 
**scheduled_delivery_date** | **date, none_type** |  | [optional] 
**requested_pickup_date** | **date, none_type** |  | [optional] 
**actual_pickup_date** | **date, none_type** |  | [optional] 
**actual_delivery_date** | **date, none_type** | The actual date that the shipment was delivered to the destination address by the Prime | [optional] 
**requested_delivery_date** | **date, none_type** |  | [optional] 
**required_delivery_date** | **date, none_type** |  | [optional] 
**approved_date** | **datetime, none_type** |  | [optional] 
**diversion** | **bool** |  | [optional] 
**pickup_address** | [**Address**](Address.md) |  | [optional] 
**destination_address** | [**Address**](Address.md) |  | [optional] 
**destination_type** | [**DestinationType**](DestinationType.md) |  | [optional] 
**secondary_pickup_address** | [**Address**](Address.md) |  | [optional] 
**secondary_delivery_address** | [**Address**](Address.md) |  | [optional] 
**customer_remarks** | **str, none_type** |  | [optional] 
**counselor_remarks** | **str, none_type** | The counselor can use the counselor remarks field to inform the movers about any special circumstances for this shipment. Typical examples:   * bulky or fragile items,   * weapons,   * access info for their address. Counselors enters this information when creating or editing an MTO Shipment. Optional field.  | [optional] 
**shipment_type** | [**MTOShipmentType**](MTOShipmentType.md) |  | [optional] 
**status** | [**MTOShipmentStatus**](MTOShipmentStatus.md) |  | [optional] 
**rejection_reason** | **str, none_type** |  | [optional] 
**reweigh** | [**Reweigh**](Reweigh.md) |  | [optional] 
**mto_agents** | [**MTOAgents**](MTOAgents.md) |  | [optional] 
**mto_service_items** | [**MTOServiceItems**](MTOServiceItems.md) |  | [optional] 
**sit_days_allowance** | **int, none_type** |  | [optional] 
**sit_extensions** | [**SITExtensions**](SITExtensions.md) |  | [optional] 
**sit_status** | [**SITStatus**](SITStatus.md) |  | [optional] 
**e_tag** | **str** |  | [optional] 
**billable_weight_cap** | **int, none_type** | TIO override billable weight to be used for calculations | [optional] 
**billable_weight_justification** | **str, none_type** |  | [optional] 
**tac_type** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**sac_type** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**uses_external_vendor** | **bool** |  | [optional] 
**service_order_number** | **str, none_type** |  | [optional] 
**storage_facility** | [**StorageFacility**](StorageFacility.md) |  | [optional] 
**ppm_shipment** | [**PPMShipment**](PPMShipment.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


