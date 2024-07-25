# ghc_client.OfficeUsersApi

All URIs are relative to */ghc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_requested_office_user**](OfficeUsersApi.md#create_requested_office_user) | **POST** /open/requested-office-users | Create an Office User


# **create_requested_office_user**
> OfficeUser create_requested_office_user()

Create an Office User

This endpoint is publicly accessible as it is utilized for individuals who do not have an office account to request the creation of an office account. Request the creation of an office user. An administrator will need to approve them after creation. Note on requirements: An identification method must be present. The following 2 fields have an \"OR\" requirement. - edipi - other_unique_id One of these two fields MUST be present to serve as identification for the office user being created. This logic is handled at the application level. 

### Example


```python
import time
import ghc_client
from ghc_client.api import office_users_api
from ghc_client.model.office_user_create import OfficeUserCreate
from ghc_client.model.office_user import OfficeUser
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
    api_instance = office_users_api.OfficeUsersApi(api_client)
    office_user = OfficeUserCreate(
        email="user@userdomain.com",
        edipi="1234567890",
        other_unique_id="other_unique_id_example",
        first_name="first_name_example",
        middle_initials="L.",
        last_name="last_name_example",
        telephone="212-555-5555",
        transportation_office_id="c56a4180-65aa-42ec-a945-5fd21dec0538",
        roles=[
            OfficeUserRole(
                name="Task Ordering Officer",
                role_type="task_ordering_officer",
            ),
        ],
    ) # OfficeUserCreate | Office User information (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an Office User
        api_response = api_instance.create_requested_office_user(office_user=office_user)
        pprint(api_response)
    except ghc_client.ApiException as e:
        print("Exception when calling OfficeUsersApi->create_requested_office_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_user** | [**OfficeUserCreate**](OfficeUserCreate.md)| Office User information | [optional]

### Return type

[**OfficeUser**](OfficeUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successfully requested the creation of provided office user |  -  |
**422** | validation error |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

