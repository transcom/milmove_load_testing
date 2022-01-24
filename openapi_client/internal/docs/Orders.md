# Orders


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**service_member_id** | **str** |  | 
**issue_date** | **date** | The date and time that these orders were cut. | 
**report_by_date** | **date** | Report By Date | 
**orders_type** | [**OrdersType**](OrdersType.md) |  | 
**has_dependents** | **bool** |  | 
**spouse_has_pro_gear** | **bool** |  | 
**new_duty_station** | [**DutyStationPayload**](DutyStationPayload.md) |  | 
**uploaded_orders** | [**DocumentPayload**](DocumentPayload.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**grade** | **str, none_type** |  | [optional] 
**status** | [**OrdersStatus**](OrdersStatus.md) |  | [optional] 
**orders_type_detail** | [**OrdersTypeDetail**](OrdersTypeDetail.md) |  | [optional] 
**origin_duty_station** | [**DutyStationPayload**](DutyStationPayload.md) |  | [optional] 
**uploaded_amended_orders** | [**DocumentPayload**](DocumentPayload.md) |  | [optional] 
**uploaded_amended_orders_id** | **str** |  | [optional] 
**moves** | [**IndexMovesPayload**](IndexMovesPayload.md) |  | [optional] 
**orders_number** | **str, none_type** |  | [optional] 
**tac** | **str, none_type** |  | [optional] 
**sac** | **str, none_type** |  | [optional] 
**department_indicator** | [**DeptIndicator**](DeptIndicator.md) |  | [optional] 
**authorized_weight** | **int, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


