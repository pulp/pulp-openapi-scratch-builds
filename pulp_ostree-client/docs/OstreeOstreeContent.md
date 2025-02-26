# OstreeOstreeContent

A Serializer class for uncategorized content units (e.g., static deltas).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | A URI of a repository the new content unit should be associated with. | [optional] 
**artifact** | **str** | Artifact file representing the physical content | 
**relative_path** | **str** |  | 
**digest** | **str** |  | 

## Example

```python
from pulpcore.client.pulp_ostree.models.ostree_ostree_content import OstreeOstreeContent

# TODO update the JSON string below
json = "{}"
# create an instance of OstreeOstreeContent from a JSON string
ostree_ostree_content_instance = OstreeOstreeContent.from_json(json)
# print the JSON string representation of the object
print(OstreeOstreeContent.to_json())

# convert the object into a dict
ostree_ostree_content_dict = ostree_ostree_content_instance.to_dict()
# create an instance of OstreeOstreeContent from a dict
ostree_ostree_content_from_dict = OstreeOstreeContent.from_dict(ostree_ostree_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


