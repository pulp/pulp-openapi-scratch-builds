# MavenMavenRepository

Serializer for Maven Repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name for this repository. | 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 

## Example

```python
from pulpcore.client.pulp_maven.models.maven_maven_repository import MavenMavenRepository

# TODO update the JSON string below
json = "{}"
# create an instance of MavenMavenRepository from a JSON string
maven_maven_repository_instance = MavenMavenRepository.from_json(json)
# print the JSON string representation of the object
print(MavenMavenRepository.to_json())

# convert the object into a dict
maven_maven_repository_dict = maven_maven_repository_instance.to_dict()
# create an instance of MavenMavenRepository from a dict
maven_maven_repository_from_dict = MavenMavenRepository.from_dict(maven_maven_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


