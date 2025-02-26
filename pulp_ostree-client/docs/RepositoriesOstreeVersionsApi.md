# pulpcore.client.pulp_ostree.RepositoriesOstreeVersionsApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](RepositoriesOstreeVersionsApi.md#delete) | **DELETE** {ostree_ostree_repository_version_href} | Delete a repository version
[**list**](RepositoriesOstreeVersionsApi.md#list) | **GET** {ostree_ostree_repository_href}versions/ | List repository versions
[**read**](RepositoriesOstreeVersionsApi.md#read) | **GET** {ostree_ostree_repository_version_href} | Inspect a repository version
[**repair**](RepositoriesOstreeVersionsApi.md#repair) | **POST** {ostree_ostree_repository_version_href}repair/ | 


# **delete**
> AsyncOperationResponse delete(ostree_ostree_repository_version_href)

Delete a repository version

Trigger an asynchronous task to delete a repository version.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.RepositoriesOstreeVersionsApi(api_client)
    ostree_ostree_repository_version_href = 'ostree_ostree_repository_version_href_example' # str | 

    try:
        # Delete a repository version
        api_response = api_instance.delete(ostree_ostree_repository_version_href)
        print("The response of RepositoriesOstreeVersionsApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesOstreeVersionsApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_repository_version_href** | **str**|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

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

# **list**
> PaginatedRepositoryVersionResponseList list(ostree_ostree_repository_href, content=content, content__in=content__in, limit=limit, number=number, number__gt=number__gt, number__gte=number__gte, number__lt=number__lt, number__lte=number__lte, number__range=number__range, offset=offset, ordering=ordering, prn__in=prn__in, pulp_created=pulp_created, pulp_created__gt=pulp_created__gt, pulp_created__gte=pulp_created__gte, pulp_created__isnull=pulp_created__isnull, pulp_created__lt=pulp_created__lt, pulp_created__lte=pulp_created__lte, pulp_created__range=pulp_created__range, pulp_href__in=pulp_href__in, q=q, fields=fields, exclude_fields=exclude_fields)

List repository versions

A ViewSet class that represents a single OSTree repository version.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.models.paginated_repository_version_response_list import PaginatedRepositoryVersionResponseList
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.RepositoriesOstreeVersionsApi(api_client)
    ostree_ostree_repository_href = 'ostree_ostree_repository_href_example' # str | 
    content = 'content_example' # str | Content Unit referenced by HREF/PRN (optional)
    content__in = ['content__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    number = 56 # int | Filter results where number matches value (optional)
    number__gt = 56 # int | Filter results where number is greater than value (optional)
    number__gte = 56 # int | Filter results where number is greater than or equal to value (optional)
    number__lt = 56 # int | Filter results where number is less than value (optional)
    number__lte = 56 # int | Filter results where number is less than or equal to value (optional)
    number__range = [56] # List[int] | Filter results where number is between two comma separated values (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    ordering = ['ordering_example'] # List[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `number` - Number * `-number` - Number (descending) * `complete` - Complete * `-complete` - Complete (descending) * `info` - Info * `-info` - Info (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
    prn__in = ['prn__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_created = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created matches value (optional)
    pulp_created__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is greater than value (optional)
    pulp_created__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is greater than or equal to value (optional)
    pulp_created__isnull = True # bool | Filter results where pulp_created has a null value (optional)
    pulp_created__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is less than value (optional)
    pulp_created__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where pulp_created is less than or equal to value (optional)
    pulp_created__range = ['2013-10-20T19:20:30+01:00'] # List[datetime] | Filter results where pulp_created is between two comma separated values (optional)
    pulp_href__in = ['pulp_href__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List repository versions
        api_response = api_instance.list(ostree_ostree_repository_href, content=content, content__in=content__in, limit=limit, number=number, number__gt=number__gt, number__gte=number__gte, number__lt=number__lt, number__lte=number__lte, number__range=number__range, offset=offset, ordering=ordering, prn__in=prn__in, pulp_created=pulp_created, pulp_created__gt=pulp_created__gt, pulp_created__gte=pulp_created__gte, pulp_created__isnull=pulp_created__isnull, pulp_created__lt=pulp_created__lt, pulp_created__lte=pulp_created__lte, pulp_created__range=pulp_created__range, pulp_href__in=pulp_href__in, q=q, fields=fields, exclude_fields=exclude_fields)
        print("The response of RepositoriesOstreeVersionsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesOstreeVersionsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_repository_href** | **str**|  | 
 **content** | **str**| Content Unit referenced by HREF/PRN | [optional] 
 **content__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **number** | **int**| Filter results where number matches value | [optional] 
 **number__gt** | **int**| Filter results where number is greater than value | [optional] 
 **number__gte** | **int**| Filter results where number is greater than or equal to value | [optional] 
 **number__lt** | **int**| Filter results where number is less than value | [optional] 
 **number__lte** | **int**| Filter results where number is less than or equal to value | [optional] 
 **number__range** | [**List[int]**](int.md)| Filter results where number is between two comma separated values | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;number&#x60; - Number * &#x60;-number&#x60; - Number (descending) * &#x60;complete&#x60; - Complete * &#x60;-complete&#x60; - Complete (descending) * &#x60;info&#x60; - Info * &#x60;-info&#x60; - Info (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **prn__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_created** | **datetime**| Filter results where pulp_created matches value | [optional] 
 **pulp_created__gt** | **datetime**| Filter results where pulp_created is greater than value | [optional] 
 **pulp_created__gte** | **datetime**| Filter results where pulp_created is greater than or equal to value | [optional] 
 **pulp_created__isnull** | **bool**| Filter results where pulp_created has a null value | [optional] 
 **pulp_created__lt** | **datetime**| Filter results where pulp_created is less than value | [optional] 
 **pulp_created__lte** | **datetime**| Filter results where pulp_created is less than or equal to value | [optional] 
 **pulp_created__range** | [**List[datetime]**](datetime.md)| Filter results where pulp_created is between two comma separated values | [optional] 
 **pulp_href__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedRepositoryVersionResponseList**](PaginatedRepositoryVersionResponseList.md)

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

# **read**
> RepositoryVersionResponse read(ostree_ostree_repository_version_href, fields=fields, exclude_fields=exclude_fields)

Inspect a repository version

A ViewSet class that represents a single OSTree repository version.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.models.repository_version_response import RepositoryVersionResponse
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.RepositoriesOstreeVersionsApi(api_client)
    ostree_ostree_repository_version_href = 'ostree_ostree_repository_version_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a repository version
        api_response = api_instance.read(ostree_ostree_repository_version_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of RepositoriesOstreeVersionsApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesOstreeVersionsApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_repository_version_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**RepositoryVersionResponse**](RepositoryVersionResponse.md)

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

# **repair**
> AsyncOperationResponse repair(ostree_ostree_repository_version_href, repair)



Trigger an asynchronous task to repair a repository version.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_ostree
from pulpcore.client.pulp_ostree.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_ostree.models.repair import Repair
from pulpcore.client.pulp_ostree.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_ostree.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_ostree.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_ostree.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_ostree.RepositoriesOstreeVersionsApi(api_client)
    ostree_ostree_repository_version_href = 'ostree_ostree_repository_version_href_example' # str | 
    repair = pulpcore.client.pulp_ostree.Repair() # Repair | 

    try:
        api_response = api_instance.repair(ostree_ostree_repository_version_href, repair)
        print("The response of RepositoriesOstreeVersionsApi->repair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesOstreeVersionsApi->repair: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ostree_ostree_repository_version_href** | **str**|  | 
 **repair** | [**Repair**](Repair.md)|  | 

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

