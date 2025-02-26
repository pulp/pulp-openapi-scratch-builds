# TaskResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**state** | **str** | The current state of the task. The possible values include: &#39;waiting&#39;, &#39;skipped&#39;, &#39;running&#39;, &#39;completed&#39;, &#39;failed&#39;, &#39;canceled&#39; and &#39;canceling&#39;. | [optional] [readonly] 
**name** | **str** | The name of task. | 
**logging_cid** | **str** | The logging correlation id associated with this task | 
**created_by** | **str** | User who dispatched this task. | [optional] [readonly] 
**unblocked_at** | **datetime** | Timestamp of when this task was identified ready for pickup. | [optional] [readonly] 
**started_at** | **datetime** | Timestamp of when this task started execution. | [optional] [readonly] 
**finished_at** | **datetime** | Timestamp of when this task stopped execution. | [optional] [readonly] 
**error** | **object** | A JSON Object of a fatal error encountered during the execution of this task. | [optional] [readonly] 
**worker** | **str** | The worker associated with this task. This field is empty if a worker is not yet assigned. | [optional] [readonly] 
**parent_task** | **str** | The parent task that spawned this task. | [optional] [readonly] 
**child_tasks** | **List[str]** | Any tasks spawned by this task. | [optional] [readonly] 
**task_group** | **str** | The task group that this task is a member of. | [optional] [readonly] 
**progress_reports** | [**List[ProgressReportResponse]**](ProgressReportResponse.md) |  | [optional] [readonly] 
**created_resources** | **List[str]** | Resources created by this task. | [optional] [readonly] 
**reserved_resources_record** | **List[str]** | A list of resources required by that task. | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.task_response import TaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResponse from a JSON string
task_response_instance = TaskResponse.from_json(json)
# print the JSON string representation of the object
print(TaskResponse.to_json())

# convert the object into a dict
task_response_dict = task_response_instance.to_dict()
# create an instance of TaskResponse from a dict
task_response_from_dict = TaskResponse.from_dict(task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


