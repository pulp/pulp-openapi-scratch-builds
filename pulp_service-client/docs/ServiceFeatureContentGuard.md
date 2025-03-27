# ServiceFeatureContentGuard

A serializer for FeatureContentGuard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name. | 
**description** | **str** | An optional description. | [optional] 
**header_name** | **str** |  | 
**jq_filter** | **str** |  | [optional] 
**features** | **List[str]** | The list of features required to access the content. | 

## Example

```python
from pulpcore.client.pulp_service.models.service_feature_content_guard import ServiceFeatureContentGuard

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceFeatureContentGuard from a JSON string
service_feature_content_guard_instance = ServiceFeatureContentGuard.from_json(json)
# print the JSON string representation of the object
print(ServiceFeatureContentGuard.to_json())

# convert the object into a dict
service_feature_content_guard_dict = service_feature_content_guard_instance.to_dict()
# create an instance of ServiceFeatureContentGuard from a dict
service_feature_content_guard_from_dict = ServiceFeatureContentGuard.from_dict(service_feature_content_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


