# NestedOpenPGPPublicSubkey

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprint** | **str** |  | 
**created** | **datetime** |  | 

## Example

```python
from pulpcore.client.pulpcore.models.nested_open_pgp_public_subkey import NestedOpenPGPPublicSubkey

# TODO update the JSON string below
json = "{}"
# create an instance of NestedOpenPGPPublicSubkey from a JSON string
nested_open_pgp_public_subkey_instance = NestedOpenPGPPublicSubkey.from_json(json)
# print the JSON string representation of the object
print(NestedOpenPGPPublicSubkey.to_json())

# convert the object into a dict
nested_open_pgp_public_subkey_dict = nested_open_pgp_public_subkey_instance.to_dict()
# create an instance of NestedOpenPGPPublicSubkey from a dict
nested_open_pgp_public_subkey_from_dict = NestedOpenPGPPublicSubkey.from_dict(nested_open_pgp_public_subkey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


