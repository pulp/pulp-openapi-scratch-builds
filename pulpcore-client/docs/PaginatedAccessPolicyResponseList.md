# PaginatedAccessPolicyResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[AccessPolicyResponse]**](AccessPolicyResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_access_policy_response_list import PaginatedAccessPolicyResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAccessPolicyResponseList from a JSON string
paginated_access_policy_response_list_instance = PaginatedAccessPolicyResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAccessPolicyResponseList.to_json())

# convert the object into a dict
paginated_access_policy_response_list_dict = paginated_access_policy_response_list_instance.to_dict()
# create an instance of PaginatedAccessPolicyResponseList from a dict
paginated_access_policy_response_list_from_dict = PaginatedAccessPolicyResponseList.from_dict(paginated_access_policy_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


