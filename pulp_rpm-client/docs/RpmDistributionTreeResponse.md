# RpmDistributionTreeResponse

DistributionTree serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**header_version** | **str** | Header Version. | 
**release_name** | **str** | Release name. | 
**release_short** | **str** | Release short name. | 
**release_version** | **str** | Release version. | 
**release_is_layered** | **bool** | Typically False for an operating system, True otherwise. | 
**base_product_name** | **str** | Base Product name. | 
**base_product_short** | **str** | Base Product short name. | 
**base_product_version** | **str** | Base Product version. | 
**arch** | **str** | Tree architecturerch. | 
**build_timestamp** | **float** | Tree build time timestamp. | 
**instimage** | **str** | Relative path to Anaconda instimage. | 
**mainimage** | **str** | Relative path to Anaconda stage2 image. | 
**discnum** | **int** | Disc number. | 
**totaldiscs** | **int** | Number of discs in media set. | 
**addons** | [**List[AddonResponse]**](AddonResponse.md) |  | 
**checksums** | [**List[ChecksumResponse]**](ChecksumResponse.md) |  | 
**images** | [**List[ImageResponse]**](ImageResponse.md) |  | 
**variants** | [**List[VariantResponse]**](VariantResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_distribution_tree_response import RpmDistributionTreeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmDistributionTreeResponse from a JSON string
rpm_distribution_tree_response_instance = RpmDistributionTreeResponse.from_json(json)
# print the JSON string representation of the object
print(RpmDistributionTreeResponse.to_json())

# convert the object into a dict
rpm_distribution_tree_response_dict = rpm_distribution_tree_response_instance.to_dict()
# create an instance of RpmDistributionTreeResponse from a dict
rpm_distribution_tree_response_from_dict = RpmDistributionTreeResponse.from_dict(rpm_distribution_tree_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


