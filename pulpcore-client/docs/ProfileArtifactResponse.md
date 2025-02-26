# ProfileArtifactResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **Dict[str, str]** |  | 

## Example

```python
from pulpcore.client.pulpcore.models.profile_artifact_response import ProfileArtifactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileArtifactResponse from a JSON string
profile_artifact_response_instance = ProfileArtifactResponse.from_json(json)
# print the JSON string representation of the object
print(ProfileArtifactResponse.to_json())

# convert the object into a dict
profile_artifact_response_dict = profile_artifact_response_instance.to_dict()
# create an instance of ProfileArtifactResponse from a dict
profile_artifact_response_from_dict = ProfileArtifactResponse.from_dict(profile_artifact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


