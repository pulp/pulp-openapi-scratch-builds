# UploadChunkResponse

A mixin for validating unknown serializers' fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] [readonly] 
**size** | **int** |  | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.upload_chunk_response import UploadChunkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadChunkResponse from a JSON string
upload_chunk_response_instance = UploadChunkResponse.from_json(json)
# print the JSON string representation of the object
print(UploadChunkResponse.to_json())

# convert the object into a dict
upload_chunk_response_dict = upload_chunk_response_instance.to_dict()
# create an instance of UploadChunkResponse from a dict
upload_chunk_response_from_dict = UploadChunkResponse.from_dict(upload_chunk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


