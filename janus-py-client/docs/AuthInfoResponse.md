# AuthInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** | List of authorized groups | [optional] 
**users** | **List[str]** | List of authorized users | [optional] 

## Example

```python
from janus_py_client.models.auth_info_response import AuthInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthInfoResponse from a JSON string
auth_info_response_instance = AuthInfoResponse.from_json(json)
# print the JSON string representation of the object
print(AuthInfoResponse.to_json())

# convert the object into a dict
auth_info_response_dict = auth_info_response_instance.to_dict()
# create an instance of AuthInfoResponse from a dict
auth_info_response_from_dict = AuthInfoResponse.from_dict(auth_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


