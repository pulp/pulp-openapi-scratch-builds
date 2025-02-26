# RpmUpdateCollection

A Serializer for UpdateCollection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Collection name. | 
**shortname** | **str** | Collection short name. | 
**module** | **object** | Collection modular NSVCA. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_update_collection import RpmUpdateCollection

# TODO update the JSON string below
json = "{}"
# create an instance of RpmUpdateCollection from a JSON string
rpm_update_collection_instance = RpmUpdateCollection.from_json(json)
# print the JSON string representation of the object
print(RpmUpdateCollection.to_json())

# convert the object into a dict
rpm_update_collection_dict = rpm_update_collection_instance.to_dict()
# create an instance of RpmUpdateCollection from a dict
rpm_update_collection_from_dict = RpmUpdateCollection.from_dict(rpm_update_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


