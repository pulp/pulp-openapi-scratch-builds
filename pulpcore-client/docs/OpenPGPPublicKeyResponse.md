# OpenPGPPublicKeyResponse

A serializer for content types with no Artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**fingerprint** | **str** |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**user_ids** | [**List[NestedOpenPGPUserIDResponse]**](NestedOpenPGPUserIDResponse.md) |  | [optional] [readonly] 
**user_attributes** | [**List[NestedOpenPGPUserAttributeResponse]**](NestedOpenPGPUserAttributeResponse.md) |  | [optional] [readonly] 
**public_subkeys** | [**List[NestedOpenPGPPublicSubkeyResponse]**](NestedOpenPGPPublicSubkeyResponse.md) |  | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.open_pgp_public_key_response import OpenPGPPublicKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPGPPublicKeyResponse from a JSON string
open_pgp_public_key_response_instance = OpenPGPPublicKeyResponse.from_json(json)
# print the JSON string representation of the object
print(OpenPGPPublicKeyResponse.to_json())

# convert the object into a dict
open_pgp_public_key_response_dict = open_pgp_public_key_response_instance.to_dict()
# create an instance of OpenPGPPublicKeyResponse from a dict
open_pgp_public_key_response_from_dict = OpenPGPPublicKeyResponse.from_dict(open_pgp_public_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


