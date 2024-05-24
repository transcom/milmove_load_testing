# ServiceMemberPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**is_profile_complete** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**edipi** | **str, none_type** |  | [optional] 
**emplid** | **str, none_type** |  | [optional] 
**orders** | [**[Orders]**](Orders.md) |  | [optional] 
**affiliation** | [**Affiliation**](Affiliation.md) |  | [optional] 
**grade** | [**OrderPayGrade**](OrderPayGrade.md) |  | [optional] 
**first_name** | **str, none_type** |  | [optional] 
**middle_name** | **str, none_type** |  | [optional] 
**last_name** | **str, none_type** |  | [optional] 
**suffix** | **str, none_type** |  | [optional] 
**telephone** | **str, none_type** |  | [optional] 
**secondary_telephone** | **str, none_type** |  | [optional] 
**personal_email** | **str, none_type** |  | [optional] 
**phone_is_preferred** | **bool, none_type** |  | [optional] 
**email_is_preferred** | **bool, none_type** |  | [optional] 
**residential_address** | [**Address**](Address.md) |  | [optional] 
**backup_mailing_address** | [**Address**](Address.md) |  | [optional] 
**backup_contacts** | [**IndexServiceMemberBackupContactsPayload**](IndexServiceMemberBackupContactsPayload.md) |  | [optional] 
**cac_validated** | **bool** |  | [optional] 
**weight_allotment** | [**WeightAllotment**](WeightAllotment.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


