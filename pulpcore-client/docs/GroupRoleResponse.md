# GroupRoleResponse

Serializer for GroupRole.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**role** | **str** |  | 
**content_object** | **str** | pulp_href of the object for which role permissions should be asserted. If set to &#39;null&#39;, permissions will act on the model-level. | 
**description** | **str** |  | [optional] [readonly] 
**permissions** | **List[str]** |  | [optional] [readonly] 
**domain** | **str** | Domain this role should be applied on, mutually exclusive with content_object. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.group_role_response import GroupRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRoleResponse from a JSON string
group_role_response_instance = GroupRoleResponse.from_json(json)
# print the JSON string representation of the object
print(GroupRoleResponse.to_json())

# convert the object into a dict
group_role_response_dict = group_role_response_instance.to_dict()
# create an instance of GroupRoleResponse from a dict
group_role_response_from_dict = GroupRoleResponse.from_dict(group_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


