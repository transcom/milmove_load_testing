# MTOServiceItemShuttleAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**re_service_code** | **str** | A unique code for the service item. Indicates if shuttling is requested for the shipment origin (&#x60;DOSHUT&#x60;) or destination (&#x60;DDSHUT&#x60;).  | 
**reason** | **str** | The contractor&#39;s explanation for why a shuttle service is requested. Used by the TOO while deciding to approve or reject the service item.  | 
**estimated_weight** | **int, none_type** | An estimate of how much weight from a shipment will be included in the shuttling service. | [optional] 
**actual_weight** | **int, none_type** | A record of the actual weight that was shuttled. Provided by the movers, based on weight tickets. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


