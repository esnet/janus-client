# AuthBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** |  | [optional] 
**identifiers** | [**List[IdentifiersInner]**](IdentifiersInner.md) | List of resource names or IDs | 
**remove** | **bool** | If true, remove these users/groups instead of adding them | [optional] 
**resource** | **str** | Resource type | 
**users** | **List[str]** |  | [optional] 

## Example

```python
from janus_py_client.models.auth_bulk_request import AuthBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthBulkRequest from a JSON string
auth_bulk_request_instance = AuthBulkRequest.from_json(json)
# print the JSON string representation of the object
print(AuthBulkRequest.to_json())

# convert the object into a dict
auth_bulk_request_dict = auth_bulk_request_instance.to_dict()
# create an instance of AuthBulkRequest from a dict
auth_bulk_request_from_dict = AuthBulkRequest.from_dict(auth_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


