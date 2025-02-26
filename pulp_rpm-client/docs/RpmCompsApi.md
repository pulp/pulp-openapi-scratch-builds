# pulpcore.client.pulp_rpm.RpmCompsApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpm_comps_upload**](RpmCompsApi.md#rpm_comps_upload) | **POST** /api/pulp/{pulp_domain}/api/v3/rpm/comps/ | Upload comps.xml


# **rpm_comps_upload**
> AsyncOperationResponse rpm_comps_upload(pulp_domain, file, repository=repository, replace=replace)

Upload comps.xml

Trigger an asynchronous task to upload a comps.xml file.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.RpmCompsApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    file = None # bytearray | Full path of a comps.xml file that may be parsed into comps.xml Content units.
    repository = 'repository_example' # str | URI of an RPM repository the comps.xml content units should be associated to. (optional)
    replace = True # bool | If true, incoming comps.xml replaces existing comps-related ContentUnits in the specified repository. (optional)

    try:
        # Upload comps.xml
        api_response = api_instance.rpm_comps_upload(pulp_domain, file, repository=repository, replace=replace)
        print("The response of RpmCompsApi->rpm_comps_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpmCompsApi->rpm_comps_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **file** | **bytearray**| Full path of a comps.xml file that may be parsed into comps.xml Content units. | 
 **repository** | **str**| URI of an RPM repository the comps.xml content units should be associated to. | [optional] 
 **replace** | **bool**| If true, incoming comps.xml replaces existing comps-related ContentUnits in the specified repository. | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

