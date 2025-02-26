# RpmModulemdObsoleteResponse

ModulemdObsolete serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**modified** | **str** | Obsolete modified time. | 
**module_name** | **str** | Modulemd name. | 
**module_stream** | **str** | Modulemd&#39;s stream. | 
**message** | **str** | Obsolete description. | 
**override_previous** | **str** | Reset previous obsoletes. | 
**module_context** | **str** | Modulemd&#39;s context. | 
**eol_date** | **str** | End of Life date. | 
**obsoleted_by_module_name** | **str** | Obsolete by module name. | 
**obsoleted_by_module_stream** | **str** | Obsolete by module stream. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_modulemd_obsolete_response import RpmModulemdObsoleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmModulemdObsoleteResponse from a JSON string
rpm_modulemd_obsolete_response_instance = RpmModulemdObsoleteResponse.from_json(json)
# print the JSON string representation of the object
print(RpmModulemdObsoleteResponse.to_json())

# convert the object into a dict
rpm_modulemd_obsolete_response_dict = rpm_modulemd_obsolete_response_instance.to_dict()
# create an instance of RpmModulemdObsoleteResponse from a dict
rpm_modulemd_obsolete_response_from_dict = RpmModulemdObsoleteResponse.from_dict(rpm_modulemd_obsolete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


