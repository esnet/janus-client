# AddEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_type** | **int** | Active session ID | [optional] 
**name** | **str** | Name of the endpoint node | 
**public_url** | **str** | Comma separated list of fields to return | [optional] 
**type** | **int** | Endpoint type identifier (e.g. Docker, Slurm) | 
**url** | **str** | Base URL of the endpoint API | 

## Example

```python
from janus_py_client.models.add_endpoint_request import AddEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddEndpointRequest from a JSON string
add_endpoint_request_instance = AddEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(AddEndpointRequest.to_json())

# convert the object into a dict
add_endpoint_request_dict = add_endpoint_request_instance.to_dict()
# create an instance of AddEndpointRequest from a dict
add_endpoint_request_from_dict = AddEndpointRequest.from_dict(add_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


