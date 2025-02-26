# PulpExporter

Serializer for pulp exporters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the file system exporter. | 
**path** | **str** | File system directory to store exported tar.gzs. | 
**repositories** | **List[str]** |  | 
**last_export** | **str** | Last attempted export for this PulpExporter | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.pulp_exporter import PulpExporter

# TODO update the JSON string below
json = "{}"
# create an instance of PulpExporter from a JSON string
pulp_exporter_instance = PulpExporter.from_json(json)
# print the JSON string representation of the object
print(PulpExporter.to_json())

# convert the object into a dict
pulp_exporter_dict = pulp_exporter_instance.to_dict()
# create an instance of PulpExporter from a dict
pulp_exporter_from_dict = PulpExporter.from_dict(pulp_exporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


