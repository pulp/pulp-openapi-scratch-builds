# PaginatedArtifactDistributionResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ArtifactDistributionResponse]**](ArtifactDistributionResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_artifact_distribution_response_list import PaginatedArtifactDistributionResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedArtifactDistributionResponseList from a JSON string
paginated_artifact_distribution_response_list_instance = PaginatedArtifactDistributionResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedArtifactDistributionResponseList.to_json())

# convert the object into a dict
paginated_artifact_distribution_response_list_dict = paginated_artifact_distribution_response_list_instance.to_dict()
# create an instance of PaginatedArtifactDistributionResponseList from a dict
paginated_artifact_distribution_response_list_from_dict = PaginatedArtifactDistributionResponseList.from_dict(paginated_artifact_distribution_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


