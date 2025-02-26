# PatchedOpenPGPKeyring

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name for this repository. | [optional] 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.patched_open_pgp_keyring import PatchedOpenPGPKeyring

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedOpenPGPKeyring from a JSON string
patched_open_pgp_keyring_instance = PatchedOpenPGPKeyring.from_json(json)
# print the JSON string representation of the object
print(PatchedOpenPGPKeyring.to_json())

# convert the object into a dict
patched_open_pgp_keyring_dict = patched_open_pgp_keyring_instance.to_dict()
# create an instance of PatchedOpenPGPKeyring from a dict
patched_open_pgp_keyring_from_dict = PatchedOpenPGPKeyring.from_dict(patched_open_pgp_keyring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


