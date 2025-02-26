# PaginatedPulpExporterResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PulpExporterResponse]**](PulpExporterResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_pulp_exporter_response_list import PaginatedPulpExporterResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPulpExporterResponseList from a JSON string
paginated_pulp_exporter_response_list_instance = PaginatedPulpExporterResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPulpExporterResponseList.to_json())

# convert the object into a dict
paginated_pulp_exporter_response_list_dict = paginated_pulp_exporter_response_list_instance.to_dict()
# create an instance of PaginatedPulpExporterResponseList from a dict
paginated_pulp_exporter_response_list_from_dict = PaginatedPulpExporterResponseList.from_dict(paginated_pulp_exporter_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


