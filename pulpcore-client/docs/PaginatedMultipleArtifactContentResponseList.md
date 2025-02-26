# PaginatedMultipleArtifactContentResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MultipleArtifactContentResponse]**](MultipleArtifactContentResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_multiple_artifact_content_response_list import PaginatedMultipleArtifactContentResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMultipleArtifactContentResponseList from a JSON string
paginated_multiple_artifact_content_response_list_instance = PaginatedMultipleArtifactContentResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMultipleArtifactContentResponseList.to_json())

# convert the object into a dict
paginated_multiple_artifact_content_response_list_dict = paginated_multiple_artifact_content_response_list_instance.to_dict()
# create an instance of PaginatedMultipleArtifactContentResponseList from a dict
paginated_multiple_artifact_content_response_list_from_dict = PaginatedMultipleArtifactContentResponseList.from_dict(paginated_multiple_artifact_content_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


