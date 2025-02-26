# PatchedPulpImporter

Serializer for PulpImporters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the Importer. | [optional] 
**repo_mapping** | **Dict[str, str]** | Mapping of repo names in an export file to the repo names in Pulp. For example, if the export has a repo named &#39;foo&#39; and the repo to import content into was &#39;bar&#39;, the mapping would be \&quot;{&#39;foo&#39;: &#39;bar&#39;}\&quot;. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.patched_pulp_importer import PatchedPulpImporter

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPulpImporter from a JSON string
patched_pulp_importer_instance = PatchedPulpImporter.from_json(json)
# print the JSON string representation of the object
print(PatchedPulpImporter.to_json())

# convert the object into a dict
patched_pulp_importer_dict = patched_pulp_importer_instance.to_dict()
# create an instance of PatchedPulpImporter from a dict
patched_pulp_importer_from_dict = PatchedPulpImporter.from_dict(patched_pulp_importer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


