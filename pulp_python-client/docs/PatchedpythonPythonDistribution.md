# PatchedpythonPythonDistribution

Serializer for Pulp distributions for the Python type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_path** | **str** | The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \&quot;foo\&quot; and \&quot;foo/bar\&quot;) | [optional] 
**content_guard** | **str** | An optional content-guard. | [optional] 
**hidden** | **bool** | Whether this distribution should be shown in the content app. | [optional] [default to False]
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name. Ex, &#x60;rawhide&#x60; and &#x60;stable&#x60;. | [optional] 
**repository** | **str** | The latest RepositoryVersion for this Repository will be served. | [optional] 
**publication** | **str** | Publication to be served | [optional] 
**allow_uploads** | **bool** | Allow packages to be uploaded to this index. | [optional] [default to True]
**remote** | **str** | Remote that can be used to fetch content when using pull-through caching. | [optional] 

## Example

```python
from pulpcore.client.pulp_python.models.patchedpython_python_distribution import PatchedpythonPythonDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedpythonPythonDistribution from a JSON string
patchedpython_python_distribution_instance = PatchedpythonPythonDistribution.from_json(json)
# print the JSON string representation of the object
print(PatchedpythonPythonDistribution.to_json())

# convert the object into a dict
patchedpython_python_distribution_dict = patchedpython_python_distribution_instance.to_dict()
# create an instance of PatchedpythonPythonDistribution from a dict
patchedpython_python_distribution_from_dict = PatchedpythonPythonDistribution.from_dict(patchedpython_python_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


