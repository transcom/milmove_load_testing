# WeightTicket

Vehicle and optional trailer information and weight documents used to move this PPM shipment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ppm_shipment_id** | **str** | The ID of the PPM shipment that this set of weight tickets is for. | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**empty_document_id** | **str** | ID of the document that is associated with the user uploads containing the vehicle weight when empty. | [readonly] 
**empty_document** | [**WeightTicketEmptyDocument**](WeightTicketEmptyDocument.md) |  | 
**full_document_id** | **str** | ID of the document that is associated with the user uploads containing the vehicle weight when full. | [readonly] 
**full_document** | [**WeightTicketFullDocument**](WeightTicketFullDocument.md) |  | 
**proof_of_trailer_ownership_document_id** | **str** | ID of the document that is associated with the user uploads containing the proof of trailer ownership. | [readonly] 
**proof_of_trailer_ownership_document** | [**WeightTicketProofOfTrailerOwnershipDocument**](WeightTicketProofOfTrailerOwnershipDocument.md) |  | 
**id** | **str** | ID of this set of weight tickets. | [optional] [readonly] 
**vehicle_description** | **str, none_type** | Description of the vehicle used for the trip. E.g. make/model, type of truck/van, etc. | [optional] 
**empty_weight** | **int, none_type** | Weight of the vehicle when empty. | [optional] 
**missing_empty_weight_ticket** | **bool, none_type** | Indicates if the customer is missing a weight ticket for the vehicle weight when empty. | [optional] 
**full_weight** | **int, none_type** | The weight of the vehicle when full. | [optional] 
**missing_full_weight_ticket** | **bool, none_type** | Indicates if the customer is missing a weight ticket for the vehicle weight when full. | [optional] 
**owns_trailer** | **bool, none_type** | Indicates if the customer used a trailer they own for the move. | [optional] 
**trailer_meets_criteria** | **bool, none_type** | Indicates if the trailer that the customer used meets all the criteria to be claimable. | [optional] 
**status** | [**OmittablePPMDocumentStatus**](OmittablePPMDocumentStatus.md) |  | [optional] 
**reason** | **str, none_type** | The reason the services counselor has excluded or rejected the item. | [optional] 
**adjusted_net_weight** | **int, none_type** | Indicates the adjusted net weight of the vehicle | [optional] 
**net_weight_remarks** | **str, none_type** | Remarks explaining any edits made to the net weight | [optional] 
**e_tag** | **str** | A hash that should be used as the \&quot;If-Match\&quot; header for any updates. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


