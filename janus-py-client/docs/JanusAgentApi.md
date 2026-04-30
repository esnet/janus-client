# janus_py_client.JanusAgentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_delete_tc_netem_tc_netem_delete**](JanusAgentApi.md#agent_delete_tc_netem_tc_netem_delete) | **DELETE** /api/janus/agent/tc/netem | Delete netem rules
[**agent_delete_tc_pacing_tc_pacing_delete**](JanusAgentApi.md#agent_delete_tc_pacing_tc_pacing_delete) | **DELETE** /api/janus/agent/tc/pacing | Delete pacing rules
[**agent_get_node_node_get**](JanusAgentApi.md#agent_get_node_node_get) | **GET** /api/janus/agent/node | Returns static node resources
[**agent_get_tc_delay_tc_delay_get**](JanusAgentApi.md#agent_get_tc_delay_tc_delay_get) | **GET** /api/janus/agent/tc/delay | Get delay rules
[**agent_get_tc_filter_tc_filter_get**](JanusAgentApi.md#agent_get_tc_filter_tc_filter_get) | **GET** /api/janus/agent/tc/filter | Get filter rules
[**agent_get_tc_latency_tc_latency_get**](JanusAgentApi.md#agent_get_tc_latency_tc_latency_get) | **GET** /api/janus/agent/tc/latency | Get latency rules
[**agent_get_tc_netem_tc_netem_get**](JanusAgentApi.md#agent_get_tc_netem_tc_netem_get) | **GET** /api/janus/agent/tc/netem | Get netem rules
[**agent_get_tc_pacing_tc_pacing_get**](JanusAgentApi.md#agent_get_tc_pacing_tc_pacing_get) | **GET** /api/janus/agent/tc/pacing | Get pacing rules
[**agent_get_tune_endpoint_tune_get**](JanusAgentApi.md#agent_get_tune_endpoint_tune_get) | **GET** /api/janus/agent/tune | Get node tuning settings
[**agent_post_tc_delay_tc_delay_post**](JanusAgentApi.md#agent_post_tc_delay_tc_delay_post) | **POST** /api/janus/agent/tc/delay | Set delay rules
[**agent_post_tc_filter_tc_filter_post**](JanusAgentApi.md#agent_post_tc_filter_tc_filter_post) | **POST** /api/janus/agent/tc/filter | Set filter rules
[**agent_post_tc_latency_tc_latency_post**](JanusAgentApi.md#agent_post_tc_latency_tc_latency_post) | **POST** /api/janus/agent/tc/latency | Set latency rules
[**agent_post_tc_netem_tc_netem_post**](JanusAgentApi.md#agent_post_tc_netem_tc_netem_post) | **POST** /api/janus/agent/tc/netem | Set netem rules
[**agent_post_tc_pacing_tc_pacing_post**](JanusAgentApi.md#agent_post_tc_pacing_tc_pacing_post) | **POST** /api/janus/agent/tc/pacing | Set pacing rules
[**agent_post_tune_endpoint_tune_post**](JanusAgentApi.md#agent_post_tune_endpoint_tune_post) | **POST** /api/janus/agent/tune | Set node tuning settings


# **agent_delete_tc_netem_tc_netem_delete**
> agent_delete_tc_netem_tc_netem_delete(tune_request)

Delete netem rules

### Example


```python
import janus_py_client
from janus_py_client.models.tune_request import TuneRequest
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    tune_request = janus_py_client.TuneRequest() # TuneRequest | 

    try:
        # Delete netem rules
        api_instance.agent_delete_tc_netem_tc_netem_delete(tune_request)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_delete_tc_netem_tc_netem_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tune_request** | [**TuneRequest**](TuneRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_delete_tc_pacing_tc_pacing_delete**
> agent_delete_tc_pacing_tc_pacing_delete(tune_request)

Delete pacing rules

### Example


```python
import janus_py_client
from janus_py_client.models.tune_request import TuneRequest
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    tune_request = janus_py_client.TuneRequest() # TuneRequest | 

    try:
        # Delete pacing rules
        api_instance.agent_delete_tc_pacing_tc_pacing_delete(tune_request)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_delete_tc_pacing_tc_pacing_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tune_request** | [**TuneRequest**](TuneRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_get_node_node_get**
> agent_get_node_node_get()

Returns static node resources

Returns static node resources

### Example


```python
import janus_py_client
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)

    try:
        # Returns static node resources
        api_instance.agent_get_node_node_get()
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_get_node_node_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_get_tc_delay_tc_delay_get**
> agent_get_tc_delay_tc_delay_get(interface=interface, container=container)

Get delay rules

### Example


```python
import janus_py_client
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    interface = 'interface_example' # str | Network interface name (optional)
    container = 'container_example' # str | Container ID (optional)

    try:
        # Get delay rules
        api_instance.agent_get_tc_delay_tc_delay_get(interface=interface, container=container)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_get_tc_delay_tc_delay_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | **str**| Network interface name | [optional] 
 **container** | **str**| Container ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_get_tc_filter_tc_filter_get**
> agent_get_tc_filter_tc_filter_get(interface=interface, container=container)

Get filter rules

### Example


```python
import janus_py_client
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    interface = 'interface_example' # str | Network interface name (optional)
    container = 'container_example' # str | Container ID (optional)

    try:
        # Get filter rules
        api_instance.agent_get_tc_filter_tc_filter_get(interface=interface, container=container)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_get_tc_filter_tc_filter_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | **str**| Network interface name | [optional] 
 **container** | **str**| Container ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_get_tc_latency_tc_latency_get**
> agent_get_tc_latency_tc_latency_get(interface=interface, container=container)

Get latency rules

### Example


```python
import janus_py_client
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    interface = 'interface_example' # str | Network interface name (optional)
    container = 'container_example' # str | Container ID (optional)

    try:
        # Get latency rules
        api_instance.agent_get_tc_latency_tc_latency_get(interface=interface, container=container)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_get_tc_latency_tc_latency_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | **str**| Network interface name | [optional] 
 **container** | **str**| Container ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_get_tc_netem_tc_netem_get**
> agent_get_tc_netem_tc_netem_get(interface=interface, container=container)

Get netem rules

### Example


```python
import janus_py_client
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    interface = 'interface_example' # str | Network interface name (optional)
    container = 'container_example' # str | Container ID (optional)

    try:
        # Get netem rules
        api_instance.agent_get_tc_netem_tc_netem_get(interface=interface, container=container)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_get_tc_netem_tc_netem_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | **str**| Network interface name | [optional] 
 **container** | **str**| Container ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_get_tc_pacing_tc_pacing_get**
> agent_get_tc_pacing_tc_pacing_get(interface=interface, container=container)

Get pacing rules

### Example


```python
import janus_py_client
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    interface = 'interface_example' # str | Network interface name (optional)
    container = 'container_example' # str | Container ID (optional)

    try:
        # Get pacing rules
        api_instance.agent_get_tc_pacing_tc_pacing_get(interface=interface, container=container)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_get_tc_pacing_tc_pacing_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | **str**| Network interface name | [optional] 
 **container** | **str**| Container ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_get_tune_endpoint_tune_get**
> agent_get_tune_endpoint_tune_get()

Get node tuning settings

### Example


```python
import janus_py_client
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)

    try:
        # Get node tuning settings
        api_instance.agent_get_tune_endpoint_tune_get()
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_get_tune_endpoint_tune_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_post_tc_delay_tc_delay_post**
> agent_post_tc_delay_tc_delay_post(tune_request)

Set delay rules

### Example


```python
import janus_py_client
from janus_py_client.models.tune_request import TuneRequest
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    tune_request = janus_py_client.TuneRequest() # TuneRequest | 

    try:
        # Set delay rules
        api_instance.agent_post_tc_delay_tc_delay_post(tune_request)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_post_tc_delay_tc_delay_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tune_request** | [**TuneRequest**](TuneRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_post_tc_filter_tc_filter_post**
> agent_post_tc_filter_tc_filter_post(tune_request)

Set filter rules

### Example


```python
import janus_py_client
from janus_py_client.models.tune_request import TuneRequest
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    tune_request = janus_py_client.TuneRequest() # TuneRequest | 

    try:
        # Set filter rules
        api_instance.agent_post_tc_filter_tc_filter_post(tune_request)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_post_tc_filter_tc_filter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tune_request** | [**TuneRequest**](TuneRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_post_tc_latency_tc_latency_post**
> agent_post_tc_latency_tc_latency_post(tune_request)

Set latency rules

### Example


```python
import janus_py_client
from janus_py_client.models.tune_request import TuneRequest
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    tune_request = janus_py_client.TuneRequest() # TuneRequest | 

    try:
        # Set latency rules
        api_instance.agent_post_tc_latency_tc_latency_post(tune_request)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_post_tc_latency_tc_latency_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tune_request** | [**TuneRequest**](TuneRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_post_tc_netem_tc_netem_post**
> agent_post_tc_netem_tc_netem_post(qo_s_agent)

Set netem rules

### Example


```python
import janus_py_client
from janus_py_client.models.qo_s_agent import QoSAgent
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    qo_s_agent = janus_py_client.QoSAgent() # QoSAgent | 

    try:
        # Set netem rules
        api_instance.agent_post_tc_netem_tc_netem_post(qo_s_agent)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_post_tc_netem_tc_netem_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qo_s_agent** | [**QoSAgent**](QoSAgent.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_post_tc_pacing_tc_pacing_post**
> agent_post_tc_pacing_tc_pacing_post(tune_request)

Set pacing rules

### Example


```python
import janus_py_client
from janus_py_client.models.tune_request import TuneRequest
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    tune_request = janus_py_client.TuneRequest() # TuneRequest | 

    try:
        # Set pacing rules
        api_instance.agent_post_tc_pacing_tc_pacing_post(tune_request)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_post_tc_pacing_tc_pacing_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tune_request** | [**TuneRequest**](TuneRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_post_tune_endpoint_tune_post**
> agent_post_tune_endpoint_tune_post(tune_request)

Set node tuning settings

### Example


```python
import janus_py_client
from janus_py_client.models.tune_request import TuneRequest
from janus_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = janus_py_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with janus_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = janus_py_client.JanusAgentApi(api_client)
    tune_request = janus_py_client.TuneRequest() # TuneRequest | 

    try:
        # Set node tuning settings
        api_instance.agent_post_tune_endpoint_tune_post(tune_request)
    except Exception as e:
        print("Exception when calling JanusAgentApi->agent_post_tune_endpoint_tune_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tune_request** | [**TuneRequest**](TuneRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

