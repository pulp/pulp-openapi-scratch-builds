# PythonPythonPackageContentResponse

A Serializer for PythonPackageContent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**pulp_labels** | **Dict[str, Optional[str]]** | A dictionary of arbitrary key/value pairs used to describe a specific Content instance. | [optional] 
**artifact** | **str** | Artifact file representing the physical content | [optional] 
**filename** | **str** | The name of the distribution package, usually of the format: {distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.{packagetype} | [optional] [readonly] 
**packagetype** | **str** | The type of the distribution package (e.g. sdist, bdist_wheel, bdist_egg, etc) | [optional] [readonly] 
**name** | **str** | The name of the python project. | [optional] [readonly] 
**version** | **str** | The packages version number. | [optional] [readonly] 
**sha256** | **str** | The SHA256 digest of this package. | [optional] [default to '']
**metadata_version** | **str** | Version of the file format | [optional] [readonly] 
**summary** | **str** | A one-line summary of what the package does. | [optional] 
**description** | **str** | A longer description of the package that can run to several paragraphs. | [optional] 
**description_content_type** | **str** | A string stating the markup syntax (if any) used in the distribution’s description, so that tools can intelligently render the description. | [optional] 
**keywords** | **str** | Additional keywords to be used to assist searching for the package in a larger catalog. | [optional] 
**home_page** | **str** | The URL for the package&#39;s home page. | [optional] 
**download_url** | **str** | Legacy field denoting the URL from which this package can be downloaded. | [optional] 
**author** | **str** | Text containing the author&#39;s name. Contact information can also be added, separated with newlines. | [optional] 
**author_email** | **str** | The author&#39;s e-mail address.  | [optional] 
**maintainer** | **str** | The maintainer&#39;s name at a minimum; additional contact information may be provided. | [optional] 
**maintainer_email** | **str** | The maintainer&#39;s e-mail address. | [optional] 
**license** | **str** | Text indicating the license covering the distribution | [optional] 
**requires_python** | **str** | The Python version(s) that the distribution is guaranteed to be compatible with. | [optional] 
**project_url** | **str** | A browsable URL for the project and a label for it, separated by a comma. | [optional] 
**project_urls** | **object** | A dictionary of labels and URLs for the project. | [optional] 
**platform** | **str** | A comma-separated list of platform specifications, summarizing the operating systems supported by the package. | [optional] 
**supported_platform** | **str** | Field to specify the OS and CPU for which the binary package was compiled.  | [optional] 
**requires_dist** | **object** | A JSON list containing names of some other distutils project required by this distribution. | [optional] 
**provides_dist** | **object** | A JSON list containing names of a Distutils project which is contained within this distribution. | [optional] 
**obsoletes_dist** | **object** | A JSON list containing names of a distutils project&#39;s distribution which this distribution renders obsolete, meaning that the two projects should not be installed at the same time. | [optional] 
**requires_external** | **object** | A JSON list containing some dependency in the system that the distribution is to be used. | [optional] 
**classifiers** | **object** | A JSON list containing classification values for a Python package. | [optional] 

## Example

```python
from pulpcore.client.pulp_python.models.python_python_package_content_response import PythonPythonPackageContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PythonPythonPackageContentResponse from a JSON string
python_python_package_content_response_instance = PythonPythonPackageContentResponse.from_json(json)
# print the JSON string representation of the object
print(PythonPythonPackageContentResponse.to_json())

# convert the object into a dict
python_python_package_content_response_dict = python_python_package_content_response_instance.to_dict()
# create an instance of PythonPythonPackageContentResponse from a dict
python_python_package_content_response_from_dict = PythonPythonPackageContentResponse.from_dict(python_python_package_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


