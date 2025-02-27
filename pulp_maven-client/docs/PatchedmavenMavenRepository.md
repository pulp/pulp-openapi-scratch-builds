# PatchedmavenMavenRepository

Serializer for Maven Repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name for this repository. | [optional] 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 

## Example

```python
from pulpcore.client.pulp_maven.models.patchedmaven_maven_repository import PatchedmavenMavenRepository

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedmavenMavenRepository from a JSON string
patchedmaven_maven_repository_instance = PatchedmavenMavenRepository.from_json(json)
# print the JSON string representation of the object
print(PatchedmavenMavenRepository.to_json())

# convert the object into a dict
patchedmaven_maven_repository_dict = patchedmaven_maven_repository_instance.to_dict()
# create an instance of PatchedmavenMavenRepository from a dict
patchedmaven_maven_repository_from_dict = PatchedmavenMavenRepository.from_dict(patchedmaven_maven_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


