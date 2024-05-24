# internal_client.ServiceMembersApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_member**](ServiceMembersApi.md#create_service_member) | **POST** /service_members | Creates service member for a logged-in user
[**patch_service_member**](ServiceMembersApi.md#patch_service_member) | **PATCH** /service_members/{serviceMemberId} | Patches the service member
[**show_service_member**](ServiceMembersApi.md#show_service_member) | **GET** /service_members/{serviceMemberId} | Returns the given service member
[**show_service_member_orders**](ServiceMembersApi.md#show_service_member_orders) | **GET** /service_members/{serviceMemberId}/current_orders | Returns the latest orders for a given service member


# **create_service_member**
> ServiceMemberPayload create_service_member(create_service_member_payload)

Creates service member for a logged-in user

Creates an instance of a service member tied to a user

### Example


```python
import time
import internal_client
from internal_client.api import service_members_api
from internal_client.model.service_member_payload import ServiceMemberPayload
from internal_client.model.create_service_member_payload import CreateServiceMemberPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = service_members_api.ServiceMembersApi(api_client)
    create_service_member_payload = CreateServiceMemberPayload(
        user_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        edipi="5789345789",
        affiliation=Affiliation("ARMY"),
        grade=OrderPayGrade("E_1"),
        first_name="John",
        middle_name="L.",
        last_name="Donut",
        suffix="Jr.",
        telephone="212-555-5555",
        secondary_telephone="212-555-5555",
        personal_email="john_bob@example.com",
        phone_is_preferred=True,
        email_is_preferred=True,
        current_location_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        residential_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
            county="LOS ANGELES",
        ),
        backup_mailing_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
            county="LOS ANGELES",
        ),
    ) # CreateServiceMemberPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Creates service member for a logged-in user
        api_response = api_instance.create_service_member(create_service_member_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling ServiceMembersApi->create_service_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_service_member_payload** | [**CreateServiceMemberPayload**](CreateServiceMemberPayload.md)|  |

### Return type

[**ServiceMemberPayload**](ServiceMemberPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created instance of service member |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | service member not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_service_member**
> ServiceMemberPayload patch_service_member(service_member_id, patch_service_member_payload)

Patches the service member

Any fields sent in this request will be set on the service member referenced

### Example


```python
import time
import internal_client
from internal_client.api import service_members_api
from internal_client.model.service_member_payload import ServiceMemberPayload
from internal_client.model.patch_service_member_payload import PatchServiceMemberPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = service_members_api.ServiceMembersApi(api_client)
    service_member_id = "serviceMemberId_example" # str | UUID of the service member
    patch_service_member_payload = PatchServiceMemberPayload(
        user_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        edipi="5789345789",
        emplid="5789345",
        affiliation=Affiliation("ARMY"),
        first_name="John",
        middle_name="L.",
        last_name="Donut",
        suffix="Jr.",
        telephone="212-555-5555",
        secondary_telephone="212-555-5555",
        personal_email="john_bob@example.com",
        phone_is_preferred=True,
        email_is_preferred=True,
        current_location_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        residential_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
            county="LOS ANGELES",
        ),
        backup_mailing_address=Address(
            id="c56a4180-65aa-42ec-a945-5fd21dec0538",
            street_address1="123 Main Ave",
            street_address2="Apartment 9000",
            street_address3="Montmârtre",
            city="Anytown",
            state="AL",
            postal_code="90210",
            country="USA",
            county="LOS ANGELES",
        ),
    ) # PatchServiceMemberPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Patches the service member
        api_response = api_instance.patch_service_member(service_member_id, patch_service_member_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling ServiceMembersApi->patch_service_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_member_id** | **str**| UUID of the service member |
 **patch_service_member_payload** | [**PatchServiceMemberPayload**](PatchServiceMemberPayload.md)|  |

### Return type

[**ServiceMemberPayload**](ServiceMemberPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated instance of service member |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | service member not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_service_member**
> ServiceMemberPayload show_service_member(service_member_id)

Returns the given service member

Returns the given service member

### Example


```python
import time
import internal_client
from internal_client.api import service_members_api
from internal_client.model.service_member_payload import ServiceMemberPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = service_members_api.ServiceMembersApi(api_client)
    service_member_id = "serviceMemberId_example" # str | UUID of the service member

    # example passing only required values which don't have defaults set
    try:
        # Returns the given service member
        api_response = api_instance.show_service_member(service_member_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling ServiceMembersApi->show_service_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_member_id** | **str**| UUID of the service member |

### Return type

[**ServiceMemberPayload**](ServiceMemberPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the instance of the service member |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | service member not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_service_member_orders**
> Orders show_service_member_orders(service_member_id)

Returns the latest orders for a given service member

Returns orders

### Example


```python
import time
import internal_client
from internal_client.api import service_members_api
from internal_client.model.orders import Orders
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = service_members_api.ServiceMembersApi(api_client)
    service_member_id = "serviceMemberId_example" # str | UUID of the service member

    # example passing only required values which don't have defaults set
    try:
        # Returns the latest orders for a given service member
        api_response = api_instance.show_service_member_orders(service_member_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling ServiceMembersApi->show_service_member_orders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_member_id** | **str**| UUID of the service member |

### Return type

[**Orders**](Orders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the instance of the service member |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | service member not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

