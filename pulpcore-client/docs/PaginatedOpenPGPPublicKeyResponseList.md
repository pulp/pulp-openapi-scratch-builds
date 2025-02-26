# PaginatedOpenPGPPublicKeyResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OpenPGPPublicKeyResponse]**](OpenPGPPublicKeyResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_open_pgp_public_key_response_list import PaginatedOpenPGPPublicKeyResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOpenPGPPublicKeyResponseList from a JSON string
paginated_open_pgp_public_key_response_list_instance = PaginatedOpenPGPPublicKeyResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOpenPGPPublicKeyResponseList.to_json())

# convert the object into a dict
paginated_open_pgp_public_key_response_list_dict = paginated_open_pgp_public_key_response_list_instance.to_dict()
# create an instance of PaginatedOpenPGPPublicKeyResponseList from a dict
paginated_open_pgp_public_key_response_list_from_dict = PaginatedOpenPGPPublicKeyResponseList.from_dict(paginated_open_pgp_public_key_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


