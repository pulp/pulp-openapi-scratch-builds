# pulpcore.client.pulpcore.RepositoriesApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](RepositoriesApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/repositories/ | List repositories


# **list**
> PaginatedRepositoryResponseList list(pulp_domain, latest_with_content=latest_with_content, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, pulp_type=pulp_type, pulp_type__in=pulp_type__in, q=q, remote=remote, retain_repo_versions=retain_repo_versions, retain_repo_versions__gt=retain_repo_versions__gt, retain_repo_versions__gte=retain_repo_versions__gte, retain_repo_versions__isnull=retain_repo_versions__isnull, retain_repo_versions__lt=retain_repo_versions__lt, retain_repo_versions__lte=retain_repo_versions__lte, retain_repo_versions__ne=retain_repo_versions__ne, retain_repo_versions__range=retain_repo_versions__range, with_content=with_content, fields=fields, exclude_fields=exclude_fields)

List repositories

Endpoint to list all repositories.

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
    api_instance = pulpcore.client.pulpcore.RepositoriesApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
latest_with_content = 'latest_with_content_example' # str | Content Unit referenced by HREF (optional)
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
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `description` - Description * `-description` - Description (descending) * `next_version` - Next version * `-next_version` - Next version (descending) * `retain_repo_versions` - Retain repo versions * `-retain_repo_versions` - Retain repo versions (descending) * `user_hidden` - User hidden * `-user_hidden` - User hidden (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
pulp_type = 'pulp_type_example' # str | Pulp type  * `ostree.ostree` - ostree.ostree * `rpm.rpm` - rpm.rpm * `file.file` - file.file (optional)
pulp_type__in = ['pulp_type__in_example'] # list[str] | Multiple values may be separated by commas.  * `ostree.ostree` - ostree.ostree * `rpm.rpm` - rpm.rpm * `file.file` - file.file (optional)
q = 'q_example' # str |  (optional)
remote = 'remote_example' # str | Foreign Key referenced by HREF (optional)
retain_repo_versions = 56 # int | Filter results where retain_repo_versions matches value (optional)
retain_repo_versions__gt = 56 # int | Filter results where retain_repo_versions is greater than value (optional)
retain_repo_versions__gte = 56 # int | Filter results where retain_repo_versions is greater than or equal to value (optional)
retain_repo_versions__isnull = True # bool | Filter results where retain_repo_versions has a null value (optional)
retain_repo_versions__lt = 56 # int | Filter results where retain_repo_versions is less than value (optional)
retain_repo_versions__lte = 56 # int | Filter results where retain_repo_versions is less than or equal to value (optional)
retain_repo_versions__ne = 56 # int | Filter results where retain_repo_versions not equal to value (optional)
retain_repo_versions__range = [56] # list[int] | Filter results where retain_repo_versions is between two comma separated values (optional)
with_content = 'with_content_example' # str | Content Unit referenced by HREF (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List repositories
        api_response = api_instance.list(pulp_domain, latest_with_content=latest_with_content, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, pulp_type=pulp_type, pulp_type__in=pulp_type__in, q=q, remote=remote, retain_repo_versions=retain_repo_versions, retain_repo_versions__gt=retain_repo_versions__gt, retain_repo_versions__gte=retain_repo_versions__gte, retain_repo_versions__isnull=retain_repo_versions__isnull, retain_repo_versions__lt=retain_repo_versions__lt, retain_repo_versions__lte=retain_repo_versions__lte, retain_repo_versions__ne=retain_repo_versions__ne, retain_repo_versions__range=retain_repo_versions__range, with_content=with_content, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesApi->list: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.RepositoriesApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
latest_with_content = 'latest_with_content_example' # str | Content Unit referenced by HREF (optional)
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
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `description` - Description * `-description` - Description (descending) * `next_version` - Next version * `-next_version` - Next version (descending) * `retain_repo_versions` - Retain repo versions * `-retain_repo_versions` - Retain repo versions (descending) * `user_hidden` - User hidden * `-user_hidden` - User hidden (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
pulp_type = 'pulp_type_example' # str | Pulp type  * `ostree.ostree` - ostree.ostree * `rpm.rpm` - rpm.rpm * `file.file` - file.file (optional)
pulp_type__in = ['pulp_type__in_example'] # list[str] | Multiple values may be separated by commas.  * `ostree.ostree` - ostree.ostree * `rpm.rpm` - rpm.rpm * `file.file` - file.file (optional)
q = 'q_example' # str |  (optional)
remote = 'remote_example' # str | Foreign Key referenced by HREF (optional)
retain_repo_versions = 56 # int | Filter results where retain_repo_versions matches value (optional)
retain_repo_versions__gt = 56 # int | Filter results where retain_repo_versions is greater than value (optional)
retain_repo_versions__gte = 56 # int | Filter results where retain_repo_versions is greater than or equal to value (optional)
retain_repo_versions__isnull = True # bool | Filter results where retain_repo_versions has a null value (optional)
retain_repo_versions__lt = 56 # int | Filter results where retain_repo_versions is less than value (optional)
retain_repo_versions__lte = 56 # int | Filter results where retain_repo_versions is less than or equal to value (optional)
retain_repo_versions__ne = 56 # int | Filter results where retain_repo_versions not equal to value (optional)
retain_repo_versions__range = [56] # list[int] | Filter results where retain_repo_versions is between two comma separated values (optional)
with_content = 'with_content_example' # str | Content Unit referenced by HREF (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List repositories
        api_response = api_instance.list(pulp_domain, latest_with_content=latest_with_content, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, pulp_type=pulp_type, pulp_type__in=pulp_type__in, q=q, remote=remote, retain_repo_versions=retain_repo_versions, retain_repo_versions__gt=retain_repo_versions__gt, retain_repo_versions__gte=retain_repo_versions__gte, retain_repo_versions__isnull=retain_repo_versions__isnull, retain_repo_versions__lt=retain_repo_versions__lt, retain_repo_versions__lte=retain_repo_versions__lte, retain_repo_versions__ne=retain_repo_versions__ne, retain_repo_versions__range=retain_repo_versions__range, with_content=with_content, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **latest_with_content** | **str**| Content Unit referenced by HREF | [optional] 
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
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;pulp_labels&#x60; - Pulp labels * &#x60;-pulp_labels&#x60; - Pulp labels (descending) * &#x60;description&#x60; - Description * &#x60;-description&#x60; - Description (descending) * &#x60;next_version&#x60; - Next version * &#x60;-next_version&#x60; - Next version (descending) * &#x60;retain_repo_versions&#x60; - Retain repo versions * &#x60;-retain_repo_versions&#x60; - Retain repo versions (descending) * &#x60;user_hidden&#x60; - User hidden * &#x60;-user_hidden&#x60; - User hidden (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_label_select** | **str**| Filter labels by search string | [optional] 
 **pulp_type** | **str**| Pulp type  * &#x60;ostree.ostree&#x60; - ostree.ostree * &#x60;rpm.rpm&#x60; - rpm.rpm * &#x60;file.file&#x60; - file.file | [optional] 
 **pulp_type__in** | [**list[str]**](str.md)| Multiple values may be separated by commas.  * &#x60;ostree.ostree&#x60; - ostree.ostree * &#x60;rpm.rpm&#x60; - rpm.rpm * &#x60;file.file&#x60; - file.file | [optional] 
 **q** | **str**|  | [optional] 
 **remote** | [**str**](.md)| Foreign Key referenced by HREF | [optional] 
 **retain_repo_versions** | **int**| Filter results where retain_repo_versions matches value | [optional] 
 **retain_repo_versions__gt** | **int**| Filter results where retain_repo_versions is greater than value | [optional] 
 **retain_repo_versions__gte** | **int**| Filter results where retain_repo_versions is greater than or equal to value | [optional] 
 **retain_repo_versions__isnull** | **bool**| Filter results where retain_repo_versions has a null value | [optional] 
 **retain_repo_versions__lt** | **int**| Filter results where retain_repo_versions is less than value | [optional] 
 **retain_repo_versions__lte** | **int**| Filter results where retain_repo_versions is less than or equal to value | [optional] 
 **retain_repo_versions__ne** | **int**| Filter results where retain_repo_versions not equal to value | [optional] 
 **retain_repo_versions__range** | [**list[int]**](int.md)| Filter results where retain_repo_versions is between two comma separated values | [optional] 
 **with_content** | **str**| Content Unit referenced by HREF | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedRepositoryResponseList**](PaginatedRepositoryResponseList.md)

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

