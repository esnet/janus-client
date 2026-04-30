# janus_py_client.JanusControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_add_node_nodes_post**](JanusControllerApi.md#controller_add_node_nodes_post) | **POST** /api/janus/controller/nodes | Add a new node
[**controller_check_token_token_get**](JanusControllerApi.md#controller_check_token_token_get) | **GET** /api/janus/controller/token | Check Token
[**controller_create_sessions_create_post**](JanusControllerApi.md#controller_create_sessions_create_post) | **POST** /api/janus/controller/create | Create one or more new sessions.
[**controller_delete_active_active_int_aid_delete**](JanusControllerApi.md#controller_delete_active_active_int_aid_delete) | **DELETE** /api/janus/controller/active/{aid} | Delete a specific active session
[**controller_delete_auth_auth_path_resource_int_rid_delete**](JanusControllerApi.md#controller_delete_auth_auth_path_resource_int_rid_delete) | **DELETE** /api/janus/controller/auth/{resource}/{rid} | Delete auth info by ID
[**controller_delete_auth_auth_path_resource_path_rname_delete**](JanusControllerApi.md#controller_delete_auth_auth_path_resource_path_rname_delete) | **DELETE** /api/janus/controller/auth/{resource}/{rname} | Delete auth info by name
[**controller_delete_node_nodes_int_id_delete**](JanusControllerApi.md#controller_delete_node_nodes_int_id_delete) | **DELETE** /api/janus/controller/nodes/{id} | Delete node by ID
[**controller_delete_node_nodes_node_delete**](JanusControllerApi.md#controller_delete_node_nodes_node_delete) | **DELETE** /api/janus/controller/nodes/{node} | Delete node by name
[**controller_delete_profile_profiles_path_resource_path_rname_delete**](JanusControllerApi.md#controller_delete_profile_profiles_path_resource_path_rname_delete) | **DELETE** /api/janus/controller/profiles/{resource}/{rname} | Remove a profile
[**controller_exec_command_exec_post**](JanusControllerApi.md#controller_exec_command_exec_post) | **POST** /api/janus/controller/exec | Execute a container command inside an active session.
[**controller_get_active_active_get**](JanusControllerApi.md#controller_get_active_active_get) | **GET** /api/janus/controller/active | Get all active sessions
[**controller_get_active_by_id_active_int_aid_get**](JanusControllerApi.md#controller_get_active_by_id_active_int_aid_get) | **GET** /api/janus/controller/active/{aid} | Get a specific active session
[**controller_get_auth_auth_path_resource_get**](JanusControllerApi.md#controller_get_auth_auth_path_resource_get) | **GET** /api/janus/controller/auth/{resource} | Get auth info
[**controller_get_auth_auth_path_resource_int_rid_get**](JanusControllerApi.md#controller_get_auth_auth_path_resource_int_rid_get) | **GET** /api/janus/controller/auth/{resource}/{rid} | Get specific auth info by ID
[**controller_get_auth_auth_path_resource_path_rname_get**](JanusControllerApi.md#controller_get_auth_auth_path_resource_path_rname_get) | **GET** /api/janus/controller/auth/{resource}/{rname} | Get specific auth info by name
[**controller_get_images_images_get**](JanusControllerApi.md#controller_get_images_images_get) | **GET** /api/janus/controller/images | Get images
[**controller_get_images_images_path_name_get**](JanusControllerApi.md#controller_get_images_images_path_name_get) | **GET** /api/janus/controller/images/{name} | Get a specific image
[**controller_get_logs_active_int_aid_logs_path_nname_get**](JanusControllerApi.md#controller_get_logs_active_int_aid_logs_path_nname_get) | **GET** /api/janus/controller/active/{aid}/logs/{nname} | Display logs for a specific active session and node.
[**controller_get_node_by_id_or_name_nodes_int_id_get**](JanusControllerApi.md#controller_get_node_by_id_or_name_nodes_int_id_get) | **GET** /api/janus/controller/nodes/{id} | Get node by ID
[**controller_get_node_by_id_or_name_nodes_node_get**](JanusControllerApi.md#controller_get_node_by_id_or_name_nodes_node_get) | **GET** /api/janus/controller/nodes/{node} | Get node by name
[**controller_get_nodes_nodes_get**](JanusControllerApi.md#controller_get_nodes_nodes_get) | **GET** /api/janus/controller/nodes | Get nodes
[**controller_get_profile_by_name_profiles_path_resource_path_rname_get**](JanusControllerApi.md#controller_get_profile_by_name_profiles_path_resource_path_rname_get) | **GET** /api/janus/controller/profiles/{resource}/{rname} | Get a specific profile
[**controller_get_profiles_by_resource_profiles_path_resource_get**](JanusControllerApi.md#controller_get_profiles_by_resource_profiles_path_resource_get) | **GET** /api/janus/controller/profiles/{resource} | Get profiles for a resource
[**controller_get_profiles_default_profiles_get**](JanusControllerApi.md#controller_get_profiles_default_profiles_get) | **GET** /api/janus/controller/profiles | Get host profiles (default)
[**controller_get_token_token_post**](JanusControllerApi.md#controller_get_token_token_post) | **POST** /api/janus/controller/token | Get Token
[**controller_post_active_apply_active_int_aid_apply_post**](JanusControllerApi.md#controller_post_active_apply_active_int_aid_apply_post) | **POST** /api/janus/controller/active/{aid}/apply | Apply changes to a session
[**controller_post_auth_auth_path_resource_int_rid_post**](JanusControllerApi.md#controller_post_auth_auth_path_resource_int_rid_post) | **POST** /api/janus/controller/auth/{resource}/{rid} | Update auth info by ID
[**controller_post_auth_auth_path_resource_path_rname_post**](JanusControllerApi.md#controller_post_auth_auth_path_resource_path_rname_post) | **POST** /api/janus/controller/auth/{resource}/{rname} | Update auth info by name
[**controller_post_auth_bulk_auth_bulk_post**](JanusControllerApi.md#controller_post_auth_bulk_auth_bulk_post) | **POST** /api/janus/controller/auth/bulk | Bulk update auth info
[**controller_post_profile_profiles_path_resource_path_rname_post**](JanusControllerApi.md#controller_post_profile_profiles_path_resource_path_rname_post) | **POST** /api/janus/controller/profiles/{resource}/{rname} | Create a new profile
[**controller_put_active_active_int_aid_put**](JanusControllerApi.md#controller_put_active_active_int_aid_put) | **PUT** /api/janus/controller/active/{aid} | Update a specific active session
[**controller_put_profile_profiles_path_resource_path_rname_put**](JanusControllerApi.md#controller_put_profile_profiles_path_resource_path_rname_put) | **PUT** /api/janus/controller/profiles/{resource}/{rname} | Update a profile
[**controller_start_session_endpoint_start_int_aid_put**](JanusControllerApi.md#controller_start_session_endpoint_start_int_aid_put) | **PUT** /api/janus/controller/start/{aid} | Start a container service by id.
[**controller_stop_session_endpoint_stop_int_aid_put**](JanusControllerApi.md#controller_stop_session_endpoint_stop_int_aid_put) | **PUT** /api/janus/controller/stop/{aid} | Stop a container service by id.


# **controller_add_node_nodes_post**
> object controller_add_node_nodes_post(add_endpoint_request)

Add a new node

Add a new Janus endpoint.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.add_endpoint_request import AddEndpointRequest
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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    add_endpoint_request = janus_py_client.AddEndpointRequest() # AddEndpointRequest | 

    try:
        # Add a new node
        api_response = api_instance.controller_add_node_nodes_post(add_endpoint_request)
        print("The response of JanusControllerApi->controller_add_node_nodes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_add_node_nodes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_endpoint_request** | [**AddEndpointRequest**](AddEndpointRequest.md)|  | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_check_token_token_get**
> CheckTokenResponse controller_check_token_token_get()

Check Token

Check Token.<br/>https --verify no GET :5000/api/janus/controller/token Authorization:"Bearer $JWT"

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.check_token_response import CheckTokenResponse
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
    api_instance = janus_py_client.JanusControllerApi(api_client)

    try:
        # Check Token
        api_response = api_instance.controller_check_token_token_get()
        print("The response of JanusControllerApi->controller_check_token_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_check_token_token_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CheckTokenResponse**](CheckTokenResponse.md)

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_create_sessions_create_post**
> object controller_create_sessions_create_post(session_request_list)

Create one or more new sessions.

Create one or more new sessions.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.session_request_list import SessionRequestList
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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    session_request_list = janus_py_client.SessionRequestList() # SessionRequestList | 

    try:
        # Create one or more new sessions.
        api_response = api_instance.controller_create_sessions_create_post(session_request_list)
        print("The response of JanusControllerApi->controller_create_sessions_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_create_sessions_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_request_list** | [**SessionRequestList**](SessionRequestList.md)|  | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_delete_active_active_int_aid_delete**
> object controller_delete_active_active_int_aid_delete(aid, fields=fields, force=force)

Delete a specific active session

Delete a session by id.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    aid = 56 # int | Active session ID
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)
    force = True # bool | Force deletion of session (optional)

    try:
        # Delete a specific active session
        api_response = api_instance.controller_delete_active_active_int_aid_delete(aid, fields=fields, force=force)
        print("The response of JanusControllerApi->controller_delete_active_active_int_aid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_delete_active_active_int_aid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 
 **force** | **bool**| Force deletion of session | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_delete_auth_auth_path_resource_int_rid_delete**
> object controller_delete_auth_auth_path_resource_int_rid_delete(resource, rid, rname, auth_request)

Delete auth info by ID

Remove user and group attributes for a named resource.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_request import AuthRequest
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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    auth_request = janus_py_client.AuthRequest() # AuthRequest | 

    try:
        # Delete auth info by ID
        api_response = api_instance.controller_delete_auth_auth_path_resource_int_rid_delete(resource, rid, rname, auth_request)
        print("The response of JanusControllerApi->controller_delete_auth_auth_path_resource_int_rid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_delete_auth_auth_path_resource_int_rid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_delete_auth_auth_path_resource_path_rname_delete**
> object controller_delete_auth_auth_path_resource_path_rname_delete(resource, rid, rname, auth_request)

Delete auth info by name

Remove user and group attributes for a named resource.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_request import AuthRequest
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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    auth_request = janus_py_client.AuthRequest() # AuthRequest | 

    try:
        # Delete auth info by name
        api_response = api_instance.controller_delete_auth_auth_path_resource_path_rname_delete(resource, rid, rname, auth_request)
        print("The response of JanusControllerApi->controller_delete_auth_auth_path_resource_path_rname_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_delete_auth_auth_path_resource_path_rname_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_delete_node_nodes_int_id_delete**
> object controller_delete_node_nodes_int_id_delete(node, id)

Delete node by ID

Deletes a node (endpoint).

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    node = 'node_example' # str | Node name
    id = 56 # int | Node ID

    try:
        # Delete node by ID
        api_response = api_instance.controller_delete_node_nodes_int_id_delete(node, id)
        print("The response of JanusControllerApi->controller_delete_node_nodes_int_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_delete_node_nodes_int_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| Node name | 
 **id** | **int**| Node ID | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_delete_node_nodes_node_delete**
> object controller_delete_node_nodes_node_delete(node, id)

Delete node by name

Deletes a node (endpoint).

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    node = 'node_example' # str | Node name
    id = 56 # int | Node ID

    try:
        # Delete node by name
        api_response = api_instance.controller_delete_node_nodes_node_delete(node, id)
        print("The response of JanusControllerApi->controller_delete_node_nodes_node_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_delete_node_nodes_node_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| Node name | 
 **id** | **int**| Node ID | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_delete_profile_profiles_path_resource_path_rname_delete**
> object controller_delete_profile_profiles_path_resource_path_rname_delete(resource, rname)

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    resource = 'resource_example' # str | Resource type
    rname = 'rname_example' # str | Profile name

    try:
        # Remove a profile
        api_response = api_instance.controller_delete_profile_profiles_path_resource_path_rname_delete(resource, rname)
        print("The response of JanusControllerApi->controller_delete_profile_profiles_path_resource_path_rname_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_delete_profile_profiles_path_resource_path_rname_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rname** | **str**| Profile name | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_exec_command_exec_post**
> object controller_exec_command_exec_post(exec_request)

Execute a container command inside an active session.

Execute a container command inside an active session.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.exec_request import ExecRequest
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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    exec_request = janus_py_client.ExecRequest() # ExecRequest | 

    try:
        # Execute a container command inside an active session.
        api_response = api_instance.controller_exec_command_exec_post(exec_request)
        print("The response of JanusControllerApi->controller_exec_command_exec_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_exec_command_exec_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exec_request** | [**ExecRequest**](ExecRequest.md)|  | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_active_active_get**
> object controller_get_active_active_get(fields=fields, force=force)

Get all active sessions

Get active sessions

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)
    force = True # bool | Force deletion of session (optional)

    try:
        # Get all active sessions
        api_response = api_instance.controller_get_active_active_get(fields=fields, force=force)
        print("The response of JanusControllerApi->controller_get_active_active_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_active_active_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma separated list of fields to return | [optional] 
 **force** | **bool**| Force deletion of session | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_active_by_id_active_int_aid_get**
> object controller_get_active_by_id_active_int_aid_get(aid, fields=fields, force=force)

Get a specific active session

Get a specific active session

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    aid = 56 # int | Active session ID
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)
    force = True # bool | Force deletion of session (optional)

    try:
        # Get a specific active session
        api_response = api_instance.controller_get_active_by_id_active_int_aid_get(aid, fields=fields, force=force)
        print("The response of JanusControllerApi->controller_get_active_by_id_active_int_aid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_active_by_id_active_int_aid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 
 **force** | **bool**| Force deletion of session | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_auth_auth_path_resource_get**
> object controller_get_auth_auth_path_resource_get(resource, rid, rname, fields=fields)

Get auth info

Get user and group attributes for a named resource.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get auth info
        api_response = api_instance.controller_get_auth_auth_path_resource_get(resource, rid, rname, fields=fields)
        print("The response of JanusControllerApi->controller_get_auth_auth_path_resource_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_auth_auth_path_resource_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_auth_auth_path_resource_int_rid_get**
> object controller_get_auth_auth_path_resource_int_rid_get(resource, rid, rname, fields=fields)

Get specific auth info by ID

Get user and group attributes for a named resource.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get specific auth info by ID
        api_response = api_instance.controller_get_auth_auth_path_resource_int_rid_get(resource, rid, rname, fields=fields)
        print("The response of JanusControllerApi->controller_get_auth_auth_path_resource_int_rid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_auth_auth_path_resource_int_rid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_auth_auth_path_resource_path_rname_get**
> object controller_get_auth_auth_path_resource_path_rname_get(resource, rid, rname, fields=fields)

Get specific auth info by name

Get user and group attributes for a named resource.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get specific auth info by name
        api_response = api_instance.controller_get_auth_auth_path_resource_path_rname_get(resource, rid, rname, fields=fields)
        print("The response of JanusControllerApi->controller_get_auth_auth_path_resource_path_rname_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_auth_auth_path_resource_path_rname_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_images_images_get**
> object controller_get_images_images_get(name, fields=fields)

Get images

List all images or a specific image.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    name = 'name_example' # str | Image name
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get images
        api_response = api_instance.controller_get_images_images_get(name, fields=fields)
        print("The response of JanusControllerApi->controller_get_images_images_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_images_images_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Image name | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_images_images_path_name_get**
> object controller_get_images_images_path_name_get(name, fields=fields)

Get a specific image

List all images or a specific image.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    name = 'name_example' # str | Image name
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get a specific image
        api_response = api_instance.controller_get_images_images_path_name_get(name, fields=fields)
        print("The response of JanusControllerApi->controller_get_images_images_path_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_images_images_path_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Image name | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_logs_active_int_aid_logs_path_nname_get**
> object controller_get_logs_active_int_aid_logs_path_nname_get(aid, nname, timestamps=timestamps, stderr=stderr, stdout=stdout, since=since, tail=tail)

Display logs for a specific active session and node.

Display logs for a specific active session and node.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    aid = 56 # int | Active session ID
    nname = 'nname_example' # str | Node name
    timestamps = True # bool | Include timestamps in logs (optional)
    stderr = True # bool | Include stderr in logs (optional)
    stdout = True # bool | Include stdout in logs (optional)
    since = 56 # int | Return logs since this timestamp (optional)
    tail = 56 # int | Number of lines to return from the end of the log (optional)

    try:
        # Display logs for a specific active session and node.
        api_response = api_instance.controller_get_logs_active_int_aid_logs_path_nname_get(aid, nname, timestamps=timestamps, stderr=stderr, stdout=stdout, since=since, tail=tail)
        print("The response of JanusControllerApi->controller_get_logs_active_int_aid_logs_path_nname_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_logs_active_int_aid_logs_path_nname_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 
 **nname** | **str**| Node name | 
 **timestamps** | **bool**| Include timestamps in logs | [optional] 
 **stderr** | **bool**| Include stderr in logs | [optional] 
 **stdout** | **bool**| Include stdout in logs | [optional] 
 **since** | **int**| Return logs since this timestamp | [optional] 
 **tail** | **int**| Number of lines to return from the end of the log | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_node_by_id_or_name_nodes_int_id_get**
> object controller_get_node_by_id_or_name_nodes_int_id_get(node, id, refresh=refresh, fields=fields)

Get node by ID

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    node = 'node_example' # str | Node name
    id = 56 # int | Node ID
    refresh = True # bool | Refresh nodes from backends (optional)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get node by ID
        api_response = api_instance.controller_get_node_by_id_or_name_nodes_int_id_get(node, id, refresh=refresh, fields=fields)
        print("The response of JanusControllerApi->controller_get_node_by_id_or_name_nodes_int_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_node_by_id_or_name_nodes_int_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| Node name | 
 **id** | **int**| Node ID | 
 **refresh** | **bool**| Refresh nodes from backends | [optional] 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_node_by_id_or_name_nodes_node_get**
> object controller_get_node_by_id_or_name_nodes_node_get(node, id, refresh=refresh, fields=fields)

Get node by name

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    node = 'node_example' # str | Node name
    id = 56 # int | Node ID
    refresh = True # bool | Refresh nodes from backends (optional)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get node by name
        api_response = api_instance.controller_get_node_by_id_or_name_nodes_node_get(node, id, refresh=refresh, fields=fields)
        print("The response of JanusControllerApi->controller_get_node_by_id_or_name_nodes_node_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_node_by_id_or_name_nodes_node_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| Node name | 
 **id** | **int**| Node ID | 
 **refresh** | **bool**| Refresh nodes from backends | [optional] 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_nodes_nodes_get**
> object controller_get_nodes_nodes_get(refresh=refresh, fields=fields)

Get nodes

List all nodes.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    refresh = True # bool | Refresh nodes from backends (optional)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get nodes
        api_response = api_instance.controller_get_nodes_nodes_get(refresh=refresh, fields=fields)
        print("The response of JanusControllerApi->controller_get_nodes_nodes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_nodes_nodes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Refresh nodes from backends | [optional] 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_profile_by_name_profiles_path_resource_path_rname_get**
> object controller_get_profile_by_name_profiles_path_resource_path_rname_get(resource, rname, refresh=refresh, reset=reset, fields=fields)

Get a specific profile

Get a specific profile by resource type and name.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    resource = 'resource_example' # str | Resource type
    rname = 'rname_example' # str | Profile name
    refresh = True # bool | Refresh profiles from files (optional)
    reset = True # bool | Reset database tables (optional)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get a specific profile
        api_response = api_instance.controller_get_profile_by_name_profiles_path_resource_path_rname_get(resource, rname, refresh=refresh, reset=reset, fields=fields)
        print("The response of JanusControllerApi->controller_get_profile_by_name_profiles_path_resource_path_rname_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_profile_by_name_profiles_path_resource_path_rname_get: %s\n" % e)
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

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_profiles_by_resource_profiles_path_resource_get**
> object controller_get_profiles_by_resource_profiles_path_resource_get(resource, refresh=refresh, reset=reset, fields=fields)

Get profiles for a resource

Get all profiles for a specific resource type.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    resource = 'resource_example' # str | Resource type (e.g., host, net, vol, qos)
    refresh = True # bool | Refresh profiles from files (optional)
    reset = True # bool | Reset database tables (optional)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get profiles for a resource
        api_response = api_instance.controller_get_profiles_by_resource_profiles_path_resource_get(resource, refresh=refresh, reset=reset, fields=fields)
        print("The response of JanusControllerApi->controller_get_profiles_by_resource_profiles_path_resource_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_profiles_by_resource_profiles_path_resource_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type (e.g., host, net, vol, qos) | 
 **refresh** | **bool**| Refresh profiles from files | [optional] 
 **reset** | **bool**| Reset database tables | [optional] 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_profiles_default_profiles_get**
> object controller_get_profiles_default_profiles_get(refresh=refresh, reset=reset, fields=fields)

Get host profiles (default)

Get host profiles (defaults to 'host' resource).

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    refresh = True # bool | Refresh profiles from files (optional)
    reset = True # bool | Reset database tables (optional)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get host profiles (default)
        api_response = api_instance.controller_get_profiles_default_profiles_get(refresh=refresh, reset=reset, fields=fields)
        print("The response of JanusControllerApi->controller_get_profiles_default_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_profiles_default_profiles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Refresh profiles from files | [optional] 
 **reset** | **bool**| Reset database tables | [optional] 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_get_token_token_post**
> TokenResponse controller_get_token_token_post()

Get Token

Get Token<br/>https --verify no -a admin:admin_password POST :5000/api/janus/controller/token

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.token_response import TokenResponse
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
    api_instance = janus_py_client.JanusControllerApi(api_client)

    try:
        # Get Token
        api_response = api_instance.controller_get_token_token_post()
        print("The response of JanusControllerApi->controller_get_token_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_get_token_token_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_post_active_apply_active_int_aid_apply_post**
> object controller_post_active_apply_active_int_aid_apply_post(aid)

Apply changes to a session

Re-provision a session to apply modified settings.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    aid = 56 # int | Active session ID

    try:
        # Apply changes to a session
        api_response = api_instance.controller_post_active_apply_active_int_aid_apply_post(aid)
        print("The response of JanusControllerApi->controller_post_active_apply_active_int_aid_apply_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_post_active_apply_active_int_aid_apply_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_post_auth_auth_path_resource_int_rid_post**
> object controller_post_auth_auth_path_resource_int_rid_post(resource, rid, rname, auth_request)

Update auth info by ID

Set user and group attributes for a named resource.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_request import AuthRequest
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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    auth_request = janus_py_client.AuthRequest() # AuthRequest | 

    try:
        # Update auth info by ID
        api_response = api_instance.controller_post_auth_auth_path_resource_int_rid_post(resource, rid, rname, auth_request)
        print("The response of JanusControllerApi->controller_post_auth_auth_path_resource_int_rid_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_post_auth_auth_path_resource_int_rid_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_post_auth_auth_path_resource_path_rname_post**
> object controller_post_auth_auth_path_resource_path_rname_post(resource, rid, rname, auth_request)

Update auth info by name

Set user and group attributes for a named resource.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_request import AuthRequest
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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    auth_request = janus_py_client.AuthRequest() # AuthRequest | 

    try:
        # Update auth info by name
        api_response = api_instance.controller_post_auth_auth_path_resource_path_rname_post(resource, rid, rname, auth_request)
        print("The response of JanusControllerApi->controller_post_auth_auth_path_resource_path_rname_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_post_auth_auth_path_resource_path_rname_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_post_auth_bulk_auth_bulk_post**
> object controller_post_auth_bulk_auth_bulk_post(auth_bulk_request)

Bulk update auth info

Bulk update user and group attributes for multiple resources.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_bulk_request import AuthBulkRequest
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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    auth_bulk_request = janus_py_client.AuthBulkRequest() # AuthBulkRequest | 

    try:
        # Bulk update auth info
        api_response = api_instance.controller_post_auth_bulk_auth_bulk_post(auth_bulk_request)
        print("The response of JanusControllerApi->controller_post_auth_bulk_auth_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_post_auth_bulk_auth_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_bulk_request** | [**AuthBulkRequest**](AuthBulkRequest.md)|  | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_post_profile_profiles_path_resource_path_rname_post**
> object controller_post_profile_profiles_path_resource_path_rname_post(resource, rname, profile_request)

Create a new profile

Create a new profile.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.profile_request import ProfileRequest
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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    resource = 'resource_example' # str | Resource type
    rname = 'rname_example' # str | Profile name
    profile_request = janus_py_client.ProfileRequest() # ProfileRequest | 

    try:
        # Create a new profile
        api_response = api_instance.controller_post_profile_profiles_path_resource_path_rname_post(resource, rname, profile_request)
        print("The response of JanusControllerApi->controller_post_profile_profiles_path_resource_path_rname_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_post_profile_profiles_path_resource_path_rname_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rname** | **str**| Profile name | 
 **profile_request** | [**ProfileRequest**](ProfileRequest.md)|  | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_put_active_active_int_aid_put**
> object controller_put_active_active_int_aid_put(aid, session_request)

Update a specific active session

Update a session's name or desired configuration.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.session_request import SessionRequest
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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    aid = 56 # int | Active session ID
    session_request = janus_py_client.SessionRequest() # SessionRequest | 

    try:
        # Update a specific active session
        api_response = api_instance.controller_put_active_active_int_aid_put(aid, session_request)
        print("The response of JanusControllerApi->controller_put_active_active_int_aid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_put_active_active_int_aid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 
 **session_request** | [**SessionRequest**](SessionRequest.md)|  | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_put_profile_profiles_path_resource_path_rname_put**
> object controller_put_profile_profiles_path_resource_path_rname_put(resource, rname, profile_request)

Update a profile

Update an existing profile.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.profile_request import ProfileRequest
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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    resource = 'resource_example' # str | Resource type
    rname = 'rname_example' # str | Profile name
    profile_request = janus_py_client.ProfileRequest() # ProfileRequest | 

    try:
        # Update a profile
        api_response = api_instance.controller_put_profile_profiles_path_resource_path_rname_put(resource, rname, profile_request)
        print("The response of JanusControllerApi->controller_put_profile_profiles_path_resource_path_rname_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_put_profile_profiles_path_resource_path_rname_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rname** | **str**| Profile name | 
 **profile_request** | [**ProfileRequest**](ProfileRequest.md)|  | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_start_session_endpoint_start_int_aid_put**
> object controller_start_session_endpoint_start_int_aid_put(aid)

Start a container service by id.

Start a container service by id.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    aid = 56 # int | Active session ID

    try:
        # Start a container service by id.
        api_response = api_instance.controller_start_session_endpoint_start_int_aid_put(aid)
        print("The response of JanusControllerApi->controller_start_session_endpoint_start_int_aid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_start_session_endpoint_start_int_aid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_stop_session_endpoint_stop_int_aid_put**
> object controller_stop_session_endpoint_stop_int_aid_put(aid)

Stop a container service by id.

Stop a container service by id.

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
    api_instance = janus_py_client.JanusControllerApi(api_client)
    aid = 56 # int | Active session ID

    try:
        # Stop a container service by id.
        api_response = api_instance.controller_stop_session_endpoint_stop_int_aid_put(aid)
        print("The response of JanusControllerApi->controller_stop_session_endpoint_stop_int_aid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JanusControllerApi->controller_stop_session_endpoint_stop_int_aid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

