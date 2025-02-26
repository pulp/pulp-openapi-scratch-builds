# FilesystemExporterResponse

Serializer for FilesystemExporters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | Unique name of the file system exporter. | 
**path** | **str** | File system location to export to. | 
**method** | [**MethodEnum**](MethodEnum.md) | Method of exporting  * &#x60;write&#x60; - Export by writing * &#x60;hardlink&#x60; - Export by hardlinking * &#x60;symlink&#x60; - Export by symlinking | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.filesystem_exporter_response import FilesystemExporterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemExporterResponse from a JSON string
filesystem_exporter_response_instance = FilesystemExporterResponse.from_json(json)
# print the JSON string representation of the object
print(FilesystemExporterResponse.to_json())

# convert the object into a dict
filesystem_exporter_response_dict = filesystem_exporter_response_instance.to_dict()
# create an instance of FilesystemExporterResponse from a dict
filesystem_exporter_response_from_dict = FilesystemExporterResponse.from_dict(filesystem_exporter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


