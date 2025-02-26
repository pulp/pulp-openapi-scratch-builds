# PaginatedGroupResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GroupResponse]**](GroupResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_group_response_list import PaginatedGroupResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupResponseList from a JSON string
paginated_group_response_list_instance = PaginatedGroupResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGroupResponseList.to_json())

# convert the object into a dict
paginated_group_response_list_dict = paginated_group_response_list_instance.to_dict()
# create an instance of PaginatedGroupResponseList from a dict
paginated_group_response_list_from_dict = PaginatedGroupResponseList.from_dict(paginated_group_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


