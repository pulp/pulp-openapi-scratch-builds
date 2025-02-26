# RepositoryResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**versions_href** | **str** |  | [optional] [readonly] 
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**latest_version_href** | **str** |  | [optional] [readonly] 
**name** | **str** | A unique name for this repository. | 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.repository_response import RepositoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryResponse from a JSON string
repository_response_instance = RepositoryResponse.from_json(json)
# print the JSON string representation of the object
print(RepositoryResponse.to_json())

# convert the object into a dict
repository_response_dict = repository_response_instance.to_dict()
# create an instance of RepositoryResponse from a dict
repository_response_from_dict = RepositoryResponse.from_dict(repository_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


