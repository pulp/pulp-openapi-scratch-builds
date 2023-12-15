# pulpcore.client.pulpcore.TasksApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role**](TasksApi.md#add_role) | **POST** {task_href}add_role/ | Add a role
[**delete**](TasksApi.md#delete) | **DELETE** {task_href} | Delete a task
[**list**](TasksApi.md#list) | **GET** /pulp/{pulp_domain}/api/v3/tasks/ | List tasks
[**list_roles**](TasksApi.md#list_roles) | **GET** {task_href}list_roles/ | List roles
[**my_permissions**](TasksApi.md#my_permissions) | **GET** {task_href}my_permissions/ | List user permissions
[**purge**](TasksApi.md#purge) | **POST** /pulp/{pulp_domain}/api/v3/tasks/purge/ | Purge Completed Tasks
[**read**](TasksApi.md#read) | **GET** {task_href} | Inspect a task
[**remove_role**](TasksApi.md#remove_role) | **POST** {task_href}remove_role/ | Remove a role
[**tasks_cancel**](TasksApi.md#tasks_cancel) | **PATCH** {task_href} | Cancel a task


# **add_role**
> NestedRoleResponse add_role(task_href, nested_role)

Add a role

Add a role for this object to users/groups.

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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 
nested_role = pulpcore.client.pulpcore.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.add_role(task_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->add_role: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 
nested_role = pulpcore.client.pulpcore.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.add_role(task_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->add_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**|  | 
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

# **delete**
> delete(task_href)

Delete a task

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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 

    try:
        # Delete a task
        api_instance.delete(task_href)
    except ApiException as e:
        print("Exception when calling TasksApi->delete: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 

    try:
        # Delete a task
        api_instance.delete(task_href)
    except ApiException as e:
        print("Exception when calling TasksApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**|  | 

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
> PaginatedTaskResponseList list(pulp_domain, child_tasks=child_tasks, created_resources=created_resources, exclusive_resources=exclusive_resources, exclusive_resources__in=exclusive_resources__in, finished_at=finished_at, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__range=finished_at__range, limit=limit, logging_cid=logging_cid, logging_cid__contains=logging_cid__contains, name=name, name__contains=name__contains, name__in=name__in, name__ne=name__ne, offset=offset, ordering=ordering, parent_task=parent_task, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, reserved_resources=reserved_resources, reserved_resources__in=reserved_resources__in, reserved_resources_record=reserved_resources_record, shared_resources=shared_resources, shared_resources__in=shared_resources__in, started_at=started_at, started_at__gt=started_at__gt, started_at__gte=started_at__gte, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__range=started_at__range, state=state, state__in=state__in, state__ne=state__ne, task_group=task_group, worker=worker, worker__in=worker__in, worker__isnull=worker__isnull, fields=fields, exclude_fields=exclude_fields)

List tasks

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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
child_tasks = 'child_tasks_example' # str | Filter results where child_tasks matches value (optional)
created_resources = 'created_resources_example' # str |  (optional)
exclusive_resources = 'exclusive_resources_example' # str |  (optional)
exclusive_resources__in = ['exclusive_resources__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
finished_at = '2013-10-20T19:20:30+01:00' # datetime | Filter results where finished_at matches value (optional)
finished_at__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where finished_at is greater than value (optional)
finished_at__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where finished_at is greater than or equal to value (optional)
finished_at__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where finished_at is less than value (optional)
finished_at__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where finished_at is less than or equal to value (optional)
finished_at__range = ['2013-10-20T19:20:30+01:00'] # list[datetime] | Filter results where finished_at is between two comma separated values (optional)
limit = 56 # int | Number of results to return per page. (optional)
logging_cid = 'logging_cid_example' # str | Filter results where logging_cid matches value (optional)
logging_cid__contains = 'logging_cid__contains_example' # str | Filter results where logging_cid contains value (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__ne = 'name__ne_example' # str | Filter results where name not equal to value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `state` - State * `-state` - State (descending) * `name` - Name * `-name` - Name (descending) * `logging_cid` - Logging cid * `-logging_cid` - Logging cid (descending) * `started_at` - Started at * `-started_at` - Started at (descending) * `finished_at` - Finished at * `-finished_at` - Finished at (descending) * `error` - Error * `-error` - Error (descending) * `enc_args` - Enc args * `-enc_args` - Enc args (descending) * `enc_kwargs` - Enc kwargs * `-enc_kwargs` - Enc kwargs (descending) * `reserved_resources_record` - Reserved resources record * `-reserved_resources_record` - Reserved resources record (descending) * `versions` - Versions * `-versions` - Versions (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
parent_task = 'parent_task_example' # str | Filter results where parent_task matches value (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
reserved_resources = 'reserved_resources_example' # str |  (optional)
reserved_resources__in = ['reserved_resources__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
reserved_resources_record = ['reserved_resources_record_example'] # list[str] |  (optional)
shared_resources = 'shared_resources_example' # str |  (optional)
shared_resources__in = ['shared_resources__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
started_at = '2013-10-20T19:20:30+01:00' # datetime | Filter results where started_at matches value (optional)
started_at__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where started_at is greater than value (optional)
started_at__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where started_at is greater than or equal to value (optional)
started_at__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where started_at is less than value (optional)
started_at__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where started_at is less than or equal to value (optional)
started_at__range = ['2013-10-20T19:20:30+01:00'] # list[datetime] | Filter results where started_at is between two comma separated values (optional)
state = 'state_example' # str | Filter results where state matches value  * `waiting` - Waiting * `skipped` - Skipped * `running` - Running * `completed` - Completed * `failed` - Failed * `canceled` - Canceled * `canceling` - Canceling (optional)
state__in = ['state__in_example'] # list[str] | Filter results where state is in a comma-separated list of values (optional)
state__ne = 'state__ne_example' # str | Filter results where state not equal to value (optional)
task_group = 'task_group_example' # str | Filter results where task_group matches value (optional)
worker = 'worker_example' # str | Filter results where worker matches value (optional)
worker__in = ['worker__in_example'] # list[str] | Filter results where worker is in a comma-separated list of values (optional)
worker__isnull = True # bool | Filter results where worker has a null value (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List tasks
        api_response = api_instance.list(pulp_domain, child_tasks=child_tasks, created_resources=created_resources, exclusive_resources=exclusive_resources, exclusive_resources__in=exclusive_resources__in, finished_at=finished_at, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__range=finished_at__range, limit=limit, logging_cid=logging_cid, logging_cid__contains=logging_cid__contains, name=name, name__contains=name__contains, name__in=name__in, name__ne=name__ne, offset=offset, ordering=ordering, parent_task=parent_task, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, reserved_resources=reserved_resources, reserved_resources__in=reserved_resources__in, reserved_resources_record=reserved_resources_record, shared_resources=shared_resources, shared_resources__in=shared_resources__in, started_at=started_at, started_at__gt=started_at__gt, started_at__gte=started_at__gte, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__range=started_at__range, state=state, state__in=state__in, state__ne=state__ne, task_group=task_group, worker=worker, worker__in=worker__in, worker__isnull=worker__isnull, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->list: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
child_tasks = 'child_tasks_example' # str | Filter results where child_tasks matches value (optional)
created_resources = 'created_resources_example' # str |  (optional)
exclusive_resources = 'exclusive_resources_example' # str |  (optional)
exclusive_resources__in = ['exclusive_resources__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
finished_at = '2013-10-20T19:20:30+01:00' # datetime | Filter results where finished_at matches value (optional)
finished_at__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where finished_at is greater than value (optional)
finished_at__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where finished_at is greater than or equal to value (optional)
finished_at__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where finished_at is less than value (optional)
finished_at__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where finished_at is less than or equal to value (optional)
finished_at__range = ['2013-10-20T19:20:30+01:00'] # list[datetime] | Filter results where finished_at is between two comma separated values (optional)
limit = 56 # int | Number of results to return per page. (optional)
logging_cid = 'logging_cid_example' # str | Filter results where logging_cid matches value (optional)
logging_cid__contains = 'logging_cid__contains_example' # str | Filter results where logging_cid contains value (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__ne = 'name__ne_example' # str | Filter results where name not equal to value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `state` - State * `-state` - State (descending) * `name` - Name * `-name` - Name (descending) * `logging_cid` - Logging cid * `-logging_cid` - Logging cid (descending) * `started_at` - Started at * `-started_at` - Started at (descending) * `finished_at` - Finished at * `-finished_at` - Finished at (descending) * `error` - Error * `-error` - Error (descending) * `enc_args` - Enc args * `-enc_args` - Enc args (descending) * `enc_kwargs` - Enc kwargs * `-enc_kwargs` - Enc kwargs (descending) * `reserved_resources_record` - Reserved resources record * `-reserved_resources_record` - Reserved resources record (descending) * `versions` - Versions * `-versions` - Versions (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
parent_task = 'parent_task_example' # str | Filter results where parent_task matches value (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
reserved_resources = 'reserved_resources_example' # str |  (optional)
reserved_resources__in = ['reserved_resources__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
reserved_resources_record = ['reserved_resources_record_example'] # list[str] |  (optional)
shared_resources = 'shared_resources_example' # str |  (optional)
shared_resources__in = ['shared_resources__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
started_at = '2013-10-20T19:20:30+01:00' # datetime | Filter results where started_at matches value (optional)
started_at__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where started_at is greater than value (optional)
started_at__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where started_at is greater than or equal to value (optional)
started_at__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where started_at is less than value (optional)
started_at__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where started_at is less than or equal to value (optional)
started_at__range = ['2013-10-20T19:20:30+01:00'] # list[datetime] | Filter results where started_at is between two comma separated values (optional)
state = 'state_example' # str | Filter results where state matches value  * `waiting` - Waiting * `skipped` - Skipped * `running` - Running * `completed` - Completed * `failed` - Failed * `canceled` - Canceled * `canceling` - Canceling (optional)
state__in = ['state__in_example'] # list[str] | Filter results where state is in a comma-separated list of values (optional)
state__ne = 'state__ne_example' # str | Filter results where state not equal to value (optional)
task_group = 'task_group_example' # str | Filter results where task_group matches value (optional)
worker = 'worker_example' # str | Filter results where worker matches value (optional)
worker__in = ['worker__in_example'] # list[str] | Filter results where worker is in a comma-separated list of values (optional)
worker__isnull = True # bool | Filter results where worker has a null value (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List tasks
        api_response = api_instance.list(pulp_domain, child_tasks=child_tasks, created_resources=created_resources, exclusive_resources=exclusive_resources, exclusive_resources__in=exclusive_resources__in, finished_at=finished_at, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__range=finished_at__range, limit=limit, logging_cid=logging_cid, logging_cid__contains=logging_cid__contains, name=name, name__contains=name__contains, name__in=name__in, name__ne=name__ne, offset=offset, ordering=ordering, parent_task=parent_task, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, reserved_resources=reserved_resources, reserved_resources__in=reserved_resources__in, reserved_resources_record=reserved_resources_record, shared_resources=shared_resources, shared_resources__in=shared_resources__in, started_at=started_at, started_at__gt=started_at__gt, started_at__gte=started_at__gte, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__range=started_at__range, state=state, state__in=state__in, state__ne=state__ne, task_group=task_group, worker=worker, worker__in=worker__in, worker__isnull=worker__isnull, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **child_tasks** | [**str**](.md)| Filter results where child_tasks matches value | [optional] 
 **created_resources** | [**str**](.md)|  | [optional] 
 **exclusive_resources** | **str**|  | [optional] 
 **exclusive_resources__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **finished_at** | **datetime**| Filter results where finished_at matches value | [optional] 
 **finished_at__gt** | **datetime**| Filter results where finished_at is greater than value | [optional] 
 **finished_at__gte** | **datetime**| Filter results where finished_at is greater than or equal to value | [optional] 
 **finished_at__lt** | **datetime**| Filter results where finished_at is less than value | [optional] 
 **finished_at__lte** | **datetime**| Filter results where finished_at is less than or equal to value | [optional] 
 **finished_at__range** | [**list[datetime]**](datetime.md)| Filter results where finished_at is between two comma separated values | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **logging_cid** | **str**| Filter results where logging_cid matches value | [optional] 
 **logging_cid__contains** | **str**| Filter results where logging_cid contains value | [optional] 
 **name** | **str**| Filter results where name matches value | [optional] 
 **name__contains** | **str**| Filter results where name contains value | [optional] 
 **name__in** | [**list[str]**](str.md)| Filter results where name is in a comma-separated list of values | [optional] 
 **name__ne** | **str**| Filter results where name not equal to value | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;state&#x60; - State * &#x60;-state&#x60; - State (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;logging_cid&#x60; - Logging cid * &#x60;-logging_cid&#x60; - Logging cid (descending) * &#x60;started_at&#x60; - Started at * &#x60;-started_at&#x60; - Started at (descending) * &#x60;finished_at&#x60; - Finished at * &#x60;-finished_at&#x60; - Finished at (descending) * &#x60;error&#x60; - Error * &#x60;-error&#x60; - Error (descending) * &#x60;enc_args&#x60; - Enc args * &#x60;-enc_args&#x60; - Enc args (descending) * &#x60;enc_kwargs&#x60; - Enc kwargs * &#x60;-enc_kwargs&#x60; - Enc kwargs (descending) * &#x60;reserved_resources_record&#x60; - Reserved resources record * &#x60;-reserved_resources_record&#x60; - Reserved resources record (descending) * &#x60;versions&#x60; - Versions * &#x60;-versions&#x60; - Versions (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **parent_task** | [**str**](.md)| Filter results where parent_task matches value | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **reserved_resources** | **str**|  | [optional] 
 **reserved_resources__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **reserved_resources_record** | [**list[str]**](str.md)|  | [optional] 
 **shared_resources** | **str**|  | [optional] 
 **shared_resources__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **started_at** | **datetime**| Filter results where started_at matches value | [optional] 
 **started_at__gt** | **datetime**| Filter results where started_at is greater than value | [optional] 
 **started_at__gte** | **datetime**| Filter results where started_at is greater than or equal to value | [optional] 
 **started_at__lt** | **datetime**| Filter results where started_at is less than value | [optional] 
 **started_at__lte** | **datetime**| Filter results where started_at is less than or equal to value | [optional] 
 **started_at__range** | [**list[datetime]**](datetime.md)| Filter results where started_at is between two comma separated values | [optional] 
 **state** | **str**| Filter results where state matches value  * &#x60;waiting&#x60; - Waiting * &#x60;skipped&#x60; - Skipped * &#x60;running&#x60; - Running * &#x60;completed&#x60; - Completed * &#x60;failed&#x60; - Failed * &#x60;canceled&#x60; - Canceled * &#x60;canceling&#x60; - Canceling | [optional] 
 **state__in** | [**list[str]**](str.md)| Filter results where state is in a comma-separated list of values | [optional] 
 **state__ne** | **str**| Filter results where state not equal to value | [optional] 
 **task_group** | [**str**](.md)| Filter results where task_group matches value | [optional] 
 **worker** | [**str**](.md)| Filter results where worker matches value | [optional] 
 **worker__in** | [**list[str]**](str.md)| Filter results where worker is in a comma-separated list of values | [optional] 
 **worker__isnull** | **bool**| Filter results where worker has a null value | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedTaskResponseList**](PaginatedTaskResponseList.md)

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
> ObjectRolesResponse list_roles(task_href, fields=fields, exclude_fields=exclude_fields)

List roles

List roles assigned to this object.

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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.list_roles(task_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->list_roles: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List roles
        api_response = api_instance.list_roles(task_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->list_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

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
> MyPermissionsResponse my_permissions(task_href, fields=fields, exclude_fields=exclude_fields)

List user permissions

List permissions available to the current user on this object.

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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.my_permissions(task_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->my_permissions: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List user permissions
        api_response = api_instance.my_permissions(task_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->my_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

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

# **purge**
> AsyncOperationResponse purge(pulp_domain, purge)

Purge Completed Tasks

Trigger an asynchronous task that deletes completed tasks that finished prior to a specified timestamp.

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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
purge = pulpcore.client.pulpcore.Purge() # Purge | 

    try:
        # Purge Completed Tasks
        api_response = api_instance.purge(pulp_domain, purge)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->purge: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
purge = pulpcore.client.pulpcore.Purge() # Purge | 

    try:
        # Purge Completed Tasks
        api_response = api_instance.purge(pulp_domain, purge)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->purge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **purge** | [**Purge**](Purge.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> TaskResponse read(task_href, fields=fields, exclude_fields=exclude_fields)

Inspect a task

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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a task
        api_response = api_instance.read(task_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->read: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a task
        api_response = api_instance.read(task_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

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
> NestedRoleResponse remove_role(task_href, nested_role)

Remove a role

Remove a role for this object from users/groups.

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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 
nested_role = pulpcore.client.pulpcore.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.remove_role(task_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->remove_role: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 
nested_role = pulpcore.client.pulpcore.NestedRole() # NestedRole | 

    try:
        # Remove a role
        api_response = api_instance.remove_role(task_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->remove_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**|  | 
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

# **tasks_cancel**
> TaskResponse tasks_cancel(task_href, patched_task_cancel)

Cancel a task

This operation cancels a task.

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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 
patched_task_cancel = pulpcore.client.pulpcore.PatchedTaskCancel() # PatchedTaskCancel | 

    try:
        # Cancel a task
        api_response = api_instance.tasks_cancel(task_href, patched_task_cancel)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_cancel: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.TasksApi(api_client)
    task_href = 'task_href_example' # str | 
patched_task_cancel = pulpcore.client.pulpcore.PatchedTaskCancel() # PatchedTaskCancel | 

    try:
        # Cancel a task
        api_response = api_instance.tasks_cancel(task_href, patched_task_cancel)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**|  | 
 **patched_task_cancel** | [**PatchedTaskCancel**](PatchedTaskCancel.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

