# PatchedostreeOstreeRepository

A Serializer class for an OSTree repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name for this repository. | [optional] 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 
**compute_delta** | **bool** |  | [optional] [default to True]

## Example

```python
from pulpcore.client.pulp_ostree.models.patchedostree_ostree_repository import PatchedostreeOstreeRepository

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedostreeOstreeRepository from a JSON string
patchedostree_ostree_repository_instance = PatchedostreeOstreeRepository.from_json(json)
# print the JSON string representation of the object
print(PatchedostreeOstreeRepository.to_json())

# convert the object into a dict
patchedostree_ostree_repository_dict = patchedostree_ostree_repository_instance.to_dict()
# create an instance of PatchedostreeOstreeRepository from a dict
patchedostree_ostree_repository_from_dict = PatchedostreeOstreeRepository.from_dict(patchedostree_ostree_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


