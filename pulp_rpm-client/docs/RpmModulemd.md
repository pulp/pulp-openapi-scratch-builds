# RpmModulemd

Modulemd serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | A URI of a repository the new content unit should be associated with. | [optional] 
**name** | **str** | Modulemd name. | 
**stream** | **str** | Stream name. | 
**version** | **str** | Modulemd version. | 
**static_context** | **bool** | Modulemd static-context flag. | [optional] 
**context** | **str** | Modulemd context. | 
**arch** | **str** | Modulemd architecture. | 
**artifacts** | **object** | Modulemd artifacts. | 
**dependencies** | **object** | Modulemd dependencies. | 
**packages** | **List[Optional[str]]** | Modulemd artifacts&#39; packages. | [optional] 
**snippet** | **str** | Modulemd snippet | 
**profiles** | **object** | Modulemd profiles. | 
**description** | **str** | Description of module. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_modulemd import RpmModulemd

# TODO update the JSON string below
json = "{}"
# create an instance of RpmModulemd from a JSON string
rpm_modulemd_instance = RpmModulemd.from_json(json)
# print the JSON string representation of the object
print(RpmModulemd.to_json())

# convert the object into a dict
rpm_modulemd_dict = rpm_modulemd_instance.to_dict()
# create an instance of RpmModulemd from a dict
rpm_modulemd_from_dict = RpmModulemd.from_dict(rpm_modulemd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


