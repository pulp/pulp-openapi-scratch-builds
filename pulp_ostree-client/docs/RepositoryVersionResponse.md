# RepositoryVersionResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**number** | **int** |  | [optional] [readonly] 
**repository** | **str** |  | [optional] [readonly] 
**base_version** | **str** | A repository version whose content was used as the initial set of content for this repository version | [optional] 
**content_summary** | [**ContentSummaryResponse**](ContentSummaryResponse.md) | Various count summaries of the content in the version and the HREF to view them. | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulp_ostree.models.repository_version_response import RepositoryVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryVersionResponse from a JSON string
repository_version_response_instance = RepositoryVersionResponse.from_json(json)
# print the JSON string representation of the object
print(RepositoryVersionResponse.to_json())

# convert the object into a dict
repository_version_response_dict = repository_version_response_instance.to_dict()
# create an instance of RepositoryVersionResponse from a dict
repository_version_response_from_dict = RepositoryVersionResponse.from_dict(repository_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


