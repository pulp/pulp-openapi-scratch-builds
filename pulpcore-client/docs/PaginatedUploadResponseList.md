# PaginatedUploadResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UploadResponse]**](UploadResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_upload_response_list import PaginatedUploadResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUploadResponseList from a JSON string
paginated_upload_response_list_instance = PaginatedUploadResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUploadResponseList.to_json())

# convert the object into a dict
paginated_upload_response_list_dict = paginated_upload_response_list_instance.to_dict()
# create an instance of PaginatedUploadResponseList from a dict
paginated_upload_response_list_from_dict = PaginatedUploadResponseList.from_dict(paginated_upload_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


