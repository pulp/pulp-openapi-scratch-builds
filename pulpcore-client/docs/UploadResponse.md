# UploadResponse

Serializer for chunked uploads.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**size** | **int** | The size of the upload in bytes. | 
**completed** | **datetime** | Timestamp when upload is committed. | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.upload_response import UploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadResponse from a JSON string
upload_response_instance = UploadResponse.from_json(json)
# print the JSON string representation of the object
print(UploadResponse.to_json())

# convert the object into a dict
upload_response_dict = upload_response_instance.to_dict()
# create an instance of UploadResponse from a dict
upload_response_from_dict = UploadResponse.from_dict(upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


