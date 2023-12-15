# UpstreamPulp

Serializer for a Server.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique name for this Pulp server. | 
**base_url** | **str** | The transport, hostname, and an optional port of the Pulp server. e.g. https://example.com | 
**api_root** | **str** | The API root. Defaults to &#39;/pulp/&#39;. | 
**domain** | **str** | The domain of the Pulp server if enabled. | [optional] 
**ca_cert** | **str** | A PEM encoded CA certificate used to validate the server certificate presented by the remote server. | [optional] 
**client_cert** | **str** | A PEM encoded client certificate used for authentication. | [optional] 
**client_key** | **str** | A PEM encoded private key used for authentication. | [optional] 
**tls_validation** | **bool** | If True, TLS peer validation must be performed. | [optional] 
**username** | **str** | The username to be used for authentication when syncing. | [optional] 
**password** | **str** | The password to be used for authentication when syncing. Extra leading and trailing whitespace characters are not trimmed. | [optional] 
**pulp_label_select** | **str** | One or more comma separated labels that will be used to filter distributions on the upstream Pulp. E.g. \&quot;foo&#x3D;bar,key&#x3D;val\&quot; or \&quot;foo,key\&quot; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


