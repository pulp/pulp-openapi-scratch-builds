# FilesystemExport

Serializer for FilesystemExports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | **str** | A URI of the task that ran the Export. | [optional] 
**publication** | **str** | A URI of the publication to be exported. | [optional] 
**repository_version** | **str** | A URI of the repository version export. | [optional] 
**start_repository_version** | **str** | The URI of the last-exported-repo-version. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.filesystem_export import FilesystemExport

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemExport from a JSON string
filesystem_export_instance = FilesystemExport.from_json(json)
# print the JSON string representation of the object
print(FilesystemExport.to_json())

# convert the object into a dict
filesystem_export_dict = filesystem_export_instance.to_dict()
# create an instance of FilesystemExport from a dict
filesystem_export_from_dict = FilesystemExport.from_dict(filesystem_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


