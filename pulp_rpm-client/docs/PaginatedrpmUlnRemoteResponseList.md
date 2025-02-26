# PaginatedrpmUlnRemoteResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RpmUlnRemoteResponse]**](RpmUlnRemoteResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.paginatedrpm_uln_remote_response_list import PaginatedrpmUlnRemoteResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedrpmUlnRemoteResponseList from a JSON string
paginatedrpm_uln_remote_response_list_instance = PaginatedrpmUlnRemoteResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedrpmUlnRemoteResponseList.to_json())

# convert the object into a dict
paginatedrpm_uln_remote_response_list_dict = paginatedrpm_uln_remote_response_list_instance.to_dict()
# create an instance of PaginatedrpmUlnRemoteResponseList from a dict
paginatedrpm_uln_remote_response_list_from_dict = PaginatedrpmUlnRemoteResponseList.from_dict(paginatedrpm_uln_remote_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


