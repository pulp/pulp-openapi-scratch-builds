# RpmRpmPublicationResponse

A Serializer for RpmPublication.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**repository_version** | **str** |  | [optional] 
**repository** | **str** | A URI of the repository to be published. | [optional] 
**checksum_type** | [**PackageChecksumTypeEnum**](PackageChecksumTypeEnum.md) | The preferred checksum type used during repo publishes.  * &#x60;unknown&#x60; - unknown * &#x60;md5&#x60; - md5 * &#x60;sha1&#x60; - sha1 * &#x60;sha224&#x60; - sha224 * &#x60;sha256&#x60; - sha256 * &#x60;sha384&#x60; - sha384 * &#x60;sha512&#x60; - sha512 | [optional] 
**metadata_checksum_type** | [**PackageChecksumTypeEnum**](PackageChecksumTypeEnum.md) | DEPRECATED: The checksum type for metadata.  * &#x60;unknown&#x60; - unknown * &#x60;md5&#x60; - md5 * &#x60;sha1&#x60; - sha1 * &#x60;sha224&#x60; - sha224 * &#x60;sha256&#x60; - sha256 * &#x60;sha384&#x60; - sha384 * &#x60;sha512&#x60; - sha512 | [optional] 
**package_checksum_type** | [**PackageChecksumTypeEnum**](PackageChecksumTypeEnum.md) | DEPRECATED: The checksum type for packages.  * &#x60;unknown&#x60; - unknown * &#x60;md5&#x60; - md5 * &#x60;sha1&#x60; - sha1 * &#x60;sha224&#x60; - sha224 * &#x60;sha256&#x60; - sha256 * &#x60;sha384&#x60; - sha384 * &#x60;sha512&#x60; - sha512 | [optional] 
**gpgcheck** | **int** | DEPRECATED: An option specifying whether a client should perform a GPG signature check on packages. | [optional] 
**repo_gpgcheck** | **int** | DEPRECATED: An option specifying whether a client should perform a GPG signature check on the repodata. | [optional] 
**sqlite_metadata** | **bool** | REMOVED: An option specifying whether Pulp should generate SQLite metadata. Not operation since pulp_rpm 3.25.0 release | [optional] [readonly] [default to False]
**repo_config** | [**object**](.md) | A JSON document describing config.repo file | [optional] 
**compression_type** | [**CompressionTypeEnum**](CompressionTypeEnum.md) | The compression type to use for metadata files.  * &#x60;zstd&#x60; - zstd * &#x60;gz&#x60; - gz | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


