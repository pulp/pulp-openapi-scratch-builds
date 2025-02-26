# PaginatedrpmPackageCategoryResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RpmPackageCategoryResponse]**](RpmPackageCategoryResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.paginatedrpm_package_category_response_list import PaginatedrpmPackageCategoryResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedrpmPackageCategoryResponseList from a JSON string
paginatedrpm_package_category_response_list_instance = PaginatedrpmPackageCategoryResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedrpmPackageCategoryResponseList.to_json())

# convert the object into a dict
paginatedrpm_package_category_response_list_dict = paginatedrpm_package_category_response_list_instance.to_dict()
# create an instance of PaginatedrpmPackageCategoryResponseList from a dict
paginatedrpm_package_category_response_list_from_dict = PaginatedrpmPackageCategoryResponseList.from_dict(paginatedrpm_package_category_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


