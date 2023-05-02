# ProGearWeightTicket

Pro-gear associated information and weight docs for a PPM shipment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ppm_shipment_id** | **str** | The ID of the PPM shipment that this pro-gear weight ticket is associated with. | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**document_id** | **str** | The ID of the document that is associated with the user uploads containing the pro-gear weight. | [readonly] 
**document** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**id** | **str** | The ID of the pro-gear weight ticket. | [optional] [readonly] 
**belongs_to_self** | **bool, none_type** | Indicates if this information is for the customer&#39;s own pro-gear, otherwise, it&#39;s the spouse&#39;s. | [optional] 
**description** | **str, none_type** | Describes the pro-gear that was moved. | [optional] 
**has_weight_tickets** | **bool, none_type** | Indicates if the user has a weight ticket for their pro-gear, otherwise they have a constructed weight. | [optional] 
**weight** | **int, none_type** | Weight of the pro-gear. | [optional] 
**status** | [**OmittablePPMDocumentStatus**](OmittablePPMDocumentStatus.md) |  | [optional] 
**reason** | **str, none_type** | The reason the services counselor has excluded or rejected the item. | [optional] 
**e_tag** | **str** | A hash that should be used as the \&quot;If-Match\&quot; header for any updates. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


