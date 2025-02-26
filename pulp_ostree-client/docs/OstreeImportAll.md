# OstreeImportAll

A Serializer class for importing all refs and commits to a repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact** | **str** | An artifact representing OSTree content compressed as a tarball. | 
**repository_name** | **str** | The name of a repository that contains the compressed OSTree content. | 

## Example

```python
from pulpcore.client.pulp_ostree.models.ostree_import_all import OstreeImportAll

# TODO update the JSON string below
json = "{}"
# create an instance of OstreeImportAll from a JSON string
ostree_import_all_instance = OstreeImportAll.from_json(json)
# print the JSON string representation of the object
print(OstreeImportAll.to_json())

# convert the object into a dict
ostree_import_all_dict = ostree_import_all_instance.to_dict()
# create an instance of OstreeImportAll from a dict
ostree_import_all_from_dict = OstreeImportAll.from_dict(ostree_import_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


