# SummaryResponse

A Serializer for summary information of an index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | **int** | Number of Python projects in index | 
**releases** | **int** | Number of Python distribution releases in index | 
**files** | **int** | Number of files for all distributions in index | 

## Example

```python
from pulpcore.client.pulp_python.models.summary_response import SummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryResponse from a JSON string
summary_response_instance = SummaryResponse.from_json(json)
# print the JSON string representation of the object
print(SummaryResponse.to_json())

# convert the object into a dict
summary_response_dict = summary_response_instance.to_dict()
# create an instance of SummaryResponse from a dict
summary_response_from_dict = SummaryResponse.from_dict(summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


