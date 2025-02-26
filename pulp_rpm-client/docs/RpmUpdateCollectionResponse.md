# RpmUpdateCollectionResponse

A Serializer for UpdateCollection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Collection name. | 
**shortname** | **str** | Collection short name. | 
**module** | **object** | Collection modular NSVCA. | 
**packages** | **List[object]** | List of packages | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_update_collection_response import RpmUpdateCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmUpdateCollectionResponse from a JSON string
rpm_update_collection_response_instance = RpmUpdateCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(RpmUpdateCollectionResponse.to_json())

# convert the object into a dict
rpm_update_collection_response_dict = rpm_update_collection_response_instance.to_dict()
# create an instance of RpmUpdateCollectionResponse from a dict
rpm_update_collection_response_from_dict = RpmUpdateCollectionResponse.from_dict(rpm_update_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


