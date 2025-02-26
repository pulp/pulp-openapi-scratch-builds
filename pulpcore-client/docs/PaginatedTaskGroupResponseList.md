# PaginatedTaskGroupResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TaskGroupResponse]**](TaskGroupResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_task_group_response_list import PaginatedTaskGroupResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTaskGroupResponseList from a JSON string
paginated_task_group_response_list_instance = PaginatedTaskGroupResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTaskGroupResponseList.to_json())

# convert the object into a dict
paginated_task_group_response_list_dict = paginated_task_group_response_list_instance.to_dict()
# create an instance of PaginatedTaskGroupResponseList from a dict
paginated_task_group_response_list_from_dict = PaginatedTaskGroupResponseList.from_dict(paginated_task_group_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


