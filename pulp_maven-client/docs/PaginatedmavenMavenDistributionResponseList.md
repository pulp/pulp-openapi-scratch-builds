# PaginatedmavenMavenDistributionResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MavenMavenDistributionResponse]**](MavenMavenDistributionResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_maven.models.paginatedmaven_maven_distribution_response_list import PaginatedmavenMavenDistributionResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedmavenMavenDistributionResponseList from a JSON string
paginatedmaven_maven_distribution_response_list_instance = PaginatedmavenMavenDistributionResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedmavenMavenDistributionResponseList.to_json())

# convert the object into a dict
paginatedmaven_maven_distribution_response_list_dict = paginatedmaven_maven_distribution_response_list_instance.to_dict()
# create an instance of PaginatedmavenMavenDistributionResponseList from a dict
paginatedmaven_maven_distribution_response_list_from_dict = PaginatedmavenMavenDistributionResponseList.from_dict(paginatedmaven_maven_distribution_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


