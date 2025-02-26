# PaginatedrpmModulemdDefaultsResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RpmModulemdDefaultsResponse]**](RpmModulemdDefaultsResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.paginatedrpm_modulemd_defaults_response_list import PaginatedrpmModulemdDefaultsResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedrpmModulemdDefaultsResponseList from a JSON string
paginatedrpm_modulemd_defaults_response_list_instance = PaginatedrpmModulemdDefaultsResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedrpmModulemdDefaultsResponseList.to_json())

# convert the object into a dict
paginatedrpm_modulemd_defaults_response_list_dict = paginatedrpm_modulemd_defaults_response_list_instance.to_dict()
# create an instance of PaginatedrpmModulemdDefaultsResponseList from a dict
paginatedrpm_modulemd_defaults_response_list_from_dict = PaginatedrpmModulemdDefaultsResponseList.from_dict(paginatedrpm_modulemd_defaults_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


