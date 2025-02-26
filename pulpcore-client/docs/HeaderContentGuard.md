# HeaderContentGuard

A serializer for HeaderContentGuard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name. | 
**description** | **str** | An optional description. | [optional] 
**header_name** | **str** | The header name the guard will check on. | 
**header_value** | **str** | The value that will authorize the request. | 
**jq_filter** | **str** | A JQ syntax compatible filter. If jq_filter is not set, then the value willonly be Base64 decoded and checked as an explicit string match. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.header_content_guard import HeaderContentGuard

# TODO update the JSON string below
json = "{}"
# create an instance of HeaderContentGuard from a JSON string
header_content_guard_instance = HeaderContentGuard.from_json(json)
# print the JSON string representation of the object
print(HeaderContentGuard.to_json())

# convert the object into a dict
header_content_guard_dict = header_content_guard_instance.to_dict()
# create an instance of HeaderContentGuard from a dict
header_content_guard_from_dict = HeaderContentGuard.from_dict(header_content_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


