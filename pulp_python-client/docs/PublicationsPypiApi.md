# pulpcore.client.pulp_python.PublicationsPypiApi

All URIs are relative to *https://console.redhat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role**](PublicationsPypiApi.md#add_role) | **POST** {python_python_publication_href}add_role/ | Add a role
[**create**](PublicationsPypiApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/publications/python/pypi/ | Create a python publication
[**delete**](PublicationsPypiApi.md#delete) | **DELETE** {python_python_publication_href} | Delete a python publication
[**list**](PublicationsPypiApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/publications/python/pypi/ | List python publications
[**list_roles**](PublicationsPypiApi.md#list_roles) | **GET** {python_python_publication_href}list_roles/ | List roles
[**my_permissions**](PublicationsPypiApi.md#my_permissions) | **GET** {python_python_publication_href}my_permissions/ | List user permissions
[**read**](PublicationsPypiApi.md#read) | **GET** {python_python_publication_href} | Inspect a python publication
[**remove_role**](PublicationsPypiApi.md#remove_role) | **POST** {python_python_publication_href}remove_role/ | Remove a role


# **add_role**
> NestedRoleResponse add_role(python_python_publication_href, nested_role)

Add a role

Add a role for this object to users/groups.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.nested_role import NestedRole
from pulpcore.client.pulp_python.models.nested_role_response import NestedRoleResponse
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
    nested_role = pulpcore.client.pulp_python.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.add_role(python_python_publication_href, nested_role)
        print("The response of PublicationsPypiApi->add_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsPypiApi->add_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_publication_href** | **str**|  | 
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
> AsyncOperationResponse create(pulp_domain, python_python_publication)

Create a python publication

 Dispatches a publish task, which generates metadata that will be used by pip.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_python.models.python_python_publication import PythonPythonPublication
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.PublicationsPypiApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    python_python_publication = pulpcore.client.pulp_python.PythonPythonPublication() # PythonPythonPublication | 

    try:
        # Create a python publication
        api_response = api_instance.create(pulp_domain, python_python_publication)
        print("The response of PublicationsPypiApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsPypiApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **python_python_publication** | [**PythonPythonPublication**](PythonPythonPublication.md)|  | 

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
> delete(python_python_publication_href)

Delete a python publication

 Python Publications refer to the Python Package content in a repository version, and include metadata about that content.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 

    try:
        # Delete a python publication
        api_instance.delete(python_python_publication_href)
    except Exception as e:
        print("Exception when calling PublicationsPypiApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_publication_href** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedpythonPythonPublicationResponseList list(pulp_domain, checkpoint=checkpoint, content=content, content__in=content__in, limit=limit, offset=offset, ordering=ordering, prn__in=prn__in, pulp_created=pulp_created, pulp_created__gt=pulp_created__gt, pulp_created__gte=pulp_created__gte, pulp_created__isnull=pulp_created__isnull, pulp_created__lt=pulp_created__lt, pulp_created__lte=pulp_created__lte, pulp_created__range=pulp_created__range, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository=repository, repository_version=repository_version, fields=fields, exclude_fields=exclude_fields)

List python publications

 Python Publications refer to the Python Package content in a repository version, and include metadata about that content.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.paginatedpython_python_publication_response_list import PaginatedpythonPythonPublicationResponseList
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.PublicationsPypiApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    checkpoint = True # bool | Filter results where checkpoint matches value (optional)
    content = 'content_example' # str | Content Unit referenced by HREF/PRN (optional)
    content__in = ['content__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    ordering = ['ordering_example'] # List[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `complete` - Complete * `-complete` - Complete (descending) * `pass_through` - Pass through * `-pass_through` - Pass through (descending) * `checkpoint` - Checkpoint * `-checkpoint` - Checkpoint (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
    prn__in = ['prn__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_created = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created matches value (optional)
    pulp_created__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is greater than value (optional)
    pulp_created__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is greater than or equal to value (optional)
    pulp_created__isnull = True # bool | Filter results where pulp_created has a null value (optional)
    pulp_created__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is less than value (optional)
    pulp_created__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is less than or equal to value (optional)
    pulp_created__range = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Filter results where pulp_created is between two comma separated values (optional)
    pulp_href__in = ['pulp_href__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_id__in = ['pulp_id__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    repository = 'repository_example' # str | Repository referenced by HREF/PRN (optional)
    repository_version = 'repository_version_example' # str | Repository Version referenced by HREF/PRN (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List python publications
        api_response = api_instance.list(pulp_domain, checkpoint=checkpoint, content=content, content__in=content__in, limit=limit, offset=offset, ordering=ordering, prn__in=prn__in, pulp_created=pulp_created, pulp_created__gt=pulp_created__gt, pulp_created__gte=pulp_created__gte, pulp_created__isnull=pulp_created__isnull, pulp_created__lt=pulp_created__lt, pulp_created__lte=pulp_created__lte, pulp_created__range=pulp_created__range, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository=repository, repository_version=repository_version, fields=fields, exclude_fields=exclude_fields)
        print("The response of PublicationsPypiApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsPypiApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **checkpoint** | **bool**| Filter results where checkpoint matches value | [optional] 
 **content** | **str**| Content Unit referenced by HREF/PRN | [optional] 
 **content__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;complete&#x60; - Complete * &#x60;-complete&#x60; - Complete (descending) * &#x60;pass_through&#x60; - Pass through * &#x60;-pass_through&#x60; - Pass through (descending) * &#x60;checkpoint&#x60; - Checkpoint * &#x60;-checkpoint&#x60; - Checkpoint (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **prn__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_created** | **datetime**| Filter results where pulp_created matches value | [optional] 
 **pulp_created__gt** | **datetime**| Filter results where pulp_created is greater than value | [optional] 
 **pulp_created__gte** | **datetime**| Filter results where pulp_created is greater than or equal to value | [optional] 
 **pulp_created__isnull** | **bool**| Filter results where pulp_created has a null value | [optional] 
 **pulp_created__lt** | **datetime**| Filter results where pulp_created is less than value | [optional] 
 **pulp_created__lte** | **datetime**| Filter results where pulp_created is less than or equal to value | [optional] 
 **pulp_created__range** | [**List[datetime]**](datetime.md)| Filter results where pulp_created is between two comma separated values | [optional] 
 **pulp_href__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **repository** | **str**| Repository referenced by HREF/PRN | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedpythonPythonPublicationResponseList**](PaginatedpythonPythonPublicationResponseList.md)

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
> ObjectRolesResponse list_roles(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)

List roles

List roles assigned to this object.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.object_roles_response import ObjectRolesResponse
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.list_roles(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of PublicationsPypiApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsPypiApi->list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_publication_href** | **str**|  | 
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
> MyPermissionsResponse my_permissions(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)

List user permissions

List permissions available to the current user on this object.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.my_permissions_response import MyPermissionsResponse
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.my_permissions(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of PublicationsPypiApi->my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsPypiApi->my_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_publication_href** | **str**|  | 
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

# **read**
> PythonPythonPublicationResponse read(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)

Inspect a python publication

 Python Publications refer to the Python Package content in a repository version, and include metadata about that content.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.python_python_publication_response import PythonPythonPublicationResponse
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a python publication
        api_response = api_instance.read(python_python_publication_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of PublicationsPypiApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsPypiApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_publication_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PythonPythonPublicationResponse**](PythonPythonPublicationResponse.md)

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
> NestedRoleResponse remove_role(python_python_publication_href, nested_role)

Remove a role

Remove a role for this object from users/groups.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.nested_role import NestedRole
from pulpcore.client.pulp_python.models.nested_role_response import NestedRoleResponse
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.PublicationsPypiApi(api_client)
    python_python_publication_href = 'python_python_publication_href_example' # str | 
    nested_role = pulpcore.client.pulp_python.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.remove_role(python_python_publication_href, nested_role)
        print("The response of PublicationsPypiApi->remove_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsPypiApi->remove_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_publication_href** | **str**|  | 
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

