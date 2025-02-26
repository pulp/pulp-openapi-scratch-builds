# PatchedrpmRpmAlternateContentSource

Serializer for RPM alternate content source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Alternate Content Source. | [optional] 
**last_refreshed** | **datetime** | Date of last refresh of AlternateContentSource. | [optional] 
**paths** | **List[str]** | List of paths that will be appended to the Remote url when searching for content. | [optional] 
**remote** | **str** | The remote to provide alternate content source. | [optional] 

## Example

```python
from pulpcore.client.pulp_rpm.models.patchedrpm_rpm_alternate_content_source import PatchedrpmRpmAlternateContentSource

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedrpmRpmAlternateContentSource from a JSON string
patchedrpm_rpm_alternate_content_source_instance = PatchedrpmRpmAlternateContentSource.from_json(json)
# print the JSON string representation of the object
print(PatchedrpmRpmAlternateContentSource.to_json())

# convert the object into a dict
patchedrpm_rpm_alternate_content_source_dict = patchedrpm_rpm_alternate_content_source_instance.to_dict()
# create an instance of PatchedrpmRpmAlternateContentSource from a dict
patchedrpm_rpm_alternate_content_source_from_dict = PatchedrpmRpmAlternateContentSource.from_dict(patchedrpm_rpm_alternate_content_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


