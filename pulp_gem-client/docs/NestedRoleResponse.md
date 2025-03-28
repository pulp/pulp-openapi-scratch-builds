# NestedRoleResponse

Serializer to add/remove object roles to/from users/groups.  This is used in conjunction with ``pulpcore.app.viewsets.base.RolesMixin`` and requires the underlying object to be passed as ``content_object`` in the context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** |  | [optional] [default to []]
**groups** | **List[str]** |  | [optional] [default to []]
**role** | **str** |  | 

## Example

```python
from pulpcore.client.pulp_gem.models.nested_role_response import NestedRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NestedRoleResponse from a JSON string
nested_role_response_instance = NestedRoleResponse.from_json(json)
# print the JSON string representation of the object
print(NestedRoleResponse.to_json())

# convert the object into a dict
nested_role_response_dict = nested_role_response_instance.to_dict()
# create an instance of NestedRoleResponse from a dict
nested_role_response_from_dict = NestedRoleResponse.from_dict(nested_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


