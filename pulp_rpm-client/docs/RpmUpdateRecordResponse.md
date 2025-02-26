# RpmUpdateRecordResponse

A Serializer for UpdateRecord.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**id** | **str** | Update id (short update name, e.g. RHEA-2013:1777) | [optional] [readonly] 
**updated_date** | **str** | Date when the update was updated (e.g. &#39;2013-12-02 00:00:00&#39;) | [optional] [readonly] 
**description** | **str** | Update description | [optional] [readonly] 
**issued_date** | **str** | Date when the update was issued (e.g. &#39;2013-12-02 00:00:00&#39;) | [optional] [readonly] 
**fromstr** | **str** | Source of the update (e.g. security@redhat.com) | [optional] [readonly] 
**status** | **str** | Update status (&#39;final&#39;, ...) | [optional] [readonly] 
**title** | **str** | Update name | [optional] [readonly] 
**summary** | **str** | Short summary | [optional] [readonly] 
**version** | **str** | Update version (probably always an integer number) | [optional] [readonly] 
**type** | **str** | Update type (&#39;enhancement&#39;, &#39;bugfix&#39;, ...) | [optional] [readonly] 
**severity** | **str** | Severity | [optional] [readonly] 
**solution** | **str** | Solution | [optional] [readonly] 
**release** | **str** | Update release | [optional] [readonly] 
**rights** | **str** | Copyrights | [optional] [readonly] 
**pushcount** | **str** | Push count | [optional] [readonly] 
**pkglist** | [**List[RpmUpdateCollectionResponse]**](RpmUpdateCollectionResponse.md) | List of packages | [optional] [readonly] 
**references** | **List[object]** | List of references | [optional] [readonly] 
**reboot_suggested** | **bool** | Reboot suggested | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_update_record_response import RpmUpdateRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmUpdateRecordResponse from a JSON string
rpm_update_record_response_instance = RpmUpdateRecordResponse.from_json(json)
# print the JSON string representation of the object
print(RpmUpdateRecordResponse.to_json())

# convert the object into a dict
rpm_update_record_response_dict = rpm_update_record_response_instance.to_dict()
# create an instance of RpmUpdateRecordResponse from a dict
rpm_update_record_response_from_dict = RpmUpdateRecordResponse.from_dict(rpm_update_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


