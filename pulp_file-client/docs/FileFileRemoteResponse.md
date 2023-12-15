# FileFileRemoteResponse

Serializer for File Remotes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**name** | **str** | A unique name for this remote. | 
**url** | **str** | The URL of an external content source. | 
**ca_cert** | **str** | A PEM encoded CA certificate used to validate the server certificate presented by the remote server. | [optional] 
**client_cert** | **str** | A PEM encoded client certificate used for authentication. | [optional] 
**tls_validation** | **bool** | If True, TLS peer validation must be performed. | [optional] 
**proxy_url** | **str** | The proxy URL. Format: scheme://host:port | [optional] 
**pulp_labels** | **dict(str, str)** |  | [optional] 
**pulp_last_updated** | **datetime** | Timestamp of the most recent update of the remote. | [optional] [readonly] 
**download_concurrency** | **int** | Total number of simultaneous connections. If not set then the default value will be used. | [optional] 
**max_retries** | **int** | Maximum number of retry attempts after a download failure. If not set then the default value (3) will be used. | [optional] 
**policy** | [**PolicyEnum**](PolicyEnum.md) | The policy to use when downloading content. The possible values include: &#39;immediate&#39;, &#39;on_demand&#39;, and &#39;streamed&#39;. &#39;immediate&#39; is the default.  * &#x60;immediate&#x60; - When syncing, download all metadata and content now. * &#x60;on_demand&#x60; - When syncing, download metadata, but do not download content now. Instead, download content as clients request it, and save it in Pulp to be served for future client requests. * &#x60;streamed&#x60; - When syncing, download metadata, but do not download content now. Instead,download content as clients request it, but never save it in Pulp. This causes future requests for that same content to have to be downloaded again. | [optional] 
**total_timeout** | **float** | aiohttp.ClientTimeout.total (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used. | [optional] 
**connect_timeout** | **float** | aiohttp.ClientTimeout.connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used. | [optional] 
**sock_connect_timeout** | **float** | aiohttp.ClientTimeout.sock_connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used. | [optional] 
**sock_read_timeout** | **float** | aiohttp.ClientTimeout.sock_read (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used. | [optional] 
**headers** | **list[object]** | Headers for aiohttp.Clientsession | [optional] 
**rate_limit** | **int** | Limits requests per second for each concurrent downloader | [optional] 
**hidden_fields** | [**list[FileFileRemoteResponseHiddenFields]**](FileFileRemoteResponseHiddenFields.md) | List of hidden (write only) fields | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


