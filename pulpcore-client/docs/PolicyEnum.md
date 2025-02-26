# PolicyEnum

* `immediate` - When syncing, download all metadata and content now. * `on_demand` - When syncing, download metadata, but do not download content now. Instead, download content as clients request it, and save it in Pulp to be served for future client requests. * `streamed` - When syncing, download metadata, but do not download content now. Instead,download content as clients request it, but never save it in Pulp. This causes future requests for that same content to have to be downloaded again.

## Enum

* `IMMEDIATE` (value: `'immediate'`)

* `ON_DEMAND` (value: `'on_demand'`)

* `STREAMED` (value: `'streamed'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


