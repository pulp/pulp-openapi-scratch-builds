# SigningServiceResponse

A serializer for the model declaring a signing service.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | A unique name used to recognize a script. | 
**public_key** | **str** | The value of a public key used for the repository verification. | 
**pubkey_fingerprint** | **str** | The fingerprint of the public key. | 
**script** | **str** | An absolute path to a script which is going to be used for the signing. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


