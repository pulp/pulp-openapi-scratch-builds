# PaginatedPublicationResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PublicationResponse]**](PublicationResponse.md) |  | 

## Example

```python
from pulpcore.client.pulpcore.models.paginated_publication_response_list import PaginatedPublicationResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPublicationResponseList from a JSON string
paginated_publication_response_list_instance = PaginatedPublicationResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPublicationResponseList.to_json())

# convert the object into a dict
paginated_publication_response_list_dict = paginated_publication_response_list_instance.to_dict()
# create an instance of PaginatedPublicationResponseList from a dict
paginated_publication_response_list_from_dict = PaginatedPublicationResponseList.from_dict(paginated_publication_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


