# PackageUploadTaskResponse

A Serializer for responding to a package upload task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session** | **str** |  | 
**task** | **str** |  | 
**task_start_time** | **datetime** |  | 

## Example

```python
from pulpcore.client.pulp_python.models.package_upload_task_response import PackageUploadTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PackageUploadTaskResponse from a JSON string
package_upload_task_response_instance = PackageUploadTaskResponse.from_json(json)
# print the JSON string representation of the object
print(PackageUploadTaskResponse.to_json())

# convert the object into a dict
package_upload_task_response_dict = package_upload_task_response_instance.to_dict()
# create an instance of PackageUploadTaskResponse from a dict
package_upload_task_response_from_dict = PackageUploadTaskResponse.from_dict(package_upload_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


