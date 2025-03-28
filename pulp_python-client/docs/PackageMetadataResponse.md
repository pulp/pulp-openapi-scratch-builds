# PackageMetadataResponse

A Serializer for a package's metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_serial** | **int** | Cache value from last PyPI sync | 
**info** | **object** | Core metadata of the package | 
**releases** | **object** | List of all the releases of the package | 
**urls** | **object** |  | 

## Example

```python
from pulpcore.client.pulp_python.models.package_metadata_response import PackageMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PackageMetadataResponse from a JSON string
package_metadata_response_instance = PackageMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(PackageMetadataResponse.to_json())

# convert the object into a dict
package_metadata_response_dict = package_metadata_response_instance.to_dict()
# create an instance of PackageMetadataResponse from a dict
package_metadata_response_from_dict = PackageMetadataResponse.from_dict(package_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


