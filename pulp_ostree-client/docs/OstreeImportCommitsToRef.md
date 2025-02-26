# OstreeImportCommitsToRef

A Serializer class for appending child commits to a repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact** | **str** | An artifact representing OSTree content compressed as a tarball. | 
**repository_name** | **str** | The name of a repository that contains the compressed OSTree content. | 
**ref** | **str** | The name of a ref branch that holds the reference to the last commit. | 

## Example

```python
from pulpcore.client.pulp_ostree.models.ostree_import_commits_to_ref import OstreeImportCommitsToRef

# TODO update the JSON string below
json = "{}"
# create an instance of OstreeImportCommitsToRef from a JSON string
ostree_import_commits_to_ref_instance = OstreeImportCommitsToRef.from_json(json)
# print the JSON string representation of the object
print(OstreeImportCommitsToRef.to_json())

# convert the object into a dict
ostree_import_commits_to_ref_dict = ostree_import_commits_to_ref_instance.to_dict()
# create an instance of OstreeImportCommitsToRef from a dict
ostree_import_commits_to_ref_from_dict = OstreeImportCommitsToRef.from_dict(ostree_import_commits_to_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


