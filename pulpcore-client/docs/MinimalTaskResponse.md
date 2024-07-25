# MinimalTaskResponse

Base serializer for use with :class:`pulpcore.app.models.Model`  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | The name of task. | 
**state** | **str** | The current state of the task. The possible values include: &#39;waiting&#39;, &#39;skipped&#39;, &#39;running&#39;, &#39;completed&#39;, &#39;failed&#39;, &#39;canceled&#39; and &#39;canceling&#39;. | [optional] [readonly] 
**unblocked_at** | **datetime** | Timestamp of when this task was identified ready for pickup. | [optional] [readonly] 
**started_at** | **datetime** | Timestamp of when this task started execution. | [optional] [readonly] 
**finished_at** | **datetime** | Timestamp of when this task stopped execution. | [optional] [readonly] 
**worker** | **str** | The worker associated with this task. This field is empty if a worker is not yet assigned. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


