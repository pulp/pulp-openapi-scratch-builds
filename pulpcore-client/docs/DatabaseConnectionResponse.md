# DatabaseConnectionResponse

Serializer for the database connection information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | **bool** | Info about whether the app can connect to the database | 

## Example

```python
from pulpcore.client.pulpcore.models.database_connection_response import DatabaseConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseConnectionResponse from a JSON string
database_connection_response_instance = DatabaseConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(DatabaseConnectionResponse.to_json())

# convert the object into a dict
database_connection_response_dict = database_connection_response_instance.to_dict()
# create an instance of DatabaseConnectionResponse from a dict
database_connection_response_from_dict = DatabaseConnectionResponse.from_dict(database_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


