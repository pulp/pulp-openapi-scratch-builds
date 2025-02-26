# PatchedHeaderContentGuard

A serializer for HeaderContentGuard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name. | [optional] 
**description** | **str** | An optional description. | [optional] 
**header_name** | **str** | The header name the guard will check on. | [optional] 
**header_value** | **str** | The value that will authorize the request. | [optional] 
**jq_filter** | **str** | A JQ syntax compatible filter. If jq_filter is not set, then the value willonly be Base64 decoded and checked as an explicit string match. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.patched_header_content_guard import PatchedHeaderContentGuard

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedHeaderContentGuard from a JSON string
patched_header_content_guard_instance = PatchedHeaderContentGuard.from_json(json)
# print the JSON string representation of the object
print(PatchedHeaderContentGuard.to_json())

# convert the object into a dict
patched_header_content_guard_dict = patched_header_content_guard_instance.to_dict()
# create an instance of PatchedHeaderContentGuard from a dict
patched_header_content_guard_from_dict = PatchedHeaderContentGuard.from_dict(patched_header_content_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


