# PaginatedserviceFeatureContentGuardResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ServiceFeatureContentGuardResponse]**](ServiceFeatureContentGuardResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_service.models.paginatedservice_feature_content_guard_response_list import PaginatedserviceFeatureContentGuardResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedserviceFeatureContentGuardResponseList from a JSON string
paginatedservice_feature_content_guard_response_list_instance = PaginatedserviceFeatureContentGuardResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedserviceFeatureContentGuardResponseList.to_json())

# convert the object into a dict
paginatedservice_feature_content_guard_response_list_dict = paginatedservice_feature_content_guard_response_list_instance.to_dict()
# create an instance of PaginatedserviceFeatureContentGuardResponseList from a dict
paginatedservice_feature_content_guard_response_list_from_dict = PaginatedserviceFeatureContentGuardResponseList.from_dict(paginatedservice_feature_content_guard_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


