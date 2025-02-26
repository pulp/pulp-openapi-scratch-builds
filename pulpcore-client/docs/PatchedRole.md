# PatchedRole

Serializer for Role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this role. | [optional] 
**description** | **str** | An optional description. | [optional] 
**permissions** | **List[str]** | List of permissions defining the role. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.patched_role import PatchedRole

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRole from a JSON string
patched_role_instance = PatchedRole.from_json(json)
# print the JSON string representation of the object
print(PatchedRole.to_json())

# convert the object into a dict
patched_role_dict = patched_role_instance.to_dict()
# create an instance of PatchedRole from a dict
patched_role_from_dict = PatchedRole.from_dict(patched_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


