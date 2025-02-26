# ArtifactResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**file** | **str** | The stored file. | 
**size** | **int** | The size of the file in bytes. | [optional] 
**md5** | **str** | The MD5 checksum of the file if available. | [optional] 
**sha1** | **str** | The SHA-1 checksum of the file if available. | [optional] 
**sha224** | **str** | The SHA-224 checksum of the file if available. | [optional] 
**sha256** | **str** | The SHA-256 checksum of the file if available. | [optional] 
**sha384** | **str** | The SHA-384 checksum of the file if available. | [optional] 
**sha512** | **str** | The SHA-512 checksum of the file if available. | [optional] 

## Example

```python
from pulpcore.client.pulp_rpm.models.artifact_response import ArtifactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactResponse from a JSON string
artifact_response_instance = ArtifactResponse.from_json(json)
# print the JSON string representation of the object
print(ArtifactResponse.to_json())

# convert the object into a dict
artifact_response_dict = artifact_response_instance.to_dict()
# create an instance of ArtifactResponse from a dict
artifact_response_from_dict = ArtifactResponse.from_dict(artifact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


