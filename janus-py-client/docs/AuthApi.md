# janus_py_client.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_delete_auth_auth_path_resource_int_rid_delete**](AuthApi.md#controller_delete_auth_auth_path_resource_int_rid_delete) | **DELETE** /api/janus/controller/auth/{resource}/{rid} | Delete auth info by ID
[**controller_delete_auth_auth_path_resource_path_rname_delete**](AuthApi.md#controller_delete_auth_auth_path_resource_path_rname_delete) | **DELETE** /api/janus/controller/auth/{resource}/{rname} | Delete auth info by name
[**controller_get_auth_auth_path_resource_get**](AuthApi.md#controller_get_auth_auth_path_resource_get) | **GET** /api/janus/controller/auth/{resource} | Get auth info
[**controller_get_auth_auth_path_resource_int_rid_get**](AuthApi.md#controller_get_auth_auth_path_resource_int_rid_get) | **GET** /api/janus/controller/auth/{resource}/{rid} | Get specific auth info by ID
[**controller_get_auth_auth_path_resource_path_rname_get**](AuthApi.md#controller_get_auth_auth_path_resource_path_rname_get) | **GET** /api/janus/controller/auth/{resource}/{rname} | Get specific auth info by name
[**controller_post_auth_auth_path_resource_int_rid_post**](AuthApi.md#controller_post_auth_auth_path_resource_int_rid_post) | **POST** /api/janus/controller/auth/{resource}/{rid} | Update auth info by ID
[**controller_post_auth_auth_path_resource_path_rname_post**](AuthApi.md#controller_post_auth_auth_path_resource_path_rname_post) | **POST** /api/janus/controller/auth/{resource}/{rname} | Update auth info by name
[**controller_post_auth_bulk_auth_bulk_post**](AuthApi.md#controller_post_auth_bulk_auth_bulk_post) | **POST** /api/janus/controller/auth/bulk | Bulk update auth info


# **controller_delete_auth_auth_path_resource_int_rid_delete**
> AuthInfoResponse controller_delete_auth_auth_path_resource_int_rid_delete(resource, rid, rname, auth_request)

Delete auth info by ID

Remove user and group attributes for a named resource.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_info_response import AuthInfoResponse
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
    api_instance = janus_py_client.AuthApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    auth_request = janus_py_client.AuthRequest() # AuthRequest | 

    try:
        # Delete auth info by ID
        api_response = api_instance.controller_delete_auth_auth_path_resource_int_rid_delete(resource, rid, rname, auth_request)
        print("The response of AuthApi->controller_delete_auth_auth_path_resource_int_rid_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->controller_delete_auth_auth_path_resource_int_rid_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

[**AuthInfoResponse**](AuthInfoResponse.md)

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

# **controller_delete_auth_auth_path_resource_path_rname_delete**
> AuthInfoResponse controller_delete_auth_auth_path_resource_path_rname_delete(resource, rid, rname, auth_request)

Delete auth info by name

Remove user and group attributes for a named resource.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_info_response import AuthInfoResponse
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
    api_instance = janus_py_client.AuthApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    auth_request = janus_py_client.AuthRequest() # AuthRequest | 

    try:
        # Delete auth info by name
        api_response = api_instance.controller_delete_auth_auth_path_resource_path_rname_delete(resource, rid, rname, auth_request)
        print("The response of AuthApi->controller_delete_auth_auth_path_resource_path_rname_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->controller_delete_auth_auth_path_resource_path_rname_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

[**AuthInfoResponse**](AuthInfoResponse.md)

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

# **controller_get_auth_auth_path_resource_get**
> AuthInfoResponse controller_get_auth_auth_path_resource_get(resource, rid, rname, fields=fields)

Get auth info

Get user and group attributes for a named resource.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_info_response import AuthInfoResponse
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
    api_instance = janus_py_client.AuthApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get auth info
        api_response = api_instance.controller_get_auth_auth_path_resource_get(resource, rid, rname, fields=fields)
        print("The response of AuthApi->controller_get_auth_auth_path_resource_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->controller_get_auth_auth_path_resource_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

[**AuthInfoResponse**](AuthInfoResponse.md)

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

# **controller_get_auth_auth_path_resource_int_rid_get**
> AuthInfoResponse controller_get_auth_auth_path_resource_int_rid_get(resource, rid, rname, fields=fields)

Get specific auth info by ID

Get user and group attributes for a named resource.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_info_response import AuthInfoResponse
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
    api_instance = janus_py_client.AuthApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get specific auth info by ID
        api_response = api_instance.controller_get_auth_auth_path_resource_int_rid_get(resource, rid, rname, fields=fields)
        print("The response of AuthApi->controller_get_auth_auth_path_resource_int_rid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->controller_get_auth_auth_path_resource_int_rid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

[**AuthInfoResponse**](AuthInfoResponse.md)

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

# **controller_get_auth_auth_path_resource_path_rname_get**
> AuthInfoResponse controller_get_auth_auth_path_resource_path_rname_get(resource, rid, rname, fields=fields)

Get specific auth info by name

Get user and group attributes for a named resource.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_info_response import AuthInfoResponse
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
    api_instance = janus_py_client.AuthApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get specific auth info by name
        api_response = api_instance.controller_get_auth_auth_path_resource_path_rname_get(resource, rid, rname, fields=fields)
        print("The response of AuthApi->controller_get_auth_auth_path_resource_path_rname_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->controller_get_auth_auth_path_resource_path_rname_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

[**AuthInfoResponse**](AuthInfoResponse.md)

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

# **controller_post_auth_auth_path_resource_int_rid_post**
> AuthInfoResponse controller_post_auth_auth_path_resource_int_rid_post(resource, rid, rname, auth_request)

Update auth info by ID

Set user and group attributes for a named resource.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_info_response import AuthInfoResponse
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
    api_instance = janus_py_client.AuthApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    auth_request = janus_py_client.AuthRequest() # AuthRequest | 

    try:
        # Update auth info by ID
        api_response = api_instance.controller_post_auth_auth_path_resource_int_rid_post(resource, rid, rname, auth_request)
        print("The response of AuthApi->controller_post_auth_auth_path_resource_int_rid_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->controller_post_auth_auth_path_resource_int_rid_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

[**AuthInfoResponse**](AuthInfoResponse.md)

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

# **controller_post_auth_auth_path_resource_path_rname_post**
> AuthInfoResponse controller_post_auth_auth_path_resource_path_rname_post(resource, rid, rname, auth_request)

Update auth info by name

Set user and group attributes for a named resource.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_info_response import AuthInfoResponse
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
    api_instance = janus_py_client.AuthApi(api_client)
    resource = 'resource_example' # str | Resource type
    rid = 56 # int | Auth ID
    rname = 'rname_example' # str | Auth name
    auth_request = janus_py_client.AuthRequest() # AuthRequest | 

    try:
        # Update auth info by name
        api_response = api_instance.controller_post_auth_auth_path_resource_path_rname_post(resource, rid, rname, auth_request)
        print("The response of AuthApi->controller_post_auth_auth_path_resource_path_rname_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->controller_post_auth_auth_path_resource_path_rname_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| Resource type | 
 **rid** | **int**| Auth ID | 
 **rname** | **str**| Auth name | 
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

[**AuthInfoResponse**](AuthInfoResponse.md)

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

# **controller_post_auth_bulk_auth_bulk_post**
> AuthBulkResponse controller_post_auth_bulk_auth_bulk_post(auth_bulk_request)

Bulk update auth info

Bulk update user and group attributes for multiple resources.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.auth_bulk_request import AuthBulkRequest
from janus_py_client.models.auth_bulk_response import AuthBulkResponse
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
    api_instance = janus_py_client.AuthApi(api_client)
    auth_bulk_request = janus_py_client.AuthBulkRequest() # AuthBulkRequest | 

    try:
        # Bulk update auth info
        api_response = api_instance.controller_post_auth_bulk_auth_bulk_post(auth_bulk_request)
        print("The response of AuthApi->controller_post_auth_bulk_auth_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->controller_post_auth_bulk_auth_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_bulk_request** | [**AuthBulkRequest**](AuthBulkRequest.md)|  | 

### Return type

[**AuthBulkResponse**](AuthBulkResponse.md)

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

