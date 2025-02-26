# PaginatedGenericRemoteResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GenericRemoteResponse]**](GenericRemoteResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_generic_remote_response_list import PaginatedGenericRemoteResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGenericRemoteResponseList from a JSON string
paginated_generic_remote_response_list_instance = PaginatedGenericRemoteResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGenericRemoteResponseList.to_json())

# convert the object into a dict
paginated_generic_remote_response_list_dict = paginated_generic_remote_response_list_instance.to_dict()
# create an instance of PaginatedGenericRemoteResponseList from a dict
paginated_generic_remote_response_list_from_dict = PaginatedGenericRemoteResponseList.from_dict(paginated_generic_remote_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


