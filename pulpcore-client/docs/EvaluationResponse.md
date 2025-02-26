# EvaluationResponse

Results from evaluating a proposed parameter to a PulpImport call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | Parameter value being evaluated. | 
**is_valid** | **bool** | True if evaluation passed, false otherwise. | 
**messages** | **List[str]** | Messages describing results of all evaluations done. May be an empty list. | 

## Example

```python
from pulpcore.client.pulpcore.models.evaluation_response import EvaluationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationResponse from a JSON string
evaluation_response_instance = EvaluationResponse.from_json(json)
# print the JSON string representation of the object
print(EvaluationResponse.to_json())

# convert the object into a dict
evaluation_response_dict = evaluation_response_instance.to_dict()
# create an instance of EvaluationResponse from a dict
evaluation_response_from_dict = EvaluationResponse.from_dict(evaluation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


