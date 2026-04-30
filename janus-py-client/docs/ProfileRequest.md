# ProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Comma separated list of fields to return | [optional] 
**settings** | **Dict[str, object]** |  | 

## Example

```python
from janus_py_client.models.profile_request import ProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileRequest from a JSON string
profile_request_instance = ProfileRequest.from_json(json)
# print the JSON string representation of the object
print(ProfileRequest.to_json())

# convert the object into a dict
profile_request_dict = profile_request_instance.to_dict()
# create an instance of ProfileRequest from a dict
profile_request_from_dict = ProfileRequest.from_dict(profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


