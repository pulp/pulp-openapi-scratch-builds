# PaginatedrpmRpmDistributionResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RpmRpmDistributionResponse]**](RpmRpmDistributionResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.paginatedrpm_rpm_distribution_response_list import PaginatedrpmRpmDistributionResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedrpmRpmDistributionResponseList from a JSON string
paginatedrpm_rpm_distribution_response_list_instance = PaginatedrpmRpmDistributionResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedrpmRpmDistributionResponseList.to_json())

# convert the object into a dict
paginatedrpm_rpm_distribution_response_list_dict = paginatedrpm_rpm_distribution_response_list_instance.to_dict()
# create an instance of PaginatedrpmRpmDistributionResponseList from a dict
paginatedrpm_rpm_distribution_response_list_from_dict = PaginatedrpmRpmDistributionResponseList.from_dict(paginatedrpm_rpm_distribution_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


