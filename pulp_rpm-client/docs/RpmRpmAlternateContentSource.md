# RpmRpmAlternateContentSource

Serializer for RPM alternate content source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Alternate Content Source. | 
**last_refreshed** | **datetime** | Date of last refresh of AlternateContentSource. | [optional] 
**paths** | **List[str]** | List of paths that will be appended to the Remote url when searching for content. | [optional] 
**remote** | **str** | The remote to provide alternate content source. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_rpm_alternate_content_source import RpmRpmAlternateContentSource

# TODO update the JSON string below
json = "{}"
# create an instance of RpmRpmAlternateContentSource from a JSON string
rpm_rpm_alternate_content_source_instance = RpmRpmAlternateContentSource.from_json(json)
# print the JSON string representation of the object
print(RpmRpmAlternateContentSource.to_json())

# convert the object into a dict
rpm_rpm_alternate_content_source_dict = rpm_rpm_alternate_content_source_instance.to_dict()
# create an instance of RpmRpmAlternateContentSource from a dict
rpm_rpm_alternate_content_source_from_dict = RpmRpmAlternateContentSource.from_dict(rpm_rpm_alternate_content_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


