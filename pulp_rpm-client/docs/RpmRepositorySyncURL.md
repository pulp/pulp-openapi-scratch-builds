# RpmRepositorySyncURL

Serializer for RPM Sync.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote** | **str** | A remote to sync from. This will override a remote set on repository. | [optional] 
**mirror** | **bool** | DEPRECATED: If &#x60;&#x60;True&#x60;&#x60;, &#x60;&#x60;sync_policy&#x60;&#x60; will default to &#39;mirror_complete&#39; instead of &#39;additive&#39;. | [optional] 
**sync_policy** | [**SyncPolicyEnum**](SyncPolicyEnum.md) | Options: &#39;additive&#39;, &#39;mirror_complete&#39;, &#39;mirror_content_only&#39;. Default: &#39;additive&#39;. Modifies how the sync is performed. &#39;mirror_complete&#39; will clone the original metadata and create an automatic publication from it, but comes with some limitations and does not work for certain repositories. &#39;mirror_content_only&#39; will change the repository contents to match the remote but the metadata will be regenerated and will not be bit-for-bit identical. &#39;additive&#39; will retain the existing contents of the repository and add the contents of the repository being synced.  * &#x60;additive&#x60; - additive * &#x60;mirror_complete&#x60; - mirror_complete * &#x60;mirror_content_only&#x60; - mirror_content_only | [optional] 
**skip_types** | [**List[SkipTypesEnum]**](SkipTypesEnum.md) | List of content types to skip during sync. | [optional] [default to []]
**optimize** | **bool** | Whether or not to optimize sync. | [optional] [default to True]

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_repository_sync_url import RpmRepositorySyncURL

# TODO update the JSON string below
json = "{}"
# create an instance of RpmRepositorySyncURL from a JSON string
rpm_repository_sync_url_instance = RpmRepositorySyncURL.from_json(json)
# print the JSON string representation of the object
print(RpmRepositorySyncURL.to_json())

# convert the object into a dict
rpm_repository_sync_url_dict = rpm_repository_sync_url_instance.to_dict()
# create an instance of RpmRepositorySyncURL from a dict
rpm_repository_sync_url_from_dict = RpmRepositorySyncURL.from_dict(rpm_repository_sync_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


