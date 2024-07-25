# pulpcore.client.pulp_rpm.ContentModulemdDefaultsApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ContentModulemdDefaultsApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/content/rpm/modulemd_defaults/ | Create a modulemd defaults
[**list**](ContentModulemdDefaultsApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/content/rpm/modulemd_defaults/ | List modulemd defaultss
[**read**](ContentModulemdDefaultsApi.md#read) | **GET** {rpm_modulemd_defaults_href} | Inspect a modulemd defaults


# **create**
> AsyncOperationResponse create(pulp_domain, rpm_modulemd_defaults)

Create a modulemd defaults

Trigger an asynchronous task to create content,optionally create new repository version.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdDefaultsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
rpm_modulemd_defaults = pulpcore.client.pulp_rpm.RpmModulemdDefaults() # RpmModulemdDefaults | 

    try:
        # Create a modulemd defaults
        api_response = api_instance.create(pulp_domain, rpm_modulemd_defaults)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentModulemdDefaultsApi->create: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdDefaultsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
rpm_modulemd_defaults = pulpcore.client.pulp_rpm.RpmModulemdDefaults() # RpmModulemdDefaults | 

    try:
        # Create a modulemd defaults
        api_response = api_instance.create(pulp_domain, rpm_modulemd_defaults)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentModulemdDefaultsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **rpm_modulemd_defaults** | [**RpmModulemdDefaults**](RpmModulemdDefaults.md)|  | 

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
> PaginatedrpmModulemdDefaultsResponseList list(pulp_domain, limit=limit, module=module, module__in=module__in, offset=offset, ordering=ordering, orphaned_for=orphaned_for, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, stream=stream, stream__in=stream__in, fields=fields, exclude_fields=exclude_fields)

List modulemd defaultss

ViewSet for Modulemd.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdDefaultsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
module = 'module_example' # str | Filter results where module matches value (optional)
module__in = ['module__in_example'] # list[str] | Filter results where module is in a comma-separated list of values (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `module` - Module * `-module` - Module (descending) * `stream` - Stream * `-stream` - Stream (descending) * `profiles` - Profiles * `-profiles` - Profiles (descending) * `digest` - Digest * `-digest` - Digest (descending) * `snippet` - Snippet * `-snippet` - Snippet (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
sha256 = 'sha256_example' # str |  (optional)
stream = 'stream_example' # str | Filter results where stream matches value (optional)
stream__in = ['stream__in_example'] # list[str] | Filter results where stream is in a comma-separated list of values (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List modulemd defaultss
        api_response = api_instance.list(pulp_domain, limit=limit, module=module, module__in=module__in, offset=offset, ordering=ordering, orphaned_for=orphaned_for, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, stream=stream, stream__in=stream__in, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentModulemdDefaultsApi->list: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdDefaultsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
module = 'module_example' # str | Filter results where module matches value (optional)
module__in = ['module__in_example'] # list[str] | Filter results where module is in a comma-separated list of values (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `module` - Module * `-module` - Module (descending) * `stream` - Stream * `-stream` - Stream (descending) * `profiles` - Profiles * `-profiles` - Profiles (descending) * `digest` - Digest * `-digest` - Digest (descending) * `snippet` - Snippet * `-snippet` - Snippet (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
sha256 = 'sha256_example' # str |  (optional)
stream = 'stream_example' # str | Filter results where stream matches value (optional)
stream__in = ['stream__in_example'] # list[str] | Filter results where stream is in a comma-separated list of values (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List modulemd defaultss
        api_response = api_instance.list(pulp_domain, limit=limit, module=module, module__in=module__in, offset=offset, ordering=ordering, orphaned_for=orphaned_for, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, stream=stream, stream__in=stream__in, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentModulemdDefaultsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **module** | **str**| Filter results where module matches value | [optional] 
 **module__in** | [**list[str]**](str.md)| Filter results where module is in a comma-separated list of values | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;upstream_id&#x60; - Upstream id * &#x60;-upstream_id&#x60; - Upstream id (descending) * &#x60;timestamp_of_interest&#x60; - Timestamp of interest * &#x60;-timestamp_of_interest&#x60; - Timestamp of interest (descending) * &#x60;module&#x60; - Module * &#x60;-module&#x60; - Module (descending) * &#x60;stream&#x60; - Stream * &#x60;-stream&#x60; - Stream (descending) * &#x60;profiles&#x60; - Profiles * &#x60;-profiles&#x60; - Profiles (descending) * &#x60;digest&#x60; - Digest * &#x60;-digest&#x60; - Digest (descending) * &#x60;snippet&#x60; - Snippet * &#x60;-snippet&#x60; - Snippet (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **orphaned_for** | **float**| Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **sha256** | **str**|  | [optional] 
 **stream** | **str**| Filter results where stream matches value | [optional] 
 **stream__in** | [**list[str]**](str.md)| Filter results where stream is in a comma-separated list of values | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedrpmModulemdDefaultsResponseList**](PaginatedrpmModulemdDefaultsResponseList.md)

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
> RpmModulemdDefaultsResponse read(rpm_modulemd_defaults_href, fields=fields, exclude_fields=exclude_fields)

Inspect a modulemd defaults

ViewSet for Modulemd.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdDefaultsApi(api_client)
    rpm_modulemd_defaults_href = 'rpm_modulemd_defaults_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a modulemd defaults
        api_response = api_instance.read(rpm_modulemd_defaults_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentModulemdDefaultsApi->read: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdDefaultsApi(api_client)
    rpm_modulemd_defaults_href = 'rpm_modulemd_defaults_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a modulemd defaults
        api_response = api_instance.read(rpm_modulemd_defaults_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentModulemdDefaultsApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_modulemd_defaults_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**RpmModulemdDefaultsResponse**](RpmModulemdDefaultsResponse.md)

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

