# StorageResponse

Serializer for information about the storage system

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of bytes | 
**used** | **int** | Number of bytes in use | 
**free** | **int** | Number of free bytes | 

## Example

```python
from pulpcore.client.pulpcore.models.storage_response import StorageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StorageResponse from a JSON string
storage_response_instance = StorageResponse.from_json(json)
# print the JSON string representation of the object
print(StorageResponse.to_json())

# convert the object into a dict
storage_response_dict = storage_response_instance.to_dict()
# create an instance of StorageResponse from a dict
storage_response_from_dict = StorageResponse.from_dict(storage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


