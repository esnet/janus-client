# AuthBulkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Resource type updated | 
**results** | **List[Dict[str, object]]** | List of individual update results | 

## Example

```python
from janus_py_client.models.auth_bulk_response import AuthBulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthBulkResponse from a JSON string
auth_bulk_response_instance = AuthBulkResponse.from_json(json)
# print the JSON string representation of the object
print(AuthBulkResponse.to_json())

# convert the object into a dict
auth_bulk_response_dict = auth_bulk_response_instance.to_dict()
# create an instance of AuthBulkResponse from a dict
auth_bulk_response_from_dict = AuthBulkResponse.from_dict(auth_bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


