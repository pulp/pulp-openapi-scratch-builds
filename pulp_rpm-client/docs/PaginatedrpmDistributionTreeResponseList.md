# PaginatedrpmDistributionTreeResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RpmDistributionTreeResponse]**](RpmDistributionTreeResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.paginatedrpm_distribution_tree_response_list import PaginatedrpmDistributionTreeResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedrpmDistributionTreeResponseList from a JSON string
paginatedrpm_distribution_tree_response_list_instance = PaginatedrpmDistributionTreeResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedrpmDistributionTreeResponseList.to_json())

# convert the object into a dict
paginatedrpm_distribution_tree_response_list_dict = paginatedrpm_distribution_tree_response_list_instance.to_dict()
# create an instance of PaginatedrpmDistributionTreeResponseList from a dict
paginatedrpm_distribution_tree_response_list_from_dict = PaginatedrpmDistributionTreeResponseList.from_dict(paginatedrpm_distribution_tree_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


