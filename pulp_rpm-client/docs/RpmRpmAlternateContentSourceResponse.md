# RpmRpmAlternateContentSourceResponse

Serializer for RPM alternate content source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | Name of Alternate Content Source. | 
**last_refreshed** | **datetime** | Date of last refresh of AlternateContentSource. | [optional] 
**paths** | **List[str]** | List of paths that will be appended to the Remote url when searching for content. | [optional] 
**remote** | **str** | The remote to provide alternate content source. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_rpm_alternate_content_source_response import RpmRpmAlternateContentSourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmRpmAlternateContentSourceResponse from a JSON string
rpm_rpm_alternate_content_source_response_instance = RpmRpmAlternateContentSourceResponse.from_json(json)
# print the JSON string representation of the object
print(RpmRpmAlternateContentSourceResponse.to_json())

# convert the object into a dict
rpm_rpm_alternate_content_source_response_dict = rpm_rpm_alternate_content_source_response_instance.to_dict()
# create an instance of RpmRpmAlternateContentSourceResponse from a dict
rpm_rpm_alternate_content_source_response_from_dict = RpmRpmAlternateContentSourceResponse.from_dict(rpm_rpm_alternate_content_source_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


