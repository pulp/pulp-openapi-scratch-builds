# pulpcore.client.pulp_gem.RemotesGemApi

All URIs are relative to *https://console.redhat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role**](RemotesGemApi.md#add_role) | **POST** {gem_gem_remote_href}add_role/ | Add a role
[**create**](RemotesGemApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/remotes/gem/gem/ | Create a gem remote
[**delete**](RemotesGemApi.md#delete) | **DELETE** {gem_gem_remote_href} | Delete a gem remote
[**list**](RemotesGemApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/remotes/gem/gem/ | List gem remotes
[**list_roles**](RemotesGemApi.md#list_roles) | **GET** {gem_gem_remote_href}list_roles/ | List roles
[**my_permissions**](RemotesGemApi.md#my_permissions) | **GET** {gem_gem_remote_href}my_permissions/ | List user permissions
[**partial_update**](RemotesGemApi.md#partial_update) | **PATCH** {gem_gem_remote_href} | Update a gem remote
[**read**](RemotesGemApi.md#read) | **GET** {gem_gem_remote_href} | Inspect a gem remote
[**remove_role**](RemotesGemApi.md#remove_role) | **POST** {gem_gem_remote_href}remove_role/ | Remove a role
[**set_label**](RemotesGemApi.md#set_label) | **POST** {gem_gem_remote_href}set_label/ | Set a label
[**unset_label**](RemotesGemApi.md#unset_label) | **POST** {gem_gem_remote_href}unset_label/ | Unset a label
[**update**](RemotesGemApi.md#update) | **PUT** {gem_gem_remote_href} | Update a gem remote


# **add_role**
> NestedRoleResponse add_role(gem_gem_remote_href, nested_role)

Add a role

Add a role for this object to users/groups.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.nested_role import NestedRole
from pulpcore.client.pulp_gem.models.nested_role_response import NestedRoleResponse
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
    api_instance = pulpcore.client.pulp_gem.RemotesGemApi(api_client)
    gem_gem_remote_href = 'gem_gem_remote_href_example' # str | 
    nested_role = pulpcore.client.pulp_gem.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.add_role(gem_gem_remote_href, nested_role)
        print("The response of RemotesGemApi->add_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotesGemApi->add_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_remote_href** | **str**|  | 
 **nested_role** | [**NestedRole**](NestedRole.md)|  | 

### Return type

[**NestedRoleResponse**](NestedRoleResponse.md)

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

# **create**
> GemGemRemoteResponse create(pulp_domain, gem_gem_remote)

Create a gem remote

A ViewSet for GemRemote.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.gem_gem_remote import GemGemRemote
from pulpcore.client.pulp_gem.models.gem_gem_remote_response import GemGemRemoteResponse
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
    api_instance = pulpcore.client.pulp_gem.RemotesGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    gem_gem_remote = pulpcore.client.pulp_gem.GemGemRemote() # GemGemRemote | 

    try:
        # Create a gem remote
        api_response = api_instance.create(pulp_domain, gem_gem_remote)
        print("The response of RemotesGemApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotesGemApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **gem_gem_remote** | [**GemGemRemote**](GemGemRemote.md)|  | 

### Return type

[**GemGemRemoteResponse**](GemGemRemoteResponse.md)

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

# **delete**
> AsyncOperationResponse delete(gem_gem_remote_href)

Delete a gem remote

Trigger an asynchronous delete task

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
    api_instance = pulpcore.client.pulp_gem.RemotesGemApi(api_client)
    gem_gem_remote_href = 'gem_gem_remote_href_example' # str | 

    try:
        # Delete a gem remote
        api_response = api_instance.delete(gem_gem_remote_href)
        print("The response of RemotesGemApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotesGemApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_remote_href** | **str**|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedgemGemRemoteResponseList list(pulp_domain, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, pulp_last_updated=pulp_last_updated, pulp_last_updated__gt=pulp_last_updated__gt, pulp_last_updated__gte=pulp_last_updated__gte, pulp_last_updated__isnull=pulp_last_updated__isnull, pulp_last_updated__lt=pulp_last_updated__lt, pulp_last_updated__lte=pulp_last_updated__lte, pulp_last_updated__range=pulp_last_updated__range, q=q, fields=fields, exclude_fields=exclude_fields)

List gem remotes

A ViewSet for GemRemote.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.paginatedgem_gem_remote_response_list import PaginatedgemGemRemoteResponseList
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
    api_instance = pulpcore.client.pulp_gem.RemotesGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str | Filter results where name matches value (optional)
    name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
    name__icontains = 'name__icontains_example' # str | Filter results where name contains value (optional)
    name__iexact = 'name__iexact_example' # str | Filter results where name matches value (optional)
    name__in = ['name__in_example'] # List[str] | Filter results where name is in a comma-separated list of values (optional)
    name__iregex = 'name__iregex_example' # str | Filter results where name matches regex value (optional)
    name__istartswith = 'name__istartswith_example' # str | Filter results where name starts with value (optional)
    name__regex = 'name__regex_example' # str | Filter results where name matches regex value (optional)
    name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    ordering = ['ordering_example'] # List[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `url` - Url * `-url` - Url (descending) * `ca_cert` - Ca cert * `-ca_cert` - Ca cert (descending) * `client_cert` - Client cert * `-client_cert` - Client cert (descending) * `client_key` - Client key * `-client_key` - Client key (descending) * `tls_validation` - Tls validation * `-tls_validation` - Tls validation (descending) * `username` - Username * `-username` - Username (descending) * `password` - Password * `-password` - Password (descending) * `proxy_url` - Proxy url * `-proxy_url` - Proxy url (descending) * `proxy_username` - Proxy username * `-proxy_username` - Proxy username (descending) * `proxy_password` - Proxy password * `-proxy_password` - Proxy password (descending) * `download_concurrency` - Download concurrency * `-download_concurrency` - Download concurrency (descending) * `max_retries` - Max retries * `-max_retries` - Max retries (descending) * `policy` - Policy * `-policy` - Policy (descending) * `total_timeout` - Total timeout * `-total_timeout` - Total timeout (descending) * `connect_timeout` - Connect timeout * `-connect_timeout` - Connect timeout (descending) * `sock_connect_timeout` - Sock connect timeout * `-sock_connect_timeout` - Sock connect timeout (descending) * `sock_read_timeout` - Sock read timeout * `-sock_read_timeout` - Sock read timeout (descending) * `headers` - Headers * `-headers` - Headers (descending) * `rate_limit` - Rate limit * `-rate_limit` - Rate limit (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
    prn__in = ['prn__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_href__in = ['pulp_href__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_id__in = ['pulp_id__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
    pulp_last_updated = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_last_updated matches value (optional)
    pulp_last_updated__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_last_updated is greater than value (optional)
    pulp_last_updated__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_last_updated is greater than or equal to value (optional)
    pulp_last_updated__isnull = True # bool | Filter results where pulp_last_updated has a null value (optional)
    pulp_last_updated__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_last_updated is less than value (optional)
    pulp_last_updated__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_last_updated is less than or equal to value (optional)
    pulp_last_updated__range = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Filter results where pulp_last_updated is between two comma separated values (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List gem remotes
        api_response = api_instance.list(pulp_domain, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, pulp_last_updated=pulp_last_updated, pulp_last_updated__gt=pulp_last_updated__gt, pulp_last_updated__gte=pulp_last_updated__gte, pulp_last_updated__isnull=pulp_last_updated__isnull, pulp_last_updated__lt=pulp_last_updated__lt, pulp_last_updated__lte=pulp_last_updated__lte, pulp_last_updated__range=pulp_last_updated__range, q=q, fields=fields, exclude_fields=exclude_fields)
        print("The response of RemotesGemApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotesGemApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**| Filter results where name matches value | [optional] 
 **name__contains** | **str**| Filter results where name contains value | [optional] 
 **name__icontains** | **str**| Filter results where name contains value | [optional] 
 **name__iexact** | **str**| Filter results where name matches value | [optional] 
 **name__in** | [**List[str]**](str.md)| Filter results where name is in a comma-separated list of values | [optional] 
 **name__iregex** | **str**| Filter results where name matches regex value | [optional] 
 **name__istartswith** | **str**| Filter results where name starts with value | [optional] 
 **name__regex** | **str**| Filter results where name matches regex value | [optional] 
 **name__startswith** | **str**| Filter results where name starts with value | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;pulp_labels&#x60; - Pulp labels * &#x60;-pulp_labels&#x60; - Pulp labels (descending) * &#x60;url&#x60; - Url * &#x60;-url&#x60; - Url (descending) * &#x60;ca_cert&#x60; - Ca cert * &#x60;-ca_cert&#x60; - Ca cert (descending) * &#x60;client_cert&#x60; - Client cert * &#x60;-client_cert&#x60; - Client cert (descending) * &#x60;client_key&#x60; - Client key * &#x60;-client_key&#x60; - Client key (descending) * &#x60;tls_validation&#x60; - Tls validation * &#x60;-tls_validation&#x60; - Tls validation (descending) * &#x60;username&#x60; - Username * &#x60;-username&#x60; - Username (descending) * &#x60;password&#x60; - Password * &#x60;-password&#x60; - Password (descending) * &#x60;proxy_url&#x60; - Proxy url * &#x60;-proxy_url&#x60; - Proxy url (descending) * &#x60;proxy_username&#x60; - Proxy username * &#x60;-proxy_username&#x60; - Proxy username (descending) * &#x60;proxy_password&#x60; - Proxy password * &#x60;-proxy_password&#x60; - Proxy password (descending) * &#x60;download_concurrency&#x60; - Download concurrency * &#x60;-download_concurrency&#x60; - Download concurrency (descending) * &#x60;max_retries&#x60; - Max retries * &#x60;-max_retries&#x60; - Max retries (descending) * &#x60;policy&#x60; - Policy * &#x60;-policy&#x60; - Policy (descending) * &#x60;total_timeout&#x60; - Total timeout * &#x60;-total_timeout&#x60; - Total timeout (descending) * &#x60;connect_timeout&#x60; - Connect timeout * &#x60;-connect_timeout&#x60; - Connect timeout (descending) * &#x60;sock_connect_timeout&#x60; - Sock connect timeout * &#x60;-sock_connect_timeout&#x60; - Sock connect timeout (descending) * &#x60;sock_read_timeout&#x60; - Sock read timeout * &#x60;-sock_read_timeout&#x60; - Sock read timeout (descending) * &#x60;headers&#x60; - Headers * &#x60;-headers&#x60; - Headers (descending) * &#x60;rate_limit&#x60; - Rate limit * &#x60;-rate_limit&#x60; - Rate limit (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **prn__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_href__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_label_select** | **str**| Filter labels by search string | [optional] 
 **pulp_last_updated** | **datetime**| Filter results where pulp_last_updated matches value | [optional] 
 **pulp_last_updated__gt** | **datetime**| Filter results where pulp_last_updated is greater than value | [optional] 
 **pulp_last_updated__gte** | **datetime**| Filter results where pulp_last_updated is greater than or equal to value | [optional] 
 **pulp_last_updated__isnull** | **bool**| Filter results where pulp_last_updated has a null value | [optional] 
 **pulp_last_updated__lt** | **datetime**| Filter results where pulp_last_updated is less than value | [optional] 
 **pulp_last_updated__lte** | **datetime**| Filter results where pulp_last_updated is less than or equal to value | [optional] 
 **pulp_last_updated__range** | [**List[datetime]**](datetime.md)| Filter results where pulp_last_updated is between two comma separated values | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedgemGemRemoteResponseList**](PaginatedgemGemRemoteResponseList.md)

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

# **list_roles**
> ObjectRolesResponse list_roles(gem_gem_remote_href, fields=fields, exclude_fields=exclude_fields)

List roles

List roles assigned to this object.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.object_roles_response import ObjectRolesResponse
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
    api_instance = pulpcore.client.pulp_gem.RemotesGemApi(api_client)
    gem_gem_remote_href = 'gem_gem_remote_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.list_roles(gem_gem_remote_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of RemotesGemApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotesGemApi->list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_remote_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**ObjectRolesResponse**](ObjectRolesResponse.md)

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

# **my_permissions**
> MyPermissionsResponse my_permissions(gem_gem_remote_href, fields=fields, exclude_fields=exclude_fields)

List user permissions

List permissions available to the current user on this object.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.my_permissions_response import MyPermissionsResponse
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
    api_instance = pulpcore.client.pulp_gem.RemotesGemApi(api_client)
    gem_gem_remote_href = 'gem_gem_remote_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.my_permissions(gem_gem_remote_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of RemotesGemApi->my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotesGemApi->my_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_remote_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**MyPermissionsResponse**](MyPermissionsResponse.md)

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

# **partial_update**
> AsyncOperationResponse partial_update(gem_gem_remote_href, patchedgem_gem_remote)

Update a gem remote

Trigger an asynchronous partial update task

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_gem.models.patchedgem_gem_remote import PatchedgemGemRemote
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
    api_instance = pulpcore.client.pulp_gem.RemotesGemApi(api_client)
    gem_gem_remote_href = 'gem_gem_remote_href_example' # str | 
    patchedgem_gem_remote = pulpcore.client.pulp_gem.PatchedgemGemRemote() # PatchedgemGemRemote | 

    try:
        # Update a gem remote
        api_response = api_instance.partial_update(gem_gem_remote_href, patchedgem_gem_remote)
        print("The response of RemotesGemApi->partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotesGemApi->partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_remote_href** | **str**|  | 
 **patchedgem_gem_remote** | [**PatchedgemGemRemote**](PatchedgemGemRemote.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> GemGemRemoteResponse read(gem_gem_remote_href, fields=fields, exclude_fields=exclude_fields)

Inspect a gem remote

A ViewSet for GemRemote.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.gem_gem_remote_response import GemGemRemoteResponse
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
    api_instance = pulpcore.client.pulp_gem.RemotesGemApi(api_client)
    gem_gem_remote_href = 'gem_gem_remote_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a gem remote
        api_response = api_instance.read(gem_gem_remote_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of RemotesGemApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotesGemApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_remote_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**GemGemRemoteResponse**](GemGemRemoteResponse.md)

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

# **remove_role**
> NestedRoleResponse remove_role(gem_gem_remote_href, nested_role)

Remove a role

Remove a role for this object from users/groups.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.nested_role import NestedRole
from pulpcore.client.pulp_gem.models.nested_role_response import NestedRoleResponse
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
    api_instance = pulpcore.client.pulp_gem.RemotesGemApi(api_client)
    gem_gem_remote_href = 'gem_gem_remote_href_example' # str | 
    nested_role = pulpcore.client.pulp_gem.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.remove_role(gem_gem_remote_href, nested_role)
        print("The response of RemotesGemApi->remove_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotesGemApi->remove_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_remote_href** | **str**|  | 
 **nested_role** | [**NestedRole**](NestedRole.md)|  | 

### Return type

[**NestedRoleResponse**](NestedRoleResponse.md)

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

# **set_label**
> SetLabelResponse set_label(gem_gem_remote_href, set_label)

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
    api_instance = pulpcore.client.pulp_gem.RemotesGemApi(api_client)
    gem_gem_remote_href = 'gem_gem_remote_href_example' # str | 
    set_label = pulpcore.client.pulp_gem.SetLabel() # SetLabel | 

    try:
        # Set a label
        api_response = api_instance.set_label(gem_gem_remote_href, set_label)
        print("The response of RemotesGemApi->set_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotesGemApi->set_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_remote_href** | **str**|  | 
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
> UnsetLabelResponse unset_label(gem_gem_remote_href, unset_label)

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
    api_instance = pulpcore.client.pulp_gem.RemotesGemApi(api_client)
    gem_gem_remote_href = 'gem_gem_remote_href_example' # str | 
    unset_label = pulpcore.client.pulp_gem.UnsetLabel() # UnsetLabel | 

    try:
        # Unset a label
        api_response = api_instance.unset_label(gem_gem_remote_href, unset_label)
        print("The response of RemotesGemApi->unset_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotesGemApi->unset_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_remote_href** | **str**|  | 
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

# **update**
> AsyncOperationResponse update(gem_gem_remote_href, gem_gem_remote)

Update a gem remote

Trigger an asynchronous update task

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_gem.models.gem_gem_remote import GemGemRemote
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
    api_instance = pulpcore.client.pulp_gem.RemotesGemApi(api_client)
    gem_gem_remote_href = 'gem_gem_remote_href_example' # str | 
    gem_gem_remote = pulpcore.client.pulp_gem.GemGemRemote() # GemGemRemote | 

    try:
        # Update a gem remote
        api_response = api_instance.update(gem_gem_remote_href, gem_gem_remote)
        print("The response of RemotesGemApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotesGemApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_remote_href** | **str**|  | 
 **gem_gem_remote** | [**GemGemRemote**](GemGemRemote.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

