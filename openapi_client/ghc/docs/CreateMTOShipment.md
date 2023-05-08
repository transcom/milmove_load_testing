# CreateMTOShipment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_task_order_id** | **str** | The ID of the move this new shipment is for. | 
**shipment_type** | [**MTOShipmentType**](MTOShipmentType.md) |  | 
**requested_pickup_date** | **date, none_type** | The customer&#39;s preferred pickup date. Other dates, such as required delivery date and (outside MilMove) the pack date, are derived from this date.  | [optional] 
**requested_delivery_date** | **date, none_type** | The customer&#39;s preferred delivery date.  | [optional] 
**customer_remarks** | **str, none_type** | The customer can use the customer remarks field to inform the services counselor and the movers about any special circumstances for this shipment. Typical examples:   * bulky or fragile items,   * weapons,   * access info for their address. Customer enters this information during onboarding. Optional field.  | [optional] 
**counselor_remarks** | **str, none_type** | The counselor can use the counselor remarks field to inform the movers about any special circumstances for this shipment. Typical examples:   * bulky or fragile items,   * weapons,   * access info for their address. Counselors enters this information when creating or editing an MTO Shipment. Optional field.  | [optional] 
**agents** | [**MTOAgents**](MTOAgents.md) |  | [optional] 
**mto_service_items** | [**MTOServiceItems**](MTOServiceItems.md) |  | [optional] 
**pickup_address** | [**CreateMTOShipmentPickupAddress**](CreateMTOShipmentPickupAddress.md) |  | [optional] 
**destination_address** | [**CreateMTOShipmentDestinationAddress**](CreateMTOShipmentDestinationAddress.md) |  | [optional] 
**destination_type** | [**DestinationType**](DestinationType.md) |  | [optional] 
**tac_type** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**sac_type** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**uses_external_vendor** | **bool, none_type** |  | [optional] 
**service_order_number** | **str, none_type** |  | [optional] 
**nts_recorded_weight** | **int, none_type** | The previously recorded weight for the NTS Shipment. Used for NTS Release to know what the previous primeActualWeight or billable weight was. | [optional] 
**storage_facility** | [**StorageFacility**](StorageFacility.md) |  | [optional] 
**ppm_shipment** | [**CreatePPMShipment**](CreatePPMShipment.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


