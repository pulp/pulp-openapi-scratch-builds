# PatchedserviceFeatureContentGuard

A serializer for FeatureContentGuard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name. | [optional] 
**description** | **str** | An optional description. | [optional] 
**header_name** | **str** |  | [optional] 
**jq_filter** | **str** |  | [optional] 
**features** | **List[str]** | The list of features required to access the content. | [optional] 

## Example

```python
from pulpcore.client.pulp_service.models.patchedservice_feature_content_guard import PatchedserviceFeatureContentGuard

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedserviceFeatureContentGuard from a JSON string
patchedservice_feature_content_guard_instance = PatchedserviceFeatureContentGuard.from_json(json)
# print the JSON string representation of the object
print(PatchedserviceFeatureContentGuard.to_json())

# convert the object into a dict
patchedservice_feature_content_guard_dict = patchedservice_feature_content_guard_instance.to_dict()
# create an instance of PatchedserviceFeatureContentGuard from a dict
patchedservice_feature_content_guard_from_dict = PatchedserviceFeatureContentGuard.from_dict(patchedservice_feature_content_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


