# GemGemRepository

A Serializer for GemRepository.

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
from pulpcore.client.pulp_gem.models.gem_gem_repository import GemGemRepository

# TODO update the JSON string below
json = "{}"
# create an instance of GemGemRepository from a JSON string
gem_gem_repository_instance = GemGemRepository.from_json(json)
# print the JSON string representation of the object
print(GemGemRepository.to_json())

# convert the object into a dict
gem_gem_repository_dict = gem_gem_repository_instance.to_dict()
# create an instance of GemGemRepository from a dict
gem_gem_repository_from_dict = GemGemRepository.from_dict(gem_gem_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


