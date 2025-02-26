# NestedOpenPGPUserID

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 

## Example

```python
from pulpcore.client.pulpcore.models.nested_open_pgp_user_id import NestedOpenPGPUserID

# TODO update the JSON string below
json = "{}"
# create an instance of NestedOpenPGPUserID from a JSON string
nested_open_pgp_user_id_instance = NestedOpenPGPUserID.from_json(json)
# print the JSON string representation of the object
print(NestedOpenPGPUserID.to_json())

# convert the object into a dict
nested_open_pgp_user_id_dict = nested_open_pgp_user_id_instance.to_dict()
# create an instance of NestedOpenPGPUserID from a dict
nested_open_pgp_user_id_from_dict = NestedOpenPGPUserID.from_dict(nested_open_pgp_user_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


