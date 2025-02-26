# NestedRole

Serializer to add/remove object roles to/from users/groups.  This is used in conjunction with ``pulpcore.app.viewsets.base.RolesMixin`` and requires the underlying object to be passed as ``content_object`` in the context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** |  | [optional] [default to []]
**groups** | **List[str]** |  | [optional] [default to []]
**role** | **str** |  | 

## Example

```python
from pulpcore.client.pulp_ostree.models.nested_role import NestedRole

# TODO update the JSON string below
json = "{}"
# create an instance of NestedRole from a JSON string
nested_role_instance = NestedRole.from_json(json)
# print the JSON string representation of the object
print(NestedRole.to_json())

# convert the object into a dict
nested_role_dict = nested_role_instance.to_dict()
# create an instance of NestedRole from a dict
nested_role_from_dict = NestedRole.from_dict(nested_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


