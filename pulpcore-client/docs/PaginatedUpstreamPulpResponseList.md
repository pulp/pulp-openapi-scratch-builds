# PaginatedUpstreamPulpResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UpstreamPulpResponse]**](UpstreamPulpResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_upstream_pulp_response_list import PaginatedUpstreamPulpResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUpstreamPulpResponseList from a JSON string
paginated_upstream_pulp_response_list_instance = PaginatedUpstreamPulpResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUpstreamPulpResponseList.to_json())

# convert the object into a dict
paginated_upstream_pulp_response_list_dict = paginated_upstream_pulp_response_list_instance.to_dict()
# create an instance of PaginatedUpstreamPulpResponseList from a dict
paginated_upstream_pulp_response_list_from_dict = PaginatedUpstreamPulpResponseList.from_dict(paginated_upstream_pulp_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


