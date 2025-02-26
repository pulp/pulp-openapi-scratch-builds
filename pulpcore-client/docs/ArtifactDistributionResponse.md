# ArtifactDistributionResponse

A serializer for ArtifactDistribution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | The URL for accessing the publication as defined by this distribution. | [optional] [readonly] 
**name** | **str** | A unique name. Ex, &#x60;rawhide&#x60; and &#x60;stable&#x60;. | 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**content_guard** | **str** | An optional content-guard. | [optional] 
**hidden** | **bool** | Whether this distribution should be shown in the content app. | [optional] [default to False]
**no_content_change_since** | **str** | Timestamp since when the distributed content served by this distribution has not changed. If equals to &#x60;null&#x60;, no guarantee is provided about content changes. | [optional] [readonly] 
**base_path** | **str** | The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \&quot;foo\&quot; and \&quot;foo/bar\&quot;) | 
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.artifact_distribution_response import ArtifactDistributionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactDistributionResponse from a JSON string
artifact_distribution_response_instance = ArtifactDistributionResponse.from_json(json)
# print the JSON string representation of the object
print(ArtifactDistributionResponse.to_json())

# convert the object into a dict
artifact_distribution_response_dict = artifact_distribution_response_instance.to_dict()
# create an instance of ArtifactDistributionResponse from a dict
artifact_distribution_response_from_dict = ArtifactDistributionResponse.from_dict(artifact_distribution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


