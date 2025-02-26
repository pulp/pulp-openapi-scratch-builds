# RedisConnectionResponse

Serializer for information about the Redis connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | **bool** | Info about whether the app can connect to Redis | 

## Example

```python
from pulpcore.client.pulpcore.models.redis_connection_response import RedisConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RedisConnectionResponse from a JSON string
redis_connection_response_instance = RedisConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(RedisConnectionResponse.to_json())

# convert the object into a dict
redis_connection_response_dict = redis_connection_response_instance.to_dict()
# create an instance of RedisConnectionResponse from a dict
redis_connection_response_from_dict = RedisConnectionResponse.from_dict(redis_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


