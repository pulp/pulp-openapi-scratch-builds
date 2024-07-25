# UpstreamPulpResponse

Serializer for a Server.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the most recent update of the remote. | [optional] [readonly] 
**name** | **str** | A unique name for this Pulp server. | 
**base_url** | **str** | The transport, hostname, and an optional port of the Pulp server. e.g. https://example.com | 
**api_root** | **str** | The API root. Defaults to &#39;/pulp/&#39;. | 
**domain** | **str** | The domain of the Pulp server if enabled. | [optional] 
**ca_cert** | **str** | A PEM encoded CA certificate used to validate the server certificate presented by the remote server. | [optional] 
**client_cert** | **str** | A PEM encoded client certificate used for authentication. | [optional] 
**tls_validation** | **bool** | If True, TLS peer validation must be performed. | [optional] 
**hidden_fields** | [**list[RemoteResponseHiddenFields]**](RemoteResponseHiddenFields.md) | List of hidden (write only) fields | [optional] [readonly] 
**pulp_label_select** | **str** | One or more comma separated labels that will be used to filter distributions on the upstream Pulp. E.g. \&quot;foo&#x3D;bar,key&#x3D;val\&quot; or \&quot;foo,key\&quot; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


