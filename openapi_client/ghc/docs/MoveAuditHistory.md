# MoveAuditHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id from audity_history table | [optional] 
**schema_name** | **str** | Database schema audited table for this event is in | [optional] 
**table_name** | **str** | name of database table that was changed | [optional] 
**rel_id** | **int** | relation OID. Table OID (object identifier). Changes with drop/create. | [optional] 
**object_id** | **str, none_type** | id column for the tableName where the data was changed | [optional] 
**session_user_id** | **str, none_type** |  | [optional] 
**session_user_first_name** | **str, none_type** |  | [optional] 
**session_user_last_name** | **str, none_type** |  | [optional] 
**session_user_email** | **str, none_type** |  | [optional] 
**session_user_telephone** | **str, none_type** |  | [optional] 
**context** | **[{str: (str,)}], none_type** |  | [optional] 
**context_id** | **str, none_type** | id column for the context table the record belongs to | [optional] 
**event_name** | **str, none_type** | API endpoint name that was called to make the change | [optional] 
**action_tstamp_tx** | **datetime** | Transaction start timestamp for tx in which audited event occurred | [optional] 
**action_tstamp_stm** | **datetime** | Statement start timestamp for tx in which audited event occurred | [optional] 
**action_tstamp_clk** | **datetime** | Wall clock time at which audited event&#39;s trigger call occurred | [optional] 
**transaction_id** | **int, none_type** | Identifier of transaction that made the change. May wrap, but unique paired with action_tstamp_tx. | [optional] 
**action** | **str** | Action type; I &#x3D; insert, D &#x3D; delete, U &#x3D; update, T &#x3D; truncate | [optional] 
**old_values** | **bool, date, datetime, dict, float, int, list, str, none_type** | A list of (old/previous) MoveAuditHistoryItem&#39;s for a record before the change. | [optional] 
**changed_values** | **bool, date, datetime, dict, float, int, list, str, none_type** | A list of (changed/updated) MoveAuditHistoryItem&#39;s for a record after the change. | [optional] 
**statement_only** | **bool** | true if audit event is from an FOR EACH STATEMENT trigger, false for FOR EACH ROW&#39; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


