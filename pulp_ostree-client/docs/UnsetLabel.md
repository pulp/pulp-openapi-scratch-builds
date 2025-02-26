# UnsetLabel

Serializer for synchronously setting a label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 

## Example

```python
from pulpcore.client.pulp_ostree.models.unset_label import UnsetLabel

# TODO update the JSON string below
json = "{}"
# create an instance of UnsetLabel from a JSON string
unset_label_instance = UnsetLabel.from_json(json)
# print the JSON string representation of the object
print(UnsetLabel.to_json())

# convert the object into a dict
unset_label_dict = unset_label_instance.to_dict()
# create an instance of UnsetLabel from a dict
unset_label_from_dict = UnsetLabel.from_dict(unset_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


