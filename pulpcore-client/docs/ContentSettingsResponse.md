# ContentSettingsResponse

Serializer for information about content-app-settings for the pulp instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_origin** | **str** | The CONTENT_ORIGIN setting for this Pulp instance | [optional] 
**content_path_prefix** | **str** | The CONTENT_PATH_PREFIX setting for this Pulp instance | 

## Example

```python
from pulpcore.client.pulpcore.models.content_settings_response import ContentSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSettingsResponse from a JSON string
content_settings_response_instance = ContentSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(ContentSettingsResponse.to_json())

# convert the object into a dict
content_settings_response_dict = content_settings_response_instance.to_dict()
# create an instance of ContentSettingsResponse from a dict
content_settings_response_from_dict = ContentSettingsResponse.from_dict(content_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


