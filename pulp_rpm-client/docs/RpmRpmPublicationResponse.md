# RpmRpmPublicationResponse

A Serializer for RpmPublication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**prn** | **str** | The Pulp Resource Name (PRN). | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**pulp_last_updated** | **datetime** | Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same. | [optional] [readonly] 
**repository_version** | **str** |  | [optional] 
**repository** | **str** | A URI of the repository to be published. | [optional] 
**checksum_type** | [**PackageChecksumTypeEnum**](PackageChecksumTypeEnum.md) | The preferred checksum type used during repo publishes.  * &#x60;unknown&#x60; - unknown * &#x60;md5&#x60; - md5 * &#x60;sha1&#x60; - sha1 * &#x60;sha224&#x60; - sha224 * &#x60;sha256&#x60; - sha256 * &#x60;sha384&#x60; - sha384 * &#x60;sha512&#x60; - sha512 | [optional] 
**metadata_checksum_type** | [**PackageChecksumTypeEnum**](PackageChecksumTypeEnum.md) | DEPRECATED: The checksum type for metadata.  * &#x60;unknown&#x60; - unknown * &#x60;md5&#x60; - md5 * &#x60;sha1&#x60; - sha1 * &#x60;sha224&#x60; - sha224 * &#x60;sha256&#x60; - sha256 * &#x60;sha384&#x60; - sha384 * &#x60;sha512&#x60; - sha512 | [optional] 
**package_checksum_type** | [**PackageChecksumTypeEnum**](PackageChecksumTypeEnum.md) | DEPRECATED: The checksum type for packages.  * &#x60;unknown&#x60; - unknown * &#x60;md5&#x60; - md5 * &#x60;sha1&#x60; - sha1 * &#x60;sha224&#x60; - sha224 * &#x60;sha256&#x60; - sha256 * &#x60;sha384&#x60; - sha384 * &#x60;sha512&#x60; - sha512 | [optional] 
**gpgcheck** | **int** | DEPRECATED: An option specifying whether a client should perform a GPG signature check on packages. | [optional] 
**repo_gpgcheck** | **int** | DEPRECATED: An option specifying whether a client should perform a GPG signature check on the repodata. | [optional] 
**sqlite_metadata** | **bool** | REMOVED: An option specifying whether Pulp should generate SQLite metadata. Not operation since pulp_rpm 3.25.0 release | [optional] [readonly] [default to False]
**repo_config** | **object** | A JSON document describing config.repo file | [optional] 
**compression_type** | [**CompressionTypeEnum**](CompressionTypeEnum.md) | The compression type to use for metadata files.  * &#x60;zstd&#x60; - zstd * &#x60;gz&#x60; - gz | [optional] 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_rpm_publication_response import RpmRpmPublicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmRpmPublicationResponse from a JSON string
rpm_rpm_publication_response_instance = RpmRpmPublicationResponse.from_json(json)
# print the JSON string representation of the object
print(RpmRpmPublicationResponse.to_json())

# convert the object into a dict
rpm_rpm_publication_response_dict = rpm_rpm_publication_response_instance.to_dict()
# create an instance of RpmRpmPublicationResponse from a dict
rpm_rpm_publication_response_from_dict = RpmRpmPublicationResponse.from_dict(rpm_rpm_publication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


