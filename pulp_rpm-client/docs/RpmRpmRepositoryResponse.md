# RpmRpmRepositoryResponse

Serializer for Rpm Repositories.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**versions_href** | **str** |  | [optional] [readonly] 
**pulp_labels** | **dict(str, str)** |  | [optional] 
**latest_version_href** | **str** |  | [optional] [readonly] 
**name** | **str** | A unique name for this repository. | 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 
**autopublish** | **bool** | Whether to automatically create publications for new repository versions, and update any distributions pointing to this repository. | [optional] [default to False]
**metadata_signing_service** | **str** | A reference to an associated signing service. | [optional] 
**retain_package_versions** | **int** | The number of versions of each package to keep in the repository; older versions will be purged. The default is &#39;0&#39;, which will disable this feature and keep all versions of each package. | [optional] 
**checksum_type** | [**PackageChecksumTypeEnum**](PackageChecksumTypeEnum.md) | The preferred checksum type during repo publish.  * &#x60;unknown&#x60; - unknown * &#x60;md5&#x60; - md5 * &#x60;sha1&#x60; - sha1 * &#x60;sha224&#x60; - sha224 * &#x60;sha256&#x60; - sha256 * &#x60;sha384&#x60; - sha384 * &#x60;sha512&#x60; - sha512 | [optional] 
**metadata_checksum_type** | [**PackageChecksumTypeEnum**](PackageChecksumTypeEnum.md) | DEPRECATED: use CHECKSUM_TYPE instead.  * &#x60;unknown&#x60; - unknown * &#x60;md5&#x60; - md5 * &#x60;sha1&#x60; - sha1 * &#x60;sha224&#x60; - sha224 * &#x60;sha256&#x60; - sha256 * &#x60;sha384&#x60; - sha384 * &#x60;sha512&#x60; - sha512 | [optional] 
**package_checksum_type** | [**PackageChecksumTypeEnum**](PackageChecksumTypeEnum.md) | DEPRECATED: use CHECKSUM_TYPE instead.  * &#x60;unknown&#x60; - unknown * &#x60;md5&#x60; - md5 * &#x60;sha1&#x60; - sha1 * &#x60;sha224&#x60; - sha224 * &#x60;sha256&#x60; - sha256 * &#x60;sha384&#x60; - sha384 * &#x60;sha512&#x60; - sha512 | [optional] 
**gpgcheck** | **int** | DEPRECATED: An option specifying whether a client should perform a GPG signature check on packages. | [optional] 
**repo_gpgcheck** | **int** | DEPRECATED: An option specifying whether a client should perform a GPG signature check on the repodata. | [optional] 
**sqlite_metadata** | **bool** | REMOVED: An option specifying whether Pulp should generate SQLite metadata. Not operation since pulp_rpm 3.25.0 release | [optional] [readonly] [default to False]
**repo_config** | [**object**](.md) | A JSON document describing config.repo file | [optional] 
**compression_type** | [**CompressionTypeEnum**](CompressionTypeEnum.md) | The compression type to use for metadata files.  * &#x60;zstd&#x60; - zstd * &#x60;gz&#x60; - gz | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


