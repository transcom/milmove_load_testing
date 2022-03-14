# ghc_client.ReweighApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_shipment_reweigh**](ReweighApi.md#request_shipment_reweigh) | **POST** /shipments/{shipmentID}/request-reweigh | Requests a shipment reweigh


# **request_shipment_reweigh**
> Reweigh request_shipment_reweigh(shipment_id)

Requests a shipment reweigh

Requests a shipment reweigh

### Example


```python
import time
import ghc_client
from ghc_client.api import reweigh_api
from ghc_client.model.reweigh import Reweigh
from ghc_client.model.error import Error
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
    api_instance = reweigh_api.ReweighApi(api_client)
    shipment_id = "shipmentID_example" # str | ID of the shipment

    # example passing only required values which don't have defaults set
    try:
        # Requests a shipment reweigh
        api_response = api_instance.request_shipment_reweigh(shipment_id)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling ReweighApi->request_shipment_reweigh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| ID of the shipment |

### Return type

[**Reweigh**](Reweigh.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully requested a reweigh of the shipment |  -  |
**403** | The request was denied |  -  |
**404** | The requested resource wasn&#39;t found |  -  |
**409** | Conflict error |  -  |
**412** | Precondition failed |  -  |
**422** | The payload was unprocessable. |  -  |
**500** | A server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

