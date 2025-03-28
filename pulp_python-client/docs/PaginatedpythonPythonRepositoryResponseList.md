# PaginatedpythonPythonRepositoryResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PythonPythonRepositoryResponse]**](PythonPythonRepositoryResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_python.models.paginatedpython_python_repository_response_list import PaginatedpythonPythonRepositoryResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedpythonPythonRepositoryResponseList from a JSON string
paginatedpython_python_repository_response_list_instance = PaginatedpythonPythonRepositoryResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedpythonPythonRepositoryResponseList.to_json())

# convert the object into a dict
paginatedpython_python_repository_response_list_dict = paginatedpython_python_repository_response_list_instance.to_dict()
# create an instance of PaginatedpythonPythonRepositoryResponseList from a dict
paginatedpython_python_repository_response_list_from_dict = PaginatedpythonPythonRepositoryResponseList.from_dict(paginatedpython_python_repository_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


