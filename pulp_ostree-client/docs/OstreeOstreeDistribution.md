# OstreeOstreeDistribution

A Serializer class for an OSTree distribution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_path** | **str** | The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \&quot;foo\&quot; and \&quot;foo/bar\&quot;) | 
**content_guard** | **str** | An optional content-guard. | [optional] 
**hidden** | **bool** | Whether this distribution should be shown in the content app. | [optional] [default to False]
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name. Ex, &#x60;rawhide&#x60; and &#x60;stable&#x60;. | 
**repository** | **str** | The latest RepositoryVersion for this Repository will be served. | [optional] 
**repository_version** | **str** | RepositoryVersion to be served | [optional] 

## Example

```python
from pulpcore.client.pulp_ostree.models.ostree_ostree_distribution import OstreeOstreeDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of OstreeOstreeDistribution from a JSON string
ostree_ostree_distribution_instance = OstreeOstreeDistribution.from_json(json)
# print the JSON string representation of the object
print(OstreeOstreeDistribution.to_json())

# convert the object into a dict
ostree_ostree_distribution_dict = ostree_ostree_distribution_instance.to_dict()
# create an instance of OstreeOstreeDistribution from a dict
ostree_ostree_distribution_from_dict = OstreeOstreeDistribution.from_dict(ostree_ostree_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


