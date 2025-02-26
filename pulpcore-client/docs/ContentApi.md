# pulpcore.client.pulpcore.ContentApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](ContentApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/content/ | List content


# **list**
> PaginatedMultipleArtifactContentResponseList list(pulp_domain, limit=limit, offset=offset, ordering=ordering, orphaned_for=orphaned_for, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_type=pulp_type, pulp_type__in=pulp_type__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, fields=fields, exclude_fields=exclude_fields)

List content

Endpoint to list all content.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.paginated_multiple_artifact_content_response_list import PaginatedMultipleArtifactContentResponseList
from pulpcore.client.pulpcore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulpcore.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.ContentApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    ordering = ['ordering_example'] # List[str] | Ordering  * `pk` - Pk * `-pk` - Pk (descending) (optional)
    orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
    prn__in = ['prn__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_href__in = ['pulp_href__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_id__in = ['pulp_id__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_type = 'pulp_type_example' # str | Pulp type  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary (optional)
    pulp_type__in = ['pulp_type__in_example'] # List[str] | Multiple values may be separated by commas.  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    repository_version = 'repository_version_example' # str | Repository Version referenced by HREF/PRN (optional)
    repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF/PRN (optional)
    repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF/PRN (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List content
        api_response = api_instance.list(pulp_domain, limit=limit, offset=offset, ordering=ordering, orphaned_for=orphaned_for, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_type=pulp_type, pulp_type__in=pulp_type__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, fields=fields, exclude_fields=exclude_fields)
        print("The response of ContentApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **orphaned_for** | **float**| Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. | [optional] 
 **prn__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_href__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_type** | **str**| Pulp type  * &#x60;core.publishedmetadata&#x60; - core.publishedmetadata * &#x60;core.openpgp_publickey&#x60; - core.openpgp_publickey * &#x60;core.openpgp_publicsubkey&#x60; - core.openpgp_publicsubkey * &#x60;core.openpgp_userid&#x60; - core.openpgp_userid * &#x60;core.openpgp_userattribute&#x60; - core.openpgp_userattribute * &#x60;core.openpgp_signature&#x60; - core.openpgp_signature * &#x60;file.file&#x60; - file.file * &#x60;rpm.advisory&#x60; - rpm.advisory * &#x60;rpm.packagegroup&#x60; - rpm.packagegroup * &#x60;rpm.packagecategory&#x60; - rpm.packagecategory * &#x60;rpm.packageenvironment&#x60; - rpm.packageenvironment * &#x60;rpm.packagelangpacks&#x60; - rpm.packagelangpacks * &#x60;rpm.repo_metadata_file&#x60; - rpm.repo_metadata_file * &#x60;rpm.distribution_tree&#x60; - rpm.distribution_tree * &#x60;rpm.package&#x60; - rpm.package * &#x60;rpm.modulemd&#x60; - rpm.modulemd * &#x60;rpm.modulemd_defaults&#x60; - rpm.modulemd_defaults * &#x60;rpm.modulemd_obsolete&#x60; - rpm.modulemd_obsolete * &#x60;ostree.object&#x60; - ostree.object * &#x60;ostree.commit&#x60; - ostree.commit * &#x60;ostree.refs&#x60; - ostree.refs * &#x60;ostree.content&#x60; - ostree.content * &#x60;ostree.config&#x60; - ostree.config * &#x60;ostree.summary&#x60; - ostree.summary | [optional] 
 **pulp_type__in** | [**List[str]**](str.md)| Multiple values may be separated by commas.  * &#x60;core.publishedmetadata&#x60; - core.publishedmetadata * &#x60;core.openpgp_publickey&#x60; - core.openpgp_publickey * &#x60;core.openpgp_publicsubkey&#x60; - core.openpgp_publicsubkey * &#x60;core.openpgp_userid&#x60; - core.openpgp_userid * &#x60;core.openpgp_userattribute&#x60; - core.openpgp_userattribute * &#x60;core.openpgp_signature&#x60; - core.openpgp_signature * &#x60;file.file&#x60; - file.file * &#x60;rpm.advisory&#x60; - rpm.advisory * &#x60;rpm.packagegroup&#x60; - rpm.packagegroup * &#x60;rpm.packagecategory&#x60; - rpm.packagecategory * &#x60;rpm.packageenvironment&#x60; - rpm.packageenvironment * &#x60;rpm.packagelangpacks&#x60; - rpm.packagelangpacks * &#x60;rpm.repo_metadata_file&#x60; - rpm.repo_metadata_file * &#x60;rpm.distribution_tree&#x60; - rpm.distribution_tree * &#x60;rpm.package&#x60; - rpm.package * &#x60;rpm.modulemd&#x60; - rpm.modulemd * &#x60;rpm.modulemd_defaults&#x60; - rpm.modulemd_defaults * &#x60;rpm.modulemd_obsolete&#x60; - rpm.modulemd_obsolete * &#x60;ostree.object&#x60; - ostree.object * &#x60;ostree.commit&#x60; - ostree.commit * &#x60;ostree.refs&#x60; - ostree.refs * &#x60;ostree.content&#x60; - ostree.content * &#x60;ostree.config&#x60; - ostree.config * &#x60;ostree.summary&#x60; - ostree.summary | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

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

