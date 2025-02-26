# RBACContentGuard

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name. | 
**description** | **str** | An optional description. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.rbac_content_guard import RBACContentGuard

# TODO update the JSON string below
json = "{}"
# create an instance of RBACContentGuard from a JSON string
rbac_content_guard_instance = RBACContentGuard.from_json(json)
# print the JSON string representation of the object
print(RBACContentGuard.to_json())

# convert the object into a dict
rbac_content_guard_dict = rbac_content_guard_instance.to_dict()
# create an instance of RBACContentGuard from a dict
rbac_content_guard_from_dict = RBACContentGuard.from_dict(rbac_content_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


