# PaginatedUserRoleResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UserRoleResponse]**](UserRoleResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_user_role_response_list import PaginatedUserRoleResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserRoleResponseList from a JSON string
paginated_user_role_response_list_instance = PaginatedUserRoleResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserRoleResponseList.to_json())

# convert the object into a dict
paginated_user_role_response_list_dict = paginated_user_role_response_list_instance.to_dict()
# create an instance of PaginatedUserRoleResponseList from a dict
paginated_user_role_response_list_from_dict = PaginatedUserRoleResponseList.from_dict(paginated_user_role_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


