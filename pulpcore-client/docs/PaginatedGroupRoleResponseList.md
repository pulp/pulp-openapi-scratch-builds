# PaginatedGroupRoleResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GroupRoleResponse]**](GroupRoleResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_group_role_response_list import PaginatedGroupRoleResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupRoleResponseList from a JSON string
paginated_group_role_response_list_instance = PaginatedGroupRoleResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGroupRoleResponseList.to_json())

# convert the object into a dict
paginated_group_role_response_list_dict = paginated_group_role_response_list_instance.to_dict()
# create an instance of PaginatedGroupRoleResponseList from a dict
paginated_group_role_response_list_from_dict = PaginatedGroupRoleResponseList.from_dict(paginated_group_role_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


