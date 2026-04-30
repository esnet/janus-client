# ValidationErrorModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ctx** | **Dict[str, object]** | An optional object which contains values required to render the error message. | [optional] 
**input** | **object** |  | 
**loc** | **List[object]** | The error&#39;s location as a list. | 
**msg** | **str** | A human readable explanation of the error. | 
**type** | **str** | A computer-readable identifier of the error type. | 
**url** | **str** | Comma separated list of fields to return | [optional] 

## Example

```python
from janus_py_client.models.validation_error_model import ValidationErrorModel

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorModel from a JSON string
validation_error_model_instance = ValidationErrorModel.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorModel.to_json())

# convert the object into a dict
validation_error_model_dict = validation_error_model_instance.to_dict()
# create an instance of ValidationErrorModel from a dict
validation_error_model_from_dict = ValidationErrorModel.from_dict(validation_error_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


