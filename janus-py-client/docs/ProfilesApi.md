# janus_py_client.ProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_delete_profile_profiles_path_resource_path_rname_delete**](ProfilesApi.md#controller_delete_profile_profiles_path_resource_path_rname_delete) | **DELETE** /api/janus/controller/profiles/{resource}/{rname} | Remove a profile
[**controller_get_profile_by_name_profiles_path_resource_path_rname_get**](ProfilesApi.md#controller_get_profile_by_name_profiles_path_resource_path_rname_get) | **GET** /api/janus/controller/profiles/{resource}/{rname} | Get a specific profile
[**controller_get_profiles_by_resource_profiles_path_resource_get**](ProfilesApi.md#controller_get_profiles_by_resource_profiles_path_resource_get) | **GET** /api/janus/controller/profiles/{resource} | Get profiles for a resource
[**controller_get_profiles_default_profiles_get**](ProfilesApi.md#controller_get_profiles_default_profiles_get) | **GET** /api/janus/controller/profiles | Get host profiles (default)
[**controller_post_profile_profiles_path_resource_path_rname_post**](ProfilesApi.md#controller_post_profile_profiles_path_resource_path_rname_post) | **POST** /api/janus/controller/profiles/{resource}/{rname} | Create a new profile
[**controller_put_profile_profiles_path_resource_path_rname_put**](ProfilesApi.md#controller_put_profile_profiles_path_resource_path_rname_put) | **PUT** /api/janus/controller/profiles/{resource}/{rname} | Update a profile


# **controller_delete_profile_profiles_path_resource_path_rname_delete**
> controller_delete_profile_profiles_path_resource_path_rname_delete(resource, rname)

Remove a profile

Remove a profile.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): jwt
configuration = janus_py_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure HTTP basic authorization: basicAuth
configuration = janus_py_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.ProfilesApi(api_client)
    resource = 'resource_example' # str | Resource type
    rname = 'rname_example' # str | Profile name

    try:
        # Remove a profile
        api_instance.controller_delete_profile_profiles_path_resource_path_rname_delete(resource, rname)
    except Exception as e:
        print("Exception when calling ProfilesApi->controller_delete_profile_profiles_path_resource_path_rname_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rname** | **str**| Profile name | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_profile_by_name_profiles_path_resource_path_rname_get**
> ProfileResponse controller_get_profile_by_name_profiles_path_resource_path_rname_get(resource, rname, refresh=refresh, reset=reset, fields=fields)

Get a specific profile

Get a specific profile by resource type and name.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.profile_response import ProfileResponse
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): jwt
configuration = janus_py_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure HTTP basic authorization: basicAuth
configuration = janus_py_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.ProfilesApi(api_client)
    resource = 'resource_example' # str | Resource type
    rname = 'rname_example' # str | Profile name
    refresh = True # bool | Refresh profiles from files (optional)
    reset = True # bool | Reset database tables (optional)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get a specific profile
        api_response = api_instance.controller_get_profile_by_name_profiles_path_resource_path_rname_get(resource, rname, refresh=refresh, reset=reset, fields=fields)
        print("The response of ProfilesApi->controller_get_profile_by_name_profiles_path_resource_path_rname_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->controller_get_profile_by_name_profiles_path_resource_path_rname_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rname** | **str**| Profile name | 
 **refresh** | **bool**| Refresh profiles from files | [optional] 
 **reset** | **bool**| Reset database tables | [optional] 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_profiles_by_resource_profiles_path_resource_get**
> List[ProfileResponse] controller_get_profiles_by_resource_profiles_path_resource_get(resource, refresh=refresh, reset=reset, fields=fields)

Get profiles for a resource

Get all profiles for a specific resource type.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.profile_response import ProfileResponse
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): jwt
configuration = janus_py_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure HTTP basic authorization: basicAuth
configuration = janus_py_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.ProfilesApi(api_client)
    resource = 'resource_example' # str | Resource type (e.g., host, net, vol, qos)
    refresh = True # bool | Refresh profiles from files (optional)
    reset = True # bool | Reset database tables (optional)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get profiles for a resource
        api_response = api_instance.controller_get_profiles_by_resource_profiles_path_resource_get(resource, refresh=refresh, reset=reset, fields=fields)
        print("The response of ProfilesApi->controller_get_profiles_by_resource_profiles_path_resource_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->controller_get_profiles_by_resource_profiles_path_resource_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type (e.g., host, net, vol, qos) | 
 **refresh** | **bool**| Refresh profiles from files | [optional] 
 **reset** | **bool**| Reset database tables | [optional] 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

[**List[ProfileResponse]**](ProfileResponse.md)

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_profiles_default_profiles_get**
> List[ProfileResponse] controller_get_profiles_default_profiles_get(refresh=refresh, reset=reset, fields=fields)

Get host profiles (default)

Get host profiles (defaults to 'host' resource).

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.profile_response import ProfileResponse
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): jwt
configuration = janus_py_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure HTTP basic authorization: basicAuth
configuration = janus_py_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.ProfilesApi(api_client)
    refresh = True # bool | Refresh profiles from files (optional)
    reset = True # bool | Reset database tables (optional)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get host profiles (default)
        api_response = api_instance.controller_get_profiles_default_profiles_get(refresh=refresh, reset=reset, fields=fields)
        print("The response of ProfilesApi->controller_get_profiles_default_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->controller_get_profiles_default_profiles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Refresh profiles from files | [optional] 
 **reset** | **bool**| Reset database tables | [optional] 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

[**List[ProfileResponse]**](ProfileResponse.md)

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_post_profile_profiles_path_resource_path_rname_post**
> ProfileResponse controller_post_profile_profiles_path_resource_path_rname_post(resource, rname, profile_request)

Create a new profile

Create a new profile.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.profile_request import ProfileRequest
from janus_py_client.models.profile_response import ProfileResponse
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): jwt
configuration = janus_py_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure HTTP basic authorization: basicAuth
configuration = janus_py_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.ProfilesApi(api_client)
    resource = 'resource_example' # str | Resource type
    rname = 'rname_example' # str | Profile name
    profile_request = janus_py_client.ProfileRequest() # ProfileRequest | 

    try:
        # Create a new profile
        api_response = api_instance.controller_post_profile_profiles_path_resource_path_rname_post(resource, rname, profile_request)
        print("The response of ProfilesApi->controller_post_profile_profiles_path_resource_path_rname_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->controller_post_profile_profiles_path_resource_path_rname_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rname** | **str**| Profile name | 
 **profile_request** | [**ProfileRequest**](ProfileRequest.md)|  | 

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_put_profile_profiles_path_resource_path_rname_put**
> ProfileResponse controller_put_profile_profiles_path_resource_path_rname_put(resource, rname, profile_request)

Update a profile

Update an existing profile.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.profile_request import ProfileRequest
from janus_py_client.models.profile_response import ProfileResponse
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): jwt
configuration = janus_py_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure HTTP basic authorization: basicAuth
configuration = janus_py_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.ProfilesApi(api_client)
    resource = 'resource_example' # str | Resource type
    rname = 'rname_example' # str | Profile name
    profile_request = janus_py_client.ProfileRequest() # ProfileRequest | 

    try:
        # Update a profile
        api_response = api_instance.controller_put_profile_profiles_path_resource_path_rname_put(resource, rname, profile_request)
        print("The response of ProfilesApi->controller_put_profile_profiles_path_resource_path_rname_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->controller_put_profile_profiles_path_resource_path_rname_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rname** | **str**| Profile name | 
 **profile_request** | [**ProfileRequest**](ProfileRequest.md)|  | 

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

