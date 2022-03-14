# internal_client.BackupContactsApi

All URIs are relative to */internal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_member_backup_contact**](BackupContactsApi.md#create_service_member_backup_contact) | **POST** /service_members/{serviceMemberId}/backup_contacts | Submits backup contact for a logged-in user
[**index_service_member_backup_contacts**](BackupContactsApi.md#index_service_member_backup_contacts) | **GET** /service_members/{serviceMemberId}/backup_contacts | List all service member backup contacts
[**show_service_member_backup_contact**](BackupContactsApi.md#show_service_member_backup_contact) | **GET** /backup_contacts/{backupContactId} | Returns the given service member backup contact
[**update_service_member_backup_contact**](BackupContactsApi.md#update_service_member_backup_contact) | **PUT** /backup_contacts/{backupContactId} | Updates a service member backup contact


# **create_service_member_backup_contact**
> ServiceMemberBackupContactPayload create_service_member_backup_contact(service_member_id, create_backup_contact_payload)

Submits backup contact for a logged-in user

Creates an instance of a backup contact tied to a service member user

### Example


```python
import time
import internal_client
from internal_client.api import backup_contacts_api
from internal_client.model.service_member_backup_contact_payload import ServiceMemberBackupContactPayload
from internal_client.model.create_service_member_backup_contact_payload import CreateServiceMemberBackupContactPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = backup_contacts_api.BackupContactsApi(api_client)
    service_member_id = "serviceMemberId_example" # str | UUID of the service member
    create_backup_contact_payload = CreateServiceMemberBackupContactPayload(
        name="Susan Smith",
        telephone="212-555-5555",
        email="john_bob@exmaple.com",
        permission=BackupContactPermission("NONE"),
    ) # CreateServiceMemberBackupContactPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Submits backup contact for a logged-in user
        api_response = api_instance.create_service_member_backup_contact(service_member_id, create_backup_contact_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling BackupContactsApi->create_service_member_backup_contact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_member_id** | **str**| UUID of the service member |
 **create_backup_contact_payload** | [**CreateServiceMemberBackupContactPayload**](CreateServiceMemberBackupContactPayload.md)|  |

### Return type

[**ServiceMemberBackupContactPayload**](ServiceMemberBackupContactPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created instance of service member backup contact |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized to create this backup contact |  -  |
**404** | contact not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_service_member_backup_contacts**
> IndexServiceMemberBackupContactsPayload index_service_member_backup_contacts(service_member_id)

List all service member backup contacts

List all service member backup contacts

### Example


```python
import time
import internal_client
from internal_client.api import backup_contacts_api
from internal_client.model.index_service_member_backup_contacts_payload import IndexServiceMemberBackupContactsPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = backup_contacts_api.BackupContactsApi(api_client)
    service_member_id = "serviceMemberId_example" # str | UUID of the service member

    # example passing only required values which don't have defaults set
    try:
        # List all service member backup contacts
        api_response = api_instance.index_service_member_backup_contacts(service_member_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling BackupContactsApi->index_service_member_backup_contacts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_member_id** | **str**| UUID of the service member |

### Return type

[**IndexServiceMemberBackupContactsPayload**](IndexServiceMemberBackupContactsPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of service member backup contacts |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized to see this backup contact |  -  |
**404** | contact not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_service_member_backup_contact**
> ServiceMemberBackupContactPayload show_service_member_backup_contact(backup_contact_id)

Returns the given service member backup contact

Returns the given service member backup contact

### Example


```python
import time
import internal_client
from internal_client.api import backup_contacts_api
from internal_client.model.service_member_backup_contact_payload import ServiceMemberBackupContactPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = backup_contacts_api.BackupContactsApi(api_client)
    backup_contact_id = "backupContactId_example" # str | UUID of the service member backup contact

    # example passing only required values which don't have defaults set
    try:
        # Returns the given service member backup contact
        api_response = api_instance.show_service_member_backup_contact(backup_contact_id)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling BackupContactsApi->show_service_member_backup_contact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_contact_id** | **str**| UUID of the service member backup contact |

### Return type

[**ServiceMemberBackupContactPayload**](ServiceMemberBackupContactPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the instance of the service member backup contact |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | backup contact not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_member_backup_contact**
> ServiceMemberBackupContactPayload update_service_member_backup_contact(backup_contact_id, update_service_member_backup_contact_payload)

Updates a service member backup contact

Any fields sent in this request will be set on the backup contact referenced

### Example


```python
import time
import internal_client
from internal_client.api import backup_contacts_api
from internal_client.model.service_member_backup_contact_payload import ServiceMemberBackupContactPayload
from internal_client.model.update_service_member_backup_contact_payload import UpdateServiceMemberBackupContactPayload
from pprint import pprint
# Defining the host is optional and defaults to /internal
# See configuration.py for a list of all supported configuration parameters.
configuration = internal_client.Configuration(
    host = "/internal"
)


# Enter a context with an instance of the API client
with internal_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = backup_contacts_api.BackupContactsApi(api_client)
    backup_contact_id = "backupContactId_example" # str | UUID of the service member backup contact
    update_service_member_backup_contact_payload = UpdateServiceMemberBackupContactPayload(
        name="Susan Smith",
        telephone="212-555-5555",
        email="john_bob@example.com",
        permission=BackupContactPermission("NONE"),
    ) # UpdateServiceMemberBackupContactPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a service member backup contact
        api_response = api_instance.update_service_member_backup_contact(backup_contact_id, update_service_member_backup_contact_payload)
        pprint(api_response)
    except internal_client.ApiException as e:
        print("Exception when calling BackupContactsApi->update_service_member_backup_contact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_contact_id** | **str**| UUID of the service member backup contact |
 **update_service_member_backup_contact_payload** | [**UpdateServiceMemberBackupContactPayload**](UpdateServiceMemberBackupContactPayload.md)|  |

### Return type

[**ServiceMemberBackupContactPayload**](ServiceMemberBackupContactPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | updated instance of backup contact |  -  |
**400** | invalid request |  -  |
**401** | request requires user authentication |  -  |
**403** | user is not authorized |  -  |
**404** | backup contact not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

