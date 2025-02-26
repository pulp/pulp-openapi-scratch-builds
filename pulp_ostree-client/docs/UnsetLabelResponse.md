# UnsetLabelResponse

Serializer for synchronously setting a label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulp_ostree.models.unset_label_response import UnsetLabelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnsetLabelResponse from a JSON string
unset_label_response_instance = UnsetLabelResponse.from_json(json)
# print the JSON string representation of the object
print(UnsetLabelResponse.to_json())

# convert the object into a dict
unset_label_response_dict = unset_label_response_instance.to_dict()
# create an instance of UnsetLabelResponse from a dict
unset_label_response_from_dict = UnsetLabelResponse.from_dict(unset_label_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


