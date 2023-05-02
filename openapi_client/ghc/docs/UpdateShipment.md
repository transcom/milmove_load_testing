# UpdateShipment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_type** | [**MTOShipmentType**](MTOShipmentType.md) |  | [optional] 
**requested_pickup_date** | **date, none_type** |  | [optional] 
**requested_delivery_date** | **date, none_type** |  | [optional] 
**customer_remarks** | **str, none_type** |  | [optional] 
**counselor_remarks** | **str, none_type** |  | [optional] 
**billable_weight_cap** | **int, none_type** | estimated weight of the shuttle service item provided by the prime | [optional] 
**billable_weight_justification** | **str, none_type** |  | [optional] 
**pickup_address** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**destination_address** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**destination_type** | [**DestinationType**](DestinationType.md) |  | [optional] 
**agents** | [**MTOAgents**](MTOAgents.md) |  | [optional] 
**tac_type** | [**LOATypeNullable**](LOATypeNullable.md) |  | [optional] 
**sac_type** | [**LOATypeNullable**](LOATypeNullable.md) |  | [optional] 
**uses_external_vendor** | **bool, none_type** |  | [optional] 
**service_order_number** | **str, none_type** |  | [optional] 
**nts_recorded_weight** | **int, none_type** | The previously recorded weight for the NTS Shipment. Used for NTS Release to know what the previous primeActualWeight or billable weight was. | [optional] 
**storage_facility** | [**StorageFacility**](StorageFacility.md) |  | [optional] 
**ppm_shipment** | [**UpdatePPMShipment**](UpdatePPMShipment.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


