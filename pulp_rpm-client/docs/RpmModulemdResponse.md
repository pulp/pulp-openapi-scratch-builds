# RpmModulemdResponse

Modulemd serializer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**name** | **str** | Modulemd name. | 
**stream** | **str** | Stream name. | 
**version** | **str** | Modulemd version. | 
**static_context** | **bool** | Modulemd static-context flag. | [optional] 
**context** | **str** | Modulemd context. | 
**arch** | **str** | Modulemd architecture. | 
**artifacts** | [**object**](.md) | Modulemd artifacts. | 
**dependencies** | [**object**](.md) | Modulemd dependencies. | 
**packages** | **list[str]** | Modulemd artifacts&#39; packages. | [optional] 
**profiles** | [**object**](.md) | Modulemd profiles. | 
**description** | **str** | Description of module. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


