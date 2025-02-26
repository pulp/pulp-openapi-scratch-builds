# PaginatedostreeOstreeContentResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OstreeOstreeContentResponse]**](OstreeOstreeContentResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_ostree.models.paginatedostree_ostree_content_response_list import PaginatedostreeOstreeContentResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedostreeOstreeContentResponseList from a JSON string
paginatedostree_ostree_content_response_list_instance = PaginatedostreeOstreeContentResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedostreeOstreeContentResponseList.to_json())

# convert the object into a dict
paginatedostree_ostree_content_response_list_dict = paginatedostree_ostree_content_response_list_instance.to_dict()
# create an instance of PaginatedostreeOstreeContentResponseList from a dict
paginatedostree_ostree_content_response_list_from_dict = PaginatedostreeOstreeContentResponseList.from_dict(paginatedostree_ostree_content_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


