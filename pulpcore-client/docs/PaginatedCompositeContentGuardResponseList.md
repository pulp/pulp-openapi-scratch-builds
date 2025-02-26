# PaginatedCompositeContentGuardResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[CompositeContentGuardResponse]**](CompositeContentGuardResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_composite_content_guard_response_list import PaginatedCompositeContentGuardResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCompositeContentGuardResponseList from a JSON string
paginated_composite_content_guard_response_list_instance = PaginatedCompositeContentGuardResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCompositeContentGuardResponseList.to_json())

# convert the object into a dict
paginated_composite_content_guard_response_list_dict = paginated_composite_content_guard_response_list_instance.to_dict()
# create an instance of PaginatedCompositeContentGuardResponseList from a dict
paginated_composite_content_guard_response_list_from_dict = PaginatedCompositeContentGuardResponseList.from_dict(paginated_composite_content_guard_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


