# PulpExportResponse

Serializer for PulpExports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**task** | **str** | A URI of the task that ran the Export. | [optional] 
**exported_resources** | **List[str]** | Resources that were exported. | [optional] [readonly] 
**params** | **object** | Any additional parameters that were used to create the export. | [optional] [readonly] 
**output_file_info** | **object** | Dictionary of filename: sha256hash entries for export-output-file(s) | [optional] [readonly] 
**toc_info** | **object** | Filename and sha256-checksum of table-of-contents for this export | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.pulp_export_response import PulpExportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PulpExportResponse from a JSON string
pulp_export_response_instance = PulpExportResponse.from_json(json)
# print the JSON string representation of the object
print(PulpExportResponse.to_json())

# convert the object into a dict
pulp_export_response_dict = pulp_export_response_instance.to_dict()
# create an instance of PulpExportResponse from a dict
pulp_export_response_from_dict = PulpExportResponse.from_dict(pulp_export_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


