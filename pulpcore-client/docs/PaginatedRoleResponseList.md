# PaginatedRoleResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RoleResponse]**](RoleResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_role_response_list import PaginatedRoleResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRoleResponseList from a JSON string
paginated_role_response_list_instance = PaginatedRoleResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRoleResponseList.to_json())

# convert the object into a dict
paginated_role_response_list_dict = paginated_role_response_list_instance.to_dict()
# create an instance of PaginatedRoleResponseList from a dict
paginated_role_response_list_from_dict = PaginatedRoleResponseList.from_dict(paginated_role_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


