# GemGemRepositoryResponse

A Serializer for GemRepository.

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
from pulpcore.client.pulp_gem.models.gem_gem_repository_response import GemGemRepositoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GemGemRepositoryResponse from a JSON string
gem_gem_repository_response_instance = GemGemRepositoryResponse.from_json(json)
# print the JSON string representation of the object
print(GemGemRepositoryResponse.to_json())

# convert the object into a dict
gem_gem_repository_response_dict = gem_gem_repository_response_instance.to_dict()
# create an instance of GemGemRepositoryResponse from a dict
gem_gem_repository_response_from_dict = GemGemRepositoryResponse.from_dict(gem_gem_repository_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


