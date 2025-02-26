# DomainResponse

Serializer for Domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | A name for this domain. | 
**description** | **str** | An optional description. | [optional] 
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**storage_class** | [**StorageClassEnum**](StorageClassEnum.md) | Backend storage class for domain.  * &#x60;pulpcore.app.models.storage.FileSystem&#x60; - Use local filesystem as storage * &#x60;storages.backends.s3boto3.S3Boto3Storage&#x60; - Use Amazon S3 as storage * &#x60;storages.backends.azure_storage.AzureStorage&#x60; - Use Azure Blob as storage | 
**storage_settings** | **object** | Settings for storage class. | 
**redirect_to_object_storage** | **bool** | Boolean to have the content app redirect to object storage. | [optional] [default to True]
**hide_guarded_distributions** | **bool** | Boolean to hide distributions with a content guard in the content app. | [optional] [default to False]

## Example

```python
from pulpcore.client.pulpcore.models.domain_response import DomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResponse from a JSON string
domain_response_instance = DomainResponse.from_json(json)
# print the JSON string representation of the object
print(DomainResponse.to_json())

# convert the object into a dict
domain_response_dict = domain_response_instance.to_dict()
# create an instance of DomainResponse from a dict
domain_response_from_dict = DomainResponse.from_dict(domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


