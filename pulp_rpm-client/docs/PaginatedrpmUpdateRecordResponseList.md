# PaginatedrpmUpdateRecordResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RpmUpdateRecordResponse]**](RpmUpdateRecordResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.paginatedrpm_update_record_response_list import PaginatedrpmUpdateRecordResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedrpmUpdateRecordResponseList from a JSON string
paginatedrpm_update_record_response_list_instance = PaginatedrpmUpdateRecordResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedrpmUpdateRecordResponseList.to_json())

# convert the object into a dict
paginatedrpm_update_record_response_list_dict = paginatedrpm_update_record_response_list_instance.to_dict()
# create an instance of PaginatedrpmUpdateRecordResponseList from a dict
paginatedrpm_update_record_response_list_from_dict = PaginatedrpmUpdateRecordResponseList.from_dict(paginatedrpm_update_record_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


