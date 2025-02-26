# NestedOpenPGPSignatureResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** |  | [optional] 
**created** | **datetime** |  | 
**expiration_time** | **str** |  | [optional] 
**signers_user_id** | **str** |  | [optional] 
**key_expiration_time** | **str** |  | [optional] 
**expired** | **bool** |  | 
**key_expired** | **str** |  | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.nested_open_pgp_signature_response import NestedOpenPGPSignatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NestedOpenPGPSignatureResponse from a JSON string
nested_open_pgp_signature_response_instance = NestedOpenPGPSignatureResponse.from_json(json)
# print the JSON string representation of the object
print(NestedOpenPGPSignatureResponse.to_json())

# convert the object into a dict
nested_open_pgp_signature_response_dict = nested_open_pgp_signature_response_instance.to_dict()
# create an instance of NestedOpenPGPSignatureResponse from a dict
nested_open_pgp_signature_response_from_dict = NestedOpenPGPSignatureResponse.from_dict(nested_open_pgp_signature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


