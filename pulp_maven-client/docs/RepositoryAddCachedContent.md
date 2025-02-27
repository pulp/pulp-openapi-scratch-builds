# RepositoryAddCachedContent

A mixin for validating unknown serializers' fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote** | **str** | A remote to use to identify content that was cached. This will override a remote set on repository. | [optional] 

## Example

```python
from pulpcore.client.pulp_maven.models.repository_add_cached_content import RepositoryAddCachedContent

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryAddCachedContent from a JSON string
repository_add_cached_content_instance = RepositoryAddCachedContent.from_json(json)
# print the JSON string representation of the object
print(RepositoryAddCachedContent.to_json())

# convert the object into a dict
repository_add_cached_content_dict = repository_add_cached_content_instance.to_dict()
# create an instance of RepositoryAddCachedContent from a dict
repository_add_cached_content_from_dict = RepositoryAddCachedContent.from_dict(repository_add_cached_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


