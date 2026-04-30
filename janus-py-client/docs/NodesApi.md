# janus_py_client.NodesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_add_node_nodes_post**](NodesApi.md#controller_add_node_nodes_post) | **POST** /api/janus/controller/nodes | Add a new node
[**controller_delete_node_nodes_int_id_delete**](NodesApi.md#controller_delete_node_nodes_int_id_delete) | **DELETE** /api/janus/controller/nodes/{id} | Delete node by ID
[**controller_delete_node_nodes_node_delete**](NodesApi.md#controller_delete_node_nodes_node_delete) | **DELETE** /api/janus/controller/nodes/{node} | Delete node by name
[**controller_get_node_by_id_or_name_nodes_int_id_get**](NodesApi.md#controller_get_node_by_id_or_name_nodes_int_id_get) | **GET** /api/janus/controller/nodes/{id} | Get node by ID
[**controller_get_node_by_id_or_name_nodes_node_get**](NodesApi.md#controller_get_node_by_id_or_name_nodes_node_get) | **GET** /api/janus/controller/nodes/{node} | Get node by name
[**controller_get_nodes_nodes_get**](NodesApi.md#controller_get_nodes_nodes_get) | **GET** /api/janus/controller/nodes | Get nodes


# **controller_add_node_nodes_post**
> NodeResponse controller_add_node_nodes_post(add_endpoint_request)

Add a new node

Add a new Janus endpoint.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.add_endpoint_request import AddEndpointRequest
from janus_py_client.models.node_response import NodeResponse
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
    api_instance = janus_py_client.NodesApi(api_client)
    add_endpoint_request = janus_py_client.AddEndpointRequest() # AddEndpointRequest | 

    try:
        # Add a new node
        api_response = api_instance.controller_add_node_nodes_post(add_endpoint_request)
        print("The response of NodesApi->controller_add_node_nodes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->controller_add_node_nodes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_endpoint_request** | [**AddEndpointRequest**](AddEndpointRequest.md)|  | 

### Return type

[**NodeResponse**](NodeResponse.md)

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

# **controller_delete_node_nodes_int_id_delete**
> controller_delete_node_nodes_int_id_delete(node, id)

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
    api_instance = janus_py_client.NodesApi(api_client)
    node = 'node_example' # str | Node name
    id = 56 # int | Node ID

    try:
        # Delete node by ID
        api_instance.controller_delete_node_nodes_int_id_delete(node, id)
    except Exception as e:
        print("Exception when calling NodesApi->controller_delete_node_nodes_int_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| Node name | 
 **id** | **int**| Node ID | 

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

# **controller_delete_node_nodes_node_delete**
> controller_delete_node_nodes_node_delete(node, id)

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
    api_instance = janus_py_client.NodesApi(api_client)
    node = 'node_example' # str | Node name
    id = 56 # int | Node ID

    try:
        # Delete node by name
        api_instance.controller_delete_node_nodes_node_delete(node, id)
    except Exception as e:
        print("Exception when calling NodesApi->controller_delete_node_nodes_node_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| Node name | 
 **id** | **int**| Node ID | 

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

# **controller_get_node_by_id_or_name_nodes_int_id_get**
> NodeResponse controller_get_node_by_id_or_name_nodes_int_id_get(node, id, refresh=refresh, fields=fields)

Get node by ID

Get detailed information about a specific node by its ID or name.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.node_response import NodeResponse
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
    api_instance = janus_py_client.NodesApi(api_client)
    node = 'node_example' # str | Node name
    id = 56 # int | Node ID
    refresh = True # bool | Refresh nodes from backends (optional)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get node by ID
        api_response = api_instance.controller_get_node_by_id_or_name_nodes_int_id_get(node, id, refresh=refresh, fields=fields)
        print("The response of NodesApi->controller_get_node_by_id_or_name_nodes_int_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->controller_get_node_by_id_or_name_nodes_int_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| Node name | 
 **id** | **int**| Node ID | 
 **refresh** | **bool**| Refresh nodes from backends | [optional] 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

[**NodeResponse**](NodeResponse.md)

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

# **controller_get_node_by_id_or_name_nodes_node_get**
> NodeResponse controller_get_node_by_id_or_name_nodes_node_get(node, id, refresh=refresh, fields=fields)

Get node by name

Get detailed information about a specific node by its ID or name.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.node_response import NodeResponse
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
    api_instance = janus_py_client.NodesApi(api_client)
    node = 'node_example' # str | Node name
    id = 56 # int | Node ID
    refresh = True # bool | Refresh nodes from backends (optional)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get node by name
        api_response = api_instance.controller_get_node_by_id_or_name_nodes_node_get(node, id, refresh=refresh, fields=fields)
        print("The response of NodesApi->controller_get_node_by_id_or_name_nodes_node_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->controller_get_node_by_id_or_name_nodes_node_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| Node name | 
 **id** | **int**| Node ID | 
 **refresh** | **bool**| Refresh nodes from backends | [optional] 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

[**NodeResponse**](NodeResponse.md)

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

# **controller_get_nodes_nodes_get**
> List[NodeResponse] controller_get_nodes_nodes_get(refresh=refresh, fields=fields)

Get nodes

List all nodes.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.node_response import NodeResponse
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
    api_instance = janus_py_client.NodesApi(api_client)
    refresh = True # bool | Refresh nodes from backends (optional)
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get nodes
        api_response = api_instance.controller_get_nodes_nodes_get(refresh=refresh, fields=fields)
        print("The response of NodesApi->controller_get_nodes_nodes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->controller_get_nodes_nodes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Refresh nodes from backends | [optional] 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

[**List[NodeResponse]**](NodeResponse.md)

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

