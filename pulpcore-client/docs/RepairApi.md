# pulpcore.client.pulpcore.RepairApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post**](RepairApi.md#post) | **POST** /api/pulp/{pulp_domain}/api/v3/repair/ | Repair Artifact Storage


# **post**
> AsyncOperationResponse post(pulp_domain, repair)

Repair Artifact Storage

Trigger an asynchronous task that checks for missing or corrupted artifacts, and attempts to redownload them.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulpcore.models.repair import Repair
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
    api_instance = pulpcore.client.pulpcore.RepairApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    repair = pulpcore.client.pulpcore.Repair() # Repair | 

    try:
        # Repair Artifact Storage
        api_response = api_instance.post(pulp_domain, repair)
        print("The response of RepairApi->post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepairApi->post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
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

