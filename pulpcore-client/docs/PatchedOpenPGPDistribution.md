# PatchedOpenPGPDistribution

The Serializer for the Distribution model.  The serializer deliberately omits the `publication` and `repository_version` field due to plugins typically requiring one or the other but not both.  To include the ``publication`` field, it is recommended plugins define the field::    publication = DetailRelatedField(       required=False,       help_text=_(\"Publication to be served\"),       view_name_pattern=r\"publications(-.*/.*)?-detail\",       queryset=models.Publication.objects.exclude(complete=False),       allow_null=True,   )  To include the ``repository_version`` field, it is recommended plugins define the field::    repository_version = RepositoryVersionRelatedField(       required=False, help_text=_(\"RepositoryVersion to be served\"), allow_null=True   )  Additionally, the serializer omits the ``remote`` field, which is used for pull-through caching feature and only by plugins which use publications. Plugins implementing a pull-through caching should define the field in their derived serializer class like this::    remote = DetailRelatedField(       required=False,       help_text=_('Remote that can be used to fetch content when using pull-through caching.'),       queryset=models.Remote.objects.all(),       allow_null=True   )

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_path** | **str** | The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \&quot;foo\&quot; and \&quot;foo/bar\&quot;) | [optional] 
**content_guard** | **str** | An optional content-guard. | [optional] 
**hidden** | **bool** | Whether this distribution should be shown in the content app. | [optional] [default to False]
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name. Ex, &#x60;rawhide&#x60; and &#x60;stable&#x60;. | [optional] 
**repository** | **str** | The latest RepositoryVersion for this Repository will be served. | [optional] 
**repository_version** | **str** | RepositoryVersion to be served | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.patched_open_pgp_distribution import PatchedOpenPGPDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedOpenPGPDistribution from a JSON string
patched_open_pgp_distribution_instance = PatchedOpenPGPDistribution.from_json(json)
# print the JSON string representation of the object
print(PatchedOpenPGPDistribution.to_json())

# convert the object into a dict
patched_open_pgp_distribution_dict = patched_open_pgp_distribution_instance.to_dict()
# create an instance of PatchedOpenPGPDistribution from a dict
patched_open_pgp_distribution_from_dict = PatchedOpenPGPDistribution.from_dict(patched_open_pgp_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


