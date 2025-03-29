# pulpcore.client.pulp_gem.RepositoriesGemApi

All URIs are relative to *https://console.redhat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role**](RepositoriesGemApi.md#add_role) | **POST** {gem_gem_repository_href}add_role/ | Add a role
[**create**](RepositoriesGemApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/repositories/gem/gem/ | Create a gem repository
[**delete**](RepositoriesGemApi.md#delete) | **DELETE** {gem_gem_repository_href} | Delete a gem repository
[**list**](RepositoriesGemApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/repositories/gem/gem/ | List gem repositorys
[**list_roles**](RepositoriesGemApi.md#list_roles) | **GET** {gem_gem_repository_href}list_roles/ | List roles
[**modify**](RepositoriesGemApi.md#modify) | **POST** {gem_gem_repository_href}modify/ | Modify Repository Content
[**my_permissions**](RepositoriesGemApi.md#my_permissions) | **GET** {gem_gem_repository_href}my_permissions/ | List user permissions
[**partial_update**](RepositoriesGemApi.md#partial_update) | **PATCH** {gem_gem_repository_href} | Update a gem repository
[**read**](RepositoriesGemApi.md#read) | **GET** {gem_gem_repository_href} | Inspect a gem repository
[**remove_role**](RepositoriesGemApi.md#remove_role) | **POST** {gem_gem_repository_href}remove_role/ | Remove a role
[**set_label**](RepositoriesGemApi.md#set_label) | **POST** {gem_gem_repository_href}set_label/ | Set a label
[**sync**](RepositoriesGemApi.md#sync) | **POST** {gem_gem_repository_href}sync/ | Sync from a remote
[**unset_label**](RepositoriesGemApi.md#unset_label) | **POST** {gem_gem_repository_href}unset_label/ | Unset a label
[**update**](RepositoriesGemApi.md#update) | **PUT** {gem_gem_repository_href} | Update a gem repository


# **add_role**
> NestedRoleResponse add_role(gem_gem_repository_href, nested_role)

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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    gem_gem_repository_href = 'gem_gem_repository_href_example' # str | 
    nested_role = pulpcore.client.pulp_gem.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.add_role(gem_gem_repository_href, nested_role)
        print("The response of RepositoriesGemApi->add_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->add_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_repository_href** | **str**|  | 
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
> GemGemRepositoryResponse create(pulp_domain, gem_gem_repository)

Create a gem repository

A ViewSet for GemRepository.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.gem_gem_repository import GemGemRepository
from pulpcore.client.pulp_gem.models.gem_gem_repository_response import GemGemRepositoryResponse
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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    gem_gem_repository = pulpcore.client.pulp_gem.GemGemRepository() # GemGemRepository | 

    try:
        # Create a gem repository
        api_response = api_instance.create(pulp_domain, gem_gem_repository)
        print("The response of RepositoriesGemApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **gem_gem_repository** | [**GemGemRepository**](GemGemRepository.md)|  | 

### Return type

[**GemGemRepositoryResponse**](GemGemRepositoryResponse.md)

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
> AsyncOperationResponse delete(gem_gem_repository_href)

Delete a gem repository

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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    gem_gem_repository_href = 'gem_gem_repository_href_example' # str | 

    try:
        # Delete a gem repository
        api_response = api_instance.delete(gem_gem_repository_href)
        print("The response of RepositoriesGemApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_repository_href** | **str**|  | 

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
> PaginatedgemGemRepositoryResponseList list(pulp_domain, latest_with_content=latest_with_content, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, remote=remote, retain_repo_versions=retain_repo_versions, retain_repo_versions__gt=retain_repo_versions__gt, retain_repo_versions__gte=retain_repo_versions__gte, retain_repo_versions__isnull=retain_repo_versions__isnull, retain_repo_versions__lt=retain_repo_versions__lt, retain_repo_versions__lte=retain_repo_versions__lte, retain_repo_versions__ne=retain_repo_versions__ne, retain_repo_versions__range=retain_repo_versions__range, with_content=with_content, fields=fields, exclude_fields=exclude_fields)

List gem repositorys

A ViewSet for GemRepository.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.paginatedgem_gem_repository_response_list import PaginatedgemGemRepositoryResponseList
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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    latest_with_content = 'latest_with_content_example' # str | Content Unit referenced by HREF/PRN (optional)
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
    ordering = ['ordering_example'] # List[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `description` - Description * `-description` - Description (descending) * `next_version` - Next version * `-next_version` - Next version (descending) * `retain_repo_versions` - Retain repo versions * `-retain_repo_versions` - Retain repo versions (descending) * `user_hidden` - User hidden * `-user_hidden` - User hidden (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
    prn__in = ['prn__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_href__in = ['pulp_href__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_id__in = ['pulp_id__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    remote = 'remote_example' # str | Foreign Key referenced by HREF (optional)
    retain_repo_versions = 56 # int | Filter results where retain_repo_versions matches value (optional)
    retain_repo_versions__gt = 56 # int | Filter results where retain_repo_versions is greater than value (optional)
    retain_repo_versions__gte = 56 # int | Filter results where retain_repo_versions is greater than or equal to value (optional)
    retain_repo_versions__isnull = True # bool | Filter results where retain_repo_versions has a null value (optional)
    retain_repo_versions__lt = 56 # int | Filter results where retain_repo_versions is less than value (optional)
    retain_repo_versions__lte = 56 # int | Filter results where retain_repo_versions is less than or equal to value (optional)
    retain_repo_versions__ne = 56 # int | Filter results where retain_repo_versions not equal to value (optional)
    retain_repo_versions__range = [56] # List[int] | Filter results where retain_repo_versions is between two comma separated values (optional)
    with_content = 'with_content_example' # str | Content Unit referenced by HREF/PRN (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List gem repositorys
        api_response = api_instance.list(pulp_domain, latest_with_content=latest_with_content, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, remote=remote, retain_repo_versions=retain_repo_versions, retain_repo_versions__gt=retain_repo_versions__gt, retain_repo_versions__gte=retain_repo_versions__gte, retain_repo_versions__isnull=retain_repo_versions__isnull, retain_repo_versions__lt=retain_repo_versions__lt, retain_repo_versions__lte=retain_repo_versions__lte, retain_repo_versions__ne=retain_repo_versions__ne, retain_repo_versions__range=retain_repo_versions__range, with_content=with_content, fields=fields, exclude_fields=exclude_fields)
        print("The response of RepositoriesGemApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **latest_with_content** | **str**| Content Unit referenced by HREF/PRN | [optional] 
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
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;pulp_labels&#x60; - Pulp labels * &#x60;-pulp_labels&#x60; - Pulp labels (descending) * &#x60;description&#x60; - Description * &#x60;-description&#x60; - Description (descending) * &#x60;next_version&#x60; - Next version * &#x60;-next_version&#x60; - Next version (descending) * &#x60;retain_repo_versions&#x60; - Retain repo versions * &#x60;-retain_repo_versions&#x60; - Retain repo versions (descending) * &#x60;user_hidden&#x60; - User hidden * &#x60;-user_hidden&#x60; - User hidden (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **prn__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_href__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_label_select** | **str**| Filter labels by search string | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **remote** | **str**| Foreign Key referenced by HREF | [optional] 
 **retain_repo_versions** | **int**| Filter results where retain_repo_versions matches value | [optional] 
 **retain_repo_versions__gt** | **int**| Filter results where retain_repo_versions is greater than value | [optional] 
 **retain_repo_versions__gte** | **int**| Filter results where retain_repo_versions is greater than or equal to value | [optional] 
 **retain_repo_versions__isnull** | **bool**| Filter results where retain_repo_versions has a null value | [optional] 
 **retain_repo_versions__lt** | **int**| Filter results where retain_repo_versions is less than value | [optional] 
 **retain_repo_versions__lte** | **int**| Filter results where retain_repo_versions is less than or equal to value | [optional] 
 **retain_repo_versions__ne** | **int**| Filter results where retain_repo_versions not equal to value | [optional] 
 **retain_repo_versions__range** | [**List[int]**](int.md)| Filter results where retain_repo_versions is between two comma separated values | [optional] 
 **with_content** | **str**| Content Unit referenced by HREF/PRN | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedgemGemRepositoryResponseList**](PaginatedgemGemRepositoryResponseList.md)

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
> ObjectRolesResponse list_roles(gem_gem_repository_href, fields=fields, exclude_fields=exclude_fields)

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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    gem_gem_repository_href = 'gem_gem_repository_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.list_roles(gem_gem_repository_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of RepositoriesGemApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_repository_href** | **str**|  | 
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

# **modify**
> AsyncOperationResponse modify(gem_gem_repository_href, repository_add_remove_content)

Modify Repository Content

Trigger an asynchronous task to create a new repository version.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_gem.models.repository_add_remove_content import RepositoryAddRemoveContent
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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    gem_gem_repository_href = 'gem_gem_repository_href_example' # str | 
    repository_add_remove_content = pulpcore.client.pulp_gem.RepositoryAddRemoveContent() # RepositoryAddRemoveContent | 

    try:
        # Modify Repository Content
        api_response = api_instance.modify(gem_gem_repository_href, repository_add_remove_content)
        print("The response of RepositoriesGemApi->modify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->modify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_repository_href** | **str**|  | 
 **repository_add_remove_content** | [**RepositoryAddRemoveContent**](RepositoryAddRemoveContent.md)|  | 

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

# **my_permissions**
> MyPermissionsResponse my_permissions(gem_gem_repository_href, fields=fields, exclude_fields=exclude_fields)

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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    gem_gem_repository_href = 'gem_gem_repository_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.my_permissions(gem_gem_repository_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of RepositoriesGemApi->my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->my_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_repository_href** | **str**|  | 
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
> AsyncOperationResponse partial_update(gem_gem_repository_href, patchedgem_gem_repository)

Update a gem repository

Trigger an asynchronous partial update task

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_gem.models.patchedgem_gem_repository import PatchedgemGemRepository
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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    gem_gem_repository_href = 'gem_gem_repository_href_example' # str | 
    patchedgem_gem_repository = pulpcore.client.pulp_gem.PatchedgemGemRepository() # PatchedgemGemRepository | 

    try:
        # Update a gem repository
        api_response = api_instance.partial_update(gem_gem_repository_href, patchedgem_gem_repository)
        print("The response of RepositoriesGemApi->partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_repository_href** | **str**|  | 
 **patchedgem_gem_repository** | [**PatchedgemGemRepository**](PatchedgemGemRepository.md)|  | 

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
> GemGemRepositoryResponse read(gem_gem_repository_href, fields=fields, exclude_fields=exclude_fields)

Inspect a gem repository

A ViewSet for GemRepository.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.gem_gem_repository_response import GemGemRepositoryResponse
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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    gem_gem_repository_href = 'gem_gem_repository_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a gem repository
        api_response = api_instance.read(gem_gem_repository_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of RepositoriesGemApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_repository_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**GemGemRepositoryResponse**](GemGemRepositoryResponse.md)

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
> NestedRoleResponse remove_role(gem_gem_repository_href, nested_role)

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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    gem_gem_repository_href = 'gem_gem_repository_href_example' # str | 
    nested_role = pulpcore.client.pulp_gem.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.remove_role(gem_gem_repository_href, nested_role)
        print("The response of RepositoriesGemApi->remove_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->remove_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_repository_href** | **str**|  | 
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
> SetLabelResponse set_label(gem_gem_repository_href, set_label)

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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    gem_gem_repository_href = 'gem_gem_repository_href_example' # str | 
    set_label = pulpcore.client.pulp_gem.SetLabel() # SetLabel | 

    try:
        # Set a label
        api_response = api_instance.set_label(gem_gem_repository_href, set_label)
        print("The response of RepositoriesGemApi->set_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->set_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_repository_href** | **str**|  | 
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

# **sync**
> AsyncOperationResponse sync(gem_gem_repository_href, repository_sync_url)

Sync from a remote

Trigger an asynchronous task to sync gem content.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_gem.models.repository_sync_url import RepositorySyncURL
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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    gem_gem_repository_href = 'gem_gem_repository_href_example' # str | 
    repository_sync_url = pulpcore.client.pulp_gem.RepositorySyncURL() # RepositorySyncURL | 

    try:
        # Sync from a remote
        api_response = api_instance.sync(gem_gem_repository_href, repository_sync_url)
        print("The response of RepositoriesGemApi->sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_repository_href** | **str**|  | 
 **repository_sync_url** | [**RepositorySyncURL**](RepositorySyncURL.md)|  | 

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

# **unset_label**
> UnsetLabelResponse unset_label(gem_gem_repository_href, unset_label)

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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    gem_gem_repository_href = 'gem_gem_repository_href_example' # str | 
    unset_label = pulpcore.client.pulp_gem.UnsetLabel() # UnsetLabel | 

    try:
        # Unset a label
        api_response = api_instance.unset_label(gem_gem_repository_href, unset_label)
        print("The response of RepositoriesGemApi->unset_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->unset_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_repository_href** | **str**|  | 
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
> AsyncOperationResponse update(gem_gem_repository_href, gem_gem_repository)

Update a gem repository

Trigger an asynchronous update task

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_gem.models.gem_gem_repository import GemGemRepository
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
    api_instance = pulpcore.client.pulp_gem.RepositoriesGemApi(api_client)
    gem_gem_repository_href = 'gem_gem_repository_href_example' # str | 
    gem_gem_repository = pulpcore.client.pulp_gem.GemGemRepository() # GemGemRepository | 

    try:
        # Update a gem repository
        api_response = api_instance.update(gem_gem_repository_href, gem_gem_repository)
        print("The response of RepositoriesGemApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesGemApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_repository_href** | **str**|  | 
 **gem_gem_repository** | [**GemGemRepository**](GemGemRepository.md)|  | 

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

