# pulpcore.client.pulpcore.AccessPoliciesApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](AccessPoliciesApi.md#list) | **GET** /pulp/{pulp_domain}/api/v3/access_policies/ | List access policys
[**partial_update**](AccessPoliciesApi.md#partial_update) | **PATCH** {access_policy_href} | Update an access policy
[**read**](AccessPoliciesApi.md#read) | **GET** {access_policy_href} | Inspect an access policy
[**reset**](AccessPoliciesApi.md#reset) | **POST** {access_policy_href}reset/ | 
[**update**](AccessPoliciesApi.md#update) | **PUT** {access_policy_href} | Update an access policy


# **list**
> PaginatedAccessPolicyResponseList list(pulp_domain, customized=customized, limit=limit, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, viewset_name=viewset_name, viewset_name__contains=viewset_name__contains, viewset_name__icontains=viewset_name__icontains, viewset_name__iexact=viewset_name__iexact, viewset_name__in=viewset_name__in, viewset_name__iregex=viewset_name__iregex, viewset_name__istartswith=viewset_name__istartswith, viewset_name__regex=viewset_name__regex, viewset_name__startswith=viewset_name__startswith, fields=fields, exclude_fields=exclude_fields)

List access policys

ViewSet for AccessPolicy.  NOTE: This API endpoint is in \"tech preview\" and subject to change

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
    api_instance = pulpcore.client.pulpcore.AccessPoliciesApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
customized = True # bool | Filter results where customized matches value (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `creation_hooks` - Creation hooks * `-creation_hooks` - Creation hooks (descending) * `statements` - Statements * `-statements` - Statements (descending) * `viewset_name` - Viewset name * `-viewset_name` - Viewset name (descending) * `customized` - Customized * `-customized` - Customized (descending) * `queryset_scoping` - Queryset scoping * `-queryset_scoping` - Queryset scoping (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
viewset_name = 'viewset_name_example' # str | Filter results where viewset_name matches value (optional)
viewset_name__contains = 'viewset_name__contains_example' # str | Filter results where viewset_name contains value (optional)
viewset_name__icontains = 'viewset_name__icontains_example' # str | Filter results where viewset_name contains value (optional)
viewset_name__iexact = 'viewset_name__iexact_example' # str | Filter results where viewset_name matches value (optional)
viewset_name__in = ['viewset_name__in_example'] # list[str] | Filter results where viewset_name is in a comma-separated list of values (optional)
viewset_name__iregex = 'viewset_name__iregex_example' # str | Filter results where viewset_name matches regex value (optional)
viewset_name__istartswith = 'viewset_name__istartswith_example' # str | Filter results where viewset_name starts with value (optional)
viewset_name__regex = 'viewset_name__regex_example' # str | Filter results where viewset_name matches regex value (optional)
viewset_name__startswith = 'viewset_name__startswith_example' # str | Filter results where viewset_name starts with value (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List access policys
        api_response = api_instance.list(pulp_domain, customized=customized, limit=limit, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, viewset_name=viewset_name, viewset_name__contains=viewset_name__contains, viewset_name__icontains=viewset_name__icontains, viewset_name__iexact=viewset_name__iexact, viewset_name__in=viewset_name__in, viewset_name__iregex=viewset_name__iregex, viewset_name__istartswith=viewset_name__istartswith, viewset_name__regex=viewset_name__regex, viewset_name__startswith=viewset_name__startswith, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessPoliciesApi->list: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.AccessPoliciesApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
customized = True # bool | Filter results where customized matches value (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `creation_hooks` - Creation hooks * `-creation_hooks` - Creation hooks (descending) * `statements` - Statements * `-statements` - Statements (descending) * `viewset_name` - Viewset name * `-viewset_name` - Viewset name (descending) * `customized` - Customized * `-customized` - Customized (descending) * `queryset_scoping` - Queryset scoping * `-queryset_scoping` - Queryset scoping (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
viewset_name = 'viewset_name_example' # str | Filter results where viewset_name matches value (optional)
viewset_name__contains = 'viewset_name__contains_example' # str | Filter results where viewset_name contains value (optional)
viewset_name__icontains = 'viewset_name__icontains_example' # str | Filter results where viewset_name contains value (optional)
viewset_name__iexact = 'viewset_name__iexact_example' # str | Filter results where viewset_name matches value (optional)
viewset_name__in = ['viewset_name__in_example'] # list[str] | Filter results where viewset_name is in a comma-separated list of values (optional)
viewset_name__iregex = 'viewset_name__iregex_example' # str | Filter results where viewset_name matches regex value (optional)
viewset_name__istartswith = 'viewset_name__istartswith_example' # str | Filter results where viewset_name starts with value (optional)
viewset_name__regex = 'viewset_name__regex_example' # str | Filter results where viewset_name matches regex value (optional)
viewset_name__startswith = 'viewset_name__startswith_example' # str | Filter results where viewset_name starts with value (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List access policys
        api_response = api_instance.list(pulp_domain, customized=customized, limit=limit, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, viewset_name=viewset_name, viewset_name__contains=viewset_name__contains, viewset_name__icontains=viewset_name__icontains, viewset_name__iexact=viewset_name__iexact, viewset_name__in=viewset_name__in, viewset_name__iregex=viewset_name__iregex, viewset_name__istartswith=viewset_name__istartswith, viewset_name__regex=viewset_name__regex, viewset_name__startswith=viewset_name__startswith, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessPoliciesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **customized** | **bool**| Filter results where customized matches value | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;creation_hooks&#x60; - Creation hooks * &#x60;-creation_hooks&#x60; - Creation hooks (descending) * &#x60;statements&#x60; - Statements * &#x60;-statements&#x60; - Statements (descending) * &#x60;viewset_name&#x60; - Viewset name * &#x60;-viewset_name&#x60; - Viewset name (descending) * &#x60;customized&#x60; - Customized * &#x60;-customized&#x60; - Customized (descending) * &#x60;queryset_scoping&#x60; - Queryset scoping * &#x60;-queryset_scoping&#x60; - Queryset scoping (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **viewset_name** | **str**| Filter results where viewset_name matches value | [optional] 
 **viewset_name__contains** | **str**| Filter results where viewset_name contains value | [optional] 
 **viewset_name__icontains** | **str**| Filter results where viewset_name contains value | [optional] 
 **viewset_name__iexact** | **str**| Filter results where viewset_name matches value | [optional] 
 **viewset_name__in** | [**list[str]**](str.md)| Filter results where viewset_name is in a comma-separated list of values | [optional] 
 **viewset_name__iregex** | **str**| Filter results where viewset_name matches regex value | [optional] 
 **viewset_name__istartswith** | **str**| Filter results where viewset_name starts with value | [optional] 
 **viewset_name__regex** | **str**| Filter results where viewset_name matches regex value | [optional] 
 **viewset_name__startswith** | **str**| Filter results where viewset_name starts with value | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedAccessPolicyResponseList**](PaginatedAccessPolicyResponseList.md)

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
> AccessPolicyResponse partial_update(access_policy_href, patched_access_policy)

Update an access policy

ViewSet for AccessPolicy.  NOTE: This API endpoint is in \"tech preview\" and subject to change

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
    api_instance = pulpcore.client.pulpcore.AccessPoliciesApi(api_client)
    access_policy_href = 'access_policy_href_example' # str | 
patched_access_policy = pulpcore.client.pulpcore.PatchedAccessPolicy() # PatchedAccessPolicy | 

    try:
        # Update an access policy
        api_response = api_instance.partial_update(access_policy_href, patched_access_policy)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessPoliciesApi->partial_update: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.AccessPoliciesApi(api_client)
    access_policy_href = 'access_policy_href_example' # str | 
patched_access_policy = pulpcore.client.pulpcore.PatchedAccessPolicy() # PatchedAccessPolicy | 

    try:
        # Update an access policy
        api_response = api_instance.partial_update(access_policy_href, patched_access_policy)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessPoliciesApi->partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_policy_href** | **str**|  | 
 **patched_access_policy** | [**PatchedAccessPolicy**](PatchedAccessPolicy.md)|  | 

### Return type

[**AccessPolicyResponse**](AccessPolicyResponse.md)

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
> AccessPolicyResponse read(access_policy_href, fields=fields, exclude_fields=exclude_fields)

Inspect an access policy

ViewSet for AccessPolicy.  NOTE: This API endpoint is in \"tech preview\" and subject to change

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
    api_instance = pulpcore.client.pulpcore.AccessPoliciesApi(api_client)
    access_policy_href = 'access_policy_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an access policy
        api_response = api_instance.read(access_policy_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessPoliciesApi->read: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.AccessPoliciesApi(api_client)
    access_policy_href = 'access_policy_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an access policy
        api_response = api_instance.read(access_policy_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessPoliciesApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_policy_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**AccessPolicyResponse**](AccessPolicyResponse.md)

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

# **reset**
> AccessPolicyResponse reset(access_policy_href)



Reset the access policy to its uncustomized default value.

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
    api_instance = pulpcore.client.pulpcore.AccessPoliciesApi(api_client)
    access_policy_href = 'access_policy_href_example' # str | 

    try:
        api_response = api_instance.reset(access_policy_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessPoliciesApi->reset: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.AccessPoliciesApi(api_client)
    access_policy_href = 'access_policy_href_example' # str | 

    try:
        api_response = api_instance.reset(access_policy_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessPoliciesApi->reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_policy_href** | **str**|  | 

### Return type

[**AccessPolicyResponse**](AccessPolicyResponse.md)

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

# **update**
> AccessPolicyResponse update(access_policy_href, access_policy)

Update an access policy

ViewSet for AccessPolicy.  NOTE: This API endpoint is in \"tech preview\" and subject to change

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
    api_instance = pulpcore.client.pulpcore.AccessPoliciesApi(api_client)
    access_policy_href = 'access_policy_href_example' # str | 
access_policy = pulpcore.client.pulpcore.AccessPolicy() # AccessPolicy | 

    try:
        # Update an access policy
        api_response = api_instance.update(access_policy_href, access_policy)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessPoliciesApi->update: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.AccessPoliciesApi(api_client)
    access_policy_href = 'access_policy_href_example' # str | 
access_policy = pulpcore.client.pulpcore.AccessPolicy() # AccessPolicy | 

    try:
        # Update an access policy
        api_response = api_instance.update(access_policy_href, access_policy)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessPoliciesApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_policy_href** | **str**|  | 
 **access_policy** | [**AccessPolicy**](AccessPolicy.md)|  | 

### Return type

[**AccessPolicyResponse**](AccessPolicyResponse.md)

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

