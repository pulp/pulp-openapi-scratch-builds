# pulpcore.client.pulp_python.ApiPypiApi

All URIs are relative to *https://console.redhat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read**](ApiPypiApi.md#read) | **GET** /api/pulp/pypi/{pulp_domain}/{path}/ | Get index summary


# **read**
> SummaryResponse read(path, pulp_domain, fields=fields, exclude_fields=exclude_fields)

Get index summary

Gets package summary stats of index.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.summary_response import SummaryResponse
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
    api_instance = pulpcore.client.pulp_python.ApiPypiApi(api_client)
    path = 'path_example' # str | 
    pulp_domain = 'pulp_domain_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Get index summary
        api_response = api_instance.read(path, pulp_domain, fields=fields, exclude_fields=exclude_fields)
        print("The response of ApiPypiApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiPypiApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **pulp_domain** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**SummaryResponse**](SummaryResponse.md)

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

