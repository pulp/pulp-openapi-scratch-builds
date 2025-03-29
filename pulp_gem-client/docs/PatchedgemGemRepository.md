# PatchedgemGemRepository

A Serializer for GemRepository.

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
from pulpcore.client.pulp_gem.models.patchedgem_gem_repository import PatchedgemGemRepository

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedgemGemRepository from a JSON string
patchedgem_gem_repository_instance = PatchedgemGemRepository.from_json(json)
# print the JSON string representation of the object
print(PatchedgemGemRepository.to_json())

# convert the object into a dict
patchedgem_gem_repository_dict = patchedgem_gem_repository_instance.to_dict()
# create an instance of PatchedgemGemRepository from a dict
patchedgem_gem_repository_from_dict = PatchedgemGemRepository.from_dict(patchedgem_gem_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


