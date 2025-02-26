# ContentAppStatusResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the worker. | [optional] [readonly] 
**last_heartbeat** | **datetime** | Timestamp of the last time the worker talked to the service. | [optional] [readonly] 
**versions** | **Dict[str, Optional[str]]** | Versions of the components installed. | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.content_app_status_response import ContentAppStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAppStatusResponse from a JSON string
content_app_status_response_instance = ContentAppStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ContentAppStatusResponse.to_json())

# convert the object into a dict
content_app_status_response_dict = content_app_status_response_instance.to_dict()
# create an instance of ContentAppStatusResponse from a dict
content_app_status_response_from_dict = ContentAppStatusResponse.from_dict(content_app_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


