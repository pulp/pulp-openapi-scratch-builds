# PulpExporterResponse

Serializer for pulp exporters.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**name** | **str** | Unique name of the file system exporter. | 
**path** | **str** | File system directory to store exported tar.gzs. | 
**repositories** | **list[str]** |  | 
**last_export** | **str** | Last attempted export for this PulpExporter | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


