# PaginatedContentGuardResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ContentGuardResponse]**](ContentGuardResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_content_guard_response_list import PaginatedContentGuardResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedContentGuardResponseList from a JSON string
paginated_content_guard_response_list_instance = PaginatedContentGuardResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedContentGuardResponseList.to_json())

# convert the object into a dict
paginated_content_guard_response_list_dict = paginated_content_guard_response_list_instance.to_dict()
# create an instance of PaginatedContentGuardResponseList from a dict
paginated_content_guard_response_list_from_dict = PaginatedContentGuardResponseList.from_dict(paginated_content_guard_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


