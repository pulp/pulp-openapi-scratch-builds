# PulpImportCheckResponse

Return the response to a PulpImport import-check call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**toc** | [**EvaluationResponse**](EvaluationResponse.md) | Evaluation of proposed &#39;toc&#39; file for PulpImport | [optional] 
**path** | [**EvaluationResponse**](EvaluationResponse.md) | Evaluation of proposed &#39;path&#39; file for PulpImport | [optional] 
**repo_mapping** | [**EvaluationResponse**](EvaluationResponse.md) | Evaluation of proposed &#39;repo_mapping&#39; file for PulpImport | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.pulp_import_check_response import PulpImportCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PulpImportCheckResponse from a JSON string
pulp_import_check_response_instance = PulpImportCheckResponse.from_json(json)
# print the JSON string representation of the object
print(PulpImportCheckResponse.to_json())

# convert the object into a dict
pulp_import_check_response_dict = pulp_import_check_response_instance.to_dict()
# create an instance of PulpImportCheckResponse from a dict
pulp_import_check_response_from_dict = PulpImportCheckResponse.from_dict(pulp_import_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


