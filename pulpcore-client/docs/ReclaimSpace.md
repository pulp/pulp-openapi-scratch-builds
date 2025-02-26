# ReclaimSpace

Serializer for reclaim disk space operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo_hrefs** | **List[object]** | Will reclaim space for the specified list of repos. Use [&#39;*&#39;] to specify all repos. | 
**repo_versions_keeplist** | **List[str]** | Will exclude repo versions from space reclaim. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.reclaim_space import ReclaimSpace

# TODO update the JSON string below
json = "{}"
# create an instance of ReclaimSpace from a JSON string
reclaim_space_instance = ReclaimSpace.from_json(json)
# print the JSON string representation of the object
print(ReclaimSpace.to_json())

# convert the object into a dict
reclaim_space_dict = reclaim_space_instance.to_dict()
# create an instance of ReclaimSpace from a dict
reclaim_space_from_dict = ReclaimSpace.from_dict(reclaim_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


