# PaginatedContentRedirectContentGuardResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ContentRedirectContentGuardResponse]**](ContentRedirectContentGuardResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_content_redirect_content_guard_response_list import PaginatedContentRedirectContentGuardResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedContentRedirectContentGuardResponseList from a JSON string
paginated_content_redirect_content_guard_response_list_instance = PaginatedContentRedirectContentGuardResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedContentRedirectContentGuardResponseList.to_json())

# convert the object into a dict
paginated_content_redirect_content_guard_response_list_dict = paginated_content_redirect_content_guard_response_list_instance.to_dict()
# create an instance of PaginatedContentRedirectContentGuardResponseList from a dict
paginated_content_redirect_content_guard_response_list_from_dict = PaginatedContentRedirectContentGuardResponseList.from_dict(paginated_content_redirect_content_guard_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


