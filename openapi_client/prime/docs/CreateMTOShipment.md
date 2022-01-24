# CreateMTOShipment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_task_order_id** | **str** | The ID of the move this new shipment is for. | 
**requested_pickup_date** | **date** | The customer&#39;s preferred pickup date. Other dates, such as required delivery date and (outside MilMove) the pack date, are derived from this date.  | 
**pickup_address** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The address where the movers should pick up this shipment. | 
**destination_address** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Where the movers should deliver this shipment. | 
**shipment_type** | [**MTOShipmentType**](MTOShipmentType.md) |  | 
**prime_estimated_weight** | **int** | The estimated weight of this shipment, determined by the movers during the pre-move survey. This value **can only be updated once.** If there was an issue with estimating the weight and a mistake was made, the Prime contracter will need to contact the TOO to change it.  | [optional] 
**customer_remarks** | **str, none_type** | The customer can use the customer remarks field to inform the services counselor and the movers about any special circumstances for this shipment. Typical examples:   * bulky or fragile items,   * weapons,   * access info for their address.  Customer enters this information during onboarding. Optional field.  | [optional] 
**agents** | [**MTOAgents**](MTOAgents.md) |  | [optional] 
**mto_service_items** | [**[MTOServiceItem]**](MTOServiceItem.md) | A list of service items connected to this shipment. | [optional] 
**diversion** | **bool** | This value indicates whether or not this shipment is part of a diversion. If yes, the shipment can be either the starting or ending segment of the diversion.  | [optional] 
**point_of_contact** | **str** | Email or ID of the person who will be contacted in the event of questions or concerns about this update. May be the person performing the update, or someone else working with the Prime contractor.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


