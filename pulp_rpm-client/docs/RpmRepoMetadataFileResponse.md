# RpmRepoMetadataFileResponse

RepoMetadataFile serializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**md5** | **str** | The MD5 checksum if available. | [optional] [readonly] 
**sha1** | **str** | The SHA-1 checksum if available. | [optional] [readonly] 
**sha224** | **str** | The SHA-224 checksum if available. | [optional] [readonly] 
**sha256** | **str** | The SHA-256 checksum if available. | [optional] [readonly] 
**sha384** | **str** | The SHA-384 checksum if available. | [optional] [readonly] 
**sha512** | **str** | The SHA-512 checksum if available. | [optional] [readonly] 
**artifact** | **str** | Artifact file representing the physical content | [optional] 
**relative_path** | **str** | Relative path of the file. | 
**data_type** | **str** | Metadata type. | 
**checksum_type** | **str** | Checksum type for the file. | 
**checksum** | **str** | Checksum for the file. | 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_repo_metadata_file_response import RpmRepoMetadataFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmRepoMetadataFileResponse from a JSON string
rpm_repo_metadata_file_response_instance = RpmRepoMetadataFileResponse.from_json(json)
# print the JSON string representation of the object
print(RpmRepoMetadataFileResponse.to_json())

# convert the object into a dict
rpm_repo_metadata_file_response_dict = rpm_repo_metadata_file_response_instance.to_dict()
# create an instance of RpmRepoMetadataFileResponse from a dict
rpm_repo_metadata_file_response_from_dict = RpmRepoMetadataFileResponse.from_dict(rpm_repo_metadata_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


