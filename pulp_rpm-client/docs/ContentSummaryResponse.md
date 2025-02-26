# ContentSummaryResponse

Serializer for the RepositoryVersion content summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | **Dict[str, object]** |  | 
**removed** | **Dict[str, object]** |  | 
**present** | **Dict[str, object]** |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.content_summary_response import ContentSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSummaryResponse from a JSON string
content_summary_response_instance = ContentSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(ContentSummaryResponse.to_json())

# convert the object into a dict
content_summary_response_dict = content_summary_response_instance.to_dict()
# create an instance of ContentSummaryResponse from a dict
content_summary_response_from_dict = ContentSummaryResponse.from_dict(content_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


