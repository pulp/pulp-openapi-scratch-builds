# GroupRoleResponse

Serializer for GroupRole.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**role** | **str** |  | 
**content_object** | **str** | pulp_href of the object for which role permissions should be asserted. If set to &#39;null&#39;, permissions will act on the model-level. | 
**description** | **str** |  | [optional] [readonly] 
**permissions** | **list[str]** |  | [optional] [readonly] 
**domain** | **str** | Domain this role should be applied on, mutually exclusive with content_object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


