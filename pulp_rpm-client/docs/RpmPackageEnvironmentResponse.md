# RpmPackageEnvironmentResponse

PackageEnvironment serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**id** | **str** | Environment id. | 
**name** | **str** | Environment name. | 
**description** | **str** | Environment description. | 
**display_order** | **int** | Environment display order. | 
**group_ids** | **object** | Environment group list. | 
**option_ids** | **object** | Environment option ids | 
**desc_by_lang** | **object** | Environment description by language. | 
**name_by_lang** | **object** | Environment name by language. | 
**digest** | **str** | Environment digest. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_package_environment_response import RpmPackageEnvironmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmPackageEnvironmentResponse from a JSON string
rpm_package_environment_response_instance = RpmPackageEnvironmentResponse.from_json(json)
# print the JSON string representation of the object
print(RpmPackageEnvironmentResponse.to_json())

# convert the object into a dict
rpm_package_environment_response_dict = rpm_package_environment_response_instance.to_dict()
# create an instance of RpmPackageEnvironmentResponse from a dict
rpm_package_environment_response_from_dict = RpmPackageEnvironmentResponse.from_dict(rpm_package_environment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


