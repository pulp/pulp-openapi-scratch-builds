# CompositeContentGuard

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name. | 
**description** | **str** | An optional description. | [optional] 
**guards** | **List[Optional[str]]** | List of ContentGuards to ask for access-permission. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.composite_content_guard import CompositeContentGuard

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeContentGuard from a JSON string
composite_content_guard_instance = CompositeContentGuard.from_json(json)
# print the JSON string representation of the object
print(CompositeContentGuard.to_json())

# convert the object into a dict
composite_content_guard_dict = composite_content_guard_instance.to_dict()
# create an instance of CompositeContentGuard from a dict
composite_content_guard_from_dict = CompositeContentGuard.from_dict(composite_content_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


