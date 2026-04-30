# SessionRequestList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **str** | Comma separated list of fields to return | [optional] 
**constraints** | **Dict[str, object]** | Resource and scheduling constraints | [optional] 
**image** | **str** | Docker image to run | 
**instances** | [**List[InstancesInner]**](InstancesInner.md) | List of instances or node names to deploy | 
**kwargs** | **Dict[str, object]** | Additional docker kwargs | [optional] 
**name** | **str** | Comma separated list of fields to return | [optional] 
**overrides** | **Dict[str, object]** | Profile overrides specific to this session | [optional] 
**profile** | **str** | Host profile defining deployment parameters | 
**remove_container** | **bool** | Automatically remove container on exit | [optional] 

## Example

```python
from janus_py_client.models.session_request_list import SessionRequestList

# TODO update the JSON string below
json = "{}"
# create an instance of SessionRequestList from a JSON string
session_request_list_instance = SessionRequestList.from_json(json)
# print the JSON string representation of the object
print(SessionRequestList.to_json())

# convert the object into a dict
session_request_list_dict = session_request_list_instance.to_dict()
# create an instance of SessionRequestList from a dict
session_request_list_from_dict = SessionRequestList.from_dict(session_request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


