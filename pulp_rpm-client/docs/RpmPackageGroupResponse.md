# RpmPackageGroupResponse

PackageGroup serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**id** | **str** | PackageGroup id. | 
**default** | **bool** | PackageGroup default. | [optional] 
**user_visible** | **bool** | PackageGroup user visibility. | [optional] 
**display_order** | **int** | PackageGroup display order. | 
**name** | **str** | PackageGroup name. | 
**description** | **str** | PackageGroup description. | 
**packages** | **object** | PackageGroup package list. | 
**biarch_only** | **bool** | PackageGroup biarch only. | [optional] 
**desc_by_lang** | **object** | PackageGroup description by language. | 
**name_by_lang** | **object** | PackageGroup name by language. | 
**digest** | **str** | PackageGroup digest. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_package_group_response import RpmPackageGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmPackageGroupResponse from a JSON string
rpm_package_group_response_instance = RpmPackageGroupResponse.from_json(json)
# print the JSON string representation of the object
print(RpmPackageGroupResponse.to_json())

# convert the object into a dict
rpm_package_group_response_dict = rpm_package_group_response_instance.to_dict()
# create an instance of RpmPackageGroupResponse from a dict
rpm_package_group_response_from_dict = RpmPackageGroupResponse.from_dict(rpm_package_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


