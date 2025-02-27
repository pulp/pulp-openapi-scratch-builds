# pulpcore.client.pulp_maven.PulpMavenApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](PulpMavenApi.md#get) | **GET** /pulp/maven/{name}/{path} | 
[**put**](PulpMavenApi.md#put) | **PUT** /pulp/maven/{name}/{path} | 


# **get**
> get(name, path, fields=fields, exclude_fields=exclude_fields)



Responds to GET requests about manifests by reference

### Example


```python
import pulpcore.client.pulp_maven
from pulpcore.client.pulp_maven.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_maven.Configuration(
    host = "http://localhost:5001"
)


# Enter a context with an instance of the API client
with pulpcore.client.pulp_maven.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_maven.PulpMavenApi(api_client)
    name = 'name_example' # str | 
    path = 'path_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        api_instance.get(name, path, fields=fields, exclude_fields=exclude_fields)
    except Exception as e:
        print("Exception when calling PulpMavenApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **path** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

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

# **put**
> put(name, path)



ViewSet for interacting with maven deploy API

### Example


```python
import pulpcore.client.pulp_maven
from pulpcore.client.pulp_maven.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_maven.Configuration(
    host = "http://localhost:5001"
)


# Enter a context with an instance of the API client
with pulpcore.client.pulp_maven.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_maven.PulpMavenApi(api_client)
    name = 'name_example' # str | 
    path = 'path_example' # str | 

    try:
        api_instance.put(name, path)
    except Exception as e:
        print("Exception when calling PulpMavenApi->put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **path** | **str**|  | 

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

