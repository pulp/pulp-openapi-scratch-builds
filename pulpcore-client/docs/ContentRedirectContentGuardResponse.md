# ContentRedirectContentGuardResponse

A serializer for ContentRedirectContentGuard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | The unique name. | 
**description** | **str** | An optional description. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.content_redirect_content_guard_response import ContentRedirectContentGuardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentRedirectContentGuardResponse from a JSON string
content_redirect_content_guard_response_instance = ContentRedirectContentGuardResponse.from_json(json)
# print the JSON string representation of the object
print(ContentRedirectContentGuardResponse.to_json())

# convert the object into a dict
content_redirect_content_guard_response_dict = content_redirect_content_guard_response_instance.to_dict()
# create an instance of ContentRedirectContentGuardResponse from a dict
content_redirect_content_guard_response_from_dict = ContentRedirectContentGuardResponse.from_dict(content_redirect_content_guard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


