# pulpcore.client.pulpcore.UpstreamPulpsApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role**](UpstreamPulpsApi.md#add_role) | **POST** {upstream_pulp_href}add_role/ | Add a role
[**create**](UpstreamPulpsApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/upstream-pulps/ | Create an upstream pulp
[**delete**](UpstreamPulpsApi.md#delete) | **DELETE** {upstream_pulp_href} | Delete an upstream pulp
[**list**](UpstreamPulpsApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/upstream-pulps/ | List upstream pulps
[**list_roles**](UpstreamPulpsApi.md#list_roles) | **GET** {upstream_pulp_href}list_roles/ | List roles
[**my_permissions**](UpstreamPulpsApi.md#my_permissions) | **GET** {upstream_pulp_href}my_permissions/ | List user permissions
[**partial_update**](UpstreamPulpsApi.md#partial_update) | **PATCH** {upstream_pulp_href} | Update an upstream pulp
[**read**](UpstreamPulpsApi.md#read) | **GET** {upstream_pulp_href} | Inspect an upstream pulp
[**remove_role**](UpstreamPulpsApi.md#remove_role) | **POST** {upstream_pulp_href}remove_role/ | Remove a role
[**replicate**](UpstreamPulpsApi.md#replicate) | **POST** {upstream_pulp_href}replicate/ | Replicate
[**update**](UpstreamPulpsApi.md#update) | **PUT** {upstream_pulp_href} | Update an upstream pulp


# **add_role**
> NestedRoleResponse add_role(upstream_pulp_href, nested_role)

Add a role

Add a role for this object to users/groups.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.nested_role import NestedRole
from pulpcore.client.pulpcore.models.nested_role_response import NestedRoleResponse
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
    api_instance = pulpcore.client.pulpcore.UpstreamPulpsApi(api_client)
    upstream_pulp_href = 'upstream_pulp_href_example' # str | 
    nested_role = pulpcore.client.pulpcore.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.add_role(upstream_pulp_href, nested_role)
        print("The response of UpstreamPulpsApi->add_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamPulpsApi->add_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_pulp_href** | **str**|  | 
 **nested_role** | [**NestedRole**](NestedRole.md)|  | 

### Return type

[**NestedRoleResponse**](NestedRoleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> UpstreamPulpResponse create(pulp_domain, upstream_pulp)

Create an upstream pulp

API for configuring an upstream Pulp to replicate. This API is provided as a tech preview.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.upstream_pulp import UpstreamPulp
from pulpcore.client.pulpcore.models.upstream_pulp_response import UpstreamPulpResponse
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
    api_instance = pulpcore.client.pulpcore.UpstreamPulpsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    upstream_pulp = pulpcore.client.pulpcore.UpstreamPulp() # UpstreamPulp | 

    try:
        # Create an upstream pulp
        api_response = api_instance.create(pulp_domain, upstream_pulp)
        print("The response of UpstreamPulpsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamPulpsApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **upstream_pulp** | [**UpstreamPulp**](UpstreamPulp.md)|  | 

### Return type

[**UpstreamPulpResponse**](UpstreamPulpResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(upstream_pulp_href)

Delete an upstream pulp

API for configuring an upstream Pulp to replicate. This API is provided as a tech preview.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
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
    api_instance = pulpcore.client.pulpcore.UpstreamPulpsApi(api_client)
    upstream_pulp_href = 'upstream_pulp_href_example' # str | 

    try:
        # Delete an upstream pulp
        api_instance.delete(upstream_pulp_href)
    except Exception as e:
        print("Exception when calling UpstreamPulpsApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_pulp_href** | **str**|  | 

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
> PaginatedUpstreamPulpResponseList list(pulp_domain, base_url=base_url, base_url__contains=base_url__contains, base_url__icontains=base_url__icontains, base_url__iexact=base_url__iexact, base_url__in=base_url__in, base_url__iregex=base_url__iregex, base_url__istartswith=base_url__istartswith, base_url__regex=base_url__regex, base_url__startswith=base_url__startswith, last_replication=last_replication, last_replication__gt=last_replication__gt, last_replication__gte=last_replication__gte, last_replication__isnull=last_replication__isnull, last_replication__lt=last_replication__lt, last_replication__lte=last_replication__lte, last_replication__range=last_replication__range, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, fields=fields, exclude_fields=exclude_fields)

List upstream pulps

API for configuring an upstream Pulp to replicate. This API is provided as a tech preview.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.paginated_upstream_pulp_response_list import PaginatedUpstreamPulpResponseList
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
    api_instance = pulpcore.client.pulpcore.UpstreamPulpsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    base_url = 'base_url_example' # str | Filter results where base_url matches value (optional)
    base_url__contains = 'base_url__contains_example' # str | Filter results where base_url contains value (optional)
    base_url__icontains = 'base_url__icontains_example' # str | Filter results where base_url contains value (optional)
    base_url__iexact = 'base_url__iexact_example' # str | Filter results where base_url matches value (optional)
    base_url__in = ['base_url__in_example'] # List[str] | Filter results where base_url is in a comma-separated list of values (optional)
    base_url__iregex = 'base_url__iregex_example' # str | Filter results where base_url matches regex value (optional)
    base_url__istartswith = 'base_url__istartswith_example' # str | Filter results where base_url starts with value (optional)
    base_url__regex = 'base_url__regex_example' # str | Filter results where base_url matches regex value (optional)
    base_url__startswith = 'base_url__startswith_example' # str | Filter results where base_url starts with value (optional)
    last_replication = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_replication matches value (optional)
    last_replication__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_replication is greater than value (optional)
    last_replication__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_replication is greater than or equal to value (optional)
    last_replication__isnull = True # bool | Filter results where last_replication has a null value (optional)
    last_replication__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_replication is less than value (optional)
    last_replication__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_replication is less than or equal to value (optional)
    last_replication__range = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Filter results where last_replication is between two comma separated values (optional)
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
    ordering = ['ordering_example'] # List[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `name` - Name * `-name` - Name (descending) * `base_url` - Base url * `-base_url` - Base url (descending) * `api_root` - Api root * `-api_root` - Api root (descending) * `domain` - Domain * `-domain` - Domain (descending) * `ca_cert` - Ca cert * `-ca_cert` - Ca cert (descending) * `client_cert` - Client cert * `-client_cert` - Client cert (descending) * `client_key` - Client key * `-client_key` - Client key (descending) * `tls_validation` - Tls validation * `-tls_validation` - Tls validation (descending) * `username` - Username * `-username` - Username (descending) * `password` - Password * `-password` - Password (descending) * `q_select` - Q select * `-q_select` - Q select (descending) * `last_replication` - Last replication * `-last_replication` - Last replication (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
    prn__in = ['prn__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_href__in = ['pulp_href__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_id__in = ['pulp_id__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List upstream pulps
        api_response = api_instance.list(pulp_domain, base_url=base_url, base_url__contains=base_url__contains, base_url__icontains=base_url__icontains, base_url__iexact=base_url__iexact, base_url__in=base_url__in, base_url__iregex=base_url__iregex, base_url__istartswith=base_url__istartswith, base_url__regex=base_url__regex, base_url__startswith=base_url__startswith, last_replication=last_replication, last_replication__gt=last_replication__gt, last_replication__gte=last_replication__gte, last_replication__isnull=last_replication__isnull, last_replication__lt=last_replication__lt, last_replication__lte=last_replication__lte, last_replication__range=last_replication__range, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, fields=fields, exclude_fields=exclude_fields)
        print("The response of UpstreamPulpsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamPulpsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **base_url** | **str**| Filter results where base_url matches value | [optional] 
 **base_url__contains** | **str**| Filter results where base_url contains value | [optional] 
 **base_url__icontains** | **str**| Filter results where base_url contains value | [optional] 
 **base_url__iexact** | **str**| Filter results where base_url matches value | [optional] 
 **base_url__in** | [**List[str]**](str.md)| Filter results where base_url is in a comma-separated list of values | [optional] 
 **base_url__iregex** | **str**| Filter results where base_url matches regex value | [optional] 
 **base_url__istartswith** | **str**| Filter results where base_url starts with value | [optional] 
 **base_url__regex** | **str**| Filter results where base_url matches regex value | [optional] 
 **base_url__startswith** | **str**| Filter results where base_url starts with value | [optional] 
 **last_replication** | **datetime**| Filter results where last_replication matches value | [optional] 
 **last_replication__gt** | **datetime**| Filter results where last_replication is greater than value | [optional] 
 **last_replication__gte** | **datetime**| Filter results where last_replication is greater than or equal to value | [optional] 
 **last_replication__isnull** | **bool**| Filter results where last_replication has a null value | [optional] 
 **last_replication__lt** | **datetime**| Filter results where last_replication is less than value | [optional] 
 **last_replication__lte** | **datetime**| Filter results where last_replication is less than or equal to value | [optional] 
 **last_replication__range** | [**List[datetime]**](datetime.md)| Filter results where last_replication is between two comma separated values | [optional] 
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
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;base_url&#x60; - Base url * &#x60;-base_url&#x60; - Base url (descending) * &#x60;api_root&#x60; - Api root * &#x60;-api_root&#x60; - Api root (descending) * &#x60;domain&#x60; - Domain * &#x60;-domain&#x60; - Domain (descending) * &#x60;ca_cert&#x60; - Ca cert * &#x60;-ca_cert&#x60; - Ca cert (descending) * &#x60;client_cert&#x60; - Client cert * &#x60;-client_cert&#x60; - Client cert (descending) * &#x60;client_key&#x60; - Client key * &#x60;-client_key&#x60; - Client key (descending) * &#x60;tls_validation&#x60; - Tls validation * &#x60;-tls_validation&#x60; - Tls validation (descending) * &#x60;username&#x60; - Username * &#x60;-username&#x60; - Username (descending) * &#x60;password&#x60; - Password * &#x60;-password&#x60; - Password (descending) * &#x60;q_select&#x60; - Q select * &#x60;-q_select&#x60; - Q select (descending) * &#x60;last_replication&#x60; - Last replication * &#x60;-last_replication&#x60; - Last replication (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **prn__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_href__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedUpstreamPulpResponseList**](PaginatedUpstreamPulpResponseList.md)

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

# **list_roles**
> ObjectRolesResponse list_roles(upstream_pulp_href, fields=fields, exclude_fields=exclude_fields)

List roles

List roles assigned to this object.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.object_roles_response import ObjectRolesResponse
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
    api_instance = pulpcore.client.pulpcore.UpstreamPulpsApi(api_client)
    upstream_pulp_href = 'upstream_pulp_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.list_roles(upstream_pulp_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of UpstreamPulpsApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamPulpsApi->list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_pulp_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**ObjectRolesResponse**](ObjectRolesResponse.md)

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

# **my_permissions**
> MyPermissionsResponse my_permissions(upstream_pulp_href, fields=fields, exclude_fields=exclude_fields)

List user permissions

List permissions available to the current user on this object.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.my_permissions_response import MyPermissionsResponse
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
    api_instance = pulpcore.client.pulpcore.UpstreamPulpsApi(api_client)
    upstream_pulp_href = 'upstream_pulp_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.my_permissions(upstream_pulp_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of UpstreamPulpsApi->my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamPulpsApi->my_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_pulp_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**MyPermissionsResponse**](MyPermissionsResponse.md)

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

# **partial_update**
> UpstreamPulpResponse partial_update(upstream_pulp_href, patched_upstream_pulp)

Update an upstream pulp

API for configuring an upstream Pulp to replicate. This API is provided as a tech preview.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.patched_upstream_pulp import PatchedUpstreamPulp
from pulpcore.client.pulpcore.models.upstream_pulp_response import UpstreamPulpResponse
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
    api_instance = pulpcore.client.pulpcore.UpstreamPulpsApi(api_client)
    upstream_pulp_href = 'upstream_pulp_href_example' # str | 
    patched_upstream_pulp = pulpcore.client.pulpcore.PatchedUpstreamPulp() # PatchedUpstreamPulp | 

    try:
        # Update an upstream pulp
        api_response = api_instance.partial_update(upstream_pulp_href, patched_upstream_pulp)
        print("The response of UpstreamPulpsApi->partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamPulpsApi->partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_pulp_href** | **str**|  | 
 **patched_upstream_pulp** | [**PatchedUpstreamPulp**](PatchedUpstreamPulp.md)|  | 

### Return type

[**UpstreamPulpResponse**](UpstreamPulpResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> UpstreamPulpResponse read(upstream_pulp_href, fields=fields, exclude_fields=exclude_fields)

Inspect an upstream pulp

API for configuring an upstream Pulp to replicate. This API is provided as a tech preview.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.upstream_pulp_response import UpstreamPulpResponse
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
    api_instance = pulpcore.client.pulpcore.UpstreamPulpsApi(api_client)
    upstream_pulp_href = 'upstream_pulp_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an upstream pulp
        api_response = api_instance.read(upstream_pulp_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of UpstreamPulpsApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamPulpsApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_pulp_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**UpstreamPulpResponse**](UpstreamPulpResponse.md)

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

# **remove_role**
> NestedRoleResponse remove_role(upstream_pulp_href, nested_role)

Remove a role

Remove a role for this object from users/groups.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.nested_role import NestedRole
from pulpcore.client.pulpcore.models.nested_role_response import NestedRoleResponse
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
    api_instance = pulpcore.client.pulpcore.UpstreamPulpsApi(api_client)
    upstream_pulp_href = 'upstream_pulp_href_example' # str | 
    nested_role = pulpcore.client.pulpcore.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.remove_role(upstream_pulp_href, nested_role)
        print("The response of UpstreamPulpsApi->remove_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamPulpsApi->remove_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_pulp_href** | **str**|  | 
 **nested_role** | [**NestedRole**](NestedRole.md)|  | 

### Return type

[**NestedRoleResponse**](NestedRoleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replicate**
> TaskGroupOperationResponse replicate(upstream_pulp_href)

Replicate

Trigger an asynchronous repository replication task group. This API is provided as a tech preview.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.task_group_operation_response import TaskGroupOperationResponse
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
    api_instance = pulpcore.client.pulpcore.UpstreamPulpsApi(api_client)
    upstream_pulp_href = 'upstream_pulp_href_example' # str | 

    try:
        # Replicate
        api_response = api_instance.replicate(upstream_pulp_href)
        print("The response of UpstreamPulpsApi->replicate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamPulpsApi->replicate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_pulp_href** | **str**|  | 

### Return type

[**TaskGroupOperationResponse**](TaskGroupOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> UpstreamPulpResponse update(upstream_pulp_href, upstream_pulp)

Update an upstream pulp

API for configuring an upstream Pulp to replicate. This API is provided as a tech preview.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.upstream_pulp import UpstreamPulp
from pulpcore.client.pulpcore.models.upstream_pulp_response import UpstreamPulpResponse
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
    api_instance = pulpcore.client.pulpcore.UpstreamPulpsApi(api_client)
    upstream_pulp_href = 'upstream_pulp_href_example' # str | 
    upstream_pulp = pulpcore.client.pulpcore.UpstreamPulp() # UpstreamPulp | 

    try:
        # Update an upstream pulp
        api_response = api_instance.update(upstream_pulp_href, upstream_pulp)
        print("The response of UpstreamPulpsApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamPulpsApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_pulp_href** | **str**|  | 
 **upstream_pulp** | [**UpstreamPulp**](UpstreamPulp.md)|  | 

### Return type

[**UpstreamPulpResponse**](UpstreamPulpResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

