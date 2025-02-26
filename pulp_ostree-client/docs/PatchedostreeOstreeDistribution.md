# PatchedostreeOstreeDistribution

A Serializer class for an OSTree distribution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_path** | **str** | The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \&quot;foo\&quot; and \&quot;foo/bar\&quot;) | [optional] 
**content_guard** | **str** | An optional content-guard. | [optional] 
**hidden** | **bool** | Whether this distribution should be shown in the content app. | [optional] [default to False]
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name. Ex, &#x60;rawhide&#x60; and &#x60;stable&#x60;. | [optional] 
**repository** | **str** | The latest RepositoryVersion for this Repository will be served. | [optional] 
**repository_version** | **str** | RepositoryVersion to be served | [optional] 

## Example

```python
from pulpcore.client.pulp_ostree.models.patchedostree_ostree_distribution import PatchedostreeOstreeDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedostreeOstreeDistribution from a JSON string
patchedostree_ostree_distribution_instance = PatchedostreeOstreeDistribution.from_json(json)
# print the JSON string representation of the object
print(PatchedostreeOstreeDistribution.to_json())

# convert the object into a dict
patchedostree_ostree_distribution_dict = patchedostree_ostree_distribution_instance.to_dict()
# create an instance of PatchedostreeOstreeDistribution from a dict
patchedostree_ostree_distribution_from_dict = PatchedostreeOstreeDistribution.from_dict(patchedostree_ostree_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


