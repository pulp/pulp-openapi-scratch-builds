# UserResponse

Serializer for User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**email** | **str** | Email address | [optional] 
**is_staff** | **bool** | Designates whether the user can log into this admin site. | [optional] [default to False]
**is_active** | **bool** | Designates whether this user should be treated as active. | [optional] [default to True]
**date_joined** | **datetime** | Date joined | [optional] [readonly] 
**groups** | [**List[UserGroupResponse]**](UserGroupResponse.md) |  | [optional] [readonly] 
**hidden_fields** | [**List[GenericRemoteResponseHiddenFieldsInner]**](GenericRemoteResponseHiddenFieldsInner.md) | List of hidden (write only) fields | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print(UserResponse.to_json())

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_from_dict = UserResponse.from_dict(user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


