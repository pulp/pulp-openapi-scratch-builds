# GemGemPublicationResponse

A Serializer for GemPublication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**repository_version** | **str** |  | [optional] 
**repository** | **str** | A URI of the repository to be published. | [optional] 

## Example

```python
from pulpcore.client.pulp_gem.models.gem_gem_publication_response import GemGemPublicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GemGemPublicationResponse from a JSON string
gem_gem_publication_response_instance = GemGemPublicationResponse.from_json(json)
# print the JSON string representation of the object
print(GemGemPublicationResponse.to_json())

# convert the object into a dict
gem_gem_publication_response_dict = gem_gem_publication_response_instance.to_dict()
# create an instance of GemGemPublicationResponse from a dict
gem_gem_publication_response_from_dict = GemGemPublicationResponse.from_dict(gem_gem_publication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


