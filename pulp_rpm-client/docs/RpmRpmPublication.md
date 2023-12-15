# RpmRpmPublication

A Serializer for RpmPublication.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_version** | **str** |  | [optional] 
**repository** | **str** | A URI of the repository to be published. | [optional] 
**metadata_checksum_type** | [**MetadataChecksumTypeEnum**](MetadataChecksumTypeEnum.md) | The checksum type for metadata.  * &#x60;unknown&#x60; - unknown * &#x60;md5&#x60; - md5 * &#x60;sha1&#x60; - sha1 * &#x60;sha224&#x60; - sha224 * &#x60;sha256&#x60; - sha256 * &#x60;sha384&#x60; - sha384 * &#x60;sha512&#x60; - sha512 | [optional] 
**package_checksum_type** | [**PackageChecksumTypeEnum**](PackageChecksumTypeEnum.md) | The checksum type for packages.  * &#x60;unknown&#x60; - unknown * &#x60;md5&#x60; - md5 * &#x60;sha1&#x60; - sha1 * &#x60;sha224&#x60; - sha224 * &#x60;sha256&#x60; - sha256 * &#x60;sha384&#x60; - sha384 * &#x60;sha512&#x60; - sha512 | [optional] 
**gpgcheck** | **int** | DEPRECATED: An option specifying whether a client should perform a GPG signature check on packages. | [optional] 
**repo_gpgcheck** | **int** | DEPRECATED: An option specifying whether a client should perform a GPG signature check on the repodata. | [optional] 
**sqlite_metadata** | **bool** | DEPRECATED: An option specifying whether Pulp should generate SQLite metadata. | [optional] [default to False]
**repo_config** | [**object**](.md) | A JSON document describing config.repo file | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


