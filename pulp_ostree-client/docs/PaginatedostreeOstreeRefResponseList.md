# PaginatedostreeOstreeRefResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OstreeOstreeRefResponse]**](OstreeOstreeRefResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_ostree.models.paginatedostree_ostree_ref_response_list import PaginatedostreeOstreeRefResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedostreeOstreeRefResponseList from a JSON string
paginatedostree_ostree_ref_response_list_instance = PaginatedostreeOstreeRefResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedostreeOstreeRefResponseList.to_json())

# convert the object into a dict
paginatedostree_ostree_ref_response_list_dict = paginatedostree_ostree_ref_response_list_instance.to_dict()
# create an instance of PaginatedostreeOstreeRefResponseList from a dict
paginatedostree_ostree_ref_response_list_from_dict = PaginatedostreeOstreeRefResponseList.from_dict(paginatedostree_ostree_ref_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


