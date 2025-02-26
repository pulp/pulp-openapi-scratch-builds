# AccessPolicyResponse

Serializer for AccessPolicy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**permissions_assignment** | **List[object]** | List of callables that define the new permissions to be created for new objects.This is deprecated. Use &#x60;creation_hooks&#x60; instead. | [optional] 
**creation_hooks** | **List[object]** | List of callables that may associate user roles for new objects. | [optional] 
**statements** | **List[object]** | List of policy statements defining the policy. | 
**viewset_name** | **str** | The name of ViewSet this AccessPolicy authorizes. | [optional] [readonly] 
**customized** | **bool** | True if the AccessPolicy has been user-modified. False otherwise. | [optional] [readonly] 
**queryset_scoping** | **object** | A callable for performing queryset scoping. See plugin documentation for valid callables. Set to blank to turn off queryset scoping. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.access_policy_response import AccessPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyResponse from a JSON string
access_policy_response_instance = AccessPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyResponse.to_json())

# convert the object into a dict
access_policy_response_dict = access_policy_response_instance.to_dict()
# create an instance of AccessPolicyResponse from a dict
access_policy_response_from_dict = AccessPolicyResponse.from_dict(access_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


