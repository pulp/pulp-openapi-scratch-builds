# PaginatedmavenMavenRemoteResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MavenMavenRemoteResponse]**](MavenMavenRemoteResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_maven.models.paginatedmaven_maven_remote_response_list import PaginatedmavenMavenRemoteResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedmavenMavenRemoteResponseList from a JSON string
paginatedmaven_maven_remote_response_list_instance = PaginatedmavenMavenRemoteResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedmavenMavenRemoteResponseList.to_json())

# convert the object into a dict
paginatedmaven_maven_remote_response_list_dict = paginatedmaven_maven_remote_response_list_instance.to_dict()
# create an instance of PaginatedmavenMavenRemoteResponseList from a dict
paginatedmaven_maven_remote_response_list_from_dict = PaginatedmavenMavenRemoteResponseList.from_dict(paginatedmaven_maven_remote_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


