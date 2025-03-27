# ServiceFeatureContentGuardResponse

A serializer for FeatureContentGuard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | The unique name. | 
**description** | **str** | An optional description. | [optional] 
**header_name** | **str** |  | 
**jq_filter** | **str** |  | [optional] 
**features** | **List[str]** | The list of features required to access the content. | 

## Example

```python
from pulpcore.client.pulp_service.models.service_feature_content_guard_response import ServiceFeatureContentGuardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceFeatureContentGuardResponse from a JSON string
service_feature_content_guard_response_instance = ServiceFeatureContentGuardResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceFeatureContentGuardResponse.to_json())

# convert the object into a dict
service_feature_content_guard_response_dict = service_feature_content_guard_response_instance.to_dict()
# create an instance of ServiceFeatureContentGuardResponse from a dict
service_feature_content_guard_response_from_dict = ServiceFeatureContentGuardResponse.from_dict(service_feature_content_guard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


