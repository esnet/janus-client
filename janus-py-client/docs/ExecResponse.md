# ExecResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Comma separated list of fields to return | [optional] 

## Example

```python
from janus_py_client.models.exec_response import ExecResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecResponse from a JSON string
exec_response_instance = ExecResponse.from_json(json)
# print the JSON string representation of the object
print(ExecResponse.to_json())

# convert the object into a dict
exec_response_dict = exec_response_instance.to_dict()
# create an instance of ExecResponse from a dict
exec_response_from_dict = ExecResponse.from_dict(exec_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


