# PulpImporterResponse

Serializer for PulpImporters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | Unique name of the Importer. | 
**repo_mapping** | **Dict[str, str]** | Mapping of repo names in an export file to the repo names in Pulp. For example, if the export has a repo named &#39;foo&#39; and the repo to import content into was &#39;bar&#39;, the mapping would be \&quot;{&#39;foo&#39;: &#39;bar&#39;}\&quot;. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.pulp_importer_response import PulpImporterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PulpImporterResponse from a JSON string
pulp_importer_response_instance = PulpImporterResponse.from_json(json)
# print the JSON string representation of the object
print(PulpImporterResponse.to_json())

# convert the object into a dict
pulp_importer_response_dict = pulp_importer_response_instance.to_dict()
# create an instance of PulpImporterResponse from a dict
pulp_importer_response_from_dict = PulpImporterResponse.from_dict(pulp_importer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


