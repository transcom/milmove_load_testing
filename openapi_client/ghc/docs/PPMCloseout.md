# PPMCloseout

The calculations needed in the \"Review Documents\" section of a PPM closeout. LIst of all expenses/reimbursements related toa PPM shipment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary auto-generated unique identifier of the PPM shipment object | [readonly] 
**planned_move_date** | **date, none_type** | Date the customer expects to begin their move.  | [optional] 
**actual_move_date** | **date, none_type** | The actual start date of when the PPM shipment left the origin. | [optional] 
**miles** | **int, none_type** | The distance between the old address and the new address in miles. | [optional] 
**estimated_weight** | **int, none_type** | The estimated weight of the PPM shipment goods being moved. | [optional] 
**actual_weight** | **int, none_type** |  | [optional] 
**pro_gear_weight_customer** | **int, none_type** | The estimated weight of the pro-gear being moved belonging to the service member. | [optional] 
**pro_gear_weight_spouse** | **int, none_type** | The estimated weight of the pro-gear being moved belonging to a spouse. | [optional] 
**gross_incentive** | **int, none_type** | The final calculated incentive for the PPM shipment. This does not include **SIT** as it is a reimbursement.  | [optional] [readonly] 
**gcc** | **int, none_type** | Government Constructive Cost (GCC) | [optional] 
**aoa** | **int, none_type** | Advance Operating Allowance (AOA). | [optional] 
**remaining_incentive** | **int, none_type** | The remaining reimbursement amount that is still owed to the customer. | [optional] 
**haul_type** | **str, none_type** | The type of haul calculation used for this shipment (shorthaul or linehaul). | [optional] 
**haul_price** | **int, none_type** | The price of the linehaul or shorthaul. | [optional] 
**haul_fsc** | **int, none_type** | The linehaul/shorthaul Fuel Surcharge (FSC). | [optional] 
**dop** | **int, none_type** | The Domestic Origin Price (DOP). | [optional] 
**ddp** | **int, none_type** | The Domestic Destination Price (DDP). | [optional] 
**pack_price** | **int, none_type** | The full price of all packing/unpacking services. | [optional] 
**unpack_price** | **int, none_type** | The full price of all packing/unpacking services. | [optional] 
**sit_reimbursement** | **int, none_type** | The estimated amount that the government will pay the service member to put their goods into storage. This estimated storage cost is separate from the estimated incentive. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


