# QoSAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** | Network interface name | [optional] 
**corrupt** | **str** | Network interface name | [optional] 
**delay** | **str** | Network interface name | [optional] 
**dport** | **str** | Network interface name | [optional] 
**interface** | **str** | Network interface name | [optional] 
**ip** | **str** | Network interface name | [optional] 
**limit** | **str** | Network interface name | [optional] 
**loss** | **str** | Network interface name | [optional] 
**rate** | **str** | Network interface name | [optional] 
**reordering** | **str** | Network interface name | [optional] 

## Example

```python
from janus_py_client.models.qo_s_agent import QoSAgent

# TODO update the JSON string below
json = "{}"
# create an instance of QoSAgent from a JSON string
qo_s_agent_instance = QoSAgent.from_json(json)
# print the JSON string representation of the object
print(QoSAgent.to_json())

# convert the object into a dict
qo_s_agent_dict = qo_s_agent_instance.to_dict()
# create an instance of QoSAgent from a dict
qo_s_agent_from_dict = QoSAgent.from_dict(qo_s_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


