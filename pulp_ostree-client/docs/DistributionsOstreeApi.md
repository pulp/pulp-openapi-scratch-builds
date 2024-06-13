# pulpcore.client.pulp_ostree.DistributionsOstreeApi

All URIs are relative to *http://pulp-api-svc.pulp-prod.svc.cluster.local:24817*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role**](DistributionsOstreeApi.md#add_role) | **POST** {ostree_ostree_distribution_href}add_role/ | Add a role
[**create**](DistributionsOstreeApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/distributions/ostree/ostree/ | Create an ostree distribution
[**delete**](DistributionsOstreeApi.md#delete) | **DELETE** {ostree_ostree_distribution_href} | Delete an ostree distribution
[**list**](DistributionsOstreeApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/distributions/ostree/ostree/ | List ostree distributions
[**list_roles**](DistributionsOstreeApi.md#list_roles) | **GET** {ostree_ostree_distribution_href}list_roles/ | List roles
[**my_permissions**](DistributionsOstreeApi.md#my_permissions) | **GET** {ostree_ostree_distribution_href}my_permissions/ | List user permissions
[**partial_update**](DistributionsOstreeApi.md#partial_update) | **PATCH** {ostree_ostree_distribution_href} | Update an ostree distribution
[**read**](DistributionsOstreeApi.md#read) | **GET** {ostree_ostree_distribution_href} | Inspect an ostree distribution
[**remove_role**](DistributionsOstreeApi.md#remove_role) | **POST** {ostree_ostree_distribution_href}remove_role/ | Remove a role
[**set_label**](DistributionsOstreeApi.md#set_label) | **POST** {ostree_ostree_distribution_href}set_label/ | Set a label
[**unset_label**](DistributionsOstreeApi.md#unset_label) | **POST** {ostree_ostree_distribution_href}unset_label/ | Unset a label
[**update**](DistributionsOstreeApi.md#update) | **PUT** {ostree_ostree_distribution_href} | Update an ostree distribution


# **add_role**
> NestedRoleResponse add_role(ostree_ostree_distribution_href, nested_role)

Add a role

Add a role for this object to users/groups.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
nested_role = pulpcore.client.pulp_ostree.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.add_role(ostree_ostree_distribution_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->add_role: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
nested_role = pulpcore.client.pulp_ostree.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.add_role(ostree_ostree_distribution_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->add_role: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
nested_role = pulpcore.client.pulp_ostree.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.add_role(ostree_ostree_distribution_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->add_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_distribution_href** | **str**|  | 
 **nested_role** | [**NestedRole**](NestedRole.md)|  | 

### Return type

[**NestedRoleResponse**](NestedRoleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> AsyncOperationResponse create(pulp_domain, ostree_ostree_distribution)

Create an ostree distribution

Trigger an asynchronous create task

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
ostree_ostree_distribution = pulpcore.client.pulp_ostree.OstreeOstreeDistribution() # OstreeOstreeDistribution | 

    try:
        # Create an ostree distribution
        api_response = api_instance.create(pulp_domain, ostree_ostree_distribution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->create: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
ostree_ostree_distribution = pulpcore.client.pulp_ostree.OstreeOstreeDistribution() # OstreeOstreeDistribution | 

    try:
        # Create an ostree distribution
        api_response = api_instance.create(pulp_domain, ostree_ostree_distribution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->create: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
ostree_ostree_distribution = pulpcore.client.pulp_ostree.OstreeOstreeDistribution() # OstreeOstreeDistribution | 

    try:
        # Create an ostree distribution
        api_response = api_instance.create(pulp_domain, ostree_ostree_distribution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **ostree_ostree_distribution** | [**OstreeOstreeDistribution**](OstreeOstreeDistribution.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> AsyncOperationResponse delete(ostree_ostree_distribution_href)

Delete an ostree distribution

Trigger an asynchronous delete task

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 

    try:
        # Delete an ostree distribution
        api_response = api_instance.delete(ostree_ostree_distribution_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->delete: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 

    try:
        # Delete an ostree distribution
        api_response = api_instance.delete(ostree_ostree_distribution_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->delete: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 

    try:
        # Delete an ostree distribution
        api_response = api_instance.delete(ostree_ostree_distribution_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_distribution_href** | **str**|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedostreeOstreeDistributionResponseList list(pulp_domain, base_path=base_path, base_path__contains=base_path__contains, base_path__icontains=base_path__icontains, base_path__in=base_path__in, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, repository=repository, repository__in=repository__in, with_content=with_content, fields=fields, exclude_fields=exclude_fields)

List ostree distributions

A ViewSet class for OSTree distributions.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
base_path = 'base_path_example' # str | Filter results where base_path matches value (optional)
base_path__contains = 'base_path__contains_example' # str | Filter results where base_path contains value (optional)
base_path__icontains = 'base_path__icontains_example' # str | Filter results where base_path contains value (optional)
base_path__in = ['base_path__in_example'] # list[str] | Filter results where base_path is in a comma-separated list of values (optional)
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__icontains = 'name__icontains_example' # str | Filter results where name contains value (optional)
name__iexact = 'name__iexact_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__iregex = 'name__iregex_example' # str | Filter results where name matches regex value (optional)
name__istartswith = 'name__istartswith_example' # str | Filter results where name starts with value (optional)
name__regex = 'name__regex_example' # str | Filter results where name matches regex value (optional)
name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `base_path` - Base path * `-base_path` - Base path (descending) * `hidden` - Hidden * `-hidden` - Hidden (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
q = 'q_example' # str |  (optional)
repository = 'repository_example' # str | Filter results where repository matches value (optional)
repository__in = ['repository__in_example'] # list[str] | Filter results where repository is in a comma-separated list of values (optional)
with_content = 'with_content_example' # str | Filter distributions based on the content served by them (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List ostree distributions
        api_response = api_instance.list(pulp_domain, base_path=base_path, base_path__contains=base_path__contains, base_path__icontains=base_path__icontains, base_path__in=base_path__in, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, repository=repository, repository__in=repository__in, with_content=with_content, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->list: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
base_path = 'base_path_example' # str | Filter results where base_path matches value (optional)
base_path__contains = 'base_path__contains_example' # str | Filter results where base_path contains value (optional)
base_path__icontains = 'base_path__icontains_example' # str | Filter results where base_path contains value (optional)
base_path__in = ['base_path__in_example'] # list[str] | Filter results where base_path is in a comma-separated list of values (optional)
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__icontains = 'name__icontains_example' # str | Filter results where name contains value (optional)
name__iexact = 'name__iexact_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__iregex = 'name__iregex_example' # str | Filter results where name matches regex value (optional)
name__istartswith = 'name__istartswith_example' # str | Filter results where name starts with value (optional)
name__regex = 'name__regex_example' # str | Filter results where name matches regex value (optional)
name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `base_path` - Base path * `-base_path` - Base path (descending) * `hidden` - Hidden * `-hidden` - Hidden (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
q = 'q_example' # str |  (optional)
repository = 'repository_example' # str | Filter results where repository matches value (optional)
repository__in = ['repository__in_example'] # list[str] | Filter results where repository is in a comma-separated list of values (optional)
with_content = 'with_content_example' # str | Filter distributions based on the content served by them (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List ostree distributions
        api_response = api_instance.list(pulp_domain, base_path=base_path, base_path__contains=base_path__contains, base_path__icontains=base_path__icontains, base_path__in=base_path__in, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, repository=repository, repository__in=repository__in, with_content=with_content, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->list: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
base_path = 'base_path_example' # str | Filter results where base_path matches value (optional)
base_path__contains = 'base_path__contains_example' # str | Filter results where base_path contains value (optional)
base_path__icontains = 'base_path__icontains_example' # str | Filter results where base_path contains value (optional)
base_path__in = ['base_path__in_example'] # list[str] | Filter results where base_path is in a comma-separated list of values (optional)
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__icontains = 'name__icontains_example' # str | Filter results where name contains value (optional)
name__iexact = 'name__iexact_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__iregex = 'name__iregex_example' # str | Filter results where name matches regex value (optional)
name__istartswith = 'name__istartswith_example' # str | Filter results where name starts with value (optional)
name__regex = 'name__regex_example' # str | Filter results where name matches regex value (optional)
name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `base_path` - Base path * `-base_path` - Base path (descending) * `hidden` - Hidden * `-hidden` - Hidden (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
q = 'q_example' # str |  (optional)
repository = 'repository_example' # str | Filter results where repository matches value (optional)
repository__in = ['repository__in_example'] # list[str] | Filter results where repository is in a comma-separated list of values (optional)
with_content = 'with_content_example' # str | Filter distributions based on the content served by them (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List ostree distributions
        api_response = api_instance.list(pulp_domain, base_path=base_path, base_path__contains=base_path__contains, base_path__icontains=base_path__icontains, base_path__in=base_path__in, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, repository=repository, repository__in=repository__in, with_content=with_content, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **base_path** | **str**| Filter results where base_path matches value | [optional] 
 **base_path__contains** | **str**| Filter results where base_path contains value | [optional] 
 **base_path__icontains** | **str**| Filter results where base_path contains value | [optional] 
 **base_path__in** | [**list[str]**](str.md)| Filter results where base_path is in a comma-separated list of values | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**| Filter results where name matches value | [optional] 
 **name__contains** | **str**| Filter results where name contains value | [optional] 
 **name__icontains** | **str**| Filter results where name contains value | [optional] 
 **name__iexact** | **str**| Filter results where name matches value | [optional] 
 **name__in** | [**list[str]**](str.md)| Filter results where name is in a comma-separated list of values | [optional] 
 **name__iregex** | **str**| Filter results where name matches regex value | [optional] 
 **name__istartswith** | **str**| Filter results where name starts with value | [optional] 
 **name__regex** | **str**| Filter results where name matches regex value | [optional] 
 **name__startswith** | **str**| Filter results where name starts with value | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;pulp_labels&#x60; - Pulp labels * &#x60;-pulp_labels&#x60; - Pulp labels (descending) * &#x60;base_path&#x60; - Base path * &#x60;-base_path&#x60; - Base path (descending) * &#x60;hidden&#x60; - Hidden * &#x60;-hidden&#x60; - Hidden (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_label_select** | **str**| Filter labels by search string | [optional] 
 **q** | **str**|  | [optional] 
 **repository** | [**str**](.md)| Filter results where repository matches value | [optional] 
 **repository__in** | [**list[str]**](str.md)| Filter results where repository is in a comma-separated list of values | [optional] 
 **with_content** | **str**| Filter distributions based on the content served by them | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedostreeOstreeDistributionResponseList**](PaginatedostreeOstreeDistributionResponseList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> ObjectRolesResponse list_roles(ostree_ostree_distribution_href, fields=fields, exclude_fields=exclude_fields)

List roles

List roles assigned to this object.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.list_roles(ostree_ostree_distribution_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->list_roles: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.list_roles(ostree_ostree_distribution_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->list_roles: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.list_roles(ostree_ostree_distribution_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->list_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_distribution_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**ObjectRolesResponse**](ObjectRolesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **my_permissions**
> MyPermissionsResponse my_permissions(ostree_ostree_distribution_href, fields=fields, exclude_fields=exclude_fields)

List user permissions

List permissions available to the current user on this object.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.my_permissions(ostree_ostree_distribution_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->my_permissions: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.my_permissions(ostree_ostree_distribution_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->my_permissions: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.my_permissions(ostree_ostree_distribution_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->my_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_distribution_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**MyPermissionsResponse**](MyPermissionsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update**
> AsyncOperationResponse partial_update(ostree_ostree_distribution_href, patchedostree_ostree_distribution)

Update an ostree distribution

Trigger an asynchronous partial update task

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
patchedostree_ostree_distribution = pulpcore.client.pulp_ostree.PatchedostreeOstreeDistribution() # PatchedostreeOstreeDistribution | 

    try:
        # Update an ostree distribution
        api_response = api_instance.partial_update(ostree_ostree_distribution_href, patchedostree_ostree_distribution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->partial_update: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
patchedostree_ostree_distribution = pulpcore.client.pulp_ostree.PatchedostreeOstreeDistribution() # PatchedostreeOstreeDistribution | 

    try:
        # Update an ostree distribution
        api_response = api_instance.partial_update(ostree_ostree_distribution_href, patchedostree_ostree_distribution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->partial_update: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
patchedostree_ostree_distribution = pulpcore.client.pulp_ostree.PatchedostreeOstreeDistribution() # PatchedostreeOstreeDistribution | 

    try:
        # Update an ostree distribution
        api_response = api_instance.partial_update(ostree_ostree_distribution_href, patchedostree_ostree_distribution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_distribution_href** | **str**|  | 
 **patchedostree_ostree_distribution** | [**PatchedostreeOstreeDistribution**](PatchedostreeOstreeDistribution.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> OstreeOstreeDistributionResponse read(ostree_ostree_distribution_href, fields=fields, exclude_fields=exclude_fields)

Inspect an ostree distribution

A ViewSet class for OSTree distributions.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an ostree distribution
        api_response = api_instance.read(ostree_ostree_distribution_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->read: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an ostree distribution
        api_response = api_instance.read(ostree_ostree_distribution_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->read: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an ostree distribution
        api_response = api_instance.read(ostree_ostree_distribution_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_distribution_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**OstreeOstreeDistributionResponse**](OstreeOstreeDistributionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role**
> NestedRoleResponse remove_role(ostree_ostree_distribution_href, nested_role)

Remove a role

Remove a role for this object from users/groups.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
nested_role = pulpcore.client.pulp_ostree.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.remove_role(ostree_ostree_distribution_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->remove_role: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
nested_role = pulpcore.client.pulp_ostree.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.remove_role(ostree_ostree_distribution_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->remove_role: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
nested_role = pulpcore.client.pulp_ostree.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.remove_role(ostree_ostree_distribution_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->remove_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_distribution_href** | **str**|  | 
 **nested_role** | [**NestedRole**](NestedRole.md)|  | 

### Return type

[**NestedRoleResponse**](NestedRoleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_label**
> SetLabelResponse set_label(ostree_ostree_distribution_href, set_label)

Set a label

Set a single pulp_label on the object to a specific value or null.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
set_label = pulpcore.client.pulp_ostree.SetLabel() # SetLabel | 

    try:
        # Set a label
        api_response = api_instance.set_label(ostree_ostree_distribution_href, set_label)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->set_label: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
set_label = pulpcore.client.pulp_ostree.SetLabel() # SetLabel | 

    try:
        # Set a label
        api_response = api_instance.set_label(ostree_ostree_distribution_href, set_label)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->set_label: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
set_label = pulpcore.client.pulp_ostree.SetLabel() # SetLabel | 

    try:
        # Set a label
        api_response = api_instance.set_label(ostree_ostree_distribution_href, set_label)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->set_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_distribution_href** | **str**|  | 
 **set_label** | [**SetLabel**](SetLabel.md)|  | 

### Return type

[**SetLabelResponse**](SetLabelResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_label**
> UnsetLabelResponse unset_label(ostree_ostree_distribution_href, unset_label)

Unset a label

Unset a single pulp_label on the object.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
unset_label = pulpcore.client.pulp_ostree.UnsetLabel() # UnsetLabel | 

    try:
        # Unset a label
        api_response = api_instance.unset_label(ostree_ostree_distribution_href, unset_label)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->unset_label: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
unset_label = pulpcore.client.pulp_ostree.UnsetLabel() # UnsetLabel | 

    try:
        # Unset a label
        api_response = api_instance.unset_label(ostree_ostree_distribution_href, unset_label)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->unset_label: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
unset_label = pulpcore.client.pulp_ostree.UnsetLabel() # UnsetLabel | 

    try:
        # Unset a label
        api_response = api_instance.unset_label(ostree_ostree_distribution_href, unset_label)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->unset_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_distribution_href** | **str**|  | 
 **unset_label** | [**UnsetLabel**](UnsetLabel.md)|  | 

### Return type

[**UnsetLabelResponse**](UnsetLabelResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> AsyncOperationResponse update(ostree_ostree_distribution_href, ostree_ostree_distribution)

Update an ostree distribution

Trigger an asynchronous update task

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
ostree_ostree_distribution = pulpcore.client.pulp_ostree.OstreeOstreeDistribution() # OstreeOstreeDistribution | 

    try:
        # Update an ostree distribution
        api_response = api_instance.update(ostree_ostree_distribution_href, ostree_ostree_distribution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->update: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
ostree_ostree_distribution = pulpcore.client.pulp_ostree.OstreeOstreeDistribution() # OstreeOstreeDistribution | 

    try:
        # Update an ostree distribution
        api_response = api_instance.update(ostree_ostree_distribution_href, ostree_ostree_distribution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->update: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp-api-svc.pulp-prod.svc.cluster.local:24817
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://pulp-api-svc.pulp-prod.svc.cluster.local:24817"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.DistributionsOstreeApi(api_client)
    ostree_ostree_distribution_href = 'ostree_ostree_distribution_href_example' # str | 
ostree_ostree_distribution = pulpcore.client.pulp_ostree.OstreeOstreeDistribution() # OstreeOstreeDistribution | 

    try:
        # Update an ostree distribution
        api_response = api_instance.update(ostree_ostree_distribution_href, ostree_ostree_distribution)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DistributionsOstreeApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_distribution_href** | **str**|  | 
 **ostree_ostree_distribution** | [**OstreeOstreeDistribution**](OstreeOstreeDistribution.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

