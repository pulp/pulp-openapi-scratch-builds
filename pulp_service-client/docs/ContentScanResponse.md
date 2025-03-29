# ContentScanResponse

A serializer for package scan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo_version** | **str** | RepositoryVersion HREF with the packages to be checked. | [optional] 
**package_json** | **str** | package-lock.json file with the definition of dependencies to be checked. | [optional] 

## Example

```python
from pulpcore.client.pulp_service.models.content_scan_response import ContentScanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentScanResponse from a JSON string
content_scan_response_instance = ContentScanResponse.from_json(json)
# print the JSON string representation of the object
print(ContentScanResponse.to_json())

# convert the object into a dict
content_scan_response_dict = content_scan_response_instance.to_dict()
# create an instance of ContentScanResponse from a dict
content_scan_response_from_dict = ContentScanResponse.from_dict(content_scan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


