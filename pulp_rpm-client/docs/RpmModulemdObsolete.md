# RpmModulemdObsolete

ModulemdObsolete serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | A URI of a repository the new content unit should be associated with. | [optional] 
**modified** | **str** | Obsolete modified time. | 
**module_name** | **str** | Modulemd name. | 
**module_stream** | **str** | Modulemd&#39;s stream. | 
**message** | **str** | Obsolete description. | 
**override_previous** | **str** | Reset previous obsoletes. | 
**module_context** | **str** | Modulemd&#39;s context. | 
**eol_date** | **str** | End of Life date. | 
**obsoleted_by_module_name** | **str** | Obsolete by module name. | 
**obsoleted_by_module_stream** | **str** | Obsolete by module stream. | 
**snippet** | **str** | Module Obsolete snippet. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_modulemd_obsolete import RpmModulemdObsolete

# TODO update the JSON string below
json = "{}"
# create an instance of RpmModulemdObsolete from a JSON string
rpm_modulemd_obsolete_instance = RpmModulemdObsolete.from_json(json)
# print the JSON string representation of the object
print(RpmModulemdObsolete.to_json())

# convert the object into a dict
rpm_modulemd_obsolete_dict = rpm_modulemd_obsolete_instance.to_dict()
# create an instance of RpmModulemdObsolete from a dict
rpm_modulemd_obsolete_from_dict = RpmModulemdObsolete.from_dict(rpm_modulemd_obsolete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


