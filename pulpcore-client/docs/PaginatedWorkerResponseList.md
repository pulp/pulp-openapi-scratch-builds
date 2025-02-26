# PaginatedWorkerResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[WorkerResponse]**](WorkerResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_worker_response_list import PaginatedWorkerResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWorkerResponseList from a JSON string
paginated_worker_response_list_instance = PaginatedWorkerResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedWorkerResponseList.to_json())

# convert the object into a dict
paginated_worker_response_list_dict = paginated_worker_response_list_instance.to_dict()
# create an instance of PaginatedWorkerResponseList from a dict
paginated_worker_response_list_from_dict = PaginatedWorkerResponseList.from_dict(paginated_worker_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


