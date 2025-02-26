# pulpcore.client.pulpcore.RepositoriesReclaimSpaceApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reclaim**](RepositoriesReclaimSpaceApi.md#reclaim) | **POST** /api/pulp/{pulp_domain}/api/v3/repositories/reclaim_space/ | 


# **reclaim**
> AsyncOperationResponse reclaim(pulp_domain, reclaim_space)



Trigger an asynchronous space reclaim operation.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulpcore.models.reclaim_space import ReclaimSpace
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
    api_instance = pulpcore.client.pulpcore.RepositoriesReclaimSpaceApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    reclaim_space = pulpcore.client.pulpcore.ReclaimSpace() # ReclaimSpace | 

    try:
        api_response = api_instance.reclaim(pulp_domain, reclaim_space)
        print("The response of RepositoriesReclaimSpaceApi->reclaim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesReclaimSpaceApi->reclaim: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **reclaim_space** | [**ReclaimSpace**](ReclaimSpace.md)|  | 

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

