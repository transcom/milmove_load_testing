# MTOServiceItemDomesticStandaloneCratingAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The dimensions of the item being crated. | 
**crate** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The dimensions for the crate the item will be shipped in. | 
**description** | **str** | A description of the item being crated. | 
**re_service_code** | **str** | A unique code for the service item. Indicates if the service is for crating (DCRTSA). | defaults to "DCRTSA"
**reason** | **str, none_type** | The contractor&#39;s explanation for why an item needed to be crated or uncrated. Used by the TOO while deciding to approve or reject the service item.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


