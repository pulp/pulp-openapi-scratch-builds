# PaginatedRepositoryVersionResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RepositoryVersionResponse]**](RepositoryVersionResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_repository_version_response_list import PaginatedRepositoryVersionResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRepositoryVersionResponseList from a JSON string
paginated_repository_version_response_list_instance = PaginatedRepositoryVersionResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRepositoryVersionResponseList.to_json())

# convert the object into a dict
paginated_repository_version_response_list_dict = paginated_repository_version_response_list_instance.to_dict()
# create an instance of PaginatedRepositoryVersionResponseList from a dict
paginated_repository_version_response_list_from_dict = PaginatedRepositoryVersionResponseList.from_dict(paginated_repository_version_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


