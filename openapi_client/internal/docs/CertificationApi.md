# internal_client.CertificationApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_signed_certification**](CertificationApi.md#create_signed_certification) | **POST** /moves/{moveId}/signed_certifications | Submits signed certification for the given move ID
[**index_signed_certification**](CertificationApi.md#index_signed_certification) | **GET** /moves/{moveId}/signed_certifications | gets the signed certifications for the given move ID


# **create_signed_certification**
> SignedCertificationPayload create_signed_certification(move_id, create_signed_certification_payload)

Submits signed certification for the given move ID

Create an instance of signed_certification tied to the move ID

### Example


```python
import time
import internal_client
from internal_client.api import certification_api
from internal_client.model.create_signed_certification_payload import CreateSignedCertificationPayload
from internal_client.model.signed_certification_payload import SignedCertificationPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certification_api.CertificationApi(api_client)
    move_id = "moveId_example" # str | UUID of the move being signed for
    create_signed_certification_payload = CreateSignedCertificationPayload(
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        signature="signature_example",
        certification_text="certification_text_example",
        personally_procured_move_id="personally_procured_move_id_example",
        ppm_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        certification_type=SignedCertificationTypeCreate("PPM_PAYMENT"),
    ) # CreateSignedCertificationPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Submits signed certification for the given move ID
        api_response = api_instance.create_signed_certification(move_id, create_signed_certification_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling CertificationApi->create_signed_certification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**| UUID of the move being signed for |
 **create_signed_certification_payload** | [**CreateSignedCertificationPayload**](CreateSignedCertificationPayload.md)|  |

### Return type

[**SignedCertificationPayload**](SignedCertificationPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created instance of signed_certification |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized to sign for this move |  -  |
**404** | move not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_signed_certification**
> SignedCertifications index_signed_certification(move_id)

gets the signed certifications for the given move ID

returns a list of all signed_certifications associated with the move ID

### Example


```python
import time
import internal_client
from internal_client.api import certification_api
from internal_client.model.signed_certifications import SignedCertifications
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = certification_api.CertificationApi(api_client)
    move_id = "moveId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # gets the signed certifications for the given move ID
        api_response = api_instance.index_signed_certification(move_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling CertificationApi->index_signed_certification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_id** | **str**|  |

### Return type

[**SignedCertifications**](SignedCertifications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns a list of signed certifications |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | move not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

