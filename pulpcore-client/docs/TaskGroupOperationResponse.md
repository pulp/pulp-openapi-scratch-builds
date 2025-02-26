# TaskGroupOperationResponse

Serializer for asynchronous operations that return a task group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_group** | **str** | The href of the task group. | 

## Example

```python
from pulpcore.client.pulpcore.models.task_group_operation_response import TaskGroupOperationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskGroupOperationResponse from a JSON string
task_group_operation_response_instance = TaskGroupOperationResponse.from_json(json)
# print the JSON string representation of the object
print(TaskGroupOperationResponse.to_json())

# convert the object into a dict
task_group_operation_response_dict = task_group_operation_response_instance.to_dict()
# create an instance of TaskGroupOperationResponse from a dict
task_group_operation_response_from_dict = TaskGroupOperationResponse.from_dict(task_group_operation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


