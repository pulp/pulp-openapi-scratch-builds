# PrunePackages

Serializer for prune-old-Packages operation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo_hrefs** | **list[str]** | Will prune old packages from the specified list of repos. Use [&#39;*&#39;] to specify all repos. Will prune based on the specified repositories&#39; latest_versions. | 
**keep_days** | **int** | Prune packages introduced *prior-to* this many days ago. Default is 14. A value of 0 implies &#39;keep latest package only.&#39; | [optional] [default to 14]
**dry_run** | **bool** | Determine what would-be-pruned and log the list of packages. Intended as a debugging aid. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


