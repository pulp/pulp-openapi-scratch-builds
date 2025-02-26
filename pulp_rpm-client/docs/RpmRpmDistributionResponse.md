# RpmRpmDistributionResponse

Serializer for RPM Distributions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**base_path** | **str** | The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \&quot;foo\&quot; and \&quot;foo/bar\&quot;) | 
**base_url** | **str** | The URL for accessing the publication as defined by this distribution. | [optional] [readonly] 
**content_guard** | **str** | An optional content-guard. | [optional] 
**no_content_change_since** | **str** | Timestamp since when the distributed content served by this distribution has not changed. If equals to &#x60;null&#x60;, no guarantee is provided about content changes. | [optional] [readonly] 
**hidden** | **bool** | Whether this distribution should be shown in the content app. | [optional] [default to False]
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name. Ex, &#x60;rawhide&#x60; and &#x60;stable&#x60;. | 
**repository** | **str** | The latest RepositoryVersion for this Repository will be served. | [optional] 
**publication** | **str** | Publication to be served | [optional] 
**generate_repo_config** | **bool** | An option specifying whether Pulp should generate *.repo files. | [optional] [default to False]

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_rpm_distribution_response import RpmRpmDistributionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmRpmDistributionResponse from a JSON string
rpm_rpm_distribution_response_instance = RpmRpmDistributionResponse.from_json(json)
# print the JSON string representation of the object
print(RpmRpmDistributionResponse.to_json())

# convert the object into a dict
rpm_rpm_distribution_response_dict = rpm_rpm_distribution_response_instance.to_dict()
# create an instance of RpmRpmDistributionResponse from a dict
rpm_rpm_distribution_response_from_dict = RpmRpmDistributionResponse.from_dict(rpm_rpm_distribution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


