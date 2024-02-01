# ShipmentAddressUpdate

This represents a destination address change request made by the Prime that is either auto-approved or requires review if the pricing criteria has changed. If criteria has changed, then it must be approved or rejected by a TOO. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**contractor_remarks** | **str** | The reason there is an address change. | [readonly] 
**status** | [**ShipmentAddressUpdateStatus**](ShipmentAddressUpdateStatus.md) |  | 
**shipment_id** | **str** |  | [readonly] 
**original_address** | [**Address**](Address.md) |  | 
**new_address** | [**Address**](Address.md) |  | 
**office_remarks** | **str, none_type** | The TOO comment on approval or rejection. | [optional] 
**sit_original_address** | [**Address**](Address.md) |  | [optional] 
**old_sit_distance_between** | **int** | The distance between the original SIT address and the previous/old destination address of shipment | [optional] 
**new_sit_distance_between** | **int** | The distance between the original SIT address and requested new destination address of shipment | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


