# janus_py_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_check_token_token_get**](DefaultApi.md#controller_check_token_token_get) | **GET** /api/janus/controller/token | Check Token
[**controller_get_token_token_post**](DefaultApi.md#controller_get_token_token_post) | **POST** /api/janus/controller/token | Get Token


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
    api_instance = janus_py_client.DefaultApi(api_client)

    try:
        # Check Token
        api_response = api_instance.controller_check_token_token_get()
        print("The response of DefaultApi->controller_check_token_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->controller_check_token_token_get: %s\n" % e)
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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |
**500** | Internal Server Error |  -  |

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
    api_instance = janus_py_client.DefaultApi(api_client)

    try:
        # Get Token
        api_response = api_instance.controller_get_token_token_post()
        print("The response of DefaultApi->controller_get_token_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->controller_get_token_token_post: %s\n" % e)
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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

