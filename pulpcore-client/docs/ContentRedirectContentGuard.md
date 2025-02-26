# ContentRedirectContentGuard

A serializer for ContentRedirectContentGuard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name. | 
**description** | **str** | An optional description. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.content_redirect_content_guard import ContentRedirectContentGuard

# TODO update the JSON string below
json = "{}"
# create an instance of ContentRedirectContentGuard from a JSON string
content_redirect_content_guard_instance = ContentRedirectContentGuard.from_json(json)
# print the JSON string representation of the object
print(ContentRedirectContentGuard.to_json())

# convert the object into a dict
content_redirect_content_guard_dict = content_redirect_content_guard_instance.to_dict()
# create an instance of ContentRedirectContentGuard from a dict
content_redirect_content_guard_from_dict = ContentRedirectContentGuard.from_dict(content_redirect_content_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


