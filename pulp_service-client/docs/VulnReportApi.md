# pulpcore.client.pulp_service.VulnReportApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](VulnReportApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/vuln_report/ | Generate vulnerability report
[**delete**](VulnReportApi.md#delete) | **DELETE** {service_vulnerability_report_href} | Delete a vulnerability report
[**list**](VulnReportApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/vuln_report/ | List vulnerability reports
[**read**](VulnReportApi.md#read) | **GET** {service_vulnerability_report_href} | Inspect a vulnerability report


# **create**
> AsyncOperationResponse create(pulp_domain, repo_version=repo_version, package_json=package_json)

Generate vulnerability report

Trigger a task to generate the package vulnerability report

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_service
from pulpcore.client.pulp_service.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_service.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_service.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_service.VulnReportApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    repo_version = 'repo_version_example' # str | RepositoryVersion HREF with the packages to be checked. (optional)
    package_json = None # bytearray | package-lock.json file with the definition of dependencies to be checked. (optional)

    try:
        # Generate vulnerability report
        api_response = api_instance.create(pulp_domain, repo_version=repo_version, package_json=package_json)
        print("The response of VulnReportApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VulnReportApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **repo_version** | **str**| RepositoryVersion HREF with the packages to be checked. | [optional] 
 **package_json** | **bytearray**| package-lock.json file with the definition of dependencies to be checked. | [optional] 

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

# **delete**
> delete(service_vulnerability_report_href)

Delete a vulnerability report

A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_service
from pulpcore.client.pulp_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_service.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_service.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_service.VulnReportApi(api_client)
    service_vulnerability_report_href = 'service_vulnerability_report_href_example' # str | 

    try:
        # Delete a vulnerability report
        api_instance.delete(service_vulnerability_report_href)
    except Exception as e:
        print("Exception when calling VulnReportApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_vulnerability_report_href** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedserviceVulnerabilityReportResponseList list(pulp_domain, limit=limit, offset=offset, fields=fields, exclude_fields=exclude_fields)

List vulnerability reports

A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_service
from pulpcore.client.pulp_service.models.paginatedservice_vulnerability_report_response_list import PaginatedserviceVulnerabilityReportResponseList
from pulpcore.client.pulp_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_service.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_service.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_service.VulnReportApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    limit = 56 # int | Number of results to return per page. (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List vulnerability reports
        api_response = api_instance.list(pulp_domain, limit=limit, offset=offset, fields=fields, exclude_fields=exclude_fields)
        print("The response of VulnReportApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VulnReportApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedserviceVulnerabilityReportResponseList**](PaginatedserviceVulnerabilityReportResponseList.md)

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
> ServiceVulnerabilityReportResponse read(service_vulnerability_report_href, fields=fields, exclude_fields=exclude_fields)

Inspect a vulnerability report

A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_service
from pulpcore.client.pulp_service.models.service_vulnerability_report_response import ServiceVulnerabilityReportResponse
from pulpcore.client.pulp_service.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_service.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_service.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_service.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_service.VulnReportApi(api_client)
    service_vulnerability_report_href = 'service_vulnerability_report_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a vulnerability report
        api_response = api_instance.read(service_vulnerability_report_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of VulnReportApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VulnReportApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_vulnerability_report_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**ServiceVulnerabilityReportResponse**](ServiceVulnerabilityReportResponse.md)

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

