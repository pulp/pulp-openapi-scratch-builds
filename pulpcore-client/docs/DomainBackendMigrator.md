# DomainBackendMigrator

Special serializer for performing a storage backend migration on a Domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_class** | [**StorageClassEnum**](StorageClassEnum.md) | The new backend storage class to migrate to.  * &#x60;pulpcore.app.models.storage.FileSystem&#x60; - Use local filesystem as storage * &#x60;storages.backends.s3boto3.S3Boto3Storage&#x60; - Use Amazon S3 as storage * &#x60;storages.backends.azure_storage.AzureStorage&#x60; - Use Azure Blob as storage | 
**storage_settings** | **object** | The settings for the new storage class to migrate to. | 

## Example

```python
from pulpcore.client.pulpcore.models.domain_backend_migrator import DomainBackendMigrator

# TODO update the JSON string below
json = "{}"
# create an instance of DomainBackendMigrator from a JSON string
domain_backend_migrator_instance = DomainBackendMigrator.from_json(json)
# print the JSON string representation of the object
print(DomainBackendMigrator.to_json())

# convert the object into a dict
domain_backend_migrator_dict = domain_backend_migrator_instance.to_dict()
# create an instance of DomainBackendMigrator from a dict
domain_backend_migrator_from_dict = DomainBackendMigrator.from_dict(domain_backend_migrator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


