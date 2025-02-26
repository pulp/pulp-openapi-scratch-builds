# HeaderContentGuardResponse

A serializer for HeaderContentGuard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | The unique name. | 
**description** | **str** | An optional description. | [optional] 
**header_name** | **str** | The header name the guard will check on. | 
**header_value** | **str** | The value that will authorize the request. | 
**jq_filter** | **str** | A JQ syntax compatible filter. If jq_filter is not set, then the value willonly be Base64 decoded and checked as an explicit string match. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.header_content_guard_response import HeaderContentGuardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HeaderContentGuardResponse from a JSON string
header_content_guard_response_instance = HeaderContentGuardResponse.from_json(json)
# print the JSON string representation of the object
print(HeaderContentGuardResponse.to_json())

# convert the object into a dict
header_content_guard_response_dict = header_content_guard_response_instance.to_dict()
# create an instance of HeaderContentGuardResponse from a dict
header_content_guard_response_from_dict = HeaderContentGuardResponse.from_dict(header_content_guard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


