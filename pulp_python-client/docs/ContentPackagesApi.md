# pulpcore.client.pulp_python.ContentPackagesApi

All URIs are relative to *https://console.redhat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ContentPackagesApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/content/python/packages/ | Create a python package content
[**list**](ContentPackagesApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/content/python/packages/ | List python package contents
[**read**](ContentPackagesApi.md#read) | **GET** {python_python_package_content_href} | Inspect a python package content
[**set_label**](ContentPackagesApi.md#set_label) | **POST** {python_python_package_content_href}set_label/ | Set a label
[**unset_label**](ContentPackagesApi.md#unset_label) | **POST** {python_python_package_content_href}unset_label/ | Unset a label


# **create**
> AsyncOperationResponse create(pulp_domain, relative_path, repository=repository, pulp_labels=pulp_labels, artifact=artifact, file=file, upload=upload, file_url=file_url, sha256=sha256, summary=summary, description=description, description_content_type=description_content_type, keywords=keywords, home_page=home_page, download_url=download_url, author=author, author_email=author_email, maintainer=maintainer, maintainer_email=maintainer_email, license=license, requires_python=requires_python, project_url=project_url, project_urls=project_urls, platform=platform, supported_platform=supported_platform, requires_dist=requires_dist, provides_dist=provides_dist, obsoletes_dist=obsoletes_dist, requires_external=requires_external, classifiers=classifiers)

Create a python package content

Trigger an asynchronous task to create content,optionally create new repository version.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.async_operation_response import AsyncOperationResponse
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.ContentPackagesApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    relative_path = 'relative_path_example' # str | Path where the artifact is located relative to distributions base_path
    repository = 'repository_example' # str | A URI of a repository the new content unit should be associated with. (optional)
    pulp_labels = None # Dict[str, Optional[str]] | A dictionary of arbitrary key/value pairs used to describe a specific Content instance. (optional)
    artifact = 'artifact_example' # str | Artifact file representing the physical content (optional)
    file = None # bytearray | An uploaded file that may be turned into the content unit. (optional)
    upload = 'upload_example' # str | An uncommitted upload that may be turned into the content unit. (optional)
    file_url = 'file_url_example' # str | A url that Pulp can download and turn into the content unit. (optional)
    sha256 = '' # str | The SHA256 digest of this package. (optional) (default to '')
    summary = 'summary_example' # str | A one-line summary of what the package does. (optional)
    description = 'description_example' # str | A longer description of the package that can run to several paragraphs. (optional)
    description_content_type = 'description_content_type_example' # str | A string stating the markup syntax (if any) used in the distribution’s description, so that tools can intelligently render the description. (optional)
    keywords = 'keywords_example' # str | Additional keywords to be used to assist searching for the package in a larger catalog. (optional)
    home_page = 'home_page_example' # str | The URL for the package's home page. (optional)
    download_url = 'download_url_example' # str | Legacy field denoting the URL from which this package can be downloaded. (optional)
    author = 'author_example' # str | Text containing the author's name. Contact information can also be added, separated with newlines. (optional)
    author_email = 'author_email_example' # str | The author's e-mail address.  (optional)
    maintainer = 'maintainer_example' # str | The maintainer's name at a minimum; additional contact information may be provided. (optional)
    maintainer_email = 'maintainer_email_example' # str | The maintainer's e-mail address. (optional)
    license = 'license_example' # str | Text indicating the license covering the distribution (optional)
    requires_python = 'requires_python_example' # str | The Python version(s) that the distribution is guaranteed to be compatible with. (optional)
    project_url = 'project_url_example' # str | A browsable URL for the project and a label for it, separated by a comma. (optional)
    project_urls = None # object | A dictionary of labels and URLs for the project. (optional)
    platform = 'platform_example' # str | A comma-separated list of platform specifications, summarizing the operating systems supported by the package. (optional)
    supported_platform = 'supported_platform_example' # str | Field to specify the OS and CPU for which the binary package was compiled.  (optional)
    requires_dist = None # object | A JSON list containing names of some other distutils project required by this distribution. (optional)
    provides_dist = None # object | A JSON list containing names of a Distutils project which is contained within this distribution. (optional)
    obsoletes_dist = None # object | A JSON list containing names of a distutils project's distribution which this distribution renders obsolete, meaning that the two projects should not be installed at the same time. (optional)
    requires_external = None # object | A JSON list containing some dependency in the system that the distribution is to be used. (optional)
    classifiers = None # object | A JSON list containing classification values for a Python package. (optional)

    try:
        # Create a python package content
        api_response = api_instance.create(pulp_domain, relative_path, repository=repository, pulp_labels=pulp_labels, artifact=artifact, file=file, upload=upload, file_url=file_url, sha256=sha256, summary=summary, description=description, description_content_type=description_content_type, keywords=keywords, home_page=home_page, download_url=download_url, author=author, author_email=author_email, maintainer=maintainer, maintainer_email=maintainer_email, license=license, requires_python=requires_python, project_url=project_url, project_urls=project_urls, platform=platform, supported_platform=supported_platform, requires_dist=requires_dist, provides_dist=provides_dist, obsoletes_dist=obsoletes_dist, requires_external=requires_external, classifiers=classifiers)
        print("The response of ContentPackagesApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentPackagesApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **relative_path** | **str**| Path where the artifact is located relative to distributions base_path | 
 **repository** | **str**| A URI of a repository the new content unit should be associated with. | [optional] 
 **pulp_labels** | [**Dict[str, Optional[str]]**](Dict.md)| A dictionary of arbitrary key/value pairs used to describe a specific Content instance. | [optional] 
 **artifact** | **str**| Artifact file representing the physical content | [optional] 
 **file** | **bytearray**| An uploaded file that may be turned into the content unit. | [optional] 
 **upload** | **str**| An uncommitted upload that may be turned into the content unit. | [optional] 
 **file_url** | **str**| A url that Pulp can download and turn into the content unit. | [optional] 
 **sha256** | **str**| The SHA256 digest of this package. | [optional] [default to &#39;&#39;]
 **summary** | **str**| A one-line summary of what the package does. | [optional] 
 **description** | **str**| A longer description of the package that can run to several paragraphs. | [optional] 
 **description_content_type** | **str**| A string stating the markup syntax (if any) used in the distribution’s description, so that tools can intelligently render the description. | [optional] 
 **keywords** | **str**| Additional keywords to be used to assist searching for the package in a larger catalog. | [optional] 
 **home_page** | **str**| The URL for the package&#39;s home page. | [optional] 
 **download_url** | **str**| Legacy field denoting the URL from which this package can be downloaded. | [optional] 
 **author** | **str**| Text containing the author&#39;s name. Contact information can also be added, separated with newlines. | [optional] 
 **author_email** | **str**| The author&#39;s e-mail address.  | [optional] 
 **maintainer** | **str**| The maintainer&#39;s name at a minimum; additional contact information may be provided. | [optional] 
 **maintainer_email** | **str**| The maintainer&#39;s e-mail address. | [optional] 
 **license** | **str**| Text indicating the license covering the distribution | [optional] 
 **requires_python** | **str**| The Python version(s) that the distribution is guaranteed to be compatible with. | [optional] 
 **project_url** | **str**| A browsable URL for the project and a label for it, separated by a comma. | [optional] 
 **project_urls** | [**object**](object.md)| A dictionary of labels and URLs for the project. | [optional] 
 **platform** | **str**| A comma-separated list of platform specifications, summarizing the operating systems supported by the package. | [optional] 
 **supported_platform** | **str**| Field to specify the OS and CPU for which the binary package was compiled.  | [optional] 
 **requires_dist** | [**object**](object.md)| A JSON list containing names of some other distutils project required by this distribution. | [optional] 
 **provides_dist** | [**object**](object.md)| A JSON list containing names of a Distutils project which is contained within this distribution. | [optional] 
 **obsoletes_dist** | [**object**](object.md)| A JSON list containing names of a distutils project&#39;s distribution which this distribution renders obsolete, meaning that the two projects should not be installed at the same time. | [optional] 
 **requires_external** | [**object**](object.md)| A JSON list containing some dependency in the system that the distribution is to be used. | [optional] 
 **classifiers** | [**object**](object.md)| A JSON list containing classification values for a Python package. | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedpythonPythonPackageContentResponseList list(pulp_domain, author=author, author__in=author__in, filename=filename, filename__contains=filename__contains, filename__in=filename__in, keywords__contains=keywords__contains, keywords__in=keywords__in, limit=limit, name=name, name__in=name__in, offset=offset, ordering=ordering, orphaned_for=orphaned_for, packagetype=packagetype, packagetype__in=packagetype__in, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, requires_python=requires_python, requires_python__contains=requires_python__contains, requires_python__in=requires_python__in, sha256=sha256, sha256__in=sha256__in, version=version, version__gt=version__gt, version__gte=version__gte, version__lt=version__lt, version__lte=version__lte, fields=fields, exclude_fields=exclude_fields)

List python package contents

 PythonPackageContent represents each individually installable Python package. In the Python ecosystem, this is called a Python Distribution, sometimes (ambiguously) refered to as a package. In Pulp Python, we refer to it as PythonPackageContent. Each PythonPackageContent corresponds to a single filename, for example `pulpcore-3.0.0rc1-py3-none-any.whl` or `pulpcore-3.0.0rc1.tar.gz`.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.paginatedpython_python_package_content_response_list import PaginatedpythonPythonPackageContentResponseList
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.ContentPackagesApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
    author = 'author_example' # str | Filter results where author matches value (optional)
    author__in = ['author__in_example'] # List[str] | Filter results where author is in a comma-separated list of values (optional)
    filename = 'filename_example' # str | Filter results where filename matches value (optional)
    filename__contains = 'filename__contains_example' # str | Filter results where filename contains value (optional)
    filename__in = ['filename__in_example'] # List[str] | Filter results where filename is in a comma-separated list of values (optional)
    keywords__contains = 'keywords__contains_example' # str | Filter results where keywords contains value (optional)
    keywords__in = ['keywords__in_example'] # List[str] | Filter results where keywords is in a comma-separated list of values (optional)
    limit = 56 # int | Number of results to return per page. (optional)
    name = 'name_example' # str | Filter results where name matches value (optional)
    name__in = ['name__in_example'] # List[str] | Filter results where name is in a comma-separated list of values (optional)
    offset = 56 # int | The initial index from which to return the results. (optional)
    ordering = ['ordering_example'] # List[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `filename` - Filename * `-filename` - Filename (descending) * `packagetype` - Packagetype * `-packagetype` - Packagetype (descending) * `name` - Name * `-name` - Name (descending) * `version` - Version * `-version` - Version (descending) * `sha256` - Sha256 * `-sha256` - Sha256 (descending) * `python_version` - Python version * `-python_version` - Python version (descending) * `metadata_version` - Metadata version * `-metadata_version` - Metadata version (descending) * `summary` - Summary * `-summary` - Summary (descending) * `description` - Description * `-description` - Description (descending) * `keywords` - Keywords * `-keywords` - Keywords (descending) * `home_page` - Home page * `-home_page` - Home page (descending) * `download_url` - Download url * `-download_url` - Download url (descending) * `author` - Author * `-author` - Author (descending) * `author_email` - Author email * `-author_email` - Author email (descending) * `maintainer` - Maintainer * `-maintainer` - Maintainer (descending) * `maintainer_email` - Maintainer email * `-maintainer_email` - Maintainer email (descending) * `license` - License * `-license` - License (descending) * `requires_python` - Requires python * `-requires_python` - Requires python (descending) * `project_url` - Project url * `-project_url` - Project url (descending) * `platform` - Platform * `-platform` - Platform (descending) * `supported_platform` - Supported platform * `-supported_platform` - Supported platform (descending) * `requires_dist` - Requires dist * `-requires_dist` - Requires dist (descending) * `provides_dist` - Provides dist * `-provides_dist` - Provides dist (descending) * `obsoletes_dist` - Obsoletes dist * `-obsoletes_dist` - Obsoletes dist (descending) * `requires_external` - Requires external * `-requires_external` - Requires external (descending) * `classifiers` - Classifiers * `-classifiers` - Classifiers (descending) * `project_urls` - Project urls * `-project_urls` - Project urls (descending) * `description_content_type` - Description content type * `-description_content_type` - Description content type (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
    orphaned_for = 3.4 # float | Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. (optional)
    packagetype = 'packagetype_example' # str | Filter results where packagetype matches value  * `bdist_dmg` - bdist_dmg * `bdist_dumb` - bdist_dumb * `bdist_egg` - bdist_egg * `bdist_msi` - bdist_msi * `bdist_rpm` - bdist_rpm * `bdist_wheel` - bdist_wheel * `bdist_wininst` - bdist_wininst * `sdist` - sdist (optional)
    packagetype__in = ['packagetype__in_example'] # List[str] | Filter results where packagetype is in a comma-separated list of values (optional)
    prn__in = ['prn__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_href__in = ['pulp_href__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_id__in = ['pulp_id__in_example'] # List[str] | Multiple values may be separated by commas. (optional)
    pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
    q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
    repository_version = 'repository_version_example' # str | Repository Version referenced by HREF/PRN (optional)
    repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF/PRN (optional)
    repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF/PRN (optional)
    requires_python = 'requires_python_example' # str | Filter results where requires_python matches value (optional)
    requires_python__contains = 'requires_python__contains_example' # str | Filter results where requires_python contains value (optional)
    requires_python__in = ['requires_python__in_example'] # List[str] | Filter results where requires_python is in a comma-separated list of values (optional)
    sha256 = 'sha256_example' # str | Filter results where sha256 matches value (optional)
    sha256__in = ['sha256__in_example'] # List[str] | Filter results where sha256 is in a comma-separated list of values (optional)
    version = 'version_example' # str | Filter results where version matches value (optional)
    version__gt = 'version__gt_example' # str | Filter results where version is greater than value (optional)
    version__gte = 'version__gte_example' # str | Filter results where version is greater than or equal to value (optional)
    version__lt = 'version__lt_example' # str | Filter results where version is less than value (optional)
    version__lte = 'version__lte_example' # str | Filter results where version is less than or equal to value (optional)
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # List python package contents
        api_response = api_instance.list(pulp_domain, author=author, author__in=author__in, filename=filename, filename__contains=filename__contains, filename__in=filename__in, keywords__contains=keywords__contains, keywords__in=keywords__in, limit=limit, name=name, name__in=name__in, offset=offset, ordering=ordering, orphaned_for=orphaned_for, packagetype=packagetype, packagetype__in=packagetype__in, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, requires_python=requires_python, requires_python__contains=requires_python__contains, requires_python__in=requires_python__in, sha256=sha256, sha256__in=sha256__in, version=version, version__gt=version__gt, version__gte=version__gte, version__lt=version__lt, version__lte=version__lte, fields=fields, exclude_fields=exclude_fields)
        print("The response of ContentPackagesApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentPackagesApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **author** | **str**| Filter results where author matches value | [optional] 
 **author__in** | [**List[str]**](str.md)| Filter results where author is in a comma-separated list of values | [optional] 
 **filename** | **str**| Filter results where filename matches value | [optional] 
 **filename__contains** | **str**| Filter results where filename contains value | [optional] 
 **filename__in** | [**List[str]**](str.md)| Filter results where filename is in a comma-separated list of values | [optional] 
 **keywords__contains** | **str**| Filter results where keywords contains value | [optional] 
 **keywords__in** | [**List[str]**](str.md)| Filter results where keywords is in a comma-separated list of values | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**| Filter results where name matches value | [optional] 
 **name__in** | [**List[str]**](str.md)| Filter results where name is in a comma-separated list of values | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**List[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;upstream_id&#x60; - Upstream id * &#x60;-upstream_id&#x60; - Upstream id (descending) * &#x60;pulp_labels&#x60; - Pulp labels * &#x60;-pulp_labels&#x60; - Pulp labels (descending) * &#x60;timestamp_of_interest&#x60; - Timestamp of interest * &#x60;-timestamp_of_interest&#x60; - Timestamp of interest (descending) * &#x60;filename&#x60; - Filename * &#x60;-filename&#x60; - Filename (descending) * &#x60;packagetype&#x60; - Packagetype * &#x60;-packagetype&#x60; - Packagetype (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;version&#x60; - Version * &#x60;-version&#x60; - Version (descending) * &#x60;sha256&#x60; - Sha256 * &#x60;-sha256&#x60; - Sha256 (descending) * &#x60;python_version&#x60; - Python version * &#x60;-python_version&#x60; - Python version (descending) * &#x60;metadata_version&#x60; - Metadata version * &#x60;-metadata_version&#x60; - Metadata version (descending) * &#x60;summary&#x60; - Summary * &#x60;-summary&#x60; - Summary (descending) * &#x60;description&#x60; - Description * &#x60;-description&#x60; - Description (descending) * &#x60;keywords&#x60; - Keywords * &#x60;-keywords&#x60; - Keywords (descending) * &#x60;home_page&#x60; - Home page * &#x60;-home_page&#x60; - Home page (descending) * &#x60;download_url&#x60; - Download url * &#x60;-download_url&#x60; - Download url (descending) * &#x60;author&#x60; - Author * &#x60;-author&#x60; - Author (descending) * &#x60;author_email&#x60; - Author email * &#x60;-author_email&#x60; - Author email (descending) * &#x60;maintainer&#x60; - Maintainer * &#x60;-maintainer&#x60; - Maintainer (descending) * &#x60;maintainer_email&#x60; - Maintainer email * &#x60;-maintainer_email&#x60; - Maintainer email (descending) * &#x60;license&#x60; - License * &#x60;-license&#x60; - License (descending) * &#x60;requires_python&#x60; - Requires python * &#x60;-requires_python&#x60; - Requires python (descending) * &#x60;project_url&#x60; - Project url * &#x60;-project_url&#x60; - Project url (descending) * &#x60;platform&#x60; - Platform * &#x60;-platform&#x60; - Platform (descending) * &#x60;supported_platform&#x60; - Supported platform * &#x60;-supported_platform&#x60; - Supported platform (descending) * &#x60;requires_dist&#x60; - Requires dist * &#x60;-requires_dist&#x60; - Requires dist (descending) * &#x60;provides_dist&#x60; - Provides dist * &#x60;-provides_dist&#x60; - Provides dist (descending) * &#x60;obsoletes_dist&#x60; - Obsoletes dist * &#x60;-obsoletes_dist&#x60; - Obsoletes dist (descending) * &#x60;requires_external&#x60; - Requires external * &#x60;-requires_external&#x60; - Requires external (descending) * &#x60;classifiers&#x60; - Classifiers * &#x60;-classifiers&#x60; - Classifiers (descending) * &#x60;project_urls&#x60; - Project urls * &#x60;-project_urls&#x60; - Project urls (descending) * &#x60;description_content_type&#x60; - Description content type * &#x60;-description_content_type&#x60; - Description content type (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **orphaned_for** | **float**| Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME. | [optional] 
 **packagetype** | **str**| Filter results where packagetype matches value  * &#x60;bdist_dmg&#x60; - bdist_dmg * &#x60;bdist_dumb&#x60; - bdist_dumb * &#x60;bdist_egg&#x60; - bdist_egg * &#x60;bdist_msi&#x60; - bdist_msi * &#x60;bdist_rpm&#x60; - bdist_rpm * &#x60;bdist_wheel&#x60; - bdist_wheel * &#x60;bdist_wininst&#x60; - bdist_wininst * &#x60;sdist&#x60; - sdist | [optional] 
 **packagetype__in** | [**List[str]**](str.md)| Filter results where packagetype is in a comma-separated list of values | [optional] 
 **prn__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_href__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**List[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_label_select** | **str**| Filter labels by search string | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF/PRN | [optional] 
 **requires_python** | **str**| Filter results where requires_python matches value | [optional] 
 **requires_python__contains** | **str**| Filter results where requires_python contains value | [optional] 
 **requires_python__in** | [**List[str]**](str.md)| Filter results where requires_python is in a comma-separated list of values | [optional] 
 **sha256** | **str**| Filter results where sha256 matches value | [optional] 
 **sha256__in** | [**List[str]**](str.md)| Filter results where sha256 is in a comma-separated list of values | [optional] 
 **version** | **str**| Filter results where version matches value | [optional] 
 **version__gt** | **str**| Filter results where version is greater than value | [optional] 
 **version__gte** | **str**| Filter results where version is greater than or equal to value | [optional] 
 **version__lt** | **str**| Filter results where version is less than value | [optional] 
 **version__lte** | **str**| Filter results where version is less than or equal to value | [optional] 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedpythonPythonPackageContentResponseList**](PaginatedpythonPythonPackageContentResponseList.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> PythonPythonPackageContentResponse read(python_python_package_content_href, fields=fields, exclude_fields=exclude_fields)

Inspect a python package content

 PythonPackageContent represents each individually installable Python package. In the Python ecosystem, this is called a Python Distribution, sometimes (ambiguously) refered to as a package. In Pulp Python, we refer to it as PythonPackageContent. Each PythonPackageContent corresponds to a single filename, for example `pulpcore-3.0.0rc1-py3-none-any.whl` or `pulpcore-3.0.0rc1.tar.gz`.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.python_python_package_content_response import PythonPythonPackageContentResponse
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.ContentPackagesApi(api_client)
    python_python_package_content_href = 'python_python_package_content_href_example' # str | 
    fields = ['fields_example'] # List[str] | A list of fields to include in the response. (optional)
    exclude_fields = ['exclude_fields_example'] # List[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a python package content
        api_response = api_instance.read(python_python_package_content_href, fields=fields, exclude_fields=exclude_fields)
        print("The response of ContentPackagesApi->read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentPackagesApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_package_content_href** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**List[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PythonPythonPackageContentResponse**](PythonPythonPackageContentResponse.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_label**
> SetLabelResponse set_label(python_python_package_content_href, set_label)

Set a label

Set a single pulp_label on the object to a specific value or null.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.set_label import SetLabel
from pulpcore.client.pulp_python.models.set_label_response import SetLabelResponse
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.ContentPackagesApi(api_client)
    python_python_package_content_href = 'python_python_package_content_href_example' # str | 
    set_label = pulpcore.client.pulp_python.SetLabel() # SetLabel | 

    try:
        # Set a label
        api_response = api_instance.set_label(python_python_package_content_href, set_label)
        print("The response of ContentPackagesApi->set_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentPackagesApi->set_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_package_content_href** | **str**|  | 
 **set_label** | [**SetLabel**](SetLabel.md)|  | 

### Return type

[**SetLabelResponse**](SetLabelResponse.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_label**
> UnsetLabelResponse unset_label(python_python_package_content_href, unset_label)

Unset a label

Unset a single pulp_label on the object.

### Example

* OAuth Authentication (json_header_remote_authentication):
* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import pulpcore.client.pulp_python
from pulpcore.client.pulp_python.models.unset_label import UnsetLabel
from pulpcore.client.pulp_python.models.unset_label_response import UnsetLabelResponse
from pulpcore.client.pulp_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://console.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_python.Configuration(
    host = "https://console.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_python.ContentPackagesApi(api_client)
    python_python_package_content_href = 'python_python_package_content_href_example' # str | 
    unset_label = pulpcore.client.pulp_python.UnsetLabel() # UnsetLabel | 

    try:
        # Unset a label
        api_response = api_instance.unset_label(python_python_package_content_href, unset_label)
        print("The response of ContentPackagesApi->unset_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentPackagesApi->unset_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **python_python_package_content_href** | **str**|  | 
 **unset_label** | [**UnsetLabel**](UnsetLabel.md)|  | 

### Return type

[**UnsetLabelResponse**](UnsetLabelResponse.md)

### Authorization

[json_header_remote_authentication](../README.md#json_header_remote_authentication), [basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

