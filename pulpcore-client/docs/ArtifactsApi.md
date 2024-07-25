# pulpcore.client.pulpcore.ArtifactsApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ArtifactsApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/artifacts/ | Create an artifact
[**delete**](ArtifactsApi.md#delete) | **DELETE** {artifact_href} | Delete an artifact
[**list**](ArtifactsApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/artifacts/ | List artifacts
[**read**](ArtifactsApi.md#read) | **GET** {artifact_href} | Inspect an artifact


# **create**
> ArtifactResponse create(pulp_domain, file, size=size, md5=md5, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512)

Create an artifact

A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
file = '/path/to/file' # file | The stored file.
size = 56 # int | The size of the file in bytes. (optional)
md5 = 'md5_example' # str | The MD5 checksum of the file if available. (optional)
sha1 = 'sha1_example' # str | The SHA-1 checksum of the file if available. (optional)
sha224 = 'sha224_example' # str | The SHA-224 checksum of the file if available. (optional)
sha256 = 'sha256_example' # str | The SHA-256 checksum of the file if available. (optional)
sha384 = 'sha384_example' # str | The SHA-384 checksum of the file if available. (optional)
sha512 = 'sha512_example' # str | The SHA-512 checksum of the file if available. (optional)

    try:
        # Create an artifact
        api_response = api_instance.create(pulp_domain, file, size=size, md5=md5, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->create: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
file = '/path/to/file' # file | The stored file.
size = 56 # int | The size of the file in bytes. (optional)
md5 = 'md5_example' # str | The MD5 checksum of the file if available. (optional)
sha1 = 'sha1_example' # str | The SHA-1 checksum of the file if available. (optional)
sha224 = 'sha224_example' # str | The SHA-224 checksum of the file if available. (optional)
sha256 = 'sha256_example' # str | The SHA-256 checksum of the file if available. (optional)
sha384 = 'sha384_example' # str | The SHA-384 checksum of the file if available. (optional)
sha512 = 'sha512_example' # str | The SHA-512 checksum of the file if available. (optional)

    try:
        # Create an artifact
        api_response = api_instance.create(pulp_domain, file, size=size, md5=md5, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **file** | **file**| The stored file. | 
 **size** | **int**| The size of the file in bytes. | [optional] 
 **md5** | **str**| The MD5 checksum of the file if available. | [optional] 
 **sha1** | **str**| The SHA-1 checksum of the file if available. | [optional] 
 **sha224** | **str**| The SHA-224 checksum of the file if available. | [optional] 
 **sha256** | **str**| The SHA-256 checksum of the file if available. | [optional] 
 **sha384** | **str**| The SHA-384 checksum of the file if available. | [optional] 
 **sha512** | **str**| The SHA-512 checksum of the file if available. | [optional] 

### Return type

[**ArtifactResponse**](ArtifactResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(artifact_href)

Delete an artifact

Remove Artifact only if it is not associated with any Content.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    artifact_href = 'artifact_href_example' # str | 

    try:
        # Delete an artifact
        api_instance.delete(artifact_href)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->delete: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    artifact_href = 'artifact_href_example' # str | 

    try:
        # Delete an artifact
        api_instance.delete(artifact_href)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_href** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedArtifactResponseList list(pulp_domain, limit=limit, md5=md5, offset=offset, ordering=ordering, orphaned_for=orphaned_for, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512, fields=fields, exclude_fields=exclude_fields)

List artifacts

A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
md5 = 'md5_example' # str | Filter results where md5 matches value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `file` - File * `-file` - File (descending) * `size` - Size * `-size` - Size (descending) * `md5` - Md5 * `-md5` - Md5 (descending) * `sha1` - Sha1 * `-sha1` - Sha1 (descending) * `sha224` - Sha224 * `-sha224` - Sha224 (descending) * `sha256` - Sha256 * `-sha256` - Sha256 (descending) * `sha384` - Sha384 * `-sha384` - Sha384 (descending) * `sha512` - Sha512 * `-sha512` - Sha512 (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
orphaned_for = 3.4 # float | Minutes Artifacts have been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
sha1 = 'sha1_example' # str | Filter results where sha1 matches value (optional)
sha224 = 'sha224_example' # str | Filter results where sha224 matches value (optional)
sha256 = 'sha256_example' # str | Filter results where sha256 matches value (optional)
sha384 = 'sha384_example' # str | Filter results where sha384 matches value (optional)
sha512 = 'sha512_example' # str | Filter results where sha512 matches value (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List artifacts
        api_response = api_instance.list(pulp_domain, limit=limit, md5=md5, offset=offset, ordering=ordering, orphaned_for=orphaned_for, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->list: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
md5 = 'md5_example' # str | Filter results where md5 matches value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `file` - File * `-file` - File (descending) * `size` - Size * `-size` - Size (descending) * `md5` - Md5 * `-md5` - Md5 (descending) * `sha1` - Sha1 * `-sha1` - Sha1 (descending) * `sha224` - Sha224 * `-sha224` - Sha224 (descending) * `sha256` - Sha256 * `-sha256` - Sha256 (descending) * `sha384` - Sha384 * `-sha384` - Sha384 (descending) * `sha512` - Sha512 * `-sha512` - Sha512 (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
orphaned_for = 3.4 # float | Minutes Artifacts have been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
sha1 = 'sha1_example' # str | Filter results where sha1 matches value (optional)
sha224 = 'sha224_example' # str | Filter results where sha224 matches value (optional)
sha256 = 'sha256_example' # str | Filter results where sha256 matches value (optional)
sha384 = 'sha384_example' # str | Filter results where sha384 matches value (optional)
sha512 = 'sha512_example' # str | Filter results where sha512 matches value (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List artifacts
        api_response = api_instance.list(pulp_domain, limit=limit, md5=md5, offset=offset, ordering=ordering, orphaned_for=orphaned_for, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **md5** | **str**| Filter results where md5 matches value | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;file&#x60; - File * &#x60;-file&#x60; - File (descending) * &#x60;size&#x60; - Size * &#x60;-size&#x60; - Size (descending) * &#x60;md5&#x60; - Md5 * &#x60;-md5&#x60; - Md5 (descending) * &#x60;sha1&#x60; - Sha1 * &#x60;-sha1&#x60; - Sha1 (descending) * &#x60;sha224&#x60; - Sha224 * &#x60;-sha224&#x60; - Sha224 (descending) * &#x60;sha256&#x60; - Sha256 * &#x60;-sha256&#x60; - Sha256 (descending) * &#x60;sha384&#x60; - Sha384 * &#x60;-sha384&#x60; - Sha384 (descending) * &#x60;sha512&#x60; - Sha512 * &#x60;-sha512&#x60; - Sha512 (descending) * &#x60;timestamp_of_interest&#x60; - Timestamp of interest * &#x60;-timestamp_of_interest&#x60; - Timestamp of interest (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **orphaned_for** | **float**| Minutes Artifacts have been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **sha1** | **str**| Filter results where sha1 matches value | [optional] 
 **sha224** | **str**| Filter results where sha224 matches value | [optional] 
 **sha256** | **str**| Filter results where sha256 matches value | [optional] 
 **sha384** | **str**| Filter results where sha384 matches value | [optional] 
 **sha512** | **str**| Filter results where sha512 matches value | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedArtifactResponseList**](PaginatedArtifactResponseList.md)

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
> ArtifactResponse read(artifact_href, fields=fields, exclude_fields=exclude_fields)

Inspect an artifact

A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    artifact_href = 'artifact_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an artifact
        api_response = api_instance.read(artifact_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->read: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:5001",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    artifact_href = 'artifact_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an artifact
        api_response = api_instance.read(artifact_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**ArtifactResponse**](ArtifactResponse.md)

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

