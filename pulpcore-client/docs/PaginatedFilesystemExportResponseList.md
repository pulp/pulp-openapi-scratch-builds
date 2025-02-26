# PaginatedFilesystemExportResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[FilesystemExportResponse]**](FilesystemExportResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_filesystem_export_response_list import PaginatedFilesystemExportResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFilesystemExportResponseList from a JSON string
paginated_filesystem_export_response_list_instance = PaginatedFilesystemExportResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFilesystemExportResponseList.to_json())

# convert the object into a dict
paginated_filesystem_export_response_list_dict = paginated_filesystem_export_response_list_instance.to_dict()
# create an instance of PaginatedFilesystemExportResponseList from a dict
paginated_filesystem_export_response_list_from_dict = PaginatedFilesystemExportResponseList.from_dict(paginated_filesystem_export_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


