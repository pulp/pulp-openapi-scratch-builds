# FilesystemExporter

Serializer for FilesystemExporters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the file system exporter. | 
**path** | **str** | File system location to export to. | 
**method** | [**MethodEnum**](MethodEnum.md) | Method of exporting  * &#x60;write&#x60; - Export by writing * &#x60;hardlink&#x60; - Export by hardlinking * &#x60;symlink&#x60; - Export by symlinking | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.filesystem_exporter import FilesystemExporter

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemExporter from a JSON string
filesystem_exporter_instance = FilesystemExporter.from_json(json)
# print the JSON string representation of the object
print(FilesystemExporter.to_json())

# convert the object into a dict
filesystem_exporter_dict = filesystem_exporter_instance.to_dict()
# create an instance of FilesystemExporter from a dict
filesystem_exporter_from_dict = FilesystemExporter.from_dict(filesystem_exporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


