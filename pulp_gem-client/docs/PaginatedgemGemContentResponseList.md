# PaginatedgemGemContentResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GemGemContentResponse]**](GemGemContentResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_gem.models.paginatedgem_gem_content_response_list import PaginatedgemGemContentResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedgemGemContentResponseList from a JSON string
paginatedgem_gem_content_response_list_instance = PaginatedgemGemContentResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedgemGemContentResponseList.to_json())

# convert the object into a dict
paginatedgem_gem_content_response_list_dict = paginatedgem_gem_content_response_list_instance.to_dict()
# create an instance of PaginatedgemGemContentResponseList from a dict
paginatedgem_gem_content_response_list_from_dict = PaginatedgemGemContentResponseList.from_dict(paginatedgem_gem_content_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


