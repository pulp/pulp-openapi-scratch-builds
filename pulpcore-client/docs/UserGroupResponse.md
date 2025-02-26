# UserGroupResponse

Serializer for Groups that belong to an User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name. | 
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** |  | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.user_group_response import UserGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupResponse from a JSON string
user_group_response_instance = UserGroupResponse.from_json(json)
# print the JSON string representation of the object
print(UserGroupResponse.to_json())

# convert the object into a dict
user_group_response_dict = user_group_response_instance.to_dict()
# create an instance of UserGroupResponse from a dict
user_group_response_from_dict = UserGroupResponse.from_dict(user_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


