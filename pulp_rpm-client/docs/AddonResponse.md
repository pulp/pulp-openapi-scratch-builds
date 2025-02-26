# AddonResponse

Addon serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_id** | **str** | Addon id. | 
**uid** | **str** | Addon uid. | 
**name** | **str** | Addon name. | 
**type** | **str** | Addon type. | 
**packages** | **str** | Relative path to directory with binary RPMs. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.addon_response import AddonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddonResponse from a JSON string
addon_response_instance = AddonResponse.from_json(json)
# print the JSON string representation of the object
print(AddonResponse.to_json())

# convert the object into a dict
addon_response_dict = addon_response_instance.to_dict()
# create an instance of AddonResponse from a dict
addon_response_from_dict = AddonResponse.from_dict(addon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


