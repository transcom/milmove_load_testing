# UpdateWeightTicket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty_weight** | **int** | Weight of the vehicle when empty. | [optional] 
**full_weight** | **int** | The weight of the vehicle when full. | [optional] 
**owns_trailer** | **bool** | Indicates if the customer used a trailer they own for the move. | [optional] 
**trailer_meets_criteria** | **bool** | Indicates if the trailer that the customer used meets all the criteria to be claimable. | [optional] 
**status** | [**PPMDocumentStatus**](PPMDocumentStatus.md) |  | [optional] 
**reason** | **str** | The reason the services counselor has excluded or rejected the item. | [optional] 
**adjusted_net_weight** | **int** | Indicates the adjusted net weight of the vehicle | [optional] 
**net_weight_remarks** | **str** | Remarks explaining any edits made to the net weight | [optional] 
**allowable_weight** | **int** | Indicates the maximum reimbursable weight of the shipment | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


