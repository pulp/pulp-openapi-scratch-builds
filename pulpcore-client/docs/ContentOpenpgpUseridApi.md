# pulpcore.client.pulpcore.ContentOpenpgpUseridApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](ContentOpenpgpUseridApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/content/core/openpgp_userid/ | List open pgp user ids
[**read**](ContentOpenpgpUseridApi.md#read) | **GET** {open_p_g_p_user_i_d_href} | Inspect an open pgp user id


# **list**
> PaginatedOpenPGPUserIDResponseList list(pulp_domain, limit=limit, offset=offset, ordering=ordering, orphaned_for=orphaned_for, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, user_id=user_id, user_id__contains=user_id__contains, user_id__icontains=user_id__icontains, user_id__iexact=user_id__iexact, user_id__in=user_id__in, user_id__iregex=user_id__iregex, user_id__istartswith=user_id__istartswith, user_id__regex=user_id__regex, user_id__startswith=user_id__startswith, fields=fields, exclude_fields=exclude_fields)

List open pgp user ids

Content viewset that supports only GET by default.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.paginated_open_pgp_user_id_response_list import PaginatedOpenPGPUserIDResponseList
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
    api_instance = pulpcore.client.pulpcore.ContentOpenpgpUseridApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    ordering = ['ordering_example'] # List[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `raw_data` - Raw data * `-raw_data` - Raw data (descending) * `user_id` - User id * `-user_id` - User id (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
    orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
    prn__in = ['prn__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_href__in = ['pulp_href__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_id__in = ['pulp_id__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    repository_version = 'repository_version_example' # str | Repository Version referenced by HREF/PRN (optional)
    repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF/PRN (optional)
    repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF/PRN (optional)
    user_id = 'user_id_example' # str | Filter results where user_id matches value (optional)
    user_id__contains = 'user_id__contains_example' # str | Filter results where user_id contains value (optional)
    user_id__icontains = 'user_id__icontains_example' # str | Filter results where user_id contains value (optional)
    user_id__iexact = 'user_id__iexact_example' # str | Filter results where user_id matches value (optional)
    user_id__in = ['user_id__in_example'] # List[str] | Filter results where user_id is in a comma-separated list of values (optional)
    user_id__iregex = 'user_id__iregex_example' # str | Filter results where user_id matches regex value (optional)
    user_id__istartswith = 'user_id__istartswith_example' # str | Filter results where user_id starts with value (optional)
    user_id__regex = 'user_id__regex_example' # str | Filter results where user_id matches regex value (optional)
    user_id__startswith = 'user_id__startswith_example' # str | Filter results where user_id starts with value (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List open pgp user ids
        api_response = api_instance.list(pulp_domain, limit=limit, offset=offset, ordering=ordering, orphaned_for=orphaned_for, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, user_id=user_id, user_id__contains=user_id__contains, user_id__icontains=user_id__icontains, user_id__iexact=user_id__iexact, user_id__in=user_id__in, user_id__iregex=user_id__iregex, user_id__istartswith=user_id__istartswith, user_id__regex=user_id__regex, user_id__startswith=user_id__startswith, fields=fields, exclude_fields=exclude_fields)
        print("The response of ContentOpenpgpUseridApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentOpenpgpUseridApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;upstream_id&#x60; - Upstream id * &#x60;-upstream_id&#x60; - Upstream id (descending) * &#x60;timestamp_of_interest&#x60; - Timestamp of interest * &#x60;-timestamp_of_interest&#x60; - Timestamp of interest (descending) * &#x60;raw_data&#x60; - Raw data * &#x60;-raw_data&#x60; - Raw data (descending) * &#x60;user_id&#x60; - User id * &#x60;-user_id&#x60; - User id (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **orphaned_for** | **float**| Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. | [optional] 
 **prn__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_href__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **user_id** | **str**| Filter results where user_id matches value | [optional] 
 **user_id__contains** | **str**| Filter results where user_id contains value | [optional] 
 **user_id__icontains** | **str**| Filter results where user_id contains value | [optional] 
 **user_id__iexact** | **str**| Filter results where user_id matches value | [optional] 
 **user_id__in** | [**List[str]**](str.md)| Filter results where user_id is in a comma-separated list of values | [optional] 
 **user_id__iregex** | **str**| Filter results where user_id matches regex value | [optional] 
 **user_id__istartswith** | **str**| Filter results where user_id starts with value | [optional] 
 **user_id__regex** | **str**| Filter results where user_id matches regex value | [optional] 
 **user_id__startswith** | **str**| Filter results where user_id starts with value | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedOpenPGPUserIDResponseList**](PaginatedOpenPGPUserIDResponseList.md)

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
> OpenPGPUserIDResponse read(open_p_g_p_user_i_d_href, fields=fields, exclude_fields=exclude_fields)

Inspect an open pgp user id

Content viewset that supports only GET by default.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.open_pgp_user_id_response import OpenPGPUserIDResponse
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
    api_instance = pulpcore.client.pulpcore.ContentOpenpgpUseridApi(api_client)
    open_p_g_p_user_i_d_href = 'open_p_g_p_user_i_d_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an open pgp user id
        api_response = api_instance.read(open_p_g_p_user_i_d_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of ContentOpenpgpUseridApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentOpenpgpUseridApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_p_g_p_user_i_d_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**OpenPGPUserIDResponse**](OpenPGPUserIDResponse.md)

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

