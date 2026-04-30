# janus_py_client.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_create_sessions_create_post**](SessionsApi.md#controller_create_sessions_create_post) | **POST** /api/janus/controller/create | Create one or more new sessions.
[**controller_delete_active_active_int_aid_delete**](SessionsApi.md#controller_delete_active_active_int_aid_delete) | **DELETE** /api/janus/controller/active/{aid} | Delete a specific active session
[**controller_exec_command_exec_post**](SessionsApi.md#controller_exec_command_exec_post) | **POST** /api/janus/controller/exec | Execute a container command inside an active session.
[**controller_get_active_active_get**](SessionsApi.md#controller_get_active_active_get) | **GET** /api/janus/controller/active | Get all active sessions
[**controller_get_active_by_id_active_int_aid_get**](SessionsApi.md#controller_get_active_by_id_active_int_aid_get) | **GET** /api/janus/controller/active/{aid} | Get a specific active session
[**controller_get_logs_active_int_aid_logs_path_nname_get**](SessionsApi.md#controller_get_logs_active_int_aid_logs_path_nname_get) | **GET** /api/janus/controller/active/{aid}/logs/{nname} | Display logs for a specific active session and node.
[**controller_post_active_apply_active_int_aid_apply_post**](SessionsApi.md#controller_post_active_apply_active_int_aid_apply_post) | **POST** /api/janus/controller/active/{aid}/apply | Apply changes to a session
[**controller_put_active_active_int_aid_put**](SessionsApi.md#controller_put_active_active_int_aid_put) | **PUT** /api/janus/controller/active/{aid} | Update a specific active session
[**controller_start_session_endpoint_start_int_aid_put**](SessionsApi.md#controller_start_session_endpoint_start_int_aid_put) | **PUT** /api/janus/controller/start/{aid} | Start a container service by id.
[**controller_stop_session_endpoint_stop_int_aid_put**](SessionsApi.md#controller_stop_session_endpoint_stop_int_aid_put) | **PUT** /api/janus/controller/stop/{aid} | Stop a container service by id.


# **controller_create_sessions_create_post**
> Dict[str, Dict[str, int]] controller_create_sessions_create_post(session_request_list)

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
    api_instance = janus_py_client.SessionsApi(api_client)
    session_request_list = janus_py_client.SessionRequestList() # SessionRequestList | 

    try:
        # Create one or more new sessions.
        api_response = api_instance.controller_create_sessions_create_post(session_request_list)
        print("The response of SessionsApi->controller_create_sessions_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->controller_create_sessions_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_request_list** | [**SessionRequestList**](SessionRequestList.md)|  | 

### Return type

**Dict[str, Dict[str, int]]**

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

# **controller_delete_active_active_int_aid_delete**
> controller_delete_active_active_int_aid_delete(aid, fields=fields, force=force)

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
    api_instance = janus_py_client.SessionsApi(api_client)
    aid = 56 # int | Active session ID
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)
    force = True # bool | Force deletion of session (optional)

    try:
        # Delete a specific active session
        api_instance.controller_delete_active_active_int_aid_delete(aid, fields=fields, force=force)
    except Exception as e:
        print("Exception when calling SessionsApi->controller_delete_active_active_int_aid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 
 **force** | **bool**| Force deletion of session | [optional] 

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

# **controller_exec_command_exec_post**
> ExecResponse controller_exec_command_exec_post(exec_request)

Execute a container command inside an active session.

Execute a container command inside an active session.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.exec_request import ExecRequest
from janus_py_client.models.exec_response import ExecResponse
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
    api_instance = janus_py_client.SessionsApi(api_client)
    exec_request = janus_py_client.ExecRequest() # ExecRequest | 

    try:
        # Execute a container command inside an active session.
        api_response = api_instance.controller_exec_command_exec_post(exec_request)
        print("The response of SessionsApi->controller_exec_command_exec_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->controller_exec_command_exec_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exec_request** | [**ExecRequest**](ExecRequest.md)|  | 

### Return type

[**ExecResponse**](ExecResponse.md)

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

# **controller_get_active_active_get**
> List[SessionResponse] controller_get_active_active_get(fields=fields, force=force)

Get all active sessions

Get active sessions

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.session_response import SessionResponse
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
    api_instance = janus_py_client.SessionsApi(api_client)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)
    force = True # bool | Force deletion of session (optional)

    try:
        # Get all active sessions
        api_response = api_instance.controller_get_active_active_get(fields=fields, force=force)
        print("The response of SessionsApi->controller_get_active_active_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->controller_get_active_active_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma separated list of fields to return | [optional] 
 **force** | **bool**| Force deletion of session | [optional] 

### Return type

[**List[SessionResponse]**](SessionResponse.md)

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

# **controller_get_active_by_id_active_int_aid_get**
> SessionResponse controller_get_active_by_id_active_int_aid_get(aid, fields=fields, force=force)

Get a specific active session

Get a specific active session

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.session_response import SessionResponse
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
    api_instance = janus_py_client.SessionsApi(api_client)
    aid = 56 # int | Active session ID
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)
    force = True # bool | Force deletion of session (optional)

    try:
        # Get a specific active session
        api_response = api_instance.controller_get_active_by_id_active_int_aid_get(aid, fields=fields, force=force)
        print("The response of SessionsApi->controller_get_active_by_id_active_int_aid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->controller_get_active_by_id_active_int_aid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 
 **force** | **bool**| Force deletion of session | [optional] 

### Return type

[**SessionResponse**](SessionResponse.md)

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
    api_instance = janus_py_client.SessionsApi(api_client)
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
        print("The response of SessionsApi->controller_get_logs_active_int_aid_logs_path_nname_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->controller_get_logs_active_int_aid_logs_path_nname_get: %s\n" % e)
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_post_active_apply_active_int_aid_apply_post**
> SessionResponse controller_post_active_apply_active_int_aid_apply_post(aid)

Apply changes to a session

Re-provision a session to apply modified settings.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.session_response import SessionResponse
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
    api_instance = janus_py_client.SessionsApi(api_client)
    aid = 56 # int | Active session ID

    try:
        # Apply changes to a session
        api_response = api_instance.controller_post_active_apply_active_int_aid_apply_post(aid)
        print("The response of SessionsApi->controller_post_active_apply_active_int_aid_apply_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->controller_post_active_apply_active_int_aid_apply_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 

### Return type

[**SessionResponse**](SessionResponse.md)

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

# **controller_put_active_active_int_aid_put**
> SessionResponse controller_put_active_active_int_aid_put(aid, session_request)

Update a specific active session

Update a session's name or desired configuration.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.session_request import SessionRequest
from janus_py_client.models.session_response import SessionResponse
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
    api_instance = janus_py_client.SessionsApi(api_client)
    aid = 56 # int | Active session ID
    session_request = janus_py_client.SessionRequest() # SessionRequest | 

    try:
        # Update a specific active session
        api_response = api_instance.controller_put_active_active_int_aid_put(aid, session_request)
        print("The response of SessionsApi->controller_put_active_active_int_aid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->controller_put_active_active_int_aid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 
 **session_request** | [**SessionRequest**](SessionRequest.md)|  | 

### Return type

[**SessionResponse**](SessionResponse.md)

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

# **controller_start_session_endpoint_start_int_aid_put**
> Dict[str, object] controller_start_session_endpoint_start_int_aid_put(aid)

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
    api_instance = janus_py_client.SessionsApi(api_client)
    aid = 56 # int | Active session ID

    try:
        # Start a container service by id.
        api_response = api_instance.controller_start_session_endpoint_start_int_aid_put(aid)
        print("The response of SessionsApi->controller_start_session_endpoint_start_int_aid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->controller_start_session_endpoint_start_int_aid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 

### Return type

**Dict[str, object]**

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

# **controller_stop_session_endpoint_stop_int_aid_put**
> Dict[str, object] controller_stop_session_endpoint_stop_int_aid_put(aid)

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
    api_instance = janus_py_client.SessionsApi(api_client)
    aid = 56 # int | Active session ID

    try:
        # Stop a container service by id.
        api_response = api_instance.controller_stop_session_endpoint_stop_int_aid_put(aid)
        print("The response of SessionsApi->controller_stop_session_endpoint_stop_int_aid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->controller_stop_session_endpoint_stop_int_aid_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **int**| Active session ID | 

### Return type

**Dict[str, object]**

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

