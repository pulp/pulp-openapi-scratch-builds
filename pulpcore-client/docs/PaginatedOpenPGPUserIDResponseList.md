# PaginatedOpenPGPUserIDResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OpenPGPUserIDResponse]**](OpenPGPUserIDResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_open_pgp_user_id_response_list import PaginatedOpenPGPUserIDResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOpenPGPUserIDResponseList from a JSON string
paginated_open_pgp_user_id_response_list_instance = PaginatedOpenPGPUserIDResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOpenPGPUserIDResponseList.to_json())

# convert the object into a dict
paginated_open_pgp_user_id_response_list_dict = paginated_open_pgp_user_id_response_list_instance.to_dict()
# create an instance of PaginatedOpenPGPUserIDResponseList from a dict
paginated_open_pgp_user_id_response_list_from_dict = PaginatedOpenPGPUserIDResponseList.from_dict(paginated_open_pgp_user_id_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


