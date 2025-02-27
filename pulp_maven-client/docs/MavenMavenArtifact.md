# MavenMavenArtifact

A Serializer for MavenArtifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | A URI of a repository the new content unit should be associated with. | [optional] 
**artifact** | **str** | Artifact file representing the physical content | 
**relative_path** | **str** | Path where the artifact is located relative to distributions base_path | 

## Example

```python
from pulpcore.client.pulp_maven.models.maven_maven_artifact import MavenMavenArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of MavenMavenArtifact from a JSON string
maven_maven_artifact_instance = MavenMavenArtifact.from_json(json)
# print the JSON string representation of the object
print(MavenMavenArtifact.to_json())

# convert the object into a dict
maven_maven_artifact_dict = maven_maven_artifact_instance.to_dict()
# create an instance of MavenMavenArtifact from a dict
maven_maven_artifact_from_dict = MavenMavenArtifact.from_dict(maven_maven_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


