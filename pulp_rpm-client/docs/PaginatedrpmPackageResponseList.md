# PaginatedrpmPackageResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RpmPackageResponse]**](RpmPackageResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.paginatedrpm_package_response_list import PaginatedrpmPackageResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedrpmPackageResponseList from a JSON string
paginatedrpm_package_response_list_instance = PaginatedrpmPackageResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedrpmPackageResponseList.to_json())

# convert the object into a dict
paginatedrpm_package_response_list_dict = paginatedrpm_package_response_list_instance.to_dict()
# create an instance of PaginatedrpmPackageResponseList from a dict
paginatedrpm_package_response_list_from_dict = PaginatedrpmPackageResponseList.from_dict(paginatedrpm_package_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


