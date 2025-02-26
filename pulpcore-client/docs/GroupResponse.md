# GroupResponse

Serializer for Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.group_response import GroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupResponse from a JSON string
group_response_instance = GroupResponse.from_json(json)
# print the JSON string representation of the object
print(GroupResponse.to_json())

# convert the object into a dict
group_response_dict = group_response_instance.to_dict()
# create an instance of GroupResponse from a dict
group_response_from_dict = GroupResponse.from_dict(group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


