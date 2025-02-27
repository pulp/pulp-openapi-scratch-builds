# MavenMavenRemote

A Serializer for MavenRemote.  Add any new fields if defined on MavenRemote. Similar to the example above, in MavenArtifactSerializer. Additional validators can be added to the parent validators list  For example::  class Meta:     validators = platform.RemoteSerializer.Meta.validators + [myValidator1, myValidator2]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique name for this remote. | 
**url** | **str** | The URL of an external content source. | 
**ca_cert** | **str** | A PEM encoded CA certificate used to validate the server certificate presented by the remote server. | [optional] 
**client_cert** | **str** | A PEM encoded client certificate used for authentication. | [optional] 
**client_key** | **str** | A PEM encoded private key used for authentication. | [optional] 
**tls_validation** | **bool** | If True, TLS peer validation must be performed. | [optional] 
**proxy_url** | **str** | The proxy URL. Format: scheme://host:port | [optional] 
**proxy_username** | **str** | The username to authenticte to the proxy. | [optional] 
**proxy_password** | **str** | The password to authenticate to the proxy. Extra leading and trailing whitespace characters are not trimmed. | [optional] 
**username** | **str** | The username to be used for authentication when syncing. | [optional] 
**password** | **str** | The password to be used for authentication when syncing. Extra leading and trailing whitespace characters are not trimmed. | [optional] 
**pulp_labels** | **Dict[str, Optional[str]]** |  | [optional] 
**download_concurrency** | **int** | Total number of simultaneous connections. If not set then the default value will be used. | [optional] 
**max_retries** | **int** | Maximum number of retry attempts after a download failure. If not set then the default value (3) will be used. | [optional] 
**policy** | [**PolicyEnum**](PolicyEnum.md) | The policy to use when downloading content.  * &#x60;immediate&#x60; - When syncing, download all metadata and content now. | [optional] 
**total_timeout** | **float** | aiohttp.ClientTimeout.total (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used. | [optional] 
**connect_timeout** | **float** | aiohttp.ClientTimeout.connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used. | [optional] 
**sock_connect_timeout** | **float** | aiohttp.ClientTimeout.sock_connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used. | [optional] 
**sock_read_timeout** | **float** | aiohttp.ClientTimeout.sock_read (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used. | [optional] 
**headers** | **List[object]** | Headers for aiohttp.Clientsession | [optional] 
**rate_limit** | **int** | Limits requests per second for each concurrent downloader | [optional] 

## Example

```python
from pulpcore.client.pulp_maven.models.maven_maven_remote import MavenMavenRemote

# TODO update the JSON string below
json = "{}"
# create an instance of MavenMavenRemote from a JSON string
maven_maven_remote_instance = MavenMavenRemote.from_json(json)
# print the JSON string representation of the object
print(MavenMavenRemote.to_json())

# convert the object into a dict
maven_maven_remote_dict = maven_maven_remote_instance.to_dict()
# create an instance of MavenMavenRemote from a dict
maven_maven_remote_from_dict = MavenMavenRemote.from_dict(maven_maven_remote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


