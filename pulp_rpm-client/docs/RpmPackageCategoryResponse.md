# RpmPackageCategoryResponse

PackageCategory serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**id** | **str** | Category id. | 
**name** | **str** | Category name. | 
**description** | **str** | Category description. | 
**display_order** | **int** | Category display order. | 
**group_ids** | **object** | Category group list. | 
**desc_by_lang** | **object** | Category description by language. | 
**name_by_lang** | **object** | Category name by language. | 
**digest** | **str** | Category digest. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_package_category_response import RpmPackageCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmPackageCategoryResponse from a JSON string
rpm_package_category_response_instance = RpmPackageCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(RpmPackageCategoryResponse.to_json())

# convert the object into a dict
rpm_package_category_response_dict = rpm_package_category_response_instance.to_dict()
# create an instance of RpmPackageCategoryResponse from a dict
rpm_package_category_response_from_dict = RpmPackageCategoryResponse.from_dict(rpm_package_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


