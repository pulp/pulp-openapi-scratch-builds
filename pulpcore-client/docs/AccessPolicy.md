# AccessPolicy

Serializer for AccessPolicy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions_assignment** | **List[object]** | List of callables that define the new permissions to be created for new objects.This is deprecated. Use &#x60;creation_hooks&#x60; instead. | [optional] 
**creation_hooks** | **List[object]** | List of callables that may associate user roles for new objects. | [optional] 
**statements** | **List[object]** | List of policy statements defining the policy. | 
**queryset_scoping** | **object** | A callable for performing queryset scoping. See plugin documentation for valid callables. Set to blank to turn off queryset scoping. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.access_policy import AccessPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicy from a JSON string
access_policy_instance = AccessPolicy.from_json(json)
# print the JSON string representation of the object
print(AccessPolicy.to_json())

# convert the object into a dict
access_policy_dict = access_policy_instance.to_dict()
# create an instance of AccessPolicy from a dict
access_policy_from_dict = AccessPolicy.from_dict(access_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


