# pulpcore.client.pulp_gem.DistributionsGemApi

All URIs are relative to *https://console.redhat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role**](DistributionsGemApi.md#add_role) | **POST** {gem_gem_distribution_href}add_role/ | Add a role
[**create**](DistributionsGemApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/distributions/gem/gem/ | Create a gem distribution
[**delete**](DistributionsGemApi.md#delete) | **DELETE** {gem_gem_distribution_href} | Delete a gem distribution
[**list**](DistributionsGemApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/distributions/gem/gem/ | List gem distributions
[**list_roles**](DistributionsGemApi.md#list_roles) | **GET** {gem_gem_distribution_href}list_roles/ | List roles
[**my_permissions**](DistributionsGemApi.md#my_permissions) | **GET** {gem_gem_distribution_href}my_permissions/ | List user permissions
[**partial_update**](DistributionsGemApi.md#partial_update) | **PATCH** {gem_gem_distribution_href} | Update a gem distribution
[**read**](DistributionsGemApi.md#read) | **GET** {gem_gem_distribution_href} | Inspect a gem distribution
[**remove_role**](DistributionsGemApi.md#remove_role) | **POST** {gem_gem_distribution_href}remove_role/ | Remove a role
[**set_label**](DistributionsGemApi.md#set_label) | **POST** {gem_gem_distribution_href}set_label/ | Set a label
[**unset_label**](DistributionsGemApi.md#unset_label) | **POST** {gem_gem_distribution_href}unset_label/ | Unset a label
[**update**](DistributionsGemApi.md#update) | **PUT** {gem_gem_distribution_href} | Update a gem distribution


# **add_role**
> NestedRoleResponse add_role(gem_gem_distribution_href, nested_role)

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
    api_instance = pulpcore.client.pulp_gem.DistributionsGemApi(api_client)
    gem_gem_distribution_href = 'gem_gem_distribution_href_example' # str | 
    nested_role = pulpcore.client.pulp_gem.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.add_role(gem_gem_distribution_href, nested_role)
        print("The response of DistributionsGemApi->add_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsGemApi->add_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_distribution_href** | **str**|  | 
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
> AsyncOperationResponse create(pulp_domain, gem_gem_distribution)

Create a gem distribution

Trigger an asynchronous create task

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_gem.models.gem_gem_distribution import GemGemDistribution
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
    api_instance = pulpcore.client.pulp_gem.DistributionsGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    gem_gem_distribution = pulpcore.client.pulp_gem.GemGemDistribution() # GemGemDistribution | 

    try:
        # Create a gem distribution
        api_response = api_instance.create(pulp_domain, gem_gem_distribution)
        print("The response of DistributionsGemApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsGemApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **gem_gem_distribution** | [**GemGemDistribution**](GemGemDistribution.md)|  | 

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

# **delete**
> AsyncOperationResponse delete(gem_gem_distribution_href)

Delete a gem distribution

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
    api_instance = pulpcore.client.pulp_gem.DistributionsGemApi(api_client)
    gem_gem_distribution_href = 'gem_gem_distribution_href_example' # str | 

    try:
        # Delete a gem distribution
        api_response = api_instance.delete(gem_gem_distribution_href)
        print("The response of DistributionsGemApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsGemApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_distribution_href** | **str**|  | 

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
> PaginatedgemGemDistributionResponseList list(pulp_domain, base_path=base_path, base_path__contains=base_path__contains, base_path__icontains=base_path__icontains, base_path__in=base_path__in, checkpoint=checkpoint, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, repository=repository, repository__in=repository__in, with_content=with_content, fields=fields, exclude_fields=exclude_fields)

List gem distributions

ViewSet for GemDistributions.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.paginatedgem_gem_distribution_response_list import PaginatedgemGemDistributionResponseList
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
    api_instance = pulpcore.client.pulp_gem.DistributionsGemApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    base_path = 'base_path_example' # str | Filter results where base_path matches value (optional)
    base_path__contains = 'base_path__contains_example' # str | Filter results where base_path contains value (optional)
    base_path__icontains = 'base_path__icontains_example' # str | Filter results where base_path contains value (optional)
    base_path__in = ['base_path__in_example'] # List[str] | Filter results where base_path is in a comma-separated list of values (optional)
    checkpoint = True # bool | Filter results where checkpoint matches value (optional)
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
    ordering = ['ordering_example'] # List[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `base_path` - Base path * `-base_path` - Base path (descending) * `hidden` - Hidden * `-hidden` - Hidden (descending) * `checkpoint` - Checkpoint * `-checkpoint` - Checkpoint (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
    prn__in = ['prn__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_href__in = ['pulp_href__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_id__in = ['pulp_id__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    repository = 'repository_example' # str | Filter results where repository matches value (optional)
    repository__in = ['repository__in_example'] # List[str] | Filter results where repository is in a comma-separated list of values (optional)
    with_content = 'with_content_example' # str | Filter distributions based on the content served by them (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List gem distributions
        api_response = api_instance.list(pulp_domain, base_path=base_path, base_path__contains=base_path__contains, base_path__icontains=base_path__icontains, base_path__in=base_path__in, checkpoint=checkpoint, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, repository=repository, repository__in=repository__in, with_content=with_content, fields=fields, exclude_fields=exclude_fields)
        print("The response of DistributionsGemApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsGemApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **base_path** | **str**| Filter results where base_path matches value | [optional] 
 **base_path__contains** | **str**| Filter results where base_path contains value | [optional] 
 **base_path__icontains** | **str**| Filter results where base_path contains value | [optional] 
 **base_path__in** | [**List[str]**](str.md)| Filter results where base_path is in a comma-separated list of values | [optional] 
 **checkpoint** | **bool**| Filter results where checkpoint matches value | [optional] 
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
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;pulp_labels&#x60; - Pulp labels * &#x60;-pulp_labels&#x60; - Pulp labels (descending) * &#x60;base_path&#x60; - Base path * &#x60;-base_path&#x60; - Base path (descending) * &#x60;hidden&#x60; - Hidden * &#x60;-hidden&#x60; - Hidden (descending) * &#x60;checkpoint&#x60; - Checkpoint * &#x60;-checkpoint&#x60; - Checkpoint (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **prn__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_href__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_label_select** | **str**| Filter labels by search string | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **repository** | **str**| Filter results where repository matches value | [optional] 
 **repository__in** | [**List[str]**](str.md)| Filter results where repository is in a comma-separated list of values | [optional] 
 **with_content** | **str**| Filter distributions based on the content served by them | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedgemGemDistributionResponseList**](PaginatedgemGemDistributionResponseList.md)

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
> ObjectRolesResponse list_roles(gem_gem_distribution_href, fields=fields, exclude_fields=exclude_fields)

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
    api_instance = pulpcore.client.pulp_gem.DistributionsGemApi(api_client)
    gem_gem_distribution_href = 'gem_gem_distribution_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.list_roles(gem_gem_distribution_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of DistributionsGemApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsGemApi->list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_distribution_href** | **str**|  | 
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
> MyPermissionsResponse my_permissions(gem_gem_distribution_href, fields=fields, exclude_fields=exclude_fields)

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
    api_instance = pulpcore.client.pulp_gem.DistributionsGemApi(api_client)
    gem_gem_distribution_href = 'gem_gem_distribution_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.my_permissions(gem_gem_distribution_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of DistributionsGemApi->my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsGemApi->my_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_distribution_href** | **str**|  | 
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
> AsyncOperationResponse partial_update(gem_gem_distribution_href, patchedgem_gem_distribution)

Update a gem distribution

Trigger an asynchronous partial update task

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_gem.models.patchedgem_gem_distribution import PatchedgemGemDistribution
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
    api_instance = pulpcore.client.pulp_gem.DistributionsGemApi(api_client)
    gem_gem_distribution_href = 'gem_gem_distribution_href_example' # str | 
    patchedgem_gem_distribution = pulpcore.client.pulp_gem.PatchedgemGemDistribution() # PatchedgemGemDistribution | 

    try:
        # Update a gem distribution
        api_response = api_instance.partial_update(gem_gem_distribution_href, patchedgem_gem_distribution)
        print("The response of DistributionsGemApi->partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsGemApi->partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_distribution_href** | **str**|  | 
 **patchedgem_gem_distribution** | [**PatchedgemGemDistribution**](PatchedgemGemDistribution.md)|  | 

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
> GemGemDistributionResponse read(gem_gem_distribution_href, fields=fields, exclude_fields=exclude_fields)

Inspect a gem distribution

ViewSet for GemDistributions.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.gem_gem_distribution_response import GemGemDistributionResponse
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
    api_instance = pulpcore.client.pulp_gem.DistributionsGemApi(api_client)
    gem_gem_distribution_href = 'gem_gem_distribution_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a gem distribution
        api_response = api_instance.read(gem_gem_distribution_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of DistributionsGemApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsGemApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_distribution_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**GemGemDistributionResponse**](GemGemDistributionResponse.md)

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
> NestedRoleResponse remove_role(gem_gem_distribution_href, nested_role)

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
    api_instance = pulpcore.client.pulp_gem.DistributionsGemApi(api_client)
    gem_gem_distribution_href = 'gem_gem_distribution_href_example' # str | 
    nested_role = pulpcore.client.pulp_gem.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.remove_role(gem_gem_distribution_href, nested_role)
        print("The response of DistributionsGemApi->remove_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsGemApi->remove_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_distribution_href** | **str**|  | 
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
> SetLabelResponse set_label(gem_gem_distribution_href, set_label)

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
    api_instance = pulpcore.client.pulp_gem.DistributionsGemApi(api_client)
    gem_gem_distribution_href = 'gem_gem_distribution_href_example' # str | 
    set_label = pulpcore.client.pulp_gem.SetLabel() # SetLabel | 

    try:
        # Set a label
        api_response = api_instance.set_label(gem_gem_distribution_href, set_label)
        print("The response of DistributionsGemApi->set_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsGemApi->set_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_distribution_href** | **str**|  | 
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_label**
> UnsetLabelResponse unset_label(gem_gem_distribution_href, unset_label)

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
    api_instance = pulpcore.client.pulp_gem.DistributionsGemApi(api_client)
    gem_gem_distribution_href = 'gem_gem_distribution_href_example' # str | 
    unset_label = pulpcore.client.pulp_gem.UnsetLabel() # UnsetLabel | 

    try:
        # Unset a label
        api_response = api_instance.unset_label(gem_gem_distribution_href, unset_label)
        print("The response of DistributionsGemApi->unset_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsGemApi->unset_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_distribution_href** | **str**|  | 
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> AsyncOperationResponse update(gem_gem_distribution_href, gem_gem_distribution)

Update a gem distribution

Trigger an asynchronous update task

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_gem
from pulpcore.client.pulp_gem.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_gem.models.gem_gem_distribution import GemGemDistribution
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
    api_instance = pulpcore.client.pulp_gem.DistributionsGemApi(api_client)
    gem_gem_distribution_href = 'gem_gem_distribution_href_example' # str | 
    gem_gem_distribution = pulpcore.client.pulp_gem.GemGemDistribution() # GemGemDistribution | 

    try:
        # Update a gem distribution
        api_response = api_instance.update(gem_gem_distribution_href, gem_gem_distribution)
        print("The response of DistributionsGemApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsGemApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gem_gem_distribution_href** | **str**|  | 
 **gem_gem_distribution** | [**GemGemDistribution**](GemGemDistribution.md)|  | 

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

