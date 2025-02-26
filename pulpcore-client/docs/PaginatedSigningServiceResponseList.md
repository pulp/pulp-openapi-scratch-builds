# PaginatedSigningServiceResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SigningServiceResponse]**](SigningServiceResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_signing_service_response_list import PaginatedSigningServiceResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSigningServiceResponseList from a JSON string
paginated_signing_service_response_list_instance = PaginatedSigningServiceResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSigningServiceResponseList.to_json())

# convert the object into a dict
paginated_signing_service_response_list_dict = paginated_signing_service_response_list_instance.to_dict()
# create an instance of PaginatedSigningServiceResponseList from a dict
paginated_signing_service_response_list_from_dict = PaginatedSigningServiceResponseList.from_dict(paginated_signing_service_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


