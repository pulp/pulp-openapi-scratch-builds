# ProgressReportResponse

Base serializer for use with [pulpcore.app.models.Model][]  This ensures that all Serializers provide values for the 'pulp_href` field.  The class provides a default for the ``ref_name`` attribute in the ModelSerializers's ``Meta`` class. This ensures that the OpenAPI definitions of plugins are namespaced properly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message shown to the user for the progress report. | [optional] [readonly] 
**code** | **str** | Identifies the type of progress report&#39;. | [optional] [readonly] 
**state** | **str** | The current state of the progress report. The possible values are: &#39;waiting&#39;, &#39;skipped&#39;, &#39;running&#39;, &#39;completed&#39;, &#39;failed&#39;, &#39;canceled&#39; and &#39;canceling&#39;. The default is &#39;waiting&#39;. | [optional] [readonly] 
**total** | **int** | The total count of items. | [optional] [readonly] 
**done** | **int** | The count of items already processed. Defaults to 0. | [optional] [readonly] 
**suffix** | **str** | The suffix to be shown with the progress report. | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.progress_report_response import ProgressReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressReportResponse from a JSON string
progress_report_response_instance = ProgressReportResponse.from_json(json)
# print the JSON string representation of the object
print(ProgressReportResponse.to_json())

# convert the object into a dict
progress_report_response_dict = progress_report_response_instance.to_dict()
# create an instance of ProgressReportResponse from a dict
progress_report_response_from_dict = ProgressReportResponse.from_dict(progress_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


