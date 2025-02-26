# GroupProgressReportResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message shown to the user for the group progress report. | [optional] [readonly] 
**code** | **str** | Identifies the type of group progress report&#39;. | [optional] [readonly] 
**total** | **int** | The total count of items. | [optional] [readonly] 
**done** | **int** | The count of items already processed. Defaults to 0. | [optional] [readonly] 
**suffix** | **str** | The suffix to be shown with the group progress report. | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.group_progress_report_response import GroupProgressReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupProgressReportResponse from a JSON string
group_progress_report_response_instance = GroupProgressReportResponse.from_json(json)
# print the JSON string representation of the object
print(GroupProgressReportResponse.to_json())

# convert the object into a dict
group_progress_report_response_dict = group_progress_report_response_instance.to_dict()
# create an instance of GroupProgressReportResponse from a dict
group_progress_report_response_from_dict = GroupProgressReportResponse.from_dict(group_progress_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


