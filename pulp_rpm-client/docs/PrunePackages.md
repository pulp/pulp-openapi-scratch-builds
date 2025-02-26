# PrunePackages

Serializer for prune-old-Packages operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo_hrefs** | **List[str]** | Will prune old packages from the specified list of repos. Use [&#39;*&#39;] to specify all repos. Will prune based on the specified repositories&#39; latest_versions. | 
**keep_days** | **int** | Prune packages introduced *prior-to* this many days ago. Default is 14. A value of 0 implies &#39;keep latest package only.&#39; | [optional] [default to 14]
**dry_run** | **bool** | Determine what would-be-pruned and log the list of packages. Intended as a debugging aid. | [optional] [default to False]

## Example

```python
from pulpcore.client.pulp_rpm.models.prune_packages import PrunePackages

# TODO update the JSON string below
json = "{}"
# create an instance of PrunePackages from a JSON string
prune_packages_instance = PrunePackages.from_json(json)
# print the JSON string representation of the object
print(PrunePackages.to_json())

# convert the object into a dict
prune_packages_dict = prune_packages_instance.to_dict()
# create an instance of PrunePackages from a dict
prune_packages_from_dict = PrunePackages.from_dict(prune_packages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


