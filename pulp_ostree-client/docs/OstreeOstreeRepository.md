# OstreeOstreeRepository

A Serializer class for an OSTree repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name for this repository. | 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 
**compute_delta** | **bool** |  | [optional] [default to True]

## Example

```python
from pulpcore.client.pulp_ostree.models.ostree_ostree_repository import OstreeOstreeRepository

# TODO update the JSON string below
json = "{}"
# create an instance of OstreeOstreeRepository from a JSON string
ostree_ostree_repository_instance = OstreeOstreeRepository.from_json(json)
# print the JSON string representation of the object
print(OstreeOstreeRepository.to_json())

# convert the object into a dict
ostree_ostree_repository_dict = ostree_ostree_repository_instance.to_dict()
# create an instance of OstreeOstreeRepository from a dict
ostree_ostree_repository_from_dict = OstreeOstreeRepository.from_dict(ostree_ostree_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


