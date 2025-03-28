# PatchedgemGemDistribution

A Serializer for GemDistribution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_path** | **str** | The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \&quot;foo\&quot; and \&quot;foo/bar\&quot;) | [optional] 
**content_guard** | **str** | An optional content-guard. | [optional] 
**hidden** | **bool** | Whether this distribution should be shown in the content app. | [optional] [default to False]
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name. Ex, &#x60;rawhide&#x60; and &#x60;stable&#x60;. | [optional] 
**repository** | **str** | The latest RepositoryVersion for this Repository will be served. | [optional] 
**publication** | **str** | Publication to be served | [optional] 
**remote** | **str** | Remote that can be used to fetch content when using pull-through caching. | [optional] 

## Example

```python
from pulpcore.client.pulp_gem.models.patchedgem_gem_distribution import PatchedgemGemDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedgemGemDistribution from a JSON string
patchedgem_gem_distribution_instance = PatchedgemGemDistribution.from_json(json)
# print the JSON string representation of the object
print(PatchedgemGemDistribution.to_json())

# convert the object into a dict
patchedgem_gem_distribution_dict = patchedgem_gem_distribution_instance.to_dict()
# create an instance of PatchedgemGemDistribution from a dict
patchedgem_gem_distribution_from_dict = PatchedgemGemDistribution.from_dict(patchedgem_gem_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


