# pulpcore.client.pulpcore.ContentApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](ContentApi.md#list) | **GET** /pulp/api/v3/content/ | List content


# **list**
> PaginatedMultipleArtifactContentResponseList list(limit=limit, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_type=pulp_type, pulp_type__in=pulp_type__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, fields=fields, exclude_fields=exclude_fields)

List content

Endpoint to list all content.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulpcore.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:8080",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.ContentApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_type = 'pulp_type_example' # str | Pulp type  * `core.publishedmetadata` - core.publishedmetadata * `ansible.role` - ansible.role * `ansible.collection_version` - ansible.collection_version * `ansible.collection_mark` - ansible.collection_mark * `ansible.collection_signature` - ansible.collection_signature * `ansible.namespace` - ansible.namespace * `ansible.collection_deprecation` - ansible.collection_deprecation * `container.blob` - container.blob * `container.manifest` - container.manifest * `container.tag` - container.tag * `container.signature` - container.signature * `deb.package` - deb.package * `deb.installer_package` - deb.installer_package * `deb.generic` - deb.generic * `deb.source_package` - deb.source_package * `deb.release` - deb.release * `deb.release_architecture` - deb.release_architecture * `deb.release_component` - deb.release_component * `deb.package_release_component` - deb.package_release_component * `deb.source_package_release_component` - deb.source_package_release_component * `deb.release_file` - deb.release_file * `deb.package_index` - deb.package_index * `deb.installer_file_index` - deb.installer_file_index * `deb.source_index` - deb.source_index * `gem.gem` - gem.gem * `maven.artifact` - maven.artifact * `maven.metadata` - maven.metadata * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary * `python.python` - python.python * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `file.file` - file.file (optional)
pulp_type__in = ['pulp_type__in_example'] # list[str] | Multiple values may be separated by commas.  * `core.publishedmetadata` - core.publishedmetadata * `ansible.role` - ansible.role * `ansible.collection_version` - ansible.collection_version * `ansible.collection_mark` - ansible.collection_mark * `ansible.collection_signature` - ansible.collection_signature * `ansible.namespace` - ansible.namespace * `ansible.collection_deprecation` - ansible.collection_deprecation * `container.blob` - container.blob * `container.manifest` - container.manifest * `container.tag` - container.tag * `container.signature` - container.signature * `deb.package` - deb.package * `deb.installer_package` - deb.installer_package * `deb.generic` - deb.generic * `deb.source_package` - deb.source_package * `deb.release` - deb.release * `deb.release_architecture` - deb.release_architecture * `deb.release_component` - deb.release_component * `deb.package_release_component` - deb.package_release_component * `deb.source_package_release_component` - deb.source_package_release_component * `deb.release_file` - deb.release_file * `deb.package_index` - deb.package_index * `deb.installer_file_index` - deb.installer_file_index * `deb.source_index` - deb.source_index * `gem.gem` - gem.gem * `maven.artifact` - maven.artifact * `maven.metadata` - maven.metadata * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary * `python.python` - python.python * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `file.file` - file.file (optional)
q = 'q_example' # str |  (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List content
        api_response = api_instance.list(limit=limit, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_type=pulp_type, pulp_type__in=pulp_type__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentApi->list: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulpcore.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:8080",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.ContentApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_type = 'pulp_type_example' # str | Pulp type  * `core.publishedmetadata` - core.publishedmetadata * `ansible.role` - ansible.role * `ansible.collection_version` - ansible.collection_version * `ansible.collection_mark` - ansible.collection_mark * `ansible.collection_signature` - ansible.collection_signature * `ansible.namespace` - ansible.namespace * `ansible.collection_deprecation` - ansible.collection_deprecation * `container.blob` - container.blob * `container.manifest` - container.manifest * `container.tag` - container.tag * `container.signature` - container.signature * `deb.package` - deb.package * `deb.installer_package` - deb.installer_package * `deb.generic` - deb.generic * `deb.source_package` - deb.source_package * `deb.release` - deb.release * `deb.release_architecture` - deb.release_architecture * `deb.release_component` - deb.release_component * `deb.package_release_component` - deb.package_release_component * `deb.source_package_release_component` - deb.source_package_release_component * `deb.release_file` - deb.release_file * `deb.package_index` - deb.package_index * `deb.installer_file_index` - deb.installer_file_index * `deb.source_index` - deb.source_index * `gem.gem` - gem.gem * `maven.artifact` - maven.artifact * `maven.metadata` - maven.metadata * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary * `python.python` - python.python * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `file.file` - file.file (optional)
pulp_type__in = ['pulp_type__in_example'] # list[str] | Multiple values may be separated by commas.  * `core.publishedmetadata` - core.publishedmetadata * `ansible.role` - ansible.role * `ansible.collection_version` - ansible.collection_version * `ansible.collection_mark` - ansible.collection_mark * `ansible.collection_signature` - ansible.collection_signature * `ansible.namespace` - ansible.namespace * `ansible.collection_deprecation` - ansible.collection_deprecation * `container.blob` - container.blob * `container.manifest` - container.manifest * `container.tag` - container.tag * `container.signature` - container.signature * `deb.package` - deb.package * `deb.installer_package` - deb.installer_package * `deb.generic` - deb.generic * `deb.source_package` - deb.source_package * `deb.release` - deb.release * `deb.release_architecture` - deb.release_architecture * `deb.release_component` - deb.release_component * `deb.package_release_component` - deb.package_release_component * `deb.source_package_release_component` - deb.source_package_release_component * `deb.release_file` - deb.release_file * `deb.package_index` - deb.package_index * `deb.installer_file_index` - deb.installer_file_index * `deb.source_index` - deb.source_index * `gem.gem` - gem.gem * `maven.artifact` - maven.artifact * `maven.metadata` - maven.metadata * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary * `python.python` - python.python * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `file.file` - file.file (optional)
q = 'q_example' # str |  (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List content
        api_response = api_instance.list(limit=limit, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_type=pulp_type, pulp_type__in=pulp_type__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_type** | **str**| Pulp type  * &#x60;core.publishedmetadata&#x60; - core.publishedmetadata * &#x60;ansible.role&#x60; - ansible.role * &#x60;ansible.collection_version&#x60; - ansible.collection_version * &#x60;ansible.collection_mark&#x60; - ansible.collection_mark * &#x60;ansible.collection_signature&#x60; - ansible.collection_signature * &#x60;ansible.namespace&#x60; - ansible.namespace * &#x60;ansible.collection_deprecation&#x60; - ansible.collection_deprecation * &#x60;container.blob&#x60; - container.blob * &#x60;container.manifest&#x60; - container.manifest * &#x60;container.tag&#x60; - container.tag * &#x60;container.signature&#x60; - container.signature * &#x60;deb.package&#x60; - deb.package * &#x60;deb.installer_package&#x60; - deb.installer_package * &#x60;deb.generic&#x60; - deb.generic * &#x60;deb.source_package&#x60; - deb.source_package * &#x60;deb.release&#x60; - deb.release * &#x60;deb.release_architecture&#x60; - deb.release_architecture * &#x60;deb.release_component&#x60; - deb.release_component * &#x60;deb.package_release_component&#x60; - deb.package_release_component * &#x60;deb.source_package_release_component&#x60; - deb.source_package_release_component * &#x60;deb.release_file&#x60; - deb.release_file * &#x60;deb.package_index&#x60; - deb.package_index * &#x60;deb.installer_file_index&#x60; - deb.installer_file_index * &#x60;deb.source_index&#x60; - deb.source_index * &#x60;gem.gem&#x60; - gem.gem * &#x60;maven.artifact&#x60; - maven.artifact * &#x60;maven.metadata&#x60; - maven.metadata * &#x60;ostree.object&#x60; - ostree.object * &#x60;ostree.commit&#x60; - ostree.commit * &#x60;ostree.refs&#x60; - ostree.refs * &#x60;ostree.content&#x60; - ostree.content * &#x60;ostree.config&#x60; - ostree.config * &#x60;ostree.summary&#x60; - ostree.summary * &#x60;python.python&#x60; - python.python * &#x60;rpm.advisory&#x60; - rpm.advisory * &#x60;rpm.packagegroup&#x60; - rpm.packagegroup * &#x60;rpm.packagecategory&#x60; - rpm.packagecategory * &#x60;rpm.packageenvironment&#x60; - rpm.packageenvironment * &#x60;rpm.packagelangpacks&#x60; - rpm.packagelangpacks * &#x60;rpm.repo_metadata_file&#x60; - rpm.repo_metadata_file * &#x60;rpm.distribution_tree&#x60; - rpm.distribution_tree * &#x60;rpm.package&#x60; - rpm.package * &#x60;rpm.modulemd&#x60; - rpm.modulemd * &#x60;rpm.modulemd_defaults&#x60; - rpm.modulemd_defaults * &#x60;rpm.modulemd_obsolete&#x60; - rpm.modulemd_obsolete * &#x60;file.file&#x60; - file.file | [optional] 
 **pulp_type__in** | [**list[str]**](str.md)| Multiple values may be separated by commas.  * &#x60;core.publishedmetadata&#x60; - core.publishedmetadata * &#x60;ansible.role&#x60; - ansible.role * &#x60;ansible.collection_version&#x60; - ansible.collection_version * &#x60;ansible.collection_mark&#x60; - ansible.collection_mark * &#x60;ansible.collection_signature&#x60; - ansible.collection_signature * &#x60;ansible.namespace&#x60; - ansible.namespace * &#x60;ansible.collection_deprecation&#x60; - ansible.collection_deprecation * &#x60;container.blob&#x60; - container.blob * &#x60;container.manifest&#x60; - container.manifest * &#x60;container.tag&#x60; - container.tag * &#x60;container.signature&#x60; - container.signature * &#x60;deb.package&#x60; - deb.package * &#x60;deb.installer_package&#x60; - deb.installer_package * &#x60;deb.generic&#x60; - deb.generic * &#x60;deb.source_package&#x60; - deb.source_package * &#x60;deb.release&#x60; - deb.release * &#x60;deb.release_architecture&#x60; - deb.release_architecture * &#x60;deb.release_component&#x60; - deb.release_component * &#x60;deb.package_release_component&#x60; - deb.package_release_component * &#x60;deb.source_package_release_component&#x60; - deb.source_package_release_component * &#x60;deb.release_file&#x60; - deb.release_file * &#x60;deb.package_index&#x60; - deb.package_index * &#x60;deb.installer_file_index&#x60; - deb.installer_file_index * &#x60;deb.source_index&#x60; - deb.source_index * &#x60;gem.gem&#x60; - gem.gem * &#x60;maven.artifact&#x60; - maven.artifact * &#x60;maven.metadata&#x60; - maven.metadata * &#x60;ostree.object&#x60; - ostree.object * &#x60;ostree.commit&#x60; - ostree.commit * &#x60;ostree.refs&#x60; - ostree.refs * &#x60;ostree.content&#x60; - ostree.content * &#x60;ostree.config&#x60; - ostree.config * &#x60;ostree.summary&#x60; - ostree.summary * &#x60;python.python&#x60; - python.python * &#x60;rpm.advisory&#x60; - rpm.advisory * &#x60;rpm.packagegroup&#x60; - rpm.packagegroup * &#x60;rpm.packagecategory&#x60; - rpm.packagecategory * &#x60;rpm.packageenvironment&#x60; - rpm.packageenvironment * &#x60;rpm.packagelangpacks&#x60; - rpm.packagelangpacks * &#x60;rpm.repo_metadata_file&#x60; - rpm.repo_metadata_file * &#x60;rpm.distribution_tree&#x60; - rpm.distribution_tree * &#x60;rpm.package&#x60; - rpm.package * &#x60;rpm.modulemd&#x60; - rpm.modulemd * &#x60;rpm.modulemd_defaults&#x60; - rpm.modulemd_defaults * &#x60;rpm.modulemd_obsolete&#x60; - rpm.modulemd_obsolete * &#x60;file.file&#x60; - file.file | [optional] 
 **q** | **str**|  | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedMultipleArtifactContentResponseList**](PaginatedMultipleArtifactContentResponseList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

