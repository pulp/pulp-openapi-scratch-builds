# PaginatedArtifactResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ArtifactResponse]**](ArtifactResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_artifact_response_list import PaginatedArtifactResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedArtifactResponseList from a JSON string
paginated_artifact_response_list_instance = PaginatedArtifactResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedArtifactResponseList.to_json())

# convert the object into a dict
paginated_artifact_response_list_dict = paginated_artifact_response_list_instance.to_dict()
# create an instance of PaginatedArtifactResponseList from a dict
paginated_artifact_response_list_from_dict = PaginatedArtifactResponseList.from_dict(paginated_artifact_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


