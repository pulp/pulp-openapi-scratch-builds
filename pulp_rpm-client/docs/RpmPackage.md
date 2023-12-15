# RpmPackage

A Serializer for Package.  Add serializers for the new fields defined in Package and add those fields to the Meta class keeping fields from the parent class as well. Provide help_text.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | A URI of a repository the new content unit should be associated with. | [optional] 
**artifact** | **str** | Artifact file representing the physical content | [optional] 
**relative_path** | **str** | Path where the artifact is located relative to distributions base_path | [optional] 
**file** | **file** | An uploaded file that may be turned into the content unit. | [optional] 
**upload** | **str** | An uncommitted upload that may be turned into the content unit. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


