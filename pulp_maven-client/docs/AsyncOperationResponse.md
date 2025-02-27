# AsyncOperationResponse

Serializer for asynchronous operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | **str** | The href of the task. | 

## Example

```python
from pulpcore.client.pulp_maven.models.async_operation_response import AsyncOperationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncOperationResponse from a JSON string
async_operation_response_instance = AsyncOperationResponse.from_json(json)
# print the JSON string representation of the object
print(AsyncOperationResponse.to_json())

# convert the object into a dict
async_operation_response_dict = async_operation_response_instance.to_dict()
# create an instance of AsyncOperationResponse from a dict
async_operation_response_from_dict = AsyncOperationResponse.from_dict(async_operation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


