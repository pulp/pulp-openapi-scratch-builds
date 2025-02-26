# PaginatedHeaderContentGuardResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[HeaderContentGuardResponse]**](HeaderContentGuardResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_header_content_guard_response_list import PaginatedHeaderContentGuardResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedHeaderContentGuardResponseList from a JSON string
paginated_header_content_guard_response_list_instance = PaginatedHeaderContentGuardResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedHeaderContentGuardResponseList.to_json())

# convert the object into a dict
paginated_header_content_guard_response_list_dict = paginated_header_content_guard_response_list_instance.to_dict()
# create an instance of PaginatedHeaderContentGuardResponseList from a dict
paginated_header_content_guard_response_list_from_dict = PaginatedHeaderContentGuardResponseList.from_dict(paginated_header_content_guard_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


