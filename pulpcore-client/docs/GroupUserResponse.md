# GroupUserResponse

Serializer for Users that belong to a Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** |  | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.group_user_response import GroupUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupUserResponse from a JSON string
group_user_response_instance = GroupUserResponse.from_json(json)
# print the JSON string representation of the object
print(GroupUserResponse.to_json())

# convert the object into a dict
group_user_response_dict = group_user_response_instance.to_dict()
# create an instance of GroupUserResponse from a dict
group_user_response_from_dict = GroupUserResponse.from_dict(group_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


