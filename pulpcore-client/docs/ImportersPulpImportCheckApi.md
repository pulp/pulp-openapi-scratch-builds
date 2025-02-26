# pulpcore.client.pulpcore.ImportersPulpImportCheckApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pulp_import_check_post**](ImportersPulpImportCheckApi.md#pulp_import_check_post) | **POST** /api/pulp/{pulp_domain}/api/v3/importers/core/pulp/import-check/ | Validate the parameters to be used for a PulpImport call


# **pulp_import_check_post**
> PulpImportCheckResponse pulp_import_check_post(pulp_domain, pulp_import_check)

Validate the parameters to be used for a PulpImport call

Evaluates validity of proposed PulpImport parameters 'toc', 'path', and 'repo_mapping'.  * Checks that toc, path are in ALLOWED_IMPORT_PATHS * if ALLOWED:   * Checks that toc, path exist and are readable   * If toc specified, checks that containing dir is writeable * Checks that repo_mapping is valid JSON

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.pulp_import_check import PulpImportCheck
from pulpcore.client.pulpcore.models.pulp_import_check_response import PulpImportCheckResponse
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
    api_instance = pulpcore.client.pulpcore.ImportersPulpImportCheckApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    pulp_import_check = pulpcore.client.pulpcore.PulpImportCheck() # PulpImportCheck | 

    try:
        # Validate the parameters to be used for a PulpImport call
        api_response = api_instance.pulp_import_check_post(pulp_domain, pulp_import_check)
        print("The response of ImportersPulpImportCheckApi->pulp_import_check_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportersPulpImportCheckApi->pulp_import_check_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **pulp_import_check** | [**PulpImportCheck**](PulpImportCheck.md)|  | 

### Return type

[**PulpImportCheckResponse**](PulpImportCheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

