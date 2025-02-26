# RpmRpmDistribution

Serializer for RPM Distributions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_path** | **str** | The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \&quot;foo\&quot; and \&quot;foo/bar\&quot;) | 
**content_guard** | **str** | An optional content-guard. | [optional] 
**hidden** | **bool** | Whether this distribution should be shown in the content app. | [optional] [default to False]
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name. Ex, &#x60;rawhide&#x60; and &#x60;stable&#x60;. | 
**repository** | **str** | The latest RepositoryVersion for this Repository will be served. | [optional] 
**publication** | **str** | Publication to be served | [optional] 
**generate_repo_config** | **bool** | An option specifying whether Pulp should generate *.repo files. | [optional] [default to False]

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_rpm_distribution import RpmRpmDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of RpmRpmDistribution from a JSON string
rpm_rpm_distribution_instance = RpmRpmDistribution.from_json(json)
# print the JSON string representation of the object
print(RpmRpmDistribution.to_json())

# convert the object into a dict
rpm_rpm_distribution_dict = rpm_rpm_distribution_instance.to_dict()
# create an instance of RpmRpmDistribution from a dict
rpm_rpm_distribution_from_dict = RpmRpmDistribution.from_dict(rpm_rpm_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


