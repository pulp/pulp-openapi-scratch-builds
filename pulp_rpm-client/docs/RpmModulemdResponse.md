# RpmModulemdResponse

Modulemd serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | Modulemd name. | 
**stream** | **str** | Stream name. | 
**version** | **str** | Modulemd version. | 
**static_context** | **bool** | Modulemd static-context flag. | [optional] 
**context** | **str** | Modulemd context. | 
**arch** | **str** | Modulemd architecture. | 
**artifacts** | **object** | Modulemd artifacts. | 
**dependencies** | **object** | Modulemd dependencies. | 
**packages** | **List[Optional[str]]** | Modulemd artifacts&#39; packages. | [optional] 
**profiles** | **object** | Modulemd profiles. | 
**description** | **str** | Description of module. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_modulemd_response import RpmModulemdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmModulemdResponse from a JSON string
rpm_modulemd_response_instance = RpmModulemdResponse.from_json(json)
# print the JSON string representation of the object
print(RpmModulemdResponse.to_json())

# convert the object into a dict
rpm_modulemd_response_dict = rpm_modulemd_response_instance.to_dict()
# create an instance of RpmModulemdResponse from a dict
rpm_modulemd_response_from_dict = RpmModulemdResponse.from_dict(rpm_modulemd_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


