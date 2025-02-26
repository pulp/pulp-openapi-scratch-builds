# ImageResponse

Image serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | File name. | 
**path** | **str** | File path. | 
**platforms** | **str** | Compatible platforms. | 
**artifact** | [**ArtifactResponse**](ArtifactResponse.md) |  | 

## Example

```python
from pulpcore.client.pulp_rpm.models.image_response import ImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageResponse from a JSON string
image_response_instance = ImageResponse.from_json(json)
# print the JSON string representation of the object
print(ImageResponse.to_json())

# convert the object into a dict
image_response_dict = image_response_instance.to_dict()
# create an instance of ImageResponse from a dict
image_response_from_dict = ImageResponse.from_dict(image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


