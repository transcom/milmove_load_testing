# SignedCertification

Signed certification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the signed certification. | [readonly] 
**submitting_user_id** | **str** | The ID of the user that signed. | [readonly] 
**move_id** | **str** | The ID of the move associated with this signed certification. | [readonly] 
**certification_type** | [**SignedCertificationType**](SignedCertificationType.md) |  | 
**certification_text** | **str** | Full text that the customer agreed to and signed. | 
**signature** | **str** | The signature that the customer provided. | 
**date** | **date** | Date that the customer signed the certification. | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**e_tag** | **str** | A hash that should be used as the \&quot;If-Match\&quot; header for any updates. | [readonly] 
**ppm_id** | **str, none_type** | The ID of the PPM shipment associated with this signed certification, if any. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


