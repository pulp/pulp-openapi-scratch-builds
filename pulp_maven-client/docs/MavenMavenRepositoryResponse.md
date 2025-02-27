# MavenMavenRepositoryResponse

Serializer for Maven Repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**versions_href** | **str** |  | [optional] [readonly] 
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**latest_version_href** | **str** |  | [optional] [readonly] 
**name** | **str** | A unique name for this repository. | 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 

## Example

```python
from pulpcore.client.pulp_maven.models.maven_maven_repository_response import MavenMavenRepositoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MavenMavenRepositoryResponse from a JSON string
maven_maven_repository_response_instance = MavenMavenRepositoryResponse.from_json(json)
# print the JSON string representation of the object
print(MavenMavenRepositoryResponse.to_json())

# convert the object into a dict
maven_maven_repository_response_dict = maven_maven_repository_response_instance.to_dict()
# create an instance of MavenMavenRepositoryResponse from a dict
maven_maven_repository_response_from_dict = MavenMavenRepositoryResponse.from_dict(maven_maven_repository_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


