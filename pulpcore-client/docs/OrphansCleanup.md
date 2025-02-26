# OrphansCleanup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_hrefs** | **List[object]** | Will delete specified content and associated Artifacts if they are orphans. | [optional] 
**orphan_protection_time** | **int** | The time in minutes for how long Pulp will hold orphan Content and Artifacts before they become candidates for deletion by this orphan cleanup task. This should ideally be longer than your longest running task otherwise any content created during that task could be cleaned up before the task finishes. If not specified, a default value is taken from the setting ORPHAN_PROTECTION_TIME. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.orphans_cleanup import OrphansCleanup

# TODO update the JSON string below
json = "{}"
# create an instance of OrphansCleanup from a JSON string
orphans_cleanup_instance = OrphansCleanup.from_json(json)
# print the JSON string representation of the object
print(OrphansCleanup.to_json())

# convert the object into a dict
orphans_cleanup_dict = orphans_cleanup_instance.to_dict()
# create an instance of OrphansCleanup from a dict
orphans_cleanup_from_dict = OrphansCleanup.from_dict(orphans_cleanup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


