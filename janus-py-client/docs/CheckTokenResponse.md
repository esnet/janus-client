# CheckTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logged_in_as** | **str** |  | 

## Example

```python
from janus_py_client.models.check_token_response import CheckTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckTokenResponse from a JSON string
check_token_response_instance = CheckTokenResponse.from_json(json)
# print the JSON string representation of the object
print(CheckTokenResponse.to_json())

# convert the object into a dict
check_token_response_dict = check_token_response_instance.to_dict()
# create an instance of CheckTokenResponse from a dict
check_token_response_from_dict = CheckTokenResponse.from_dict(check_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


