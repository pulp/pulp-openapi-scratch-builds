# UploadCommit

A mixin for validating unknown serializers' fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha256** | **str** | The expected sha256 checksum for the file. | 

## Example

```python
from pulpcore.client.pulpcore.models.upload_commit import UploadCommit

# TODO update the JSON string below
json = "{}"
# create an instance of UploadCommit from a JSON string
upload_commit_instance = UploadCommit.from_json(json)
# print the JSON string representation of the object
print(UploadCommit.to_json())

# convert the object into a dict
upload_commit_dict = upload_commit_instance.to_dict()
# create an instance of UploadCommit from a dict
upload_commit_from_dict = UploadCommit.from_dict(upload_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


