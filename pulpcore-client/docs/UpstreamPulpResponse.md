# UpstreamPulpResponse

Serializer for a Server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the most recent update of the remote. | [optional] [readonly] 
**name** | **str** | A unique name for this Pulp server. | 
**base_url** | **str** | The transport, hostname, and an optional port of the Pulp server. e.g. https://example.com | 
**api_root** | **str** | The API root. Defaults to &#39;/pulp/&#39;. | 
**domain** | **str** | The domain of the Pulp server if enabled. | [optional] 
**ca_cert** | **str** | A PEM encoded CA certificate used to validate the server certificate presented by the remote server. | [optional] 
**client_cert** | **str** | A PEM encoded client certificate used for authentication. | [optional] 
**tls_validation** | **bool** | If True, TLS peer validation must be performed. | [optional] 
**hidden_fields** | [**List[GenericRemoteResponseHiddenFieldsInner]**](GenericRemoteResponseHiddenFieldsInner.md) | List of hidden (write only) fields | [optional] [readonly] 
**q_select** | **str** | Filter distributions on the upstream Pulp using complex filtering. E.g. pulp_label_select&#x3D;\&quot;foo\&quot; OR pulp_label_select&#x3D;\&quot;key&#x3D;val\&quot; | [optional] 
**last_replication** | **datetime** | Timestamp of the last replication that occurred. Equals to &#39;null&#39; if no replication task has been executed. | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulpcore.models.upstream_pulp_response import UpstreamPulpResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpstreamPulpResponse from a JSON string
upstream_pulp_response_instance = UpstreamPulpResponse.from_json(json)
# print the JSON string representation of the object
print(UpstreamPulpResponse.to_json())

# convert the object into a dict
upstream_pulp_response_dict = upstream_pulp_response_instance.to_dict()
# create an instance of UpstreamPulpResponse from a dict
upstream_pulp_response_from_dict = UpstreamPulpResponse.from_dict(upstream_pulp_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


