# PulpExport

Serializer for PulpExports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | **str** | A URI of the task that ran the Export. | [optional] 
**full** | **bool** | Do a Full (true) or Incremental (false) export. | [optional] [default to True]
**dry_run** | **bool** | Generate report on what would be exported and disk-space required. | [optional] [default to False]
**versions** | **List[str]** | List of explicit repo-version hrefs to export (replaces current_version). | [optional] 
**chunk_size** | **str** | Chunk export-tarfile into pieces of chunk_size bytes. Recognizes units of B/KB/MB/GB/TB. A chunk has a maximum size of 1TB. | [optional] 
**start_versions** | **List[str]** | List of explicit last-exported-repo-version hrefs (replaces last_export). | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.pulp_export import PulpExport

# TODO update the JSON string below
json = "{}"
# create an instance of PulpExport from a JSON string
pulp_export_instance = PulpExport.from_json(json)
# print the JSON string representation of the object
print(PulpExport.to_json())

# convert the object into a dict
pulp_export_dict = pulp_export_instance.to_dict()
# create an instance of PulpExport from a dict
pulp_export_from_dict = PulpExport.from_dict(pulp_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


