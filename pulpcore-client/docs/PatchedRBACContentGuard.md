# PatchedRBACContentGuard

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name. | [optional] 
**description** | **str** | An optional description. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.patched_rbac_content_guard import PatchedRBACContentGuard

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRBACContentGuard from a JSON string
patched_rbac_content_guard_instance = PatchedRBACContentGuard.from_json(json)
# print the JSON string representation of the object
print(PatchedRBACContentGuard.to_json())

# convert the object into a dict
patched_rbac_content_guard_dict = patched_rbac_content_guard_instance.to_dict()
# create an instance of PatchedRBACContentGuard from a dict
patched_rbac_content_guard_from_dict = PatchedRBACContentGuard.from_dict(patched_rbac_content_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


