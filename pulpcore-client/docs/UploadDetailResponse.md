# UploadDetailResponse

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
**chunks** | [**List[UploadChunkResponse]**](UploadChunkResponse.md) |  | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.upload_detail_response import UploadDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadDetailResponse from a JSON string
upload_detail_response_instance = UploadDetailResponse.from_json(json)
# print the JSON string representation of the object
print(UploadDetailResponse.to_json())

# convert the object into a dict
upload_detail_response_dict = upload_detail_response_instance.to_dict()
# create an instance of UploadDetailResponse from a dict
upload_detail_response_from_dict = UploadDetailResponse.from_dict(upload_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


