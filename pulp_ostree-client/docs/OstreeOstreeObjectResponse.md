# OstreeOstreeObjectResponse

A Serializer class for OSTree objects (e.g., dirtree, dirmeta, file).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**artifact** | **str** | Artifact file representing the physical content | 
**relative_path** | **str** | Path where the artifact is located relative to distributions base_path | 
**checksum** | **str** |  | 
**typ** | **int** |              The type of an object. All values are described by the mapping declared at             https://lazka.github.io/pgi-docs/OSTree-1.0/enums.html#OSTree.ObjectType              | 

## Example

```python
from pulpcore.client.pulp_ostree.models.ostree_ostree_object_response import OstreeOstreeObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OstreeOstreeObjectResponse from a JSON string
ostree_ostree_object_response_instance = OstreeOstreeObjectResponse.from_json(json)
# print the JSON string representation of the object
print(OstreeOstreeObjectResponse.to_json())

# convert the object into a dict
ostree_ostree_object_response_dict = ostree_ostree_object_response_instance.to_dict()
# create an instance of OstreeOstreeObjectResponse from a dict
ostree_ostree_object_response_from_dict = OstreeOstreeObjectResponse.from_dict(ostree_ostree_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


