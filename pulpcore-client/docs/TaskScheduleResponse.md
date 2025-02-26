# TaskScheduleResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | The name of the task schedule. | 
**task_name** | **str** | The name of the task to be scheduled. | 
**dispatch_interval** | **str** | Periodicity of the schedule. | 
**next_dispatch** | **datetime** | Timestamp of the next time the task will be dispatched. | [optional] [readonly] 
**last_task** | **str** | The last task dispatched by this schedule. | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.task_schedule_response import TaskScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskScheduleResponse from a JSON string
task_schedule_response_instance = TaskScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(TaskScheduleResponse.to_json())

# convert the object into a dict
task_schedule_response_dict = task_schedule_response_instance.to_dict()
# create an instance of TaskScheduleResponse from a dict
task_schedule_response_from_dict = TaskScheduleResponse.from_dict(task_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


