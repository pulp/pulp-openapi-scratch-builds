# NpmPackageResponse

A Serializer for Package.  Add serializers for the new fields defined in Package and add those fields to the Meta class keeping fields from the parent class as well.  For example::  field1 = serializers.TextField() field2 = serializers.IntegerField() field3 = serializers.CharField()  class Meta:     fields = platform.SingleArtifactContentSerializer.Meta.fields + (         'field1', 'field2', 'field3'     )     model = models.Package
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**artifact** | **str** | Artifact file representing the physical content | [optional] 
**relative_path** | **str** |  | 
**name** | **str** |  | 
**version** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


