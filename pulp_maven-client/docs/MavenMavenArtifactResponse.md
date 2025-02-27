# MavenMavenArtifactResponse

A Serializer for MavenArtifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**artifact** | **str** | Artifact file representing the physical content | 
**group_id** | **str** | Group Id of the artifact&#39;s package. | [optional] [readonly] 
**artifact_id** | **str** | Artifact Id of the artifact&#39;s package. | [optional] [readonly] 
**version** | **str** | Version of the artifact&#39;s package. | [optional] [readonly] 
**filename** | **str** | Filename of the artifact. | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulp_maven.models.maven_maven_artifact_response import MavenMavenArtifactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MavenMavenArtifactResponse from a JSON string
maven_maven_artifact_response_instance = MavenMavenArtifactResponse.from_json(json)
# print the JSON string representation of the object
print(MavenMavenArtifactResponse.to_json())

# convert the object into a dict
maven_maven_artifact_response_dict = maven_maven_artifact_response_instance.to_dict()
# create an instance of MavenMavenArtifactResponse from a dict
maven_maven_artifact_response_from_dict = MavenMavenArtifactResponse.from_dict(maven_maven_artifact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


