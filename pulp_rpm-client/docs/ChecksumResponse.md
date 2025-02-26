# ChecksumResponse

Checksum serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | File path. | 
**checksum** | **str** | Checksum for the file. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.checksum_response import ChecksumResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksumResponse from a JSON string
checksum_response_instance = ChecksumResponse.from_json(json)
# print the JSON string representation of the object
print(ChecksumResponse.to_json())

# convert the object into a dict
checksum_response_dict = checksum_response_instance.to_dict()
# create an instance of ChecksumResponse from a dict
checksum_response_from_dict = ChecksumResponse.from_dict(checksum_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


