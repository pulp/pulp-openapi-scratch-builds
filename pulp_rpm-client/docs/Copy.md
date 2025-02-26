# Copy

A serializer for Content Copy API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Content to be copied into the given destinations from the given sources.  Its a list of dictionaries with the following available fields:  &#x60;&#x60;&#x60;json [   {     \&quot;source_repo_version\&quot;: &lt;RepositoryVersion [pulp_href|prn]&gt;,     \&quot;dest_repo\&quot;: &lt;RpmRepository [pulp_href|prn]&gt;,     \&quot;dest_base_version\&quot;: &lt;int&gt;,     \&quot;content\&quot;: [&lt;Content [pulp_href|prn]&gt;, ...]   },   ... ] &#x60;&#x60;&#x60;  If domains are enabled, the refered pulp objects must be part of the current domain.  For usage examples, refer to the advanced copy guide: &lt;https://pulpproject.org/pulp_rpm/docs/user/guides/modify/#advanced-copy-workflow&gt;  | 
**dependency_solving** | **bool** | Also copy dependencies of the content being copied. | [optional] [default to True]

## Example

```python
from pulpcore.client.pulp_rpm.models.copy import Copy

# TODO update the JSON string below
json = "{}"
# create an instance of Copy from a JSON string
copy_instance = Copy.from_json(json)
# print the JSON string representation of the object
print(Copy.to_json())

# convert the object into a dict
copy_dict = copy_instance.to_dict()
# create an instance of Copy from a dict
copy_from_dict = Copy.from_dict(copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


