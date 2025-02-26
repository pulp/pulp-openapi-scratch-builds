# PaginatedImportResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ImportResponse]**](ImportResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_import_response_list import PaginatedImportResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedImportResponseList from a JSON string
paginated_import_response_list_instance = PaginatedImportResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedImportResponseList.to_json())

# convert the object into a dict
paginated_import_response_list_dict = paginated_import_response_list_instance.to_dict()
# create an instance of PaginatedImportResponseList from a dict
paginated_import_response_list_from_dict = PaginatedImportResponseList.from_dict(paginated_import_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


