# FilesystemExportResponse

Serializer for FilesystemExports.

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

## Example

```python
from pulpcore.client.pulpcore.models.filesystem_export_response import FilesystemExportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemExportResponse from a JSON string
filesystem_export_response_instance = FilesystemExportResponse.from_json(json)
# print the JSON string representation of the object
print(FilesystemExportResponse.to_json())

# convert the object into a dict
filesystem_export_response_dict = filesystem_export_response_instance.to_dict()
# create an instance of FilesystemExportResponse from a dict
filesystem_export_response_from_dict = FilesystemExportResponse.from_dict(filesystem_export_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


