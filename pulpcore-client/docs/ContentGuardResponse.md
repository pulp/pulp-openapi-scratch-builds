# ContentGuardResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

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
from pulpcore.client.pulpcore.models.content_guard_response import ContentGuardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGuardResponse from a JSON string
content_guard_response_instance = ContentGuardResponse.from_json(json)
# print the JSON string representation of the object
print(ContentGuardResponse.to_json())

# convert the object into a dict
content_guard_response_dict = content_guard_response_instance.to_dict()
# create an instance of ContentGuardResponse from a dict
content_guard_response_from_dict = ContentGuardResponse.from_dict(content_guard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


