# pulpcore.client.pulpcore.LivezApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**livez_read**](LivezApi.md#livez_read) | **GET** /api/pulp/api/v3/livez/ | Inspect liveness of Pulp&#39;s REST API.


# **livez_read**
> livez_read()

Inspect liveness of Pulp's REST API.

Returns 200 OK when API is alive.

### Example

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


# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.LivezApi(api_client)
    
    try:
        # Inspect liveness of Pulp's REST API.
        api_instance.livez_read()
    except ApiException as e:
        print("Exception when calling LivezApi->livez_read: %s\n" % e)
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

