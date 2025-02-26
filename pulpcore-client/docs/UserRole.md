# UserRole

Serializer for UserRole.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content_object** | **str** | pulp_href of the object for which role permissions should be asserted. If set to &#39;null&#39;, permissions will act on either domain or model-level. | 
**domain** | **str** | Domain this role should be applied on, mutually exclusive with content_object. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.user_role import UserRole

# TODO update the JSON string below
json = "{}"
# create an instance of UserRole from a JSON string
user_role_instance = UserRole.from_json(json)
# print the JSON string representation of the object
print(UserRole.to_json())

# convert the object into a dict
user_role_dict = user_role_instance.to_dict()
# create an instance of UserRole from a dict
user_role_from_dict = UserRole.from_dict(user_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


