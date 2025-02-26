# PaginatedPulpExportResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PulpExportResponse]**](PulpExportResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_pulp_export_response_list import PaginatedPulpExportResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPulpExportResponseList from a JSON string
paginated_pulp_export_response_list_instance = PaginatedPulpExportResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPulpExportResponseList.to_json())

# convert the object into a dict
paginated_pulp_export_response_list_dict = paginated_pulp_export_response_list_instance.to_dict()
# create an instance of PaginatedPulpExportResponseList from a dict
paginated_pulp_export_response_list_from_dict = PaginatedPulpExportResponseList.from_dict(paginated_pulp_export_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


