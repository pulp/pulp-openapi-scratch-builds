# PaginatedOpenPGPPublicSubkeyResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OpenPGPPublicSubkeyResponse]**](OpenPGPPublicSubkeyResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_open_pgp_public_subkey_response_list import PaginatedOpenPGPPublicSubkeyResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOpenPGPPublicSubkeyResponseList from a JSON string
paginated_open_pgp_public_subkey_response_list_instance = PaginatedOpenPGPPublicSubkeyResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOpenPGPPublicSubkeyResponseList.to_json())

# convert the object into a dict
paginated_open_pgp_public_subkey_response_list_dict = paginated_open_pgp_public_subkey_response_list_instance.to_dict()
# create an instance of PaginatedOpenPGPPublicSubkeyResponseList from a dict
paginated_open_pgp_public_subkey_response_list_from_dict = PaginatedOpenPGPPublicSubkeyResponseList.from_dict(paginated_open_pgp_public_subkey_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


