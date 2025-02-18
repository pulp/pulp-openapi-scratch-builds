# NpmPackage

A Serializer for Package.  Add serializers for the new fields defined in Package and add those fields to the Meta class keeping fields from the parent class as well.  For example::  field1 = serializers.TextField() field2 = serializers.IntegerField() field3 = serializers.CharField()  class Meta:     fields = platform.SingleArtifactContentSerializer.Meta.fields + (         'field1', 'field2', 'field3'     )     model = models.Package
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | A URI of a repository the new content unit should be associated with. | [optional] 
**artifact** | **str** | Artifact file representing the physical content | [optional] 
**relative_path** | **str** |  | 
**file** | **file** | An uploaded file that may be turned into the content unit. | [optional] 
**upload** | **str** | An uncommitted upload that may be turned into the content unit. | [optional] 
**file_url** | **str** | A url that Pulp can download and turn into the content unit. | [optional] 
**name** | **str** |  | 
**version** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


