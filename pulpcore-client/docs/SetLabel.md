# SetLabel

Serializer for synchronously setting a label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from pulpcore.client.pulpcore.models.set_label import SetLabel

# TODO update the JSON string below
json = "{}"
# create an instance of SetLabel from a JSON string
set_label_instance = SetLabel.from_json(json)
# print the JSON string representation of the object
print(SetLabel.to_json())

# convert the object into a dict
set_label_dict = set_label_instance.to_dict()
# create an instance of SetLabel from a dict
set_label_from_dict = SetLabel.from_dict(set_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


