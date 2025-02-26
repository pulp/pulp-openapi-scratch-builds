# pulpcore.client.pulpcore.StatusApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_read**](StatusApi.md#status_read) | **GET** /api/pulp/api/v3/status/ | Inspect status of Pulp


# **status_read**
> StatusResponse status_read()

Inspect status of Pulp

Returns status and app information about Pulp.  Information includes:  * version of pulpcore and loaded pulp plugins  * known workers  * known content apps  * database connection status  * redis connection status  * disk usage information

### Example


```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.status_response import StatusResponse
from pulpcore.client.pulpcore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://localhost:5001"
)


# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.StatusApi(api_client)

    try:
        # Inspect status of Pulp
        api_response = api_instance.status_read()
        print("The response of StatusApi->status_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->status_read: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

