# pulpcore.client.pulp_rpm.ContentModulemdsApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ContentModulemdsApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/content/rpm/modulemds/ | Create a modulemd
[**list**](ContentModulemdsApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/content/rpm/modulemds/ | List modulemds
[**read**](ContentModulemdsApi.md#read) | **GET** {rpm_modulemd_href} | Inspect a modulemd


# **create**
> AsyncOperationResponse create(pulp_domain, rpm_modulemd)

Create a modulemd

Trigger an asynchronous task to create content,optionally create new repository version.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_rpm.models.rpm_modulemd import RpmModulemd
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    rpm_modulemd = pulpcore.client.pulp_rpm.RpmModulemd() # RpmModulemd | 

    try:
        # Create a modulemd
        api_response = api_instance.create(pulp_domain, rpm_modulemd)
        print("The response of ContentModulemdsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentModulemdsApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **rpm_modulemd** | [**RpmModulemd**](RpmModulemd.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedrpmModulemdResponseList list(pulp_domain, arch=arch, arch__in=arch__in, context=context, context__in=context__in, limit=limit, name=name, name__in=name__in, offset=offset, ordering=ordering, orphaned_for=orphaned_for, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, stream=stream, stream__in=stream__in, version=version, version__in=version__in, fields=fields, exclude_fields=exclude_fields)

List modulemds

ViewSet for Modulemd.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.paginatedrpm_modulemd_response_list import PaginatedrpmModulemdResponseList
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    arch = 'arch_example' # str | Filter results where arch matches value (optional)
    arch__in = ['arch__in_example'] # List[str] | Filter results where arch is in a comma-separated list of values (optional)
    context = 'context_example' # str | Filter results where context matches value (optional)
    context__in = ['context__in_example'] # List[str] | Filter results where context is in a comma-separated list of values (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str | Filter results where name matches value (optional)
    name__in = ['name__in_example'] # List[str] | Filter results where name is in a comma-separated list of values (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    ordering = ['ordering_example'] # List[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `name` - Name * `-name` - Name (descending) * `stream` - Stream * `-stream` - Stream (descending) * `version` - Version * `-version` - Version (descending) * `context` - Context * `-context` - Context (descending) * `arch` - Arch * `-arch` - Arch (descending) * `static_context` - Static context * `-static_context` - Static context (descending) * `dependencies` - Dependencies * `-dependencies` - Dependencies (descending) * `artifacts` - Artifacts * `-artifacts` - Artifacts (descending) * `profiles` - Profiles * `-profiles` - Profiles (descending) * `description` - Description * `-description` - Description (descending) * `digest` - Digest * `-digest` - Digest (descending) * `snippet` - Snippet * `-snippet` - Snippet (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
    orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
    prn__in = ['prn__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_href__in = ['pulp_href__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_id__in = ['pulp_id__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    repository_version = 'repository_version_example' # str | Repository Version referenced by HREF/PRN (optional)
    repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF/PRN (optional)
    repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF/PRN (optional)
    sha256 = 'sha256_example' # str |  (optional)
    stream = 'stream_example' # str | Filter results where stream matches value (optional)
    stream__in = ['stream__in_example'] # List[str] | Filter results where stream is in a comma-separated list of values (optional)
    version = 'version_example' # str | Filter results where version matches value (optional)
    version__in = ['version__in_example'] # List[str] | Filter results where version is in a comma-separated list of values (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List modulemds
        api_response = api_instance.list(pulp_domain, arch=arch, arch__in=arch__in, context=context, context__in=context__in, limit=limit, name=name, name__in=name__in, offset=offset, ordering=ordering, orphaned_for=orphaned_for, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, stream=stream, stream__in=stream__in, version=version, version__in=version__in, fields=fields, exclude_fields=exclude_fields)
        print("The response of ContentModulemdsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentModulemdsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **arch** | **str**| Filter results where arch matches value | [optional] 
 **arch__in** | [**List[str]**](str.md)| Filter results where arch is in a comma-separated list of values | [optional] 
 **context** | **str**| Filter results where context matches value | [optional] 
 **context__in** | [**List[str]**](str.md)| Filter results where context is in a comma-separated list of values | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**| Filter results where name matches value | [optional] 
 **name__in** | [**List[str]**](str.md)| Filter results where name is in a comma-separated list of values | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;upstream_id&#x60; - Upstream id * &#x60;-upstream_id&#x60; - Upstream id (descending) * &#x60;timestamp_of_interest&#x60; - Timestamp of interest * &#x60;-timestamp_of_interest&#x60; - Timestamp of interest (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;stream&#x60; - Stream * &#x60;-stream&#x60; - Stream (descending) * &#x60;version&#x60; - Version * &#x60;-version&#x60; - Version (descending) * &#x60;context&#x60; - Context * &#x60;-context&#x60; - Context (descending) * &#x60;arch&#x60; - Arch * &#x60;-arch&#x60; - Arch (descending) * &#x60;static_context&#x60; - Static context * &#x60;-static_context&#x60; - Static context (descending) * &#x60;dependencies&#x60; - Dependencies * &#x60;-dependencies&#x60; - Dependencies (descending) * &#x60;artifacts&#x60; - Artifacts * &#x60;-artifacts&#x60; - Artifacts (descending) * &#x60;profiles&#x60; - Profiles * &#x60;-profiles&#x60; - Profiles (descending) * &#x60;description&#x60; - Description * &#x60;-description&#x60; - Description (descending) * &#x60;digest&#x60; - Digest * &#x60;-digest&#x60; - Digest (descending) * &#x60;snippet&#x60; - Snippet * &#x60;-snippet&#x60; - Snippet (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **orphaned_for** | **float**| Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. | [optional] 
 **prn__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_href__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **sha256** | **str**|  | [optional] 
 **stream** | **str**| Filter results where stream matches value | [optional] 
 **stream__in** | [**List[str]**](str.md)| Filter results where stream is in a comma-separated list of values | [optional] 
 **version** | **str**| Filter results where version matches value | [optional] 
 **version__in** | [**List[str]**](str.md)| Filter results where version is in a comma-separated list of values | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedrpmModulemdResponseList**](PaginatedrpmModulemdResponseList.md)

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

# **read**
> RpmModulemdResponse read(rpm_modulemd_href, fields=fields, exclude_fields=exclude_fields)

Inspect a modulemd

ViewSet for Modulemd.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.rpm_modulemd_response import RpmModulemdResponse
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdsApi(api_client)
    rpm_modulemd_href = 'rpm_modulemd_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a modulemd
        api_response = api_instance.read(rpm_modulemd_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of ContentModulemdsApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentModulemdsApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_modulemd_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**RpmModulemdResponse**](RpmModulemdResponse.md)

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

