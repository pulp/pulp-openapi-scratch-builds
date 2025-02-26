# OstreeOstreeRemoteResponse

A Serializer class for a remote OSTree repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the most recent update of the remote. | [optional] [readonly] 
**name** | **str** | A unique name for this remote. | 
**url** | **str** | The URL of an external content source. | 
**ca_cert** | **str** | A PEM encoded CA certificate used to validate the server certificate presented by the remote server. | [optional] 
**client_cert** | **str** | A PEM encoded client certificate used for authentication. | [optional] 
**tls_validation** | **bool** | If True, TLS peer validation must be performed. | [optional] 
**proxy_url** | **str** | The proxy URL. Format: scheme://host:port | [optional] 
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**download_concurrency** | **int** | Total number of simultaneous connections. If not set then the default value will be used. | [optional] 
**max_retries** | **int** | Maximum number of retry attempts after a download failure. If not set then the default value (3) will be used. | [optional] 
**policy** | [**PolicyEnum**](PolicyEnum.md) |          immediate - All OSTree objects are downloaded and saved during synchronization.         on_demand - Only commits, dirtrees, and refs are downloaded. Other OSTree objects are                     not downloaded until they are requested for the first time by a client.           * &#x60;immediate&#x60; - immediate * &#x60;on_demand&#x60; - on_demand | [optional] 
**total_timeout** | **float** | aiohttp.ClientTimeout.total (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used. | [optional] 
**connect_timeout** | **float** | aiohttp.ClientTimeout.connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used. | [optional] 
**sock_connect_timeout** | **float** | aiohttp.ClientTimeout.sock_connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used. | [optional] 
**sock_read_timeout** | **float** | aiohttp.ClientTimeout.sock_read (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used. | [optional] 
**headers** | **List[object]** | Headers for aiohttp.Clientsession | [optional] 
**rate_limit** | **int** | Limits requests per second for each concurrent downloader | [optional] 
**hidden_fields** | [**List[OstreeOstreeRemoteResponseHiddenFieldsInner]**](OstreeOstreeRemoteResponseHiddenFieldsInner.md) | List of hidden (write only) fields | [optional] [readonly] 
**depth** | **int** | An option to specify how many commits to traverse. | [optional] [default to 0]
**include_refs** | **List[str]** |              A list of refs to include during a sync.             The wildcards *, ? are recognized.             &#39;include_refs&#39; is evaluated before &#39;exclude_refs&#39;.              | [optional] 
**exclude_refs** | **List[str]** |              A list of tags to exclude during a sync.             The wildcards *, ? are recognized.             &#39;exclude_refs&#39; is evaluated after &#39;include_refs&#39;.              | [optional] 

## Example

```python
from pulpcore.client.pulp_ostree.models.ostree_ostree_remote_response import OstreeOstreeRemoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OstreeOstreeRemoteResponse from a JSON string
ostree_ostree_remote_response_instance = OstreeOstreeRemoteResponse.from_json(json)
# print the JSON string representation of the object
print(OstreeOstreeRemoteResponse.to_json())

# convert the object into a dict
ostree_ostree_remote_response_dict = ostree_ostree_remote_response_instance.to_dict()
# create an instance of OstreeOstreeRemoteResponse from a dict
ostree_ostree_remote_response_from_dict = OstreeOstreeRemoteResponse.from_dict(ostree_ostree_remote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


