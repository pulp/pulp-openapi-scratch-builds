# pulpcore.client.pulpcore.PublicationsApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](PublicationsApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/publications/ | List publications


# **list**
> PaginatedPublicationResponseList list(pulp_domain, content=content, content__in=content__in, limit=limit, offset=offset, ordering=ordering, prn__in=prn__in, pulp_created=pulp_created, pulp_created__gt=pulp_created__gt, pulp_created__gte=pulp_created__gte, pulp_created__isnull=pulp_created__isnull, pulp_created__lt=pulp_created__lt, pulp_created__lte=pulp_created__lte, pulp_created__range=pulp_created__range, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_type=pulp_type, pulp_type__in=pulp_type__in, q=q, repository=repository, repository_version=repository_version, fields=fields, exclude_fields=exclude_fields)

List publications

A base class for any publication viewset.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.paginated_publication_response_list import PaginatedPublicationResponseList
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
    api_instance = pulpcore.client.pulpcore.PublicationsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    content = 'content_example' # str | Content Unit referenced by HREF/PRN (optional)
    content__in = ['content__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    ordering = ['ordering_example'] # List[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `complete` - Complete * `-complete` - Complete (descending) * `pass_through` - Pass through * `-pass_through` - Pass through (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
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
    pulp_type = 'pulp_type_example' # str | Pulp type  * `file.file` - file.file * `rpm.rpm` - rpm.rpm (optional)
    pulp_type__in = ['pulp_type__in_example'] # List[str] | Multiple values may be separated by commas.  * `file.file` - file.file * `rpm.rpm` - rpm.rpm (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    repository = 'repository_example' # str | Repository referenced by HREF/PRN (optional)
    repository_version = 'repository_version_example' # str | Repository Version referenced by HREF/PRN (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List publications
        api_response = api_instance.list(pulp_domain, content=content, content__in=content__in, limit=limit, offset=offset, ordering=ordering, prn__in=prn__in, pulp_created=pulp_created, pulp_created__gt=pulp_created__gt, pulp_created__gte=pulp_created__gte, pulp_created__isnull=pulp_created__isnull, pulp_created__lt=pulp_created__lt, pulp_created__lte=pulp_created__lte, pulp_created__range=pulp_created__range, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_type=pulp_type, pulp_type__in=pulp_type__in, q=q, repository=repository, repository_version=repository_version, fields=fields, exclude_fields=exclude_fields)
        print("The response of PublicationsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **content** | **str**| Content Unit referenced by HREF/PRN | [optional] 
 **content__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;complete&#x60; - Complete * &#x60;-complete&#x60; - Complete (descending) * &#x60;pass_through&#x60; - Pass through * &#x60;-pass_through&#x60; - Pass through (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
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
 **pulp_type** | **str**| Pulp type  * &#x60;file.file&#x60; - file.file * &#x60;rpm.rpm&#x60; - rpm.rpm | [optional] 
 **pulp_type__in** | [**List[str]**](str.md)| Multiple values may be separated by commas.  * &#x60;file.file&#x60; - file.file * &#x60;rpm.rpm&#x60; - rpm.rpm | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **repository** | **str**| Repository referenced by HREF/PRN | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedPublicationResponseList**](PaginatedPublicationResponseList.md)

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

