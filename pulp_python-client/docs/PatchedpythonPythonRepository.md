# PatchedpythonPythonRepository

Serializer for Python Repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name for this repository. | [optional] 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 
**autopublish** | **bool** | Whether to automatically create publications for new repository versions, and update any distributions pointing to this repository. | [optional] [default to False]

## Example

```python
from pulpcore.client.pulp_python.models.patchedpython_python_repository import PatchedpythonPythonRepository

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedpythonPythonRepository from a JSON string
patchedpython_python_repository_instance = PatchedpythonPythonRepository.from_json(json)
# print the JSON string representation of the object
print(PatchedpythonPythonRepository.to_json())

# convert the object into a dict
patchedpython_python_repository_dict = patchedpython_python_repository_instance.to_dict()
# create an instance of PatchedpythonPythonRepository from a dict
patchedpython_python_repository_from_dict = PatchedpythonPythonRepository.from_dict(patchedpython_python_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


