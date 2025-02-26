# pulpcore.client.pulp_rpm.ContentPackagesApi

All URIs are relative to *http://localhost:5001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ContentPackagesApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/content/rpm/packages/ | Create a package
[**list**](ContentPackagesApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/content/rpm/packages/ | List packages
[**read**](ContentPackagesApi.md#read) | **GET** {rpm_package_href} | Inspect a package


# **create**
> AsyncOperationResponse create(pulp_domain, repository=repository, artifact=artifact, relative_path=relative_path, file=file, upload=upload, file_url=file_url)

Create a package

Trigger an asynchronous task to create an RPM package,optionally create new repository version.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.ContentPackagesApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    repository = 'repository_example' # str | A URI of a repository the new content unit should be associated with. (optional)
    artifact = 'artifact_example' # str | Artifact file representing the physical content (optional)
    relative_path = 'relative_path_example' # str | Path where the artifact is located relative to distributions base_path (optional)
    file = None # bytearray | An uploaded file that may be turned into the content unit. (optional)
    upload = 'upload_example' # str | An uncommitted upload that may be turned into the content unit. (optional)
    file_url = 'file_url_example' # str | A url that Pulp can download and turn into the content unit. (optional)

    try:
        # Create a package
        api_response = api_instance.create(pulp_domain, repository=repository, artifact=artifact, relative_path=relative_path, file=file, upload=upload, file_url=file_url)
        print("The response of ContentPackagesApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentPackagesApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **repository** | **str**| A URI of a repository the new content unit should be associated with. | [optional] 
 **artifact** | **str**| Artifact file representing the physical content | [optional] 
 **relative_path** | **str**| Path where the artifact is located relative to distributions base_path | [optional] 
 **file** | **bytearray**| An uploaded file that may be turned into the content unit. | [optional] 
 **upload** | **str**| An uncommitted upload that may be turned into the content unit. | [optional] 
 **file_url** | **str**| A url that Pulp can download and turn into the content unit. | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedrpmPackageResponseList list(pulp_domain, arch=arch, arch__contains=arch__contains, arch__in=arch__in, arch__ne=arch__ne, arch__startswith=arch__startswith, checksum_type=checksum_type, checksum_type__in=checksum_type__in, checksum_type__ne=checksum_type__ne, epoch=epoch, epoch__in=epoch__in, epoch__ne=epoch__ne, filename=filename, limit=limit, name=name, name__contains=name__contains, name__in=name__in, name__ne=name__ne, name__startswith=name__startswith, offset=offset, ordering=ordering, orphaned_for=orphaned_for, pkg_id=pkg_id, pkg_id__in=pkg_id__in, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, release=release, release__contains=release__contains, release__in=release__in, release__ne=release__ne, release__startswith=release__startswith, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, version=version, version__in=version__in, version__ne=version__ne, fields=fields, exclude_fields=exclude_fields)

List packages

A ViewSet for Package.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/packages/  Also specify queryset and serializer for Package.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.paginatedrpm_package_response_list import PaginatedrpmPackageResponseList
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.ContentPackagesApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    arch = 'arch_example' # str | Filter results where arch matches value (optional)
    arch__contains = 'arch__contains_example' # str | Filter results where arch contains value (optional)
    arch__in = ['arch__in_example'] # List[str] | Filter results where arch is in a comma-separated list of values (optional)
    arch__ne = 'arch__ne_example' # str | Filter results where arch not equal to value (optional)
    arch__startswith = 'arch__startswith_example' # str | Filter results where arch starts with value (optional)
    checksum_type = 'checksum_type_example' # str | Filter results where checksum_type matches value  * `unknown` - unknown * `md5` - md5 * `sha1` - sha1 * `sha1` - sha1 * `sha224` - sha224 * `sha256` - sha256 * `sha384` - sha384 * `sha512` - sha512 (optional)
    checksum_type__in = ['checksum_type__in_example'] # List[str] | Filter results where checksum_type is in a comma-separated list of values (optional)
    checksum_type__ne = 'checksum_type__ne_example' # str | Filter results where checksum_type not equal to value (optional)
    epoch = 'epoch_example' # str | Filter results where epoch matches value (optional)
    epoch__in = ['epoch__in_example'] # List[str] | Filter results where epoch is in a comma-separated list of values (optional)
    epoch__ne = 'epoch__ne_example' # str | Filter results where epoch not equal to value (optional)
    filename = 'filename_example' # str |  (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str | Filter results where name matches value (optional)
    name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
    name__in = ['name__in_example'] # List[str] | Filter results where name is in a comma-separated list of values (optional)
    name__ne = 'name__ne_example' # str | Filter results where name not equal to value (optional)
    name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    ordering = ['ordering_example'] # List[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `name` - Name * `-name` - Name (descending) * `epoch` - Epoch * `-epoch` - Epoch (descending) * `version` - Version * `-version` - Version (descending) * `release` - Release * `-release` - Release (descending) * `arch` - Arch * `-arch` - Arch (descending) * `evr` - Evr * `-evr` - Evr (descending) * `pkgId` - Pkgid * `-pkgId` - Pkgid (descending) * `checksum_type` - Checksum type * `-checksum_type` - Checksum type (descending) * `summary` - Summary * `-summary` - Summary (descending) * `description` - Description * `-description` - Description (descending) * `url` - Url * `-url` - Url (descending) * `changelogs` - Changelogs * `-changelogs` - Changelogs (descending) * `files` - Files * `-files` - Files (descending) * `requires` - Requires * `-requires` - Requires (descending) * `provides` - Provides * `-provides` - Provides (descending) * `conflicts` - Conflicts * `-conflicts` - Conflicts (descending) * `obsoletes` - Obsoletes * `-obsoletes` - Obsoletes (descending) * `suggests` - Suggests * `-suggests` - Suggests (descending) * `enhances` - Enhances * `-enhances` - Enhances (descending) * `recommends` - Recommends * `-recommends` - Recommends (descending) * `supplements` - Supplements * `-supplements` - Supplements (descending) * `location_base` - Location base * `-location_base` - Location base (descending) * `location_href` - Location href * `-location_href` - Location href (descending) * `rpm_buildhost` - Rpm buildhost * `-rpm_buildhost` - Rpm buildhost (descending) * `rpm_group` - Rpm group * `-rpm_group` - Rpm group (descending) * `rpm_license` - Rpm license * `-rpm_license` - Rpm license (descending) * `rpm_packager` - Rpm packager * `-rpm_packager` - Rpm packager (descending) * `rpm_sourcerpm` - Rpm sourcerpm * `-rpm_sourcerpm` - Rpm sourcerpm (descending) * `rpm_vendor` - Rpm vendor * `-rpm_vendor` - Rpm vendor (descending) * `rpm_header_start` - Rpm header start * `-rpm_header_start` - Rpm header start (descending) * `rpm_header_end` - Rpm header end * `-rpm_header_end` - Rpm header end (descending) * `size_archive` - Size archive * `-size_archive` - Size archive (descending) * `size_installed` - Size installed * `-size_installed` - Size installed (descending) * `size_package` - Size package * `-size_package` - Size package (descending) * `time_build` - Time build * `-time_build` - Time build (descending) * `time_file` - Time file * `-time_file` - Time file (descending) * `is_modular` - Is modular * `-is_modular` - Is modular (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
    orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
    pkg_id = 'pkg_id_example' # str | Filter results where pkgId matches value (optional)
    pkg_id__in = ['pkg_id__in_example'] # List[str] | Filter results where pkgId is in a comma-separated list of values (optional)
    prn__in = ['prn__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_href__in = ['pulp_href__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_id__in = ['pulp_id__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    release = 'release_example' # str | Filter results where release matches value (optional)
    release__contains = 'release__contains_example' # str | Filter results where release contains value (optional)
    release__in = ['release__in_example'] # List[str] | Filter results where release is in a comma-separated list of values (optional)
    release__ne = 'release__ne_example' # str | Filter results where release not equal to value (optional)
    release__startswith = 'release__startswith_example' # str | Filter results where release starts with value (optional)
    repository_version = 'repository_version_example' # str | Repository Version referenced by HREF/PRN (optional)
    repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF/PRN (optional)
    repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF/PRN (optional)
    sha256 = 'sha256_example' # str |  (optional)
    version = 'version_example' # str | Filter results where version matches value (optional)
    version__in = ['version__in_example'] # List[str] | Filter results where version is in a comma-separated list of values (optional)
    version__ne = 'version__ne_example' # str | Filter results where version not equal to value (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List packages
        api_response = api_instance.list(pulp_domain, arch=arch, arch__contains=arch__contains, arch__in=arch__in, arch__ne=arch__ne, arch__startswith=arch__startswith, checksum_type=checksum_type, checksum_type__in=checksum_type__in, checksum_type__ne=checksum_type__ne, epoch=epoch, epoch__in=epoch__in, epoch__ne=epoch__ne, filename=filename, limit=limit, name=name, name__contains=name__contains, name__in=name__in, name__ne=name__ne, name__startswith=name__startswith, offset=offset, ordering=ordering, orphaned_for=orphaned_for, pkg_id=pkg_id, pkg_id__in=pkg_id__in, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, q=q, release=release, release__contains=release__contains, release__in=release__in, release__ne=release__ne, release__startswith=release__startswith, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, version=version, version__in=version__in, version__ne=version__ne, fields=fields, exclude_fields=exclude_fields)
        print("The response of ContentPackagesApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentPackagesApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **arch** | **str**| Filter results where arch matches value | [optional] 
 **arch__contains** | **str**| Filter results where arch contains value | [optional] 
 **arch__in** | [**List[str]**](str.md)| Filter results where arch is in a comma-separated list of values | [optional] 
 **arch__ne** | **str**| Filter results where arch not equal to value | [optional] 
 **arch__startswith** | **str**| Filter results where arch starts with value | [optional] 
 **checksum_type** | **str**| Filter results where checksum_type matches value  * &#x60;unknown&#x60; - unknown * &#x60;md5&#x60; - md5 * &#x60;sha1&#x60; - sha1 * &#x60;sha1&#x60; - sha1 * &#x60;sha224&#x60; - sha224 * &#x60;sha256&#x60; - sha256 * &#x60;sha384&#x60; - sha384 * &#x60;sha512&#x60; - sha512 | [optional] 
 **checksum_type__in** | [**List[str]**](str.md)| Filter results where checksum_type is in a comma-separated list of values | [optional] 
 **checksum_type__ne** | **str**| Filter results where checksum_type not equal to value | [optional] 
 **epoch** | **str**| Filter results where epoch matches value | [optional] 
 **epoch__in** | [**List[str]**](str.md)| Filter results where epoch is in a comma-separated list of values | [optional] 
 **epoch__ne** | **str**| Filter results where epoch not equal to value | [optional] 
 **filename** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**| Filter results where name matches value | [optional] 
 **name__contains** | **str**| Filter results where name contains value | [optional] 
 **name__in** | [**List[str]**](str.md)| Filter results where name is in a comma-separated list of values | [optional] 
 **name__ne** | **str**| Filter results where name not equal to value | [optional] 
 **name__startswith** | **str**| Filter results where name starts with value | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;upstream_id&#x60; - Upstream id * &#x60;-upstream_id&#x60; - Upstream id (descending) * &#x60;timestamp_of_interest&#x60; - Timestamp of interest * &#x60;-timestamp_of_interest&#x60; - Timestamp of interest (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;epoch&#x60; - Epoch * &#x60;-epoch&#x60; - Epoch (descending) * &#x60;version&#x60; - Version * &#x60;-version&#x60; - Version (descending) * &#x60;release&#x60; - Release * &#x60;-release&#x60; - Release (descending) * &#x60;arch&#x60; - Arch * &#x60;-arch&#x60; - Arch (descending) * &#x60;evr&#x60; - Evr * &#x60;-evr&#x60; - Evr (descending) * &#x60;pkgId&#x60; - Pkgid * &#x60;-pkgId&#x60; - Pkgid (descending) * &#x60;checksum_type&#x60; - Checksum type * &#x60;-checksum_type&#x60; - Checksum type (descending) * &#x60;summary&#x60; - Summary * &#x60;-summary&#x60; - Summary (descending) * &#x60;description&#x60; - Description * &#x60;-description&#x60; - Description (descending) * &#x60;url&#x60; - Url * &#x60;-url&#x60; - Url (descending) * &#x60;changelogs&#x60; - Changelogs * &#x60;-changelogs&#x60; - Changelogs (descending) * &#x60;files&#x60; - Files * &#x60;-files&#x60; - Files (descending) * &#x60;requires&#x60; - Requires * &#x60;-requires&#x60; - Requires (descending) * &#x60;provides&#x60; - Provides * &#x60;-provides&#x60; - Provides (descending) * &#x60;conflicts&#x60; - Conflicts * &#x60;-conflicts&#x60; - Conflicts (descending) * &#x60;obsoletes&#x60; - Obsoletes * &#x60;-obsoletes&#x60; - Obsoletes (descending) * &#x60;suggests&#x60; - Suggests * &#x60;-suggests&#x60; - Suggests (descending) * &#x60;enhances&#x60; - Enhances * &#x60;-enhances&#x60; - Enhances (descending) * &#x60;recommends&#x60; - Recommends * &#x60;-recommends&#x60; - Recommends (descending) * &#x60;supplements&#x60; - Supplements * &#x60;-supplements&#x60; - Supplements (descending) * &#x60;location_base&#x60; - Location base * &#x60;-location_base&#x60; - Location base (descending) * &#x60;location_href&#x60; - Location href * &#x60;-location_href&#x60; - Location href (descending) * &#x60;rpm_buildhost&#x60; - Rpm buildhost * &#x60;-rpm_buildhost&#x60; - Rpm buildhost (descending) * &#x60;rpm_group&#x60; - Rpm group * &#x60;-rpm_group&#x60; - Rpm group (descending) * &#x60;rpm_license&#x60; - Rpm license * &#x60;-rpm_license&#x60; - Rpm license (descending) * &#x60;rpm_packager&#x60; - Rpm packager * &#x60;-rpm_packager&#x60; - Rpm packager (descending) * &#x60;rpm_sourcerpm&#x60; - Rpm sourcerpm * &#x60;-rpm_sourcerpm&#x60; - Rpm sourcerpm (descending) * &#x60;rpm_vendor&#x60; - Rpm vendor * &#x60;-rpm_vendor&#x60; - Rpm vendor (descending) * &#x60;rpm_header_start&#x60; - Rpm header start * &#x60;-rpm_header_start&#x60; - Rpm header start (descending) * &#x60;rpm_header_end&#x60; - Rpm header end * &#x60;-rpm_header_end&#x60; - Rpm header end (descending) * &#x60;size_archive&#x60; - Size archive * &#x60;-size_archive&#x60; - Size archive (descending) * &#x60;size_installed&#x60; - Size installed * &#x60;-size_installed&#x60; - Size installed (descending) * &#x60;size_package&#x60; - Size package * &#x60;-size_package&#x60; - Size package (descending) * &#x60;time_build&#x60; - Time build * &#x60;-time_build&#x60; - Time build (descending) * &#x60;time_file&#x60; - Time file * &#x60;-time_file&#x60; - Time file (descending) * &#x60;is_modular&#x60; - Is modular * &#x60;-is_modular&#x60; - Is modular (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **orphaned_for** | **float**| Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. | [optional] 
 **pkg_id** | **str**| Filter results where pkgId matches value | [optional] 
 **pkg_id__in** | [**List[str]**](str.md)| Filter results where pkgId is in a comma-separated list of values | [optional] 
 **prn__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_href__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **release** | **str**| Filter results where release matches value | [optional] 
 **release__contains** | **str**| Filter results where release contains value | [optional] 
 **release__in** | [**List[str]**](str.md)| Filter results where release is in a comma-separated list of values | [optional] 
 **release__ne** | **str**| Filter results where release not equal to value | [optional] 
 **release__startswith** | **str**| Filter results where release starts with value | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **sha256** | **str**|  | [optional] 
 **version** | **str**| Filter results where version matches value | [optional] 
 **version__in** | [**List[str]**](str.md)| Filter results where version is in a comma-separated list of values | [optional] 
 **version__ne** | **str**| Filter results where version not equal to value | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedrpmPackageResponseList**](PaginatedrpmPackageResponseList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> RpmPackageResponse read(rpm_package_href, fields=fields, exclude_fields=exclude_fields)

Inspect a package

A ViewSet for Package.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/packages/  Also specify queryset and serializer for Package.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.rpm_package_response import RpmPackageResponse
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5001
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:5001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.ContentPackagesApi(api_client)
    rpm_package_href = 'rpm_package_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a package
        api_response = api_instance.read(rpm_package_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of ContentPackagesApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentPackagesApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_package_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**RpmPackageResponse**](RpmPackageResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

