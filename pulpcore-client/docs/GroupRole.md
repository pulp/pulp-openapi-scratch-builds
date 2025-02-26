# GroupRole

Serializer for GroupRole.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content_object** | **str** | pulp_href of the object for which role permissions should be asserted. If set to &#39;null&#39;, permissions will act on the model-level. | 
**domain** | **str** | Domain this role should be applied on, mutually exclusive with content_object. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.group_role import GroupRole

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRole from a JSON string
group_role_instance = GroupRole.from_json(json)
# print the JSON string representation of the object
print(GroupRole.to_json())

# convert the object into a dict
group_role_dict = group_role_instance.to_dict()
# create an instance of GroupRole from a dict
group_role_from_dict = GroupRole.from_dict(group_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


