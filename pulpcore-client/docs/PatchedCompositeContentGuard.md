# PatchedCompositeContentGuard

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name. | [optional] 
**description** | **str** | An optional description. | [optional] 
**guards** | **List[Optional[str]]** | List of ContentGuards to ask for access-permission. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.patched_composite_content_guard import PatchedCompositeContentGuard

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedCompositeContentGuard from a JSON string
patched_composite_content_guard_instance = PatchedCompositeContentGuard.from_json(json)
# print the JSON string representation of the object
print(PatchedCompositeContentGuard.to_json())

# convert the object into a dict
patched_composite_content_guard_dict = patched_composite_content_guard_instance.to_dict()
# create an instance of PatchedCompositeContentGuard from a dict
patched_composite_content_guard_from_dict = PatchedCompositeContentGuard.from_dict(patched_composite_content_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


