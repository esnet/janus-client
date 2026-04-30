# TuneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **Dict[str, object]** |  | 

## Example

```python
from janus_py_client.models.tune_request import TuneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TuneRequest from a JSON string
tune_request_instance = TuneRequest.from_json(json)
# print the JSON string representation of the object
print(TuneRequest.to_json())

# convert the object into a dict
tune_request_dict = tune_request_instance.to_dict()
# create an instance of TuneRequest from a dict
tune_request_from_dict = TuneRequest.from_dict(tune_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


