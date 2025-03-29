# GemGemPublication

A Serializer for GemPublication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_version** | **str** |  | [optional] 
**repository** | **str** | A URI of the repository to be published. | [optional] 

## Example

```python
from pulpcore.client.pulp_gem.models.gem_gem_publication import GemGemPublication

# TODO update the JSON string below
json = "{}"
# create an instance of GemGemPublication from a JSON string
gem_gem_publication_instance = GemGemPublication.from_json(json)
# print the JSON string representation of the object
print(GemGemPublication.to_json())

# convert the object into a dict
gem_gem_publication_dict = gem_gem_publication_instance.to_dict()
# create an instance of GemGemPublication from a dict
gem_gem_publication_from_dict = GemGemPublication.from_dict(gem_gem_publication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


