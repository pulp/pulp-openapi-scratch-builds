# StatusResponse

Serializer for the status information of the app

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | [**List[VersionResponse]**](VersionResponse.md) | Version information of Pulp components | 
**online_workers** | [**List[WorkerResponse]**](WorkerResponse.md) | List of online workers known to the application. An online worker is actively heartbeating and can respond to new work. | 
**online_api_apps** | [**List[ApiAppStatusResponse]**](ApiAppStatusResponse.md) | List of online api apps known to the application. An online api app is actively heartbeating and can serve the rest api to clients. | 
**online_content_apps** | [**List[ContentAppStatusResponse]**](ContentAppStatusResponse.md) | List of online content apps known to the application. An online content app is actively heartbeating and can serve data to clients. | 
**database_connection** | [**DatabaseConnectionResponse**](DatabaseConnectionResponse.md) | Database connection information | 
**redis_connection** | [**RedisConnectionResponse**](RedisConnectionResponse.md) | Redis connection information | [optional] 
**storage** | [**StorageResponse**](StorageResponse.md) | Storage information | [optional] 
**content_settings** | [**ContentSettingsResponse**](ContentSettingsResponse.md) | Content-app settings | 
**domain_enabled** | **bool** | Is Domains enabled | 

## Example

```python
from pulpcore.client.pulpcore.models.status_response import StatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatusResponse from a JSON string
status_response_instance = StatusResponse.from_json(json)
# print the JSON string representation of the object
print(StatusResponse.to_json())

# convert the object into a dict
status_response_dict = status_response_instance.to_dict()
# create an instance of StatusResponse from a dict
status_response_from_dict = StatusResponse.from_dict(status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


