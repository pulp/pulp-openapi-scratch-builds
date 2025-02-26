# PaginatedOpenPGPDistributionResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OpenPGPDistributionResponse]**](OpenPGPDistributionResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_open_pgp_distribution_response_list import PaginatedOpenPGPDistributionResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOpenPGPDistributionResponseList from a JSON string
paginated_open_pgp_distribution_response_list_instance = PaginatedOpenPGPDistributionResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOpenPGPDistributionResponseList.to_json())

# convert the object into a dict
paginated_open_pgp_distribution_response_list_dict = paginated_open_pgp_distribution_response_list_instance.to_dict()
# create an instance of PaginatedOpenPGPDistributionResponseList from a dict
paginated_open_pgp_distribution_response_list_from_dict = PaginatedOpenPGPDistributionResponseList.from_dict(paginated_open_pgp_distribution_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


