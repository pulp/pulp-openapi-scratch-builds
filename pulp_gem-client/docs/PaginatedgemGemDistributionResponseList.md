# PaginatedgemGemDistributionResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GemGemDistributionResponse]**](GemGemDistributionResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_gem.models.paginatedgem_gem_distribution_response_list import PaginatedgemGemDistributionResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedgemGemDistributionResponseList from a JSON string
paginatedgem_gem_distribution_response_list_instance = PaginatedgemGemDistributionResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedgemGemDistributionResponseList.to_json())

# convert the object into a dict
paginatedgem_gem_distribution_response_list_dict = paginatedgem_gem_distribution_response_list_instance.to_dict()
# create an instance of PaginatedgemGemDistributionResponseList from a dict
paginatedgem_gem_distribution_response_list_from_dict = PaginatedgemGemDistributionResponseList.from_dict(paginatedgem_gem_distribution_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


