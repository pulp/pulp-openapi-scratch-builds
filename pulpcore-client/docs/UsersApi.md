# pulpcore.client.pulpcore.UsersApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UsersApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/users/ | Create an user
[**delete**](UsersApi.md#delete) | **DELETE** {auth_user_href} | Delete an user
[**list**](UsersApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/users/ | List users
[**partial_update**](UsersApi.md#partial_update) | **PATCH** {auth_user_href} | Update an user
[**read**](UsersApi.md#read) | **GET** {auth_user_href} | Inspect an user
[**update**](UsersApi.md#update) | **PUT** {auth_user_href} | Update an user


# **create**
> UserResponse create(pulp_domain, user)

Create an user

ViewSet for User.

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
    api_instance = pulpcore.client.pulpcore.UsersApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
user = pulpcore.client.pulpcore.User() # User | 

    try:
        # Create an user
        api_response = api_instance.create(pulp_domain, user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.UsersApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
user = pulpcore.client.pulpcore.User() # User | 

    try:
        # Create an user
        api_response = api_instance.create(pulp_domain, user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **user** | [**User**](User.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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
> delete(auth_user_href)

Delete an user

ViewSet for User.

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
    api_instance = pulpcore.client.pulpcore.UsersApi(api_client)
    auth_user_href = 'auth_user_href_example' # str | 

    try:
        # Delete an user
        api_instance.delete(auth_user_href)
    except ApiException as e:
        print("Exception when calling UsersApi->delete: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.UsersApi(api_client)
    auth_user_href = 'auth_user_href_example' # str | 

    try:
        # Delete an user
        api_instance.delete(auth_user_href)
    except ApiException as e:
        print("Exception when calling UsersApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_user_href** | **str**|  | 

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
> PaginatedUserResponseList list(pulp_domain, email=email, email__contains=email__contains, email__icontains=email__icontains, email__iexact=email__iexact, email__in=email__in, first_name=first_name, first_name__contains=first_name__contains, first_name__icontains=first_name__icontains, first_name__iexact=first_name__iexact, first_name__in=first_name__in, is_active=is_active, is_staff=is_staff, last_name=last_name, last_name__contains=last_name__contains, last_name__icontains=last_name__icontains, last_name__iexact=last_name__iexact, last_name__in=last_name__in, limit=limit, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, username=username, username__contains=username__contains, username__icontains=username__icontains, username__iexact=username__iexact, username__in=username__in, fields=fields, exclude_fields=exclude_fields)

List users

ViewSet for User.

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
    api_instance = pulpcore.client.pulpcore.UsersApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
email = 'email_example' # str | Filter results where email matches value (optional)
email__contains = 'email__contains_example' # str | Filter results where email contains value (optional)
email__icontains = 'email__icontains_example' # str | Filter results where email contains value (optional)
email__iexact = 'email__iexact_example' # str | Filter results where email matches value (optional)
email__in = ['email__in_example'] # list[str] | Filter results where email is in a comma-separated list of values (optional)
first_name = 'first_name_example' # str | Filter results where first_name matches value (optional)
first_name__contains = 'first_name__contains_example' # str | Filter results where first_name contains value (optional)
first_name__icontains = 'first_name__icontains_example' # str | Filter results where first_name contains value (optional)
first_name__iexact = 'first_name__iexact_example' # str | Filter results where first_name matches value (optional)
first_name__in = ['first_name__in_example'] # list[str] | Filter results where first_name is in a comma-separated list of values (optional)
is_active = True # bool | Filter results where is_active matches value (optional)
is_staff = True # bool | Filter results where is_staff matches value (optional)
last_name = 'last_name_example' # str | Filter results where last_name matches value (optional)
last_name__contains = 'last_name__contains_example' # str | Filter results where last_name contains value (optional)
last_name__icontains = 'last_name__icontains_example' # str | Filter results where last_name contains value (optional)
last_name__iexact = 'last_name__iexact_example' # str | Filter results where last_name matches value (optional)
last_name__in = ['last_name__in_example'] # list[str] | Filter results where last_name is in a comma-separated list of values (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `id` - Id * `-id` - Id (descending) * `password` - Password * `-password` - Password (descending) * `last_login` - Last login * `-last_login` - Last login (descending) * `is_superuser` - Is superuser * `-is_superuser` - Is superuser (descending) * `username` - Username * `-username` - Username (descending) * `first_name` - First name * `-first_name` - First name (descending) * `last_name` - Last name * `-last_name` - Last name (descending) * `email` - Email * `-email` - Email (descending) * `is_staff` - Is staff * `-is_staff` - Is staff (descending) * `is_active` - Is active * `-is_active` - Is active (descending) * `date_joined` - Date joined * `-date_joined` - Date joined (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
username = 'username_example' # str | Filter results where username matches value (optional)
username__contains = 'username__contains_example' # str | Filter results where username contains value (optional)
username__icontains = 'username__icontains_example' # str | Filter results where username contains value (optional)
username__iexact = 'username__iexact_example' # str | Filter results where username matches value (optional)
username__in = ['username__in_example'] # list[str] | Filter results where username is in a comma-separated list of values (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List users
        api_response = api_instance.list(pulp_domain, email=email, email__contains=email__contains, email__icontains=email__icontains, email__iexact=email__iexact, email__in=email__in, first_name=first_name, first_name__contains=first_name__contains, first_name__icontains=first_name__icontains, first_name__iexact=first_name__iexact, first_name__in=first_name__in, is_active=is_active, is_staff=is_staff, last_name=last_name, last_name__contains=last_name__contains, last_name__icontains=last_name__icontains, last_name__iexact=last_name__iexact, last_name__in=last_name__in, limit=limit, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, username=username, username__contains=username__contains, username__icontains=username__icontains, username__iexact=username__iexact, username__in=username__in, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->list: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.UsersApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
email = 'email_example' # str | Filter results where email matches value (optional)
email__contains = 'email__contains_example' # str | Filter results where email contains value (optional)
email__icontains = 'email__icontains_example' # str | Filter results where email contains value (optional)
email__iexact = 'email__iexact_example' # str | Filter results where email matches value (optional)
email__in = ['email__in_example'] # list[str] | Filter results where email is in a comma-separated list of values (optional)
first_name = 'first_name_example' # str | Filter results where first_name matches value (optional)
first_name__contains = 'first_name__contains_example' # str | Filter results where first_name contains value (optional)
first_name__icontains = 'first_name__icontains_example' # str | Filter results where first_name contains value (optional)
first_name__iexact = 'first_name__iexact_example' # str | Filter results where first_name matches value (optional)
first_name__in = ['first_name__in_example'] # list[str] | Filter results where first_name is in a comma-separated list of values (optional)
is_active = True # bool | Filter results where is_active matches value (optional)
is_staff = True # bool | Filter results where is_staff matches value (optional)
last_name = 'last_name_example' # str | Filter results where last_name matches value (optional)
last_name__contains = 'last_name__contains_example' # str | Filter results where last_name contains value (optional)
last_name__icontains = 'last_name__icontains_example' # str | Filter results where last_name contains value (optional)
last_name__iexact = 'last_name__iexact_example' # str | Filter results where last_name matches value (optional)
last_name__in = ['last_name__in_example'] # list[str] | Filter results where last_name is in a comma-separated list of values (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `id` - Id * `-id` - Id (descending) * `password` - Password * `-password` - Password (descending) * `last_login` - Last login * `-last_login` - Last login (descending) * `is_superuser` - Is superuser * `-is_superuser` - Is superuser (descending) * `username` - Username * `-username` - Username (descending) * `first_name` - First name * `-first_name` - First name (descending) * `last_name` - Last name * `-last_name` - Last name (descending) * `email` - Email * `-email` - Email (descending) * `is_staff` - Is staff * `-is_staff` - Is staff (descending) * `is_active` - Is active * `-is_active` - Is active (descending) * `date_joined` - Date joined * `-date_joined` - Date joined (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
username = 'username_example' # str | Filter results where username matches value (optional)
username__contains = 'username__contains_example' # str | Filter results where username contains value (optional)
username__icontains = 'username__icontains_example' # str | Filter results where username contains value (optional)
username__iexact = 'username__iexact_example' # str | Filter results where username matches value (optional)
username__in = ['username__in_example'] # list[str] | Filter results where username is in a comma-separated list of values (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List users
        api_response = api_instance.list(pulp_domain, email=email, email__contains=email__contains, email__icontains=email__icontains, email__iexact=email__iexact, email__in=email__in, first_name=first_name, first_name__contains=first_name__contains, first_name__icontains=first_name__icontains, first_name__iexact=first_name__iexact, first_name__in=first_name__in, is_active=is_active, is_staff=is_staff, last_name=last_name, last_name__contains=last_name__contains, last_name__icontains=last_name__icontains, last_name__iexact=last_name__iexact, last_name__in=last_name__in, limit=limit, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, username=username, username__contains=username__contains, username__icontains=username__icontains, username__iexact=username__iexact, username__in=username__in, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **email** | **str**| Filter results where email matches value | [optional] 
 **email__contains** | **str**| Filter results where email contains value | [optional] 
 **email__icontains** | **str**| Filter results where email contains value | [optional] 
 **email__iexact** | **str**| Filter results where email matches value | [optional] 
 **email__in** | [**list[str]**](str.md)| Filter results where email is in a comma-separated list of values | [optional] 
 **first_name** | **str**| Filter results where first_name matches value | [optional] 
 **first_name__contains** | **str**| Filter results where first_name contains value | [optional] 
 **first_name__icontains** | **str**| Filter results where first_name contains value | [optional] 
 **first_name__iexact** | **str**| Filter results where first_name matches value | [optional] 
 **first_name__in** | [**list[str]**](str.md)| Filter results where first_name is in a comma-separated list of values | [optional] 
 **is_active** | **bool**| Filter results where is_active matches value | [optional] 
 **is_staff** | **bool**| Filter results where is_staff matches value | [optional] 
 **last_name** | **str**| Filter results where last_name matches value | [optional] 
 **last_name__contains** | **str**| Filter results where last_name contains value | [optional] 
 **last_name__icontains** | **str**| Filter results where last_name contains value | [optional] 
 **last_name__iexact** | **str**| Filter results where last_name matches value | [optional] 
 **last_name__in** | [**list[str]**](str.md)| Filter results where last_name is in a comma-separated list of values | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;id&#x60; - Id * &#x60;-id&#x60; - Id (descending) * &#x60;password&#x60; - Password * &#x60;-password&#x60; - Password (descending) * &#x60;last_login&#x60; - Last login * &#x60;-last_login&#x60; - Last login (descending) * &#x60;is_superuser&#x60; - Is superuser * &#x60;-is_superuser&#x60; - Is superuser (descending) * &#x60;username&#x60; - Username * &#x60;-username&#x60; - Username (descending) * &#x60;first_name&#x60; - First name * &#x60;-first_name&#x60; - First name (descending) * &#x60;last_name&#x60; - Last name * &#x60;-last_name&#x60; - Last name (descending) * &#x60;email&#x60; - Email * &#x60;-email&#x60; - Email (descending) * &#x60;is_staff&#x60; - Is staff * &#x60;-is_staff&#x60; - Is staff (descending) * &#x60;is_active&#x60; - Is active * &#x60;-is_active&#x60; - Is active (descending) * &#x60;date_joined&#x60; - Date joined * &#x60;-date_joined&#x60; - Date joined (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **username** | **str**| Filter results where username matches value | [optional] 
 **username__contains** | **str**| Filter results where username contains value | [optional] 
 **username__icontains** | **str**| Filter results where username contains value | [optional] 
 **username__iexact** | **str**| Filter results where username matches value | [optional] 
 **username__in** | [**list[str]**](str.md)| Filter results where username is in a comma-separated list of values | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedUserResponseList**](PaginatedUserResponseList.md)

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
> UserResponse partial_update(auth_user_href, patched_user)

Update an user

ViewSet for User.

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
    api_instance = pulpcore.client.pulpcore.UsersApi(api_client)
    auth_user_href = 'auth_user_href_example' # str | 
patched_user = pulpcore.client.pulpcore.PatchedUser() # PatchedUser | 

    try:
        # Update an user
        api_response = api_instance.partial_update(auth_user_href, patched_user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->partial_update: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.UsersApi(api_client)
    auth_user_href = 'auth_user_href_example' # str | 
patched_user = pulpcore.client.pulpcore.PatchedUser() # PatchedUser | 

    try:
        # Update an user
        api_response = api_instance.partial_update(auth_user_href, patched_user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_user_href** | **str**|  | 
 **patched_user** | [**PatchedUser**](PatchedUser.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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
> UserResponse read(auth_user_href, fields=fields, exclude_fields=exclude_fields)

Inspect an user

ViewSet for User.

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
    api_instance = pulpcore.client.pulpcore.UsersApi(api_client)
    auth_user_href = 'auth_user_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an user
        api_response = api_instance.read(auth_user_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->read: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.UsersApi(api_client)
    auth_user_href = 'auth_user_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an user
        api_response = api_instance.read(auth_user_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_user_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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
> UserResponse update(auth_user_href, user)

Update an user

ViewSet for User.

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
    api_instance = pulpcore.client.pulpcore.UsersApi(api_client)
    auth_user_href = 'auth_user_href_example' # str | 
user = pulpcore.client.pulpcore.User() # User | 

    try:
        # Update an user
        api_response = api_instance.update(auth_user_href, user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->update: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.UsersApi(api_client)
    auth_user_href = 'auth_user_href_example' # str | 
user = pulpcore.client.pulpcore.User() # User | 

    try:
        # Update an user
        api_response = api_instance.update(auth_user_href, user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_user_href** | **str**|  | 
 **user** | [**User**](User.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

