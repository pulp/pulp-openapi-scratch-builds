# VariantResponse

Variant serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant_id** | **str** | Variant id. | 
**uid** | **str** | Variant uid. | 
**name** | **str** | Variant name. | 
**type** | **str** | Variant type. | 
**packages** | **str** | Relative path to directory with binary RPMs. | 
**source_packages** | **str** | Relative path to directory with source RPMs. | 
**source_repository** | **str** | Relative path to YUM repository with source RPMs. | 
**debug_packages** | **str** | Relative path to directory with debug RPMs. | 
**debug_repository** | **str** | Relative path to YUM repository with debug RPMs. | 
**identity** | **str** | Relative path to a pem file that identifies a product. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.variant_response import VariantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VariantResponse from a JSON string
variant_response_instance = VariantResponse.from_json(json)
# print the JSON string representation of the object
print(VariantResponse.to_json())

# convert the object into a dict
variant_response_dict = variant_response_instance.to_dict()
# create an instance of VariantResponse from a dict
variant_response_from_dict = VariantResponse.from_dict(variant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


