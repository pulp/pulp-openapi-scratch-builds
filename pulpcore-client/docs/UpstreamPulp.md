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
**q_select** | **str** | Filter distributions on the upstream Pulp using complex filtering. E.g. pulp_label_select&#x3D;\&quot;foo\&quot; OR pulp_label_select&#x3D;\&quot;key&#x3D;val\&quot; | [optional] 

## Example

```python
from pulpcore.client.pulpcore.models.upstream_pulp import UpstreamPulp

# TODO update the JSON string below
json = "{}"
# create an instance of UpstreamPulp from a JSON string
upstream_pulp_instance = UpstreamPulp.from_json(json)
# print the JSON string representation of the object
print(UpstreamPulp.to_json())

# convert the object into a dict
upstream_pulp_dict = upstream_pulp_instance.to_dict()
# create an instance of UpstreamPulp from a dict
upstream_pulp_from_dict = UpstreamPulp.from_dict(upstream_pulp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


