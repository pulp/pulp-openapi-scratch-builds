# PaginatedpythonPythonPublicationResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PythonPythonPublicationResponse]**](PythonPythonPublicationResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_python.models.paginatedpython_python_publication_response_list import PaginatedpythonPythonPublicationResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedpythonPythonPublicationResponseList from a JSON string
paginatedpython_python_publication_response_list_instance = PaginatedpythonPythonPublicationResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedpythonPythonPublicationResponseList.to_json())

# convert the object into a dict
paginatedpython_python_publication_response_list_dict = paginatedpython_python_publication_response_list_instance.to_dict()
# create an instance of PaginatedpythonPythonPublicationResponseList from a dict
paginatedpython_python_publication_response_list_from_dict = PaginatedpythonPythonPublicationResponseList.from_dict(paginatedpython_python_publication_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


