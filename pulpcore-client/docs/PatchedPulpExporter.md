# PatchedPulpExporter

Serializer for pulp exporters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the file system exporter. | [optional] 
**path** | **str** | File system directory to store exported tar.gzs. | [optional] 
**repositories** | **List[str]** |  | [optional] 
**last_export** | **str** | Last attempted export for this PulpExporter | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.patched_pulp_exporter import PatchedPulpExporter

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPulpExporter from a JSON string
patched_pulp_exporter_instance = PatchedPulpExporter.from_json(json)
# print the JSON string representation of the object
print(PatchedPulpExporter.to_json())

# convert the object into a dict
patched_pulp_exporter_dict = patched_pulp_exporter_instance.to_dict()
# create an instance of PatchedPulpExporter from a dict
patched_pulp_exporter_from_dict = PatchedPulpExporter.from_dict(patched_pulp_exporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


