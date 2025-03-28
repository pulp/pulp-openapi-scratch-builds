# PaginatedpythonPythonRemoteResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PythonPythonRemoteResponse]**](PythonPythonRemoteResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_python.models.paginatedpython_python_remote_response_list import PaginatedpythonPythonRemoteResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedpythonPythonRemoteResponseList from a JSON string
paginatedpython_python_remote_response_list_instance = PaginatedpythonPythonRemoteResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedpythonPythonRemoteResponseList.to_json())

# convert the object into a dict
paginatedpython_python_remote_response_list_dict = paginatedpython_python_remote_response_list_instance.to_dict()
# create an instance of PaginatedpythonPythonRemoteResponseList from a dict
paginatedpython_python_remote_response_list_from_dict = PaginatedpythonPythonRemoteResponseList.from_dict(paginatedpython_python_remote_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


