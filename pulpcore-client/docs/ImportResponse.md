# ImportResponse

Serializer for Imports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**task** | **str** | A URI of the Task that ran the Import. | 
**params** | **object** | Any parameters that were used to create the import. | 

## Example

```python
from pulpcore.client.pulpcore.models.import_response import ImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportResponse from a JSON string
import_response_instance = ImportResponse.from_json(json)
# print the JSON string representation of the object
print(ImportResponse.to_json())

# convert the object into a dict
import_response_dict = import_response_instance.to_dict()
# create an instance of ImportResponse from a dict
import_response_from_dict = ImportResponse.from_dict(import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


