# HeaderContentGuardResponse

A serializer for HeaderContentGuard.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | The unique name. | 
**description** | **str** | An optional description. | [optional] 
**header_name** | **str** | The header name the guard will check on. | 
**header_value** | **str** | The value that will authorize the request. | 
**jq_filter** | **str** | A JQ syntax compatible filter. If jq_filter is not set, then the value willonly be Base64 decoded and checked as an explicit string match. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


