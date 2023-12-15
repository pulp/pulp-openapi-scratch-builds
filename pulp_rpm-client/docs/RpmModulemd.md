# RpmModulemd

Modulemd serializer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | A URI of a repository the new content unit should be associated with. | [optional] 
**name** | **str** | Modulemd name. | 
**stream** | **str** | Stream name. | 
**version** | **str** | Modulemd version. | 
**static_context** | **bool** | Modulemd static-context flag. | [optional] 
**context** | **str** | Modulemd context. | 
**arch** | **str** | Modulemd architecture. | 
**artifacts** | [**object**](.md) | Modulemd artifacts. | 
**dependencies** | [**object**](.md) | Modulemd dependencies. | 
**packages** | **list[str]** | Modulemd artifacts&#39; packages. | [optional] 
**snippet** | **str** | Modulemd snippet | 
**profiles** | [**object**](.md) | Modulemd profiles. | 
**description** | **str** | Description of module. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


