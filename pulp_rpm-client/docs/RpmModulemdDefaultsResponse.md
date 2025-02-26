# RpmModulemdDefaultsResponse

ModulemdDefaults serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**module** | **str** | Modulemd name. | 
**stream** | **str** | Modulemd default stream. | 
**profiles** | **object** | Default profiles for modulemd streams. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_modulemd_defaults_response import RpmModulemdDefaultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmModulemdDefaultsResponse from a JSON string
rpm_modulemd_defaults_response_instance = RpmModulemdDefaultsResponse.from_json(json)
# print the JSON string representation of the object
print(RpmModulemdDefaultsResponse.to_json())

# convert the object into a dict
rpm_modulemd_defaults_response_dict = rpm_modulemd_defaults_response_instance.to_dict()
# create an instance of RpmModulemdDefaultsResponse from a dict
rpm_modulemd_defaults_response_from_dict = RpmModulemdDefaultsResponse.from_dict(rpm_modulemd_defaults_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


