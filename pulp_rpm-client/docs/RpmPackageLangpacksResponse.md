# RpmPackageLangpacksResponse

PackageLangpacks serializer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**matches** | [**object**](.md) | Langpacks matches. | 
**digest** | **str** | Langpacks digest. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


