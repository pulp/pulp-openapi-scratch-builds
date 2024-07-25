# pulpcore.client.pulp_rpm.ContentAdvisoriesApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ContentAdvisoriesApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/content/rpm/advisories/ | Create an update record
[**list**](ContentAdvisoriesApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/content/rpm/advisories/ | List update records
[**read**](ContentAdvisoriesApi.md#read) | **GET** {rpm_update_record_href} | Inspect an update record


# **create**
> AsyncOperationResponse create(pulp_domain, repository=repository, file=file, upload=upload, file_url=file_url)

Create an update record

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
    api_instance = pulpcore.client.pulp_rpm.ContentAdvisoriesApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
repository = 'repository_example' # str | A URI of a repository the new content unit should be associated with. (optional)
file = '/path/to/file' # file | An uploaded file that may be turned into the content unit. (optional)
upload = 'upload_example' # str | An uncommitted upload that may be turned into the content unit. (optional)
file_url = 'file_url_example' # str | A url that Pulp can download and turn into the content unit. (optional)

    try:
        # Create an update record
        api_response = api_instance.create(pulp_domain, repository=repository, file=file, upload=upload, file_url=file_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentAdvisoriesApi->create: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentAdvisoriesApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
repository = 'repository_example' # str | A URI of a repository the new content unit should be associated with. (optional)
file = '/path/to/file' # file | An uploaded file that may be turned into the content unit. (optional)
upload = 'upload_example' # str | An uncommitted upload that may be turned into the content unit. (optional)
file_url = 'file_url_example' # str | A url that Pulp can download and turn into the content unit. (optional)

    try:
        # Create an update record
        api_response = api_instance.create(pulp_domain, repository=repository, file=file, upload=upload, file_url=file_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentAdvisoriesApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **repository** | **str**| A URI of a repository the new content unit should be associated with. | [optional] 
 **file** | **file**| An uploaded file that may be turned into the content unit. | [optional] 
 **upload** | **str**| An uncommitted upload that may be turned into the content unit. | [optional] 
 **file_url** | **str**| A url that Pulp can download and turn into the content unit. | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedrpmUpdateRecordResponseList list(pulp_domain, id=id, id__in=id__in, limit=limit, offset=offset, ordering=ordering, orphaned_for=orphaned_for, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, severity=severity, severity__in=severity__in, severity__ne=severity__ne, status=status, status__in=status__in, status__ne=status__ne, type=type, type__in=type__in, type__ne=type__ne, fields=fields, exclude_fields=exclude_fields)

List update records

A ViewSet for UpdateRecord.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/advisories/  Also specify queryset and serializer for UpdateRecord.

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
    api_instance = pulpcore.client.pulp_rpm.ContentAdvisoriesApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
id = 'id_example' # str | Filter results where id matches value (optional)
id__in = ['id__in_example'] # list[str] | Filter results where id is in a comma-separated list of values (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `id` - Id * `-id` - Id (descending) * `updated_date` - Updated date * `-updated_date` - Updated date (descending) * `description` - Description * `-description` - Description (descending) * `issued_date` - Issued date * `-issued_date` - Issued date (descending) * `fromstr` - Fromstr * `-fromstr` - Fromstr (descending) * `status` - Status * `-status` - Status (descending) * `title` - Title * `-title` - Title (descending) * `summary` - Summary * `-summary` - Summary (descending) * `version` - Version * `-version` - Version (descending) * `type` - Type * `-type` - Type (descending) * `severity` - Severity * `-severity` - Severity (descending) * `solution` - Solution * `-solution` - Solution (descending) * `release` - Release * `-release` - Release (descending) * `rights` - Rights * `-rights` - Rights (descending) * `reboot_suggested` - Reboot suggested * `-reboot_suggested` - Reboot suggested (descending) * `pushcount` - Pushcount * `-pushcount` - Pushcount (descending) * `digest` - Digest * `-digest` - Digest (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
severity = 'severity_example' # str | Filter results where severity matches value (optional)
severity__in = ['severity__in_example'] # list[str] | Filter results where severity is in a comma-separated list of values (optional)
severity__ne = 'severity__ne_example' # str | Filter results where severity not equal to value (optional)
status = 'status_example' # str | Filter results where status matches value (optional)
status__in = ['status__in_example'] # list[str] | Filter results where status is in a comma-separated list of values (optional)
status__ne = 'status__ne_example' # str | Filter results where status not equal to value (optional)
type = 'type_example' # str | Filter results where type matches value (optional)
type__in = ['type__in_example'] # list[str] | Filter results where type is in a comma-separated list of values (optional)
type__ne = 'type__ne_example' # str | Filter results where type not equal to value (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List update records
        api_response = api_instance.list(pulp_domain, id=id, id__in=id__in, limit=limit, offset=offset, ordering=ordering, orphaned_for=orphaned_for, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, severity=severity, severity__in=severity__in, severity__ne=severity__ne, status=status, status__in=status__in, status__ne=status__ne, type=type, type__in=type__in, type__ne=type__ne, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentAdvisoriesApi->list: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentAdvisoriesApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
id = 'id_example' # str | Filter results where id matches value (optional)
id__in = ['id__in_example'] # list[str] | Filter results where id is in a comma-separated list of values (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `id` - Id * `-id` - Id (descending) * `updated_date` - Updated date * `-updated_date` - Updated date (descending) * `description` - Description * `-description` - Description (descending) * `issued_date` - Issued date * `-issued_date` - Issued date (descending) * `fromstr` - Fromstr * `-fromstr` - Fromstr (descending) * `status` - Status * `-status` - Status (descending) * `title` - Title * `-title` - Title (descending) * `summary` - Summary * `-summary` - Summary (descending) * `version` - Version * `-version` - Version (descending) * `type` - Type * `-type` - Type (descending) * `severity` - Severity * `-severity` - Severity (descending) * `solution` - Solution * `-solution` - Solution (descending) * `release` - Release * `-release` - Release (descending) * `rights` - Rights * `-rights` - Rights (descending) * `reboot_suggested` - Reboot suggested * `-reboot_suggested` - Reboot suggested (descending) * `pushcount` - Pushcount * `-pushcount` - Pushcount (descending) * `digest` - Digest * `-digest` - Digest (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
severity = 'severity_example' # str | Filter results where severity matches value (optional)
severity__in = ['severity__in_example'] # list[str] | Filter results where severity is in a comma-separated list of values (optional)
severity__ne = 'severity__ne_example' # str | Filter results where severity not equal to value (optional)
status = 'status_example' # str | Filter results where status matches value (optional)
status__in = ['status__in_example'] # list[str] | Filter results where status is in a comma-separated list of values (optional)
status__ne = 'status__ne_example' # str | Filter results where status not equal to value (optional)
type = 'type_example' # str | Filter results where type matches value (optional)
type__in = ['type__in_example'] # list[str] | Filter results where type is in a comma-separated list of values (optional)
type__ne = 'type__ne_example' # str | Filter results where type not equal to value (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List update records
        api_response = api_instance.list(pulp_domain, id=id, id__in=id__in, limit=limit, offset=offset, ordering=ordering, orphaned_for=orphaned_for, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, severity=severity, severity__in=severity__in, severity__ne=severity__ne, status=status, status__in=status__in, status__ne=status__ne, type=type, type__in=type__in, type__ne=type__ne, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentAdvisoriesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **id** | **str**| Filter results where id matches value | [optional] 
 **id__in** | [**list[str]**](str.md)| Filter results where id is in a comma-separated list of values | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;upstream_id&#x60; - Upstream id * &#x60;-upstream_id&#x60; - Upstream id (descending) * &#x60;timestamp_of_interest&#x60; - Timestamp of interest * &#x60;-timestamp_of_interest&#x60; - Timestamp of interest (descending) * &#x60;id&#x60; - Id * &#x60;-id&#x60; - Id (descending) * &#x60;updated_date&#x60; - Updated date * &#x60;-updated_date&#x60; - Updated date (descending) * &#x60;description&#x60; - Description * &#x60;-description&#x60; - Description (descending) * &#x60;issued_date&#x60; - Issued date * &#x60;-issued_date&#x60; - Issued date (descending) * &#x60;fromstr&#x60; - Fromstr * &#x60;-fromstr&#x60; - Fromstr (descending) * &#x60;status&#x60; - Status * &#x60;-status&#x60; - Status (descending) * &#x60;title&#x60; - Title * &#x60;-title&#x60; - Title (descending) * &#x60;summary&#x60; - Summary * &#x60;-summary&#x60; - Summary (descending) * &#x60;version&#x60; - Version * &#x60;-version&#x60; - Version (descending) * &#x60;type&#x60; - Type * &#x60;-type&#x60; - Type (descending) * &#x60;severity&#x60; - Severity * &#x60;-severity&#x60; - Severity (descending) * &#x60;solution&#x60; - Solution * &#x60;-solution&#x60; - Solution (descending) * &#x60;release&#x60; - Release * &#x60;-release&#x60; - Release (descending) * &#x60;rights&#x60; - Rights * &#x60;-rights&#x60; - Rights (descending) * &#x60;reboot_suggested&#x60; - Reboot suggested * &#x60;-reboot_suggested&#x60; - Reboot suggested (descending) * &#x60;pushcount&#x60; - Pushcount * &#x60;-pushcount&#x60; - Pushcount (descending) * &#x60;digest&#x60; - Digest * &#x60;-digest&#x60; - Digest (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **orphaned_for** | **float**| Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **severity** | **str**| Filter results where severity matches value | [optional] 
 **severity__in** | [**list[str]**](str.md)| Filter results where severity is in a comma-separated list of values | [optional] 
 **severity__ne** | **str**| Filter results where severity not equal to value | [optional] 
 **status** | **str**| Filter results where status matches value | [optional] 
 **status__in** | [**list[str]**](str.md)| Filter results where status is in a comma-separated list of values | [optional] 
 **status__ne** | **str**| Filter results where status not equal to value | [optional] 
 **type** | **str**| Filter results where type matches value | [optional] 
 **type__in** | [**list[str]**](str.md)| Filter results where type is in a comma-separated list of values | [optional] 
 **type__ne** | **str**| Filter results where type not equal to value | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedrpmUpdateRecordResponseList**](PaginatedrpmUpdateRecordResponseList.md)

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
> RpmUpdateRecordResponse read(rpm_update_record_href, fields=fields, exclude_fields=exclude_fields)

Inspect an update record

A ViewSet for UpdateRecord.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/advisories/  Also specify queryset and serializer for UpdateRecord.

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
    api_instance = pulpcore.client.pulp_rpm.ContentAdvisoriesApi(api_client)
    rpm_update_record_href = 'rpm_update_record_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an update record
        api_response = api_instance.read(rpm_update_record_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentAdvisoriesApi->read: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentAdvisoriesApi(api_client)
    rpm_update_record_href = 'rpm_update_record_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an update record
        api_response = api_instance.read(rpm_update_record_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentAdvisoriesApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_update_record_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**RpmUpdateRecordResponse**](RpmUpdateRecordResponse.md)

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

