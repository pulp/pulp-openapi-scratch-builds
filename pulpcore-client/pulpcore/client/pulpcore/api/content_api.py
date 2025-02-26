# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import List, Optional, Union
from typing_extensions import Annotated
from pulpcore.client.pulpcore.models.paginated_multiple_artifact_content_response_list import PaginatedMultipleArtifactContentResponseList

from pulpcore.client.pulpcore.api_client import ApiClient, RequestSerialized
from pulpcore.client.pulpcore.api_response import ApiResponse
from pulpcore.client.pulpcore.rest import RESTResponseType


class ContentApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def list(
        self,
        limit: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="The initial index from which to return the results.")] = None,
        ordering: Annotated[Optional[List[StrictStr]], Field(description="Ordering  * `pk` - Pk * `-pk` - Pk (descending)")] = None,
        orphaned_for: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME.")] = None,
        prn__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        pulp_href__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        pulp_id__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        pulp_type: Annotated[Optional[StrictStr], Field(description="Pulp type  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary")] = None,
        pulp_type__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary")] = None,
        q: Annotated[Optional[StrictStr], Field(description="Filter results by using NOT, AND and OR operations on other filters")] = None,
        repository_version: Annotated[Optional[StrictStr], Field(description="Repository Version referenced by HREF/PRN")] = None,
        repository_version_added: Annotated[Optional[StrictStr], Field(description="Repository Version referenced by HREF/PRN")] = None,
        repository_version_removed: Annotated[Optional[StrictStr], Field(description="Repository Version referenced by HREF/PRN")] = None,
        fields: Annotated[Optional[List[StrictStr]], Field(description="A list of fields to include in the response.")] = None,
        exclude_fields: Annotated[Optional[List[StrictStr]], Field(description="A list of fields to exclude from the response.")] = None,
        pulp_domain: StrictStr = "default",
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PaginatedMultipleArtifactContentResponseList:
        """List content

        Endpoint to list all content.

        :param pulp_domain: (required)
        :type pulp_domain: str
        :param limit: Number of results to return per page.
        :type limit: int
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param ordering: Ordering  * `pk` - Pk * `-pk` - Pk (descending)
        :type ordering: List[str]
        :param orphaned_for: Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME.
        :type orphaned_for: float
        :param prn__in: Multiple values may be separated by commas.
        :type prn__in: List[str]
        :param pulp_href__in: Multiple values may be separated by commas.
        :type pulp_href__in: List[str]
        :param pulp_id__in: Multiple values may be separated by commas.
        :type pulp_id__in: List[str]
        :param pulp_type: Pulp type  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary
        :type pulp_type: str
        :param pulp_type__in: Multiple values may be separated by commas.  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary
        :type pulp_type__in: List[str]
        :param q: Filter results by using NOT, AND and OR operations on other filters
        :type q: str
        :param repository_version: Repository Version referenced by HREF/PRN
        :type repository_version: str
        :param repository_version_added: Repository Version referenced by HREF/PRN
        :type repository_version_added: str
        :param repository_version_removed: Repository Version referenced by HREF/PRN
        :type repository_version_removed: str
        :param fields: A list of fields to include in the response.
        :type fields: List[str]
        :param exclude_fields: A list of fields to exclude from the response.
        :type exclude_fields: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_serialize(
            pulp_domain=pulp_domain,
            limit=limit,
            offset=offset,
            ordering=ordering,
            orphaned_for=orphaned_for,
            prn__in=prn__in,
            pulp_href__in=pulp_href__in,
            pulp_id__in=pulp_id__in,
            pulp_type=pulp_type,
            pulp_type__in=pulp_type__in,
            q=q,
            repository_version=repository_version,
            repository_version_added=repository_version_added,
            repository_version_removed=repository_version_removed,
            fields=fields,
            exclude_fields=exclude_fields,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedMultipleArtifactContentResponseList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_with_http_info(
        self,
        limit: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="The initial index from which to return the results.")] = None,
        ordering: Annotated[Optional[List[StrictStr]], Field(description="Ordering  * `pk` - Pk * `-pk` - Pk (descending)")] = None,
        orphaned_for: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME.")] = None,
        prn__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        pulp_href__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        pulp_id__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        pulp_type: Annotated[Optional[StrictStr], Field(description="Pulp type  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary")] = None,
        pulp_type__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary")] = None,
        q: Annotated[Optional[StrictStr], Field(description="Filter results by using NOT, AND and OR operations on other filters")] = None,
        repository_version: Annotated[Optional[StrictStr], Field(description="Repository Version referenced by HREF/PRN")] = None,
        repository_version_added: Annotated[Optional[StrictStr], Field(description="Repository Version referenced by HREF/PRN")] = None,
        repository_version_removed: Annotated[Optional[StrictStr], Field(description="Repository Version referenced by HREF/PRN")] = None,
        fields: Annotated[Optional[List[StrictStr]], Field(description="A list of fields to include in the response.")] = None,
        exclude_fields: Annotated[Optional[List[StrictStr]], Field(description="A list of fields to exclude from the response.")] = None,
        pulp_domain: StrictStr = "default",
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PaginatedMultipleArtifactContentResponseList]:
        """List content

        Endpoint to list all content.

        :param pulp_domain: (required)
        :type pulp_domain: str
        :param limit: Number of results to return per page.
        :type limit: int
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param ordering: Ordering  * `pk` - Pk * `-pk` - Pk (descending)
        :type ordering: List[str]
        :param orphaned_for: Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME.
        :type orphaned_for: float
        :param prn__in: Multiple values may be separated by commas.
        :type prn__in: List[str]
        :param pulp_href__in: Multiple values may be separated by commas.
        :type pulp_href__in: List[str]
        :param pulp_id__in: Multiple values may be separated by commas.
        :type pulp_id__in: List[str]
        :param pulp_type: Pulp type  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary
        :type pulp_type: str
        :param pulp_type__in: Multiple values may be separated by commas.  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary
        :type pulp_type__in: List[str]
        :param q: Filter results by using NOT, AND and OR operations on other filters
        :type q: str
        :param repository_version: Repository Version referenced by HREF/PRN
        :type repository_version: str
        :param repository_version_added: Repository Version referenced by HREF/PRN
        :type repository_version_added: str
        :param repository_version_removed: Repository Version referenced by HREF/PRN
        :type repository_version_removed: str
        :param fields: A list of fields to include in the response.
        :type fields: List[str]
        :param exclude_fields: A list of fields to exclude from the response.
        :type exclude_fields: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_serialize(
            pulp_domain=pulp_domain,
            limit=limit,
            offset=offset,
            ordering=ordering,
            orphaned_for=orphaned_for,
            prn__in=prn__in,
            pulp_href__in=pulp_href__in,
            pulp_id__in=pulp_id__in,
            pulp_type=pulp_type,
            pulp_type__in=pulp_type__in,
            q=q,
            repository_version=repository_version,
            repository_version_added=repository_version_added,
            repository_version_removed=repository_version_removed,
            fields=fields,
            exclude_fields=exclude_fields,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedMultipleArtifactContentResponseList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_without_preload_content(
        self,
        limit: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="The initial index from which to return the results.")] = None,
        ordering: Annotated[Optional[List[StrictStr]], Field(description="Ordering  * `pk` - Pk * `-pk` - Pk (descending)")] = None,
        orphaned_for: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME.")] = None,
        prn__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        pulp_href__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        pulp_id__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.")] = None,
        pulp_type: Annotated[Optional[StrictStr], Field(description="Pulp type  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary")] = None,
        pulp_type__in: Annotated[Optional[List[StrictStr]], Field(description="Multiple values may be separated by commas.  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary")] = None,
        q: Annotated[Optional[StrictStr], Field(description="Filter results by using NOT, AND and OR operations on other filters")] = None,
        repository_version: Annotated[Optional[StrictStr], Field(description="Repository Version referenced by HREF/PRN")] = None,
        repository_version_added: Annotated[Optional[StrictStr], Field(description="Repository Version referenced by HREF/PRN")] = None,
        repository_version_removed: Annotated[Optional[StrictStr], Field(description="Repository Version referenced by HREF/PRN")] = None,
        fields: Annotated[Optional[List[StrictStr]], Field(description="A list of fields to include in the response.")] = None,
        exclude_fields: Annotated[Optional[List[StrictStr]], Field(description="A list of fields to exclude from the response.")] = None,
        pulp_domain: StrictStr = "default",
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List content

        Endpoint to list all content.

        :param pulp_domain: (required)
        :type pulp_domain: str
        :param limit: Number of results to return per page.
        :type limit: int
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param ordering: Ordering  * `pk` - Pk * `-pk` - Pk (descending)
        :type ordering: List[str]
        :param orphaned_for: Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME.
        :type orphaned_for: float
        :param prn__in: Multiple values may be separated by commas.
        :type prn__in: List[str]
        :param pulp_href__in: Multiple values may be separated by commas.
        :type pulp_href__in: List[str]
        :param pulp_id__in: Multiple values may be separated by commas.
        :type pulp_id__in: List[str]
        :param pulp_type: Pulp type  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary
        :type pulp_type: str
        :param pulp_type__in: Multiple values may be separated by commas.  * `core.publishedmetadata` - core.publishedmetadata * `core.openpgp_publickey` - core.openpgp_publickey * `core.openpgp_publicsubkey` - core.openpgp_publicsubkey * `core.openpgp_userid` - core.openpgp_userid * `core.openpgp_userattribute` - core.openpgp_userattribute * `core.openpgp_signature` - core.openpgp_signature * `file.file` - file.file * `rpm.advisory` - rpm.advisory * `rpm.packagegroup` - rpm.packagegroup * `rpm.packagecategory` - rpm.packagecategory * `rpm.packageenvironment` - rpm.packageenvironment * `rpm.packagelangpacks` - rpm.packagelangpacks * `rpm.repo_metadata_file` - rpm.repo_metadata_file * `rpm.distribution_tree` - rpm.distribution_tree * `rpm.package` - rpm.package * `rpm.modulemd` - rpm.modulemd * `rpm.modulemd_defaults` - rpm.modulemd_defaults * `rpm.modulemd_obsolete` - rpm.modulemd_obsolete * `ostree.object` - ostree.object * `ostree.commit` - ostree.commit * `ostree.refs` - ostree.refs * `ostree.content` - ostree.content * `ostree.config` - ostree.config * `ostree.summary` - ostree.summary
        :type pulp_type__in: List[str]
        :param q: Filter results by using NOT, AND and OR operations on other filters
        :type q: str
        :param repository_version: Repository Version referenced by HREF/PRN
        :type repository_version: str
        :param repository_version_added: Repository Version referenced by HREF/PRN
        :type repository_version_added: str
        :param repository_version_removed: Repository Version referenced by HREF/PRN
        :type repository_version_removed: str
        :param fields: A list of fields to include in the response.
        :type fields: List[str]
        :param exclude_fields: A list of fields to exclude from the response.
        :type exclude_fields: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_serialize(
            pulp_domain=pulp_domain,
            limit=limit,
            offset=offset,
            ordering=ordering,
            orphaned_for=orphaned_for,
            prn__in=prn__in,
            pulp_href__in=pulp_href__in,
            pulp_id__in=pulp_id__in,
            pulp_type=pulp_type,
            pulp_type__in=pulp_type__in,
            q=q,
            repository_version=repository_version,
            repository_version_added=repository_version_added,
            repository_version_removed=repository_version_removed,
            fields=fields,
            exclude_fields=exclude_fields,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedMultipleArtifactContentResponseList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_serialize(
        self,
        pulp_domain,
        limit,
        offset,
        ordering,
        orphaned_for,
        prn__in,
        pulp_href__in,
        pulp_id__in,
        pulp_type,
        pulp_type__in,
        q,
        repository_version,
        repository_version_added,
        repository_version_removed,
        fields,
        exclude_fields,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'ordering': 'csv',
            'prn__in': 'csv',
            'pulp_href__in': 'csv',
            'pulp_id__in': 'csv',
            'pulp_type__in': 'csv',
            'fields': 'multi',
            'exclude_fields': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if pulp_domain is not None:
            _path_params['pulp_domain'] = pulp_domain
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if ordering is not None:
            
            _query_params.append(('ordering', ordering))
            
        if orphaned_for is not None:
            
            _query_params.append(('orphaned_for', orphaned_for))
            
        if prn__in is not None:
            
            _query_params.append(('prn__in', prn__in))
            
        if pulp_href__in is not None:
            
            _query_params.append(('pulp_href__in', pulp_href__in))
            
        if pulp_id__in is not None:
            
            _query_params.append(('pulp_id__in', pulp_id__in))
            
        if pulp_type is not None:
            
            _query_params.append(('pulp_type', pulp_type))
            
        if pulp_type__in is not None:
            
            _query_params.append(('pulp_type__in', pulp_type__in))
            
        if q is not None:
            
            _query_params.append(('q', q))
            
        if repository_version is not None:
            
            _query_params.append(('repository_version', repository_version))
            
        if repository_version_added is not None:
            
            _query_params.append(('repository_version_added', repository_version_added))
            
        if repository_version_removed is not None:
            
            _query_params.append(('repository_version_removed', repository_version_removed))
            
        if fields is not None:
            
            _query_params.append(('fields', fields))
            
        if exclude_fields is not None:
            
            _query_params.append(('exclude_fields', exclude_fields))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'basicAuth', 
            'cookieAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/pulp/{pulp_domain}/api/v3/content/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


