# PaginatedrpmRepoMetadataFileResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RpmRepoMetadataFileResponse]**](RpmRepoMetadataFileResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.paginatedrpm_repo_metadata_file_response_list import PaginatedrpmRepoMetadataFileResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedrpmRepoMetadataFileResponseList from a JSON string
paginatedrpm_repo_metadata_file_response_list_instance = PaginatedrpmRepoMetadataFileResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedrpmRepoMetadataFileResponseList.to_json())

# convert the object into a dict
paginatedrpm_repo_metadata_file_response_list_dict = paginatedrpm_repo_metadata_file_response_list_instance.to_dict()
# create an instance of PaginatedrpmRepoMetadataFileResponseList from a dict
paginatedrpm_repo_metadata_file_response_list_from_dict = PaginatedrpmRepoMetadataFileResponseList.from_dict(paginatedrpm_repo_metadata_file_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


