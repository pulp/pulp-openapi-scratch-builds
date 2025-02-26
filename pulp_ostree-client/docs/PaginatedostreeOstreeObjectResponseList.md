# PaginatedostreeOstreeObjectResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OstreeOstreeObjectResponse]**](OstreeOstreeObjectResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_ostree.models.paginatedostree_ostree_object_response_list import PaginatedostreeOstreeObjectResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedostreeOstreeObjectResponseList from a JSON string
paginatedostree_ostree_object_response_list_instance = PaginatedostreeOstreeObjectResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedostreeOstreeObjectResponseList.to_json())

# convert the object into a dict
paginatedostree_ostree_object_response_list_dict = paginatedostree_ostree_object_response_list_instance.to_dict()
# create an instance of PaginatedostreeOstreeObjectResponseList from a dict
paginatedostree_ostree_object_response_list_from_dict = PaginatedostreeOstreeObjectResponseList.from_dict(paginatedostree_ostree_object_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


