# Domain

Serializer for Domain.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for this domain. | 
**description** | **str** | An optional description. | [optional] 
**storage_class** | [**StorageClassEnum**](StorageClassEnum.md) | Backend storage class for domain.  * &#x60;pulpcore.app.models.storage.FileSystem&#x60; - Use local filesystem as storage * &#x60;storages.backends.s3boto3.S3Boto3Storage&#x60; - Use Amazon S3 as storage * &#x60;storages.backends.azure_storage.AzureStorage&#x60; - Use Azure Blob as storage | 
**storage_settings** | [**object**](.md) | Settings for storage class. | 
**redirect_to_object_storage** | **bool** | Boolean to have the content app redirect to object storage. | [optional] [default to True]
**hide_guarded_distributions** | **bool** | Boolean to hide distributions with a content guard in the content app. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


