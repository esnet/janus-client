# janus_py_client.ImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_get_images_images_get**](ImagesApi.md#controller_get_images_images_get) | **GET** /api/janus/controller/images | Get images
[**controller_get_images_images_path_name_get**](ImagesApi.md#controller_get_images_images_path_name_get) | **GET** /api/janus/controller/images/{name} | Get a specific image


# **controller_get_images_images_get**
> List[ImageResponse] controller_get_images_images_get(name, fields=fields)

Get images

List all images or a specific image.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.image_response import ImageResponse
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
    api_instance = janus_py_client.ImagesApi(api_client)
    name = 'name_example' # str | Image name
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get images
        api_response = api_instance.controller_get_images_images_get(name, fields=fields)
        print("The response of ImagesApi->controller_get_images_images_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->controller_get_images_images_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Image name | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

[**List[ImageResponse]**](ImageResponse.md)

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

# **controller_get_images_images_path_name_get**
> ImageResponse controller_get_images_images_path_name_get(name, fields=fields)

Get a specific image

List all images or a specific image.

### Example

* Bearer (JWT) Authentication (jwt):
* Basic Authentication (basicAuth):

```python
import janus_py_client
from janus_py_client.models.image_response import ImageResponse
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
    api_instance = janus_py_client.ImagesApi(api_client)
    name = 'name_example' # str | Image name
    fields = 'fields_example' # str | Comma separated list of fields to return (optional)

    try:
        # Get a specific image
        api_response = api_instance.controller_get_images_images_path_name_get(name, fields=fields)
        print("The response of ImagesApi->controller_get_images_images_path_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->controller_get_images_images_path_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Image name | 
 **fields** | **str**| Comma separated list of fields to return | [optional] 

### Return type

[**ImageResponse**](ImageResponse.md)

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

