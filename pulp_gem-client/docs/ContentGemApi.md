# pulpcore.client.pulp_gem.ContentGemApi

All URIs are relative to *https://console.redhat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ContentGemApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/content/gem/gem/ | Create a gem content
[**list**](ContentGemApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/content/gem/gem/ | List gem contents
[**read**](ContentGemApi.md#read) | **GET** {gem_gem_content_href} | Inspect a gem content
[**set_label**](ContentGemApi.md#set_label) | **POST** {gem_gem_content_href}set_label/ | Set a label
[**unset_label**](ContentGemApi.md#unset_label) | **POST** {gem_gem_content_href}unset_label/ | Unset a label


# **create**
> AsyncOperationResponse create(pulp_domain, repository=repository, pulp_labels=pulp_labels, artifact=artifact, file=file)

Create a gem content

Trigger an asynchronous task to create content,optionally create new repository version.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_gem.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_gem.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_gem.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_gem.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_gem.ContentGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    repository = 'repository_example' # str | A URI of a repository the new content unit should be associated with. (optional)
    pulp_labels = None # Dict[str, Optional[str]] | A dictionary of arbitrary key/value pairs used to describe a specific Content instance. (optional)
    artifact = 'artifact_example' # str | Artifact file representing the physical content (optional)
    file = None # bytearray | An uploaded file that should be turned into the artifact of the content unit. (optional)

    try:
        # Create a gem content
        api_response = api_instance.create(pulp_domain, repository=repository, pulp_labels=pulp_labels, artifact=artifact, file=file)
        print("The response of ContentGemApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGemApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **repository** | **str**| A URI of a repository the new content unit should be associated with. | [optional] 
 **pulp_labels** | [**Dict[str, Optional[str]]**](Dict.md)| A dictionary of arbitrary key/value pairs used to describe a specific Content instance. | [optional] 
 **artifact** | **str**| Artifact file representing the physical content | [optional] 
 **file** | **bytearray**| An uploaded file that should be turned into the artifact of the content unit. | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedgemGemContentResponseList list(pulp_domain, checksum=checksum, limit=limit, name=name, offset=offset, ordering=ordering, orphaned_for=orphaned_for, prerelease=prerelease, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, version=version, fields=fields, exclude_fields=exclude_fields)

List gem contents

A ViewSet for GemContent.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.paginatedgem_gem_content_response_list import PaginatedgemGemContentResponseList
from pulpcore.client.pulp_gem.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_gem.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_gem.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_gem.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_gem.ContentGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    checksum = 'checksum_example' # str | Filter results where checksum matches value (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str | Filter results where name matches value (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    ordering = ['ordering_example'] # List[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `name` - Name * `-name` - Name (descending) * `version` - Version * `-version` - Version (descending) * `platform` - Platform * `-platform` - Platform (descending) * `checksum` - Checksum * `-checksum` - Checksum (descending) * `prerelease` - Prerelease * `-prerelease` - Prerelease (descending) * `dependencies` - Dependencies * `-dependencies` - Dependencies (descending) * `required_ruby_version` - Required ruby version * `-required_ruby_version` - Required ruby version (descending) * `required_rubygems_version` - Required rubygems version * `-required_rubygems_version` - Required rubygems version (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
    orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
    prerelease = True # bool | Filter results where prerelease matches value (optional)
    prn__in = ['prn__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_href__in = ['pulp_href__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_id__in = ['pulp_id__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    repository_version = 'repository_version_example' # str | Repository Version referenced by HREF/PRN (optional)
    repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF/PRN (optional)
    repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF/PRN (optional)
    version = 'version_example' # str | Filter results where version matches value (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List gem contents
        api_response = api_instance.list(pulp_domain, checksum=checksum, limit=limit, name=name, offset=offset, ordering=ordering, orphaned_for=orphaned_for, prerelease=prerelease, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, version=version, fields=fields, exclude_fields=exclude_fields)
        print("The response of ContentGemApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGemApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **checksum** | **str**| Filter results where checksum matches value | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**| Filter results where name matches value | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;upstream_id&#x60; - Upstream id * &#x60;-upstream_id&#x60; - Upstream id (descending) * &#x60;pulp_labels&#x60; - Pulp labels * &#x60;-pulp_labels&#x60; - Pulp labels (descending) * &#x60;timestamp_of_interest&#x60; - Timestamp of interest * &#x60;-timestamp_of_interest&#x60; - Timestamp of interest (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;version&#x60; - Version * &#x60;-version&#x60; - Version (descending) * &#x60;platform&#x60; - Platform * &#x60;-platform&#x60; - Platform (descending) * &#x60;checksum&#x60; - Checksum * &#x60;-checksum&#x60; - Checksum (descending) * &#x60;prerelease&#x60; - Prerelease * &#x60;-prerelease&#x60; - Prerelease (descending) * &#x60;dependencies&#x60; - Dependencies * &#x60;-dependencies&#x60; - Dependencies (descending) * &#x60;required_ruby_version&#x60; - Required ruby version * &#x60;-required_ruby_version&#x60; - Required ruby version (descending) * &#x60;required_rubygems_version&#x60; - Required rubygems version * &#x60;-required_rubygems_version&#x60; - Required rubygems version (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **orphaned_for** | **float**| Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. | [optional] 
 **prerelease** | **bool**| Filter results where prerelease matches value | [optional] 
 **prn__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_href__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_label_select** | **str**| Filter labels by search string | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **version** | **str**| Filter results where version matches value | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedgemGemContentResponseList**](PaginatedgemGemContentResponseList.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> GemGemContentResponse read(gem_gem_content_href, fields=fields, exclude_fields=exclude_fields)

Inspect a gem content

A ViewSet for GemContent.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.gem_gem_content_response import GemGemContentResponse
from pulpcore.client.pulp_gem.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_gem.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_gem.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_gem.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_gem.ContentGemApi(api_client)
    gem_gem_content_href = 'gem_gem_content_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a gem content
        api_response = api_instance.read(gem_gem_content_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of ContentGemApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGemApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_content_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**GemGemContentResponse**](GemGemContentResponse.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_label**
> SetLabelResponse set_label(gem_gem_content_href, set_label)

Set a label

Set a single pulp_label on the object to a specific value or null.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.set_label import SetLabel
from pulpcore.client.pulp_gem.models.set_label_response import SetLabelResponse
from pulpcore.client.pulp_gem.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_gem.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_gem.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_gem.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_gem.ContentGemApi(api_client)
    gem_gem_content_href = 'gem_gem_content_href_example' # str | 
    set_label = pulpcore.client.pulp_gem.SetLabel() # SetLabel | 

    try:
        # Set a label
        api_response = api_instance.set_label(gem_gem_content_href, set_label)
        print("The response of ContentGemApi->set_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGemApi->set_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_content_href** | **str**|  | 
 **set_label** | [**SetLabel**](SetLabel.md)|  | 

### Return type

[**SetLabelResponse**](SetLabelResponse.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_label**
> UnsetLabelResponse unset_label(gem_gem_content_href, unset_label)

Unset a label

Unset a single pulp_label on the object.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.unset_label import UnsetLabel
from pulpcore.client.pulp_gem.models.unset_label_response import UnsetLabelResponse
from pulpcore.client.pulp_gem.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_gem.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_gem.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_gem.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_gem.ContentGemApi(api_client)
    gem_gem_content_href = 'gem_gem_content_href_example' # str | 
    unset_label = pulpcore.client.pulp_gem.UnsetLabel() # UnsetLabel | 

    try:
        # Unset a label
        api_response = api_instance.unset_label(gem_gem_content_href, unset_label)
        print("The response of ContentGemApi->unset_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGemApi->unset_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_content_href** | **str**|  | 
 **unset_label** | [**UnsetLabel**](UnsetLabel.md)|  | 

### Return type

[**UnsetLabelResponse**](UnsetLabelResponse.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

