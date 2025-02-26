# PaginatedostreeOstreeRemoteResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OstreeOstreeRemoteResponse]**](OstreeOstreeRemoteResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_ostree.models.paginatedostree_ostree_remote_response_list import PaginatedostreeOstreeRemoteResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedostreeOstreeRemoteResponseList from a JSON string
paginatedostree_ostree_remote_response_list_instance = PaginatedostreeOstreeRemoteResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedostreeOstreeRemoteResponseList.to_json())

# convert the object into a dict
paginatedostree_ostree_remote_response_list_dict = paginatedostree_ostree_remote_response_list_instance.to_dict()
# create an instance of PaginatedostreeOstreeRemoteResponseList from a dict
paginatedostree_ostree_remote_response_list_from_dict = PaginatedostreeOstreeRemoteResponseList.from_dict(paginatedostree_ostree_remote_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


