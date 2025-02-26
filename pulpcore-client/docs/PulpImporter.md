# PulpImporter

Serializer for PulpImporters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the Importer. | 
**repo_mapping** | **Dict[str, str]** | Mapping of repo names in an export file to the repo names in Pulp. For example, if the export has a repo named &#39;foo&#39; and the repo to import content into was &#39;bar&#39;, the mapping would be \&quot;{&#39;foo&#39;: &#39;bar&#39;}\&quot;. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.pulp_importer import PulpImporter

# TODO update the JSON string below
json = "{}"
# create an instance of PulpImporter from a JSON string
pulp_importer_instance = PulpImporter.from_json(json)
# print the JSON string representation of the object
print(PulpImporter.to_json())

# convert the object into a dict
pulp_importer_dict = pulp_importer_instance.to_dict()
# create an instance of PulpImporter from a dict
pulp_importer_from_dict = PulpImporter.from_dict(pulp_importer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


