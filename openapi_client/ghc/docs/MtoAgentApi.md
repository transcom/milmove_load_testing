# ghc_client.MtoAgentApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_mto_agent_list**](MtoAgentApi.md#fetch_mto_agent_list) | **GET** /move_task_orders/{moveTaskOrderID}/mto_shipments/{shipmentID}/mto-agents | Fetch move task order agents.


# **fetch_mto_agent_list**
> MTOAgents fetch_mto_agent_list(move_task_order_id, shipment_id)

Fetch move task order agents.

Fetches a list of agents associated with a move task order.

### Example


```python
import time
import ghc_client
from ghc_client.api import mto_agent_api
from ghc_client.model.error import Error
from ghc_client.model.mto_agents import MTOAgents
from ghc_client.model.validation_error import ValidationError
from pprint import pprint
# Defining the host is optional and defaults to /ghc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ghc_client.Configuration(
    host = "/ghc/v1"
)


# Enter a context with an instance of the API client
with ghc_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mto_agent_api.MtoAgentApi(api_client)
    move_task_order_id = "moveTaskOrderID_example" # str | ID of move task order
    shipment_id = "shipmentID_example" # str | ID of the shipment

    # example passing only required values which don't have defaults set
    try:
        # Fetch move task order agents.
        api_response = api_instance.fetch_mto_agent_list(move_task_order_id, shipment_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling MtoAgentApi->fetch_mto_agent_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_task_order_id** | **str**| ID of move task order |
 **shipment_id** | **str**| ID of the shipment |

### Return type

[**MTOAgents**](MTOAgents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved all agents for a move task order |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

