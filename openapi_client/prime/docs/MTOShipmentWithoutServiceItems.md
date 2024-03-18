# MTOShipmentWithoutServiceItems


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the shipment. | [optional] [readonly] 
**move_task_order_id** | **str** | The ID of the move for this shipment. | [optional] [readonly] 
**approved_date** | **date, none_type** | The date when the Transportation Ordering Officer first approved this shipment for the move. | [optional] [readonly] 
**requested_pickup_date** | **date, none_type** | The date the customer selects during onboarding as their preferred pickup date. Other dates, such as required delivery date and (outside MilMove) the pack date, are derived from this date.  | [optional] [readonly] 
**requested_delivery_date** | **date, none_type** | The customer&#39;s preferred delivery date. | [optional] [readonly] 
**scheduled_pickup_date** | **date, none_type** | The date the Prime contractor scheduled to pick up this shipment after consultation with the customer. | [optional] 
**actual_pickup_date** | **date, none_type** | The date when the Prime contractor actually picked up the shipment. Updated after-the-fact. | [optional] 
**first_available_delivery_date** | **date, none_type** | The date the Prime provides to the customer as the first possible delivery date so that they can plan their travel accordingly.  | [optional] 
**required_delivery_date** | **date, none_type** | The latest date by which the Prime can deliver a customer&#39;s shipment without violating the contract. This is calculated based on weight, distance, and the scheduled pickup date. It cannot be modified.  | [optional] [readonly] 
**scheduled_delivery_date** | **date, none_type** | The date the Prime contractor scheduled to deliver this shipment after consultation with the customer. | [optional] 
**actual_delivery_date** | **date, none_type** | The date when the Prime contractor actually delivered the shipment. Updated after-the-fact. | [optional] 
**prime_estimated_weight** | **int, none_type** | The estimated weight of this shipment, determined by the movers during the pre-move survey. This value **can only be updated once.** If there was an issue with estimating the weight and a mistake was made, the Prime contracter will need to contact the TOO to change it.  | [optional] 
**prime_estimated_weight_recorded_date** | **date, none_type** | The date when the Prime contractor recorded the shipment&#39;s estimated weight. | [optional] [readonly] 
**prime_actual_weight** | **int, none_type** | The actual weight of the shipment, provided after the Prime packs, picks up, and weighs a customer&#39;s shipment. | [optional] 
**nts_recorded_weight** | **int, none_type** | The previously recorded weight for the NTS Shipment. Used for NTS Release to know what the previous primeActualWeight or billable weight was. | [optional] 
**customer_remarks** | **str, none_type** | The customer can use the customer remarks field to inform the services counselor and the movers about any special circumstances for this shipment. Typical examples:   * bulky or fragile items,   * weapons,   * access info for their address.  Customer enters this information during onboarding. Optional field.  | [optional] [readonly] 
**counselor_remarks** | **str, none_type** | The counselor can use the counselor remarks field to inform the movers about any special circumstances for this shipment. Typical examples:   * bulky or fragile items,   * weapons,   * access info for their address.  Counselors enters this information when creating or editing an MTO Shipment. Optional field.  | [optional] [readonly] 
**actual_pro_gear_weight** | **int, none_type** | The actual weight of any pro gear being shipped.  | [optional] 
**actual_spouse_pro_gear_weight** | **int, none_type** | The actual weight of any spouse pro gear being shipped.  | [optional] 
**agents** | [**MTOAgents**](MTOAgents.md) |  | [optional] 
**sit_extensions** | [**SITExtensions**](SITExtensions.md) |  | [optional] 
**reweigh** | [**Reweigh**](Reweigh.md) |  | [optional] 
**pickup_address** | [**UpdateMTOShipmentPickupAddress**](UpdateMTOShipmentPickupAddress.md) |  | [optional] 
**destination_address** | [**UpdateMTOShipmentDestinationAddress**](UpdateMTOShipmentDestinationAddress.md) |  | [optional] 
**destination_type** | [**DestinationType**](DestinationType.md) |  | [optional] 
**secondary_pickup_address** | [**UpdateMTOShipmentSecondaryPickupAddress**](UpdateMTOShipmentSecondaryPickupAddress.md) |  | [optional] 
**secondary_delivery_address** | [**UpdateMTOShipmentSecondaryDeliveryAddress**](UpdateMTOShipmentSecondaryDeliveryAddress.md) |  | [optional] 
**storage_facility** | [**UpdateMTOShipmentStorageFacility**](UpdateMTOShipmentStorageFacility.md) |  | [optional] 
**shipment_type** | [**MTOShipmentType**](MTOShipmentType.md) |  | [optional] 
**diversion** | **bool** | This value indicates whether or not this shipment is part of a diversion. If yes, the shipment can be either the starting or ending segment of the diversion.  | [optional] 
**status** | **str** | The status of a shipment, indicating where it is in the TOO&#39;s approval process. Can only be updated by the contractor in special circumstances.  | [optional] [readonly] 
**ppm_shipment** | [**PPMShipment**](PPMShipment.md) |  | [optional] 
**delivery_address_update** | [**ShipmentAddressUpdate**](ShipmentAddressUpdate.md) |  | [optional] 
**e_tag** | **str** | A hash unique to this shipment that should be used as the \&quot;If-Match\&quot; header for any updates. | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**point_of_contact** | **str** | Email or ID of the person who will be contacted in the event of questions or concerns about this update. May be the person performing the update, or someone else working with the Prime contractor.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


