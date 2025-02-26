# RpmModulemdDefaults

ModulemdDefaults serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | A URI of a repository the new content unit should be associated with. | [optional] 
**module** | **str** | Modulemd name. | 
**stream** | **str** | Modulemd default stream. | 
**profiles** | **object** | Default profiles for modulemd streams. | 
**snippet** | **str** | Modulemd default snippet | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_modulemd_defaults import RpmModulemdDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of RpmModulemdDefaults from a JSON string
rpm_modulemd_defaults_instance = RpmModulemdDefaults.from_json(json)
# print the JSON string representation of the object
print(RpmModulemdDefaults.to_json())

# convert the object into a dict
rpm_modulemd_defaults_dict = rpm_modulemd_defaults_instance.to_dict()
# create an instance of RpmModulemdDefaults from a dict
rpm_modulemd_defaults_from_dict = RpmModulemdDefaults.from_dict(rpm_modulemd_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


