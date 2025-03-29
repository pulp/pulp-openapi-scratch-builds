# SetLabelResponse

Serializer for synchronously setting a label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from pulpcore.client.pulp_python.models.set_label_response import SetLabelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetLabelResponse from a JSON string
set_label_response_instance = SetLabelResponse.from_json(json)
# print the JSON string representation of the object
print(SetLabelResponse.to_json())

# convert the object into a dict
set_label_response_dict = set_label_response_instance.to_dict()
# create an instance of SetLabelResponse from a dict
set_label_response_from_dict = SetLabelResponse.from_dict(set_label_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


