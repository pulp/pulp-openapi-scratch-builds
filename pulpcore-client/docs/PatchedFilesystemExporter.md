# PatchedFilesystemExporter

Serializer for FilesystemExporters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the file system exporter. | [optional] 
**path** | **str** | File system location to export to. | [optional] 
**method** | [**MethodEnum**](MethodEnum.md) | Method of exporting  * &#x60;write&#x60; - Export by writing * &#x60;hardlink&#x60; - Export by hardlinking * &#x60;symlink&#x60; - Export by symlinking | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.patched_filesystem_exporter import PatchedFilesystemExporter

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFilesystemExporter from a JSON string
patched_filesystem_exporter_instance = PatchedFilesystemExporter.from_json(json)
# print the JSON string representation of the object
print(PatchedFilesystemExporter.to_json())

# convert the object into a dict
patched_filesystem_exporter_dict = patched_filesystem_exporter_instance.to_dict()
# create an instance of PatchedFilesystemExporter from a dict
patched_filesystem_exporter_from_dict = PatchedFilesystemExporter.from_dict(patched_filesystem_exporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


