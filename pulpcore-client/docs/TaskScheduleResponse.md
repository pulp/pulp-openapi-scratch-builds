# TaskScheduleResponse

Base serializer for use with :class:`pulpcore.app.models.Model`  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**name** | **str** | The name of the task schedule. | 
**task_name** | **str** | The name of the task to be scheduled. | 
**dispatch_interval** | **str** | Periodicity of the schedule. | 
**next_dispatch** | **datetime** | Timestamp of the next time the task will be dispatched. | [optional] [readonly] 
**last_task** | **str** | The last task dispatched by this schedule. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


