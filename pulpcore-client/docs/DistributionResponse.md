# DistributionResponse

The Serializer for the Distribution model.  The serializer deliberately omits the `publication` and `repository_version` field due to plugins typically requiring one or the other but not both.  To include the ``publication`` field, it is recommended plugins define the field::    publication = DetailRelatedField(       required=False,       help_text=_(\"Publication to be served\"),       view_name_pattern=r\"publications(-.*/.*)?-detail\",       queryset=models.Publication.objects.exclude(complete=False),       allow_null=True,   )  To include the ``repository_version`` field, it is recommended plugins define the field::    repository_version = RepositoryVersionRelatedField(       required=False, help_text=_(\"RepositoryVersion to be served\"), allow_null=True   )  Additionally, the serializer omits the ``remote`` field, which is used for pull-through caching feature and only by plugins which use publications. Plugins implementing a pull-through caching should define the field in their derived serializer class like this::    remote = DetailRelatedField(       required=False,       help_text=_('Remote that can be used to fetch content when using pull-through caching.'),       queryset=models.Remote.objects.all(),       allow_null=True   )

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**base_path** | **str** | The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \&quot;foo\&quot; and \&quot;foo/bar\&quot;) | 
**base_url** | **str** | The URL for accessing the publication as defined by this distribution. | [optional] [readonly] 
**content_guard** | **str** | An optional content-guard. | [optional] 
**no_content_change_since** | **str** | Timestamp since when the distributed content served by this distribution has not changed. If equals to &#x60;null&#x60;, no guarantee is provided about content changes. | [optional] [readonly] 
**hidden** | **bool** | Whether this distribution should be shown in the content app. | [optional] [default to False]
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**name** | **str** | A unique name. Ex, &#x60;rawhide&#x60; and &#x60;stable&#x60;. | 
**repository** | **str** | The latest RepositoryVersion for this Repository will be served. | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.distribution_response import DistributionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DistributionResponse from a JSON string
distribution_response_instance = DistributionResponse.from_json(json)
# print the JSON string representation of the object
print(DistributionResponse.to_json())

# convert the object into a dict
distribution_response_dict = distribution_response_instance.to_dict()
# create an instance of DistributionResponse from a dict
distribution_response_from_dict = DistributionResponse.from_dict(distribution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


