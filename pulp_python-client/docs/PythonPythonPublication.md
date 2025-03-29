# PythonPythonPublication

A Serializer for PythonPublication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_version** | **str** |  | [optional] 
**repository** | **str** | A URI of the repository to be published. | [optional] 

## Example

```python
from pulpcore.client.pulp_python.models.python_python_publication import PythonPythonPublication

# TODO update the JSON string below
json = "{}"
# create an instance of PythonPythonPublication from a JSON string
python_python_publication_instance = PythonPythonPublication.from_json(json)
# print the JSON string representation of the object
print(PythonPythonPublication.to_json())

# convert the object into a dict
python_python_publication_dict = python_python_publication_instance.to_dict()
# create an instance of PythonPythonPublication from a dict
python_python_publication_from_dict = PythonPythonPublication.from_dict(python_python_publication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


