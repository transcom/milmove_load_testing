# UpdateMTOShipment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_pickup_date** | **date, none_type** | The date the Prime contractor scheduled to pick up this shipment after consultation with the customer. | [optional] 
**actual_pickup_date** | **date, none_type** | The date when the Prime contractor actually picked up the shipment. Updated after-the-fact. | [optional] 
**first_available_delivery_date** | **date, none_type** | The date the Prime provides to the customer as the first possible delivery date so that they can plan their travel accordingly.  | [optional] 
**scheduled_delivery_date** | **date, none_type** | The date the Prime contractor scheduled to deliver this shipment after consultation with the customer. | [optional] 
**actual_delivery_date** | **date, none_type** | The date when the Prime contractor actually delivered the shipment. Updated after-the-fact. | [optional] 
**prime_estimated_weight** | **int, none_type** | The estimated weight of this shipment, determined by the movers during the pre-move survey. This value **can only be updated once.** If there was an issue with estimating the weight and a mistake was made, the Prime contracter will need to contact the TOO to change it.  | [optional] 
**prime_actual_weight** | **int, none_type** | The actual weight of the shipment, provided after the Prime packs, picks up, and weighs a customer&#39;s shipment. | [optional] 
**nts_recorded_weight** | **int, none_type** | The previously recorded weight for the NTS Shipment. Used for NTS Release to know what the previous primeActualWeight or billable weight was. | [optional] 
**pickup_address** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The address where the movers should pick up this shipment, entered by the customer during onboarding when they enter shipment details.  | [optional] 
**destination_address** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Where the movers should deliver this shipment. Often provided by the customer when they enter shipment details during onboarding, if they know their new address already.  May be blank when entered by the customer, required when entered by the Prime. May not represent the true final destination due to the shipment being diverted or placed in SIT.  | [optional] 
**destination_type** | [**DestinationType**](DestinationType.md) |  | [optional] 
**secondary_pickup_address** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A second pickup address for this shipment, if the customer entered one. An optional field. | [optional] 
**secondary_delivery_address** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A second delivery address for this shipment, if the customer entered one. An optional field. | [optional] 
**storage_facility** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**shipment_type** | [**MTOShipmentType**](MTOShipmentType.md) |  | [optional] 
**diversion** | **bool** | This value indicates whether or not this shipment is part of a diversion. If yes, the shipment can be either the starting or ending segment of the diversion.  | [optional] 
**point_of_contact** | **str** | Email or ID of the person who will be contacted in the event of questions or concerns about this update. May be the person performing the update, or someone else working with the Prime contractor.  | [optional] 
**counselor_remarks** | **str, none_type** |  | [optional] 
**ppm_shipment** | [**UpdatePPMShipment**](UpdatePPMShipment.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


