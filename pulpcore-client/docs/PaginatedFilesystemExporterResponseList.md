# PaginatedFilesystemExporterResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FilesystemExporterResponse]**](FilesystemExporterResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_filesystem_exporter_response_list import PaginatedFilesystemExporterResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFilesystemExporterResponseList from a JSON string
paginated_filesystem_exporter_response_list_instance = PaginatedFilesystemExporterResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFilesystemExporterResponseList.to_json())

# convert the object into a dict
paginated_filesystem_exporter_response_list_dict = paginated_filesystem_exporter_response_list_instance.to_dict()
# create an instance of PaginatedFilesystemExporterResponseList from a dict
paginated_filesystem_exporter_response_list_from_dict = PaginatedFilesystemExporterResponseList.from_dict(paginated_filesystem_exporter_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


