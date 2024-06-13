# OstreeOstreeRepository

A Serializer class for an OSTree repository.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_labels** | **dict(str, str)** |  | [optional] 
**name** | **str** | A unique name for this repository. | 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 
**compute_delta** | **bool** |  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


