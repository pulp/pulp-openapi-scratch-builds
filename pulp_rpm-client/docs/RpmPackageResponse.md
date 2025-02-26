# RpmPackageResponse

A Serializer for Package.  Add serializers for the new fields defined in Package and add those fields to the Meta class keeping fields from the parent class as well. Provide help_text.

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
**name** | **str** | Name of the package | [optional] [readonly] 
**epoch** | **str** | The package&#39;s epoch | [optional] [readonly] 
**version** | **str** | The version of the package. For example, &#39;2.8.0&#39; | [optional] [readonly] 
**release** | **str** | The release of a particular version of the package. e.g. &#39;1.el7&#39; or &#39;3.f24&#39; | [optional] [readonly] 
**arch** | **str** | The target architecture for a package.For example, &#39;x86_64&#39;, &#39;i686&#39;, or &#39;noarch&#39; | [optional] [readonly] 
**pkg_id** | **str** | Checksum of the package file | [optional] [readonly] 
**checksum_type** | **str** | Type of checksum, e.g. &#39;sha256&#39;, &#39;md5&#39; | [optional] [readonly] 
**summary** | **str** | Short description of the packaged software | [optional] [readonly] 
**description** | **str** | In-depth description of the packaged software | [optional] [readonly] 
**url** | **str** | URL with more information about the packaged software | [optional] [readonly] 
**changelogs** | **object** | Changelogs that package contains | [optional] [readonly] 
**files** | **object** | Files that package contains | [optional] [readonly] 
**requires** | **object** | Capabilities the package requires | [optional] [readonly] 
**provides** | **object** | Capabilities the package provides | [optional] [readonly] 
**conflicts** | **object** | Capabilities the package conflicts | [optional] [readonly] 
**obsoletes** | **object** | Capabilities the package obsoletes | [optional] [readonly] 
**suggests** | **object** | Capabilities the package suggests | [optional] [readonly] 
**enhances** | **object** | Capabilities the package enhances | [optional] [readonly] 
**recommends** | **object** | Capabilities the package recommends | [optional] [readonly] 
**supplements** | **object** | Capabilities the package supplements | [optional] [readonly] 
**location_base** | **str** | Base location of this package | [optional] [readonly] 
**location_href** | **str** | Relative location of package to the repodata | [optional] [readonly] 
**rpm_buildhost** | **str** | Hostname of the system that built the package | [optional] [readonly] 
**rpm_group** | **str** | RPM group (See: http://fedoraproject.org/wiki/RPMGroups) | [optional] [readonly] 
**rpm_license** | **str** | License term applicable to the package software (GPLv2, etc.) | [optional] [readonly] 
**rpm_packager** | **str** | Person or persons responsible for creating the package | [optional] [readonly] 
**rpm_sourcerpm** | **str** | Name of the source package (srpm) the package was built from | [optional] [readonly] 
**rpm_vendor** | **str** | Name of the organization that produced the package | [optional] [readonly] 
**rpm_header_start** | **int** | First byte of the header | [optional] [readonly] 
**rpm_header_end** | **int** | Last byte of the header | [optional] [readonly] 
**is_modular** | **bool** | Flag to identify if the package is modular | [optional] [readonly] 
**size_archive** | **int** | Size, in bytes, of the archive portion of the original package file | [optional] [readonly] 
**size_installed** | **int** | Total size, in bytes, of every file installed by this package | [optional] [readonly] 
**size_package** | **int** | Size, in bytes, of the package | [optional] [readonly] 
**time_build** | **int** | Time the package was built in seconds since the epoch | [optional] [readonly] 
**time_file** | **int** | The &#39;file&#39; time attribute in the primary XML - file mtime in seconds since the epoch. | [optional] [readonly] 

## Example

```python
from pulpcore.client.pulp_rpm.models.rpm_package_response import RpmPackageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpmPackageResponse from a JSON string
rpm_package_response_instance = RpmPackageResponse.from_json(json)
# print the JSON string representation of the object
print(RpmPackageResponse.to_json())

# convert the object into a dict
rpm_package_response_dict = rpm_package_response_instance.to_dict()
# create an instance of RpmPackageResponse from a dict
rpm_package_response_from_dict = RpmPackageResponse.from_dict(rpm_package_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


