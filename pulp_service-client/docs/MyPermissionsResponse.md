# MyPermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **List[str]** |  | 

## Example

```python
from pulpcore.client.pulp_service.models.my_permissions_response import MyPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MyPermissionsResponse from a JSON string
my_permissions_response_instance = MyPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(MyPermissionsResponse.to_json())

# convert the object into a dict
my_permissions_response_dict = my_permissions_response_instance.to_dict()
# create an instance of MyPermissionsResponse from a dict
my_permissions_response_from_dict = MyPermissionsResponse.from_dict(my_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


