# PaginatedrpmPackageGroupResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RpmPackageGroupResponse]**](RpmPackageGroupResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.paginatedrpm_package_group_response_list import PaginatedrpmPackageGroupResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedrpmPackageGroupResponseList from a JSON string
paginatedrpm_package_group_response_list_instance = PaginatedrpmPackageGroupResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedrpmPackageGroupResponseList.to_json())

# convert the object into a dict
paginatedrpm_package_group_response_list_dict = paginatedrpm_package_group_response_list_instance.to_dict()
# create an instance of PaginatedrpmPackageGroupResponseList from a dict
paginatedrpm_package_group_response_list_from_dict = PaginatedrpmPackageGroupResponseList.from_dict(paginatedrpm_package_group_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


