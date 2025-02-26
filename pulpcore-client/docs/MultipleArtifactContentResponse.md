# MultipleArtifactContentResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**artifacts** | **object** | A dict mapping relative paths inside the Content to the correspondingArtifact URLs. E.g.: {&#39;relative/path&#39;: &#39;/artifacts/1/&#39; | 

## Example

```python
from pulpcore.client.pulpcore.models.multiple_artifact_content_response import MultipleArtifactContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleArtifactContentResponse from a JSON string
multiple_artifact_content_response_instance = MultipleArtifactContentResponse.from_json(json)
# print the JSON string representation of the object
print(MultipleArtifactContentResponse.to_json())

# convert the object into a dict
multiple_artifact_content_response_dict = multiple_artifact_content_response_instance.to_dict()
# create an instance of MultipleArtifactContentResponse from a dict
multiple_artifact_content_response_from_dict = MultipleArtifactContentResponse.from_dict(multiple_artifact_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


