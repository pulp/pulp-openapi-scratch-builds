# pulpcore.client.pulp_python.PypiSimpleApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](PypiSimpleApi.md#create) | **POST** /pypi/{pulp_domain}/{path}/simple/ | Upload a package
[**pypi_simple_package_read**](PypiSimpleApi.md#pypi_simple_package_read) | **GET** /pypi/{pulp_domain}/{path}/simple/{package}/ | Get package simple page
[**read**](PypiSimpleApi.md#read) | **GET** /pypi/{pulp_domain}/{path}/simple/ | Get index simple page


# **create**
> PackageUploadTaskResponse create(path, pulp_domain, content, sha256_digest, action=action)

Upload a package

Upload package to the index. This endpoint has the same functionality as the upload endpoint at the `/legacy` url of the index. This is provided for convenience for users who want a single index url for all their Python tools. (pip, twine, poetry, pipenv, ...)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.package_upload_task_response import PackageUploadTaskResponse
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

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
    api_instance = pulpcore.client.pulp_python.PypiSimpleApi(api_client)
    path = 'path_example' # str | 
    pulp_domain = 'pulp_domain_example' # str | 
    content = None # bytearray | A Python package release file to upload to the index.
    sha256_digest = 'sha256_digest_example' # str | SHA256 of package to validate upload integrity.
    action = 'file_upload' # str | Defaults to `file_upload`, don't change it or request will fail! (optional) (default to 'file_upload')

    try:
        # Upload a package
        api_response = api_instance.create(path, pulp_domain, content, sha256_digest, action=action)
        print("The response of PypiSimpleApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PypiSimpleApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **pulp_domain** | **str**|  | 
 **content** | **bytearray**| A Python package release file to upload to the index. | 
 **sha256_digest** | **str**| SHA256 of package to validate upload integrity. | 
 **action** | **str**| Defaults to &#x60;file_upload&#x60;, don&#39;t change it or request will fail! | [optional] [default to &#39;file_upload&#39;]

### Return type

[**PackageUploadTaskResponse**](PackageUploadTaskResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pypi_simple_package_read**
> pypi_simple_package_read(package, path, pulp_domain, fields=fields, exclude_fields=exclude_fields)

Get package simple page

Retrieves the simple api html page for a package.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

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
    api_instance = pulpcore.client.pulp_python.PypiSimpleApi(api_client)
    package = 'package_example' # str | 
    path = 'path_example' # str | 
    pulp_domain = 'pulp_domain_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Get package simple page
        api_instance.pypi_simple_package_read(package, path, pulp_domain, fields=fields, exclude_fields=exclude_fields)
    except Exception as e:
        print("Exception when calling PypiSimpleApi->pypi_simple_package_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package** | **str**|  | 
 **path** | **str**|  | 
 **pulp_domain** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> read(path, pulp_domain, fields=fields, exclude_fields=exclude_fields)

Get index simple page

Gets the simple api html page for the index.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

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
    api_instance = pulpcore.client.pulp_python.PypiSimpleApi(api_client)
    path = 'path_example' # str | 
    pulp_domain = 'pulp_domain_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Get index simple page
        api_instance.read(path, pulp_domain, fields=fields, exclude_fields=exclude_fields)
    except Exception as e:
        print("Exception when calling PypiSimpleApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **pulp_domain** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

