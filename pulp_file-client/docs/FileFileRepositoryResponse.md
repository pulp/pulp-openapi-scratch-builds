# FileFileRepositoryResponse

Serializer for File Repositories.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**versions_href** | **str** |  | [optional] [readonly] 
**pulp_labels** | **dict(str, str)** |  | [optional] 
**latest_version_href** | **str** |  | [optional] [readonly] 
**name** | **str** | A unique name for this repository. | 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 
**autopublish** | **bool** | Whether to automatically create publications for new repository versions, and update any distributions pointing to this repository. | [optional] [default to False]
**manifest** | **str** | Filename to use for manifest file containing metadata for all the files. | [optional] [default to 'PULP_MANIFEST']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


