# pulpcore.client.pulp_service.ApiDebugAuthHeaderApi

All URIs are relative to *https://console.redhat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](ApiDebugAuthHeaderApi.md#get) | **GET** /api/pulp/debug_auth_header/ | 


# **get**
> get()



Returns the content of the authentication headers.

### Example


```python
import pulpcore.client.pulp_service
from pulpcore.client.pulp_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_service.Configuration(
    host = "https://console.redhat.com"
)


# Enter a context with an instance of the API client
with pulpcore.client.pulp_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_service.ApiDebugAuthHeaderApi(api_client)

    try:
        api_instance.get()
    except Exception as e:
        print("Exception when calling ApiDebugAuthHeaderApi->get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

