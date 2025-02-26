# Purge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finished_before** | **datetime** | Purge tasks completed earlier than this timestamp. Format &#39;%Y-%m-%d[T%H:%M:%S]&#39; | [optional] 
**states** | [**List[StatesEnum]**](StatesEnum.md) | List of task-states to be purged. Only &#39;final&#39; states are allowed. | [optional] [default to ["completed"]]

## Example

```python
from pulpcore.client.pulpcore.models.purge import Purge

# TODO update the JSON string below
json = "{}"
# create an instance of Purge from a JSON string
purge_instance = Purge.from_json(json)
# print the JSON string representation of the object
print(Purge.to_json())

# convert the object into a dict
purge_dict = purge_instance.to_dict()
# create an instance of Purge from a dict
purge_from_dict = Purge.from_dict(purge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


