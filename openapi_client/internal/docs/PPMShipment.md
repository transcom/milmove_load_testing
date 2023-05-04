# PPMShipment

A personally procured move is a type of shipment that a service member moves themselves.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary auto-generated unique identifier of the PPM shipment object | [readonly] 
**shipment_id** | **str** | The id of the parent MTOShipment object | [readonly] 
**created_at** | **datetime** | Timestamp of when the PPM Shipment was initially created (UTC) | [readonly] 
**status** | [**PPMShipmentStatus**](PPMShipmentStatus.md) |  | 
**expected_departure_date** | **date** | Date the customer expects to begin their move.  | 
**pickup_postal_code** | **str** | The postal code of the origin location where goods are being moved from. | 
**destination_postal_code** | **str** | The postal code of the destination location where goods are being delivered to. | 
**sit_expected** | **bool** | Captures whether some or all of the PPM shipment will require temporary storage at the origin or destination.  Must be set to &#x60;true&#x60; when providing &#x60;sitLocation&#x60;, &#x60;sitEstimatedWeight&#x60;, &#x60;sitEstimatedEntryDate&#x60;, and &#x60;sitEstimatedDepartureDate&#x60; values to calculate the &#x60;sitEstimatedCost&#x60;.  | 
**e_tag** | **str** | A hash unique to this shipment that should be used as the \&quot;If-Match\&quot; header for any updates. | [readonly] 
**updated_at** | **datetime** | Timestamp of when a property of this object was last updated (UTC) | [optional] [readonly] 
**w2_address** | [**Address**](Address.md) |  | [optional] 
**advance_status** | [**PPMAdvanceStatus**](PPMAdvanceStatus.md) |  | [optional] 
**actual_move_date** | **date, none_type** | The actual start date of when the PPM shipment left the origin. | [optional] 
**submitted_at** | **datetime, none_type** | The timestamp of when the customer submitted their PPM documentation to the counselor for review. | [optional] 
**reviewed_at** | **datetime, none_type** | The timestamp of when the Service Counselor has reviewed all of the closeout documents. | [optional] 
**approved_at** | **datetime, none_type** | The timestamp of when the shipment was approved and the service member can begin their move. | [optional] 
**secondary_pickup_postal_code** | **str, none_type** |  | [optional] 
**actual_pickup_postal_code** | **str, none_type** | The actual postal code where the PPM shipment started. To be filled once the customer has moved the shipment.  | [optional] 
**secondary_destination_postal_code** | **str, none_type** | An optional secondary location near the destination where goods will be dropped off. | [optional] 
**actual_destination_postal_code** | **str, none_type** | The actual postal code where the PPM shipment ended. To be filled once the customer has moved the shipment.  | [optional] 
**estimated_weight** | **int, none_type** | The estimated weight of the PPM shipment goods being moved. | [optional] 
**has_pro_gear** | **bool, none_type** | Indicates whether PPM shipment has pro gear for themselves or their spouse.  | [optional] 
**pro_gear_weight** | **int, none_type** | The estimated weight of the pro-gear being moved belonging to the service member. | [optional] 
**spouse_pro_gear_weight** | **int, none_type** | The estimated weight of the pro-gear being moved belonging to a spouse. | [optional] 
**estimated_incentive** | **int, none_type** | The estimated amount the government will pay the service member to move their belongings based on the moving date, locations, and shipment weight. | [optional] 
**final_incentive** | **int, none_type** | The final calculated incentive for the PPM shipment. This does not include **SIT** as it is a reimbursement.  | [optional] [readonly] 
**has_requested_advance** | **bool, none_type** | Indicates whether an advance has been requested for the PPM shipment.  | [optional] 
**advance_amount_requested** | **int, none_type** | The amount requested as an advance by the service member up to a maximum percentage of the estimated incentive.  | [optional] 
**has_received_advance** | **bool, none_type** | Indicates whether an advance was received for the PPM shipment.  | [optional] 
**advance_amount_received** | **int, none_type** | The amount received for an advance, or null if no advance is received.  | [optional] 
**sit_location** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**sit_estimated_weight** | **int, none_type** | The estimated weight of the goods being put into storage. | [optional] 
**sit_estimated_entry_date** | **date, none_type** | The date that goods will first enter the storage location. | [optional] 
**sit_estimated_departure_date** | **date, none_type** | The date that goods will exit the storage location. | [optional] 
**sit_estimated_cost** | **int, none_type** | The estimated amount that the government will pay the service member to put their goods into storage. This estimated storage cost is separate from the estimated incentive. | [optional] 
**weight_tickets** | [**WeightTickets**](WeightTickets.md) |  | [optional] 
**moving_expenses** | [**[MovingExpense]**](MovingExpense.md) | All expense documentation receipt records of this PPM shipment. | [optional] 
**pro_gear_weight_tickets** | [**[ProGearWeightTicket]**](ProGearWeightTicket.md) | All pro-gear weight ticket documentation records for this PPM shipment. | [optional] 
**signed_certification** | [**SignedCertification**](SignedCertification.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


