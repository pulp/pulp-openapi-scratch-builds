# PatchedContentRedirectContentGuard

A serializer for ContentRedirectContentGuard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name. | [optional] 
**description** | **str** | An optional description. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.patched_content_redirect_content_guard import PatchedContentRedirectContentGuard

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedContentRedirectContentGuard from a JSON string
patched_content_redirect_content_guard_instance = PatchedContentRedirectContentGuard.from_json(json)
# print the JSON string representation of the object
print(PatchedContentRedirectContentGuard.to_json())

# convert the object into a dict
patched_content_redirect_content_guard_dict = patched_content_redirect_content_guard_instance.to_dict()
# create an instance of PatchedContentRedirectContentGuard from a dict
patched_content_redirect_content_guard_from_dict = PatchedContentRedirectContentGuard.from_dict(patched_content_redirect_content_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


