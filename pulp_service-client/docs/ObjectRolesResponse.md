# ObjectRolesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[NestedRoleResponse]**](NestedRoleResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_service.models.object_roles_response import ObjectRolesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectRolesResponse from a JSON string
object_roles_response_instance = ObjectRolesResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectRolesResponse.to_json())

# convert the object into a dict
object_roles_response_dict = object_roles_response_instance.to_dict()
# create an instance of ObjectRolesResponse from a dict
object_roles_response_from_dict = ObjectRolesResponse.from_dict(object_roles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


