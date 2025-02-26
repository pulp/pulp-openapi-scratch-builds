# PaginatedTaskScheduleResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TaskScheduleResponse]**](TaskScheduleResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_task_schedule_response_list import PaginatedTaskScheduleResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTaskScheduleResponseList from a JSON string
paginated_task_schedule_response_list_instance = PaginatedTaskScheduleResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTaskScheduleResponseList.to_json())

# convert the object into a dict
paginated_task_schedule_response_list_dict = paginated_task_schedule_response_list_instance.to_dict()
# create an instance of PaginatedTaskScheduleResponseList from a dict
paginated_task_schedule_response_list_from_dict = PaginatedTaskScheduleResponseList.from_dict(paginated_task_schedule_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


