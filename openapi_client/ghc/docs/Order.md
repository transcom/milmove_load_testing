# Order


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**move_code** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] [readonly] 
**last_name** | **str** |  | [optional] [readonly] 
**grade** | [**Grade**](Grade.md) |  | [optional] 
**agency** | [**Affiliation**](Affiliation.md) |  | [optional] 
**entitlement** | [**Entitlements**](Entitlements.md) |  | [optional] 
**destination_duty_location** | [**DutyLocation**](DutyLocation.md) |  | [optional] 
**origin_duty_location** | [**DutyLocation**](DutyLocation.md) |  | [optional] 
**origin_duty_location_gbloc** | [**GBLOC**](GBLOC.md) |  | [optional] 
**move_task_order_id** | **str** |  | [optional] 
**uploaded_order_id** | **str** |  | [optional] 
**uploaded_amended_order_id** | **str, none_type** |  | [optional] 
**amended_orders_acknowledged_at** | **datetime, none_type** |  | [optional] 
**order_number** | **str, none_type** |  | [optional] 
**order_type** | [**OrdersType**](OrdersType.md) |  | [optional] 
**order_type_detail** | [**OrdersTypeDetail**](OrdersTypeDetail.md) |  | [optional] 
**date_issued** | **date** |  | [optional] 
**report_by_date** | **date** |  | [optional] 
**department_indicator** | [**DeptIndicator**](DeptIndicator.md) |  | [optional] 
**tac** | **str, none_type** |  | [optional] 
**sac** | **str, none_type** |  | [optional] 
**nts_tac** | **str, none_type** |  | [optional] 
**nts_sac** | **str, none_type** |  | [optional] 
**has_dependents** | **bool** |  | [optional] 
**spouse_has_pro_gear** | **bool** |  | [optional] 
**supply_and_services_cost_estimate** | **str** |  | [optional] 
**packing_and_shipping_instructions** | **str** |  | [optional] 
**method_of_payment** | **str** |  | [optional] 
**naics** | **str** |  | [optional] 
**e_tag** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


