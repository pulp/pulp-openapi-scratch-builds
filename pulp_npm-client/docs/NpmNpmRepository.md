# NpmNpmRepository

A Serializer for NpmRepository.  Add any new fields if defined on NpmRepository. Similar to the example above, in PackageSerializer. Additional validators can be added to the parent validators list  For example::  class Meta:     validators = platform.RepositorySerializer.Meta.validators + [myValidator1, myValidator2]
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_labels** | **dict(str, str)** |  | [optional] 
**name** | **str** | A unique name for this repository. | 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


