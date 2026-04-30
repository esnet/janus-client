# AuthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** |  | 
**users** | **List[str]** |  | 

## Example

```python
from janus_py_client.models.auth_request import AuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRequest from a JSON string
auth_request_instance = AuthRequest.from_json(json)
# print the JSON string representation of the object
print(AuthRequest.to_json())

# convert the object into a dict
auth_request_dict = auth_request_instance.to_dict()
# create an instance of AuthRequest from a dict
auth_request_from_dict = AuthRequest.from_dict(auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


