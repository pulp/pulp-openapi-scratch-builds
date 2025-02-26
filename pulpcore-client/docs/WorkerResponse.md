# WorkerResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | The name of the worker. | [optional] [readonly] 
**last_heartbeat** | **datetime** | Timestamp of the last time the worker talked to the service. | [optional] [readonly] 
**versions** | **Dict[str, Optional[str]]** | Versions of the components installed. | [optional] [readonly] 
**current_task** | **str** | The task this worker is currently executing, or empty if the worker is not currently assigned to a task. | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.worker_response import WorkerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerResponse from a JSON string
worker_response_instance = WorkerResponse.from_json(json)
# print the JSON string representation of the object
print(WorkerResponse.to_json())

# convert the object into a dict
worker_response_dict = worker_response_instance.to_dict()
# create an instance of WorkerResponse from a dict
worker_response_from_dict = WorkerResponse.from_dict(worker_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


