# PaginatedrpmModulemdResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RpmModulemdResponse]**](RpmModulemdResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.paginatedrpm_modulemd_response_list import PaginatedrpmModulemdResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedrpmModulemdResponseList from a JSON string
paginatedrpm_modulemd_response_list_instance = PaginatedrpmModulemdResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedrpmModulemdResponseList.to_json())

# convert the object into a dict
paginatedrpm_modulemd_response_list_dict = paginatedrpm_modulemd_response_list_instance.to_dict()
# create an instance of PaginatedrpmModulemdResponseList from a dict
paginatedrpm_modulemd_response_list_from_dict = PaginatedrpmModulemdResponseList.from_dict(paginatedrpm_modulemd_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


