# UpdateMTOServiceItemShuttle

Subtype used to provide the estimated weight and actual weight for shuttle. This is not creating a new service item but rather updating an existing service item. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_type** | [**UpdateMTOServiceItemModelType**](UpdateMTOServiceItemModelType.md) |  | 
**actual_weight** | **int, none_type** | Provided by the movers, based on weight tickets. Relevant for shuttling (DDSHUT &amp; DOSHUT) service items. | [optional] 
**estimated_weight** | **int, none_type** | An estimate of how much weight from a shipment will be included in a shuttling (DDSHUT &amp; DOSHUT) service item. | [optional] 
**re_service_code** | **str** | Service code allowed for this model type. | [optional] 
**id** | **str** | ID of the service item. Must match path. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


