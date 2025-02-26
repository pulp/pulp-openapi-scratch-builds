# PatchedTaskCancel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The desired state of the task. Only &#39;canceled&#39; is accepted. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.patched_task_cancel import PatchedTaskCancel

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTaskCancel from a JSON string
patched_task_cancel_instance = PatchedTaskCancel.from_json(json)
# print the JSON string representation of the object
print(PatchedTaskCancel.to_json())

# convert the object into a dict
patched_task_cancel_dict = patched_task_cancel_instance.to_dict()
# create an instance of PatchedTaskCancel from a dict
patched_task_cancel_from_dict = PatchedTaskCancel.from_dict(patched_task_cancel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


