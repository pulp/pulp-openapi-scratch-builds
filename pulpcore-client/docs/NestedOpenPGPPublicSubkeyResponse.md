# NestedOpenPGPPublicSubkeyResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprint** | **str** |  | 
**created** | **datetime** |  | 
**signatures** | [**List[NestedOpenPGPSignatureResponse]**](NestedOpenPGPSignatureResponse.md) |  | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.nested_open_pgp_public_subkey_response import NestedOpenPGPPublicSubkeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NestedOpenPGPPublicSubkeyResponse from a JSON string
nested_open_pgp_public_subkey_response_instance = NestedOpenPGPPublicSubkeyResponse.from_json(json)
# print the JSON string representation of the object
print(NestedOpenPGPPublicSubkeyResponse.to_json())

# convert the object into a dict
nested_open_pgp_public_subkey_response_dict = nested_open_pgp_public_subkey_response_instance.to_dict()
# create an instance of NestedOpenPGPPublicSubkeyResponse from a dict
nested_open_pgp_public_subkey_response_from_dict = NestedOpenPGPPublicSubkeyResponse.from_dict(nested_open_pgp_public_subkey_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


