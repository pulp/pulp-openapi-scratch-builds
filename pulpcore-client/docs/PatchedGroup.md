# PatchedGroup

Serializer for Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.patched_group import PatchedGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGroup from a JSON string
patched_group_instance = PatchedGroup.from_json(json)
# print the JSON string representation of the object
print(PatchedGroup.to_json())

# convert the object into a dict
patched_group_dict = patched_group_instance.to_dict()
# create an instance of PatchedGroup from a dict
patched_group_from_dict = PatchedGroup.from_dict(patched_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


