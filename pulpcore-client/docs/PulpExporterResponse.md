# PulpExporterResponse

Serializer for pulp exporters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | Unique name of the file system exporter. | 
**path** | **str** | File system directory to store exported tar.gzs. | 
**repositories** | **List[str]** |  | 
**last_export** | **str** | Last attempted export for this PulpExporter | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.pulp_exporter_response import PulpExporterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PulpExporterResponse from a JSON string
pulp_exporter_response_instance = PulpExporterResponse.from_json(json)
# print the JSON string representation of the object
print(PulpExporterResponse.to_json())

# convert the object into a dict
pulp_exporter_response_dict = pulp_exporter_response_instance.to_dict()
# create an instance of PulpExporterResponse from a dict
pulp_exporter_response_from_dict = PulpExporterResponse.from_dict(pulp_exporter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


