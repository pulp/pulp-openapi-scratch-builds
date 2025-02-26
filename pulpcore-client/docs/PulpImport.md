# PulpImport

Serializer for call to import into Pulp.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path to export that will be imported. | [optional] 
**toc** | **str** | Path to a table-of-contents file describing chunks to be validated, reassembled, and imported. | [optional] 
**create_repositories** | **bool** | If True, missing repositories will be automatically created during the import. | [optional] [default to False]

## Example

```python
from pulpcore.client.pulpcore.models.pulp_import import PulpImport

# TODO update the JSON string below
json = "{}"
# create an instance of PulpImport from a JSON string
pulp_import_instance = PulpImport.from_json(json)
# print the JSON string representation of the object
print(PulpImport.to_json())

# convert the object into a dict
pulp_import_dict = pulp_import_instance.to_dict()
# create an instance of PulpImport from a dict
pulp_import_from_dict = PulpImport.from_dict(pulp_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


