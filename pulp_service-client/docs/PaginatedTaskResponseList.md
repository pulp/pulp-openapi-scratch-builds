# PaginatedTaskResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TaskResponse]**](TaskResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_service.models.paginated_task_response_list import PaginatedTaskResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTaskResponseList from a JSON string
paginated_task_response_list_instance = PaginatedTaskResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTaskResponseList.to_json())

# convert the object into a dict
paginated_task_response_list_dict = paginated_task_response_list_instance.to_dict()
# create an instance of PaginatedTaskResponseList from a dict
paginated_task_response_list_from_dict = PaginatedTaskResponseList.from_dict(paginated_task_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


