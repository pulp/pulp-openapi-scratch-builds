# PaginatedrpmRpmAlternateContentSourceResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RpmRpmAlternateContentSourceResponse]**](RpmRpmAlternateContentSourceResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.paginatedrpm_rpm_alternate_content_source_response_list import PaginatedrpmRpmAlternateContentSourceResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedrpmRpmAlternateContentSourceResponseList from a JSON string
paginatedrpm_rpm_alternate_content_source_response_list_instance = PaginatedrpmRpmAlternateContentSourceResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedrpmRpmAlternateContentSourceResponseList.to_json())

# convert the object into a dict
paginatedrpm_rpm_alternate_content_source_response_list_dict = paginatedrpm_rpm_alternate_content_source_response_list_instance.to_dict()
# create an instance of PaginatedrpmRpmAlternateContentSourceResponseList from a dict
paginatedrpm_rpm_alternate_content_source_response_list_from_dict = PaginatedrpmRpmAlternateContentSourceResponseList.from_dict(paginatedrpm_rpm_alternate_content_source_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


