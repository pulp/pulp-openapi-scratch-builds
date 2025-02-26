# RepositorySyncURL

A mixin for validating unknown serializers' fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote** | **str** | A remote to sync from. This will override a remote set on repository. | [optional] 
**mirror** | **bool** | If &#x60;&#x60;True&#x60;&#x60;, synchronization will remove all content that is not present in the remote repository. If &#x60;&#x60;False&#x60;&#x60;, sync will be additive only. | [optional] [default to False]

## Example

```python
from pulpcore.client.pulp_ostree.models.repository_sync_url import RepositorySyncURL

# TODO update the JSON string below
json = "{}"
# create an instance of RepositorySyncURL from a JSON string
repository_sync_url_instance = RepositorySyncURL.from_json(json)
# print the JSON string representation of the object
print(RepositorySyncURL.to_json())

# convert the object into a dict
repository_sync_url_dict = repository_sync_url_instance.to_dict()
# create an instance of RepositorySyncURL from a dict
repository_sync_url_from_dict = RepositorySyncURL.from_dict(repository_sync_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


