# PaginatedDistributionResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DistributionResponse]**](DistributionResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_distribution_response_list import PaginatedDistributionResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDistributionResponseList from a JSON string
paginated_distribution_response_list_instance = PaginatedDistributionResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDistributionResponseList.to_json())

# convert the object into a dict
paginated_distribution_response_list_dict = paginated_distribution_response_list_instance.to_dict()
# create an instance of PaginatedDistributionResponseList from a dict
paginated_distribution_response_list_from_dict = PaginatedDistributionResponseList.from_dict(paginated_distribution_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


