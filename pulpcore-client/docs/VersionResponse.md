# VersionResponse

Serializer for the version information of Pulp components

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | Name of a versioned component of Pulp | 
**version** | **str** | Version of the component (e.g. 3.0.0) | 
**package** | **str** | Python package name providing the component | 
**module** | **str** | Python module name of the component | 
**domain_compatible** | **bool** | Domain feature compatibility of component | 

## Example

```python
from pulpcore.client.pulpcore.models.version_response import VersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VersionResponse from a JSON string
version_response_instance = VersionResponse.from_json(json)
# print the JSON string representation of the object
print(VersionResponse.to_json())

# convert the object into a dict
version_response_dict = version_response_instance.to_dict()
# create an instance of VersionResponse from a dict
version_response_from_dict = VersionResponse.from_dict(version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


