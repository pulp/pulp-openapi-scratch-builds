# PaginatedUserResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UserResponse]**](UserResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_user_response_list import PaginatedUserResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserResponseList from a JSON string
paginated_user_response_list_instance = PaginatedUserResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserResponseList.to_json())

# convert the object into a dict
paginated_user_response_list_dict = paginated_user_response_list_instance.to_dict()
# create an instance of PaginatedUserResponseList from a dict
paginated_user_response_list_from_dict = PaginatedUserResponseList.from_dict(paginated_user_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


