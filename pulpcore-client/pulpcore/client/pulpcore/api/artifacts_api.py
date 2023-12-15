# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pulpcore.client.pulpcore.api_client import ApiClient
from pulpcore.client.pulpcore.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ArtifactsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create(self, file,  **kwargs):  # noqa: E501
        """Create an artifact  # noqa: E501

        A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file file: The stored file. (required)
        :param int size: The size of the file in bytes.
        :param str md5: The MD5 checksum of the file if available.
        :param str sha1: The SHA-1 checksum of the file if available.
        :param str sha224: The SHA-224 checksum of the file if available.
        :param str sha256: The SHA-256 checksum of the file if available.
        :param str sha384: The SHA-384 checksum of the file if available.
        :param str sha512: The SHA-512 checksum of the file if available.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ArtifactResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_with_http_info(file,  **kwargs)  # noqa: E501

    def create_with_http_info(self, file,  **kwargs):  # noqa: E501
        """Create an artifact  # noqa: E501

        A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file file: The stored file. (required)
        :param int size: The size of the file in bytes.
        :param str md5: The MD5 checksum of the file if available.
        :param str sha1: The SHA-1 checksum of the file if available.
        :param str sha224: The SHA-224 checksum of the file if available.
        :param str sha256: The SHA-256 checksum of the file if available.
        :param str sha384: The SHA-384 checksum of the file if available.
        :param str sha512: The SHA-512 checksum of the file if available.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ArtifactResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'file',
            'size',
            'md5',
            'sha1',
            'sha224',
            'sha256',
            'sha384',
            'sha512'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in local_var_params or  # noqa: E501
                                                        local_var_params['file'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `file` when calling `create`")  # noqa: E501

        if self.api_client.client_side_validation and ('md5' in local_var_params and  # noqa: E501
                                                        len(local_var_params['md5']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `md5` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('sha1' in local_var_params and  # noqa: E501
                                                        len(local_var_params['sha1']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `sha1` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('sha224' in local_var_params and  # noqa: E501
                                                        len(local_var_params['sha224']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `sha224` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('sha256' in local_var_params and  # noqa: E501
                                                        len(local_var_params['sha256']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `sha256` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('sha384' in local_var_params and  # noqa: E501
                                                        len(local_var_params['sha384']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `sha384` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('sha512' in local_var_params and  # noqa: E501
                                                        len(local_var_params['sha512']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `sha512` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
        if 'size' in local_var_params:
            form_params.append(('size', local_var_params['size']))  # noqa: E501
        if 'md5' in local_var_params:
            form_params.append(('md5', local_var_params['md5']))  # noqa: E501
        if 'sha1' in local_var_params:
            form_params.append(('sha1', local_var_params['sha1']))  # noqa: E501
        if 'sha224' in local_var_params:
            form_params.append(('sha224', local_var_params['sha224']))  # noqa: E501
        if 'sha256' in local_var_params:
            form_params.append(('sha256', local_var_params['sha256']))  # noqa: E501
        if 'sha384' in local_var_params:
            form_params.append(('sha384', local_var_params['sha384']))  # noqa: E501
        if 'sha512' in local_var_params:
            form_params.append(('sha512', local_var_params['sha512']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pulp/api/v3/artifacts/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArtifactResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete(self, artifact_href,  **kwargs):  # noqa: E501
        """Delete an artifact  # noqa: E501

        Remove Artifact only if it is not associated with any Content.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete(artifact_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str artifact_href: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_with_http_info(artifact_href,  **kwargs)  # noqa: E501

    def delete_with_http_info(self, artifact_href,  **kwargs):  # noqa: E501
        """Delete an artifact  # noqa: E501

        Remove Artifact only if it is not associated with any Content.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_with_http_info(artifact_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str artifact_href: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'artifact_href'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'artifact_href' is set
        if self.api_client.client_side_validation and ('artifact_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['artifact_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `artifact_href` when calling `delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'artifact_href' in local_var_params:
            path_params['artifact_href'] = local_var_params['artifact_href']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{artifact_href}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self,  **kwargs):  # noqa: E501
        """List artifacts  # noqa: E501

        A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Number of results to return per page.
        :param str md5: Filter results where md5 matches value
        :param int offset: The initial index from which to return the results.
        :param list[str] ordering: Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `file` - File * `-file` - File (descending) * `size` - Size * `-size` - Size (descending) * `md5` - Md5 * `-md5` - Md5 (descending) * `sha1` - Sha1 * `-sha1` - Sha1 (descending) * `sha224` - Sha224 * `-sha224` - Sha224 (descending) * `sha256` - Sha256 * `-sha256` - Sha256 (descending) * `sha384` - Sha384 * `-sha384` - Sha384 (descending) * `sha512` - Sha512 * `-sha512` - Sha512 (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `pk` - Pk * `-pk` - Pk (descending)
        :param list[str] pulp_href__in: Multiple values may be separated by commas.
        :param list[str] pulp_id__in: Multiple values may be separated by commas.
        :param str q:
        :param str repository_version: Repository Version referenced by HREF
        :param str sha1: Filter results where sha1 matches value
        :param str sha224: Filter results where sha224 matches value
        :param str sha256: Filter results where sha256 matches value
        :param str sha384: Filter results where sha384 matches value
        :param str sha512: Filter results where sha512 matches value
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatedArtifactResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_with_http_info( **kwargs)  # noqa: E501

    def list_with_http_info(self,  **kwargs):  # noqa: E501
        """List artifacts  # noqa: E501

        A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Number of results to return per page.
        :param str md5: Filter results where md5 matches value
        :param int offset: The initial index from which to return the results.
        :param list[str] ordering: Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `file` - File * `-file` - File (descending) * `size` - Size * `-size` - Size (descending) * `md5` - Md5 * `-md5` - Md5 (descending) * `sha1` - Sha1 * `-sha1` - Sha1 (descending) * `sha224` - Sha224 * `-sha224` - Sha224 (descending) * `sha256` - Sha256 * `-sha256` - Sha256 (descending) * `sha384` - Sha384 * `-sha384` - Sha384 (descending) * `sha512` - Sha512 * `-sha512` - Sha512 (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `pk` - Pk * `-pk` - Pk (descending)
        :param list[str] pulp_href__in: Multiple values may be separated by commas.
        :param list[str] pulp_id__in: Multiple values may be separated by commas.
        :param str q:
        :param str repository_version: Repository Version referenced by HREF
        :param str sha1: Filter results where sha1 matches value
        :param str sha224: Filter results where sha224 matches value
        :param str sha256: Filter results where sha256 matches value
        :param str sha384: Filter results where sha384 matches value
        :param str sha512: Filter results where sha512 matches value
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaginatedArtifactResponseList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'md5',
            'offset',
            'ordering',
            'pulp_href__in',
            'pulp_id__in',
            'q',
            'repository_version',
            'sha1',
            'sha224',
            'sha256',
            'sha384',
            'sha512',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'md5' in local_var_params and local_var_params['md5'] is not None:  # noqa: E501
            query_params.append(('md5', local_var_params['md5']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'ordering' in local_var_params and local_var_params['ordering'] is not None:  # noqa: E501
            query_params.append(('ordering', local_var_params['ordering']))  # noqa: E501
            collection_formats['ordering'] = 'csv'  # noqa: E501
        if 'pulp_href__in' in local_var_params and local_var_params['pulp_href__in'] is not None:  # noqa: E501
            query_params.append(('pulp_href__in', local_var_params['pulp_href__in']))  # noqa: E501
            collection_formats['pulp_href__in'] = 'csv'  # noqa: E501
        if 'pulp_id__in' in local_var_params and local_var_params['pulp_id__in'] is not None:  # noqa: E501
            query_params.append(('pulp_id__in', local_var_params['pulp_id__in']))  # noqa: E501
            collection_formats['pulp_id__in'] = 'csv'  # noqa: E501
        if 'q' in local_var_params and local_var_params['q'] is not None:  # noqa: E501
            query_params.append(('q', local_var_params['q']))  # noqa: E501
        if 'repository_version' in local_var_params and local_var_params['repository_version'] is not None:  # noqa: E501
            query_params.append(('repository_version', local_var_params['repository_version']))  # noqa: E501
        if 'sha1' in local_var_params and local_var_params['sha1'] is not None:  # noqa: E501
            query_params.append(('sha1', local_var_params['sha1']))  # noqa: E501
        if 'sha224' in local_var_params and local_var_params['sha224'] is not None:  # noqa: E501
            query_params.append(('sha224', local_var_params['sha224']))  # noqa: E501
        if 'sha256' in local_var_params and local_var_params['sha256'] is not None:  # noqa: E501
            query_params.append(('sha256', local_var_params['sha256']))  # noqa: E501
        if 'sha384' in local_var_params and local_var_params['sha384'] is not None:  # noqa: E501
            query_params.append(('sha384', local_var_params['sha384']))  # noqa: E501
        if 'sha512' in local_var_params and local_var_params['sha512'] is not None:  # noqa: E501
            query_params.append(('sha512', local_var_params['sha512']))  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pulp/api/v3/artifacts/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedArtifactResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, artifact_href,  **kwargs):  # noqa: E501
        """Inspect an artifact  # noqa: E501

        A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(artifact_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str artifact_href: (required)
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ArtifactResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.read_with_http_info(artifact_href,  **kwargs)  # noqa: E501

    def read_with_http_info(self, artifact_href,  **kwargs):  # noqa: E501
        """Inspect an artifact  # noqa: E501

        A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(artifact_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str artifact_href: (required)
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ArtifactResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'artifact_href',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'artifact_href' is set
        if self.api_client.client_side_validation and ('artifact_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['artifact_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `artifact_href` when calling `read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'artifact_href' in local_var_params:
            path_params['artifact_href'] = local_var_params['artifact_href']  # noqa: E501

        query_params = []
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{artifact_href}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArtifactResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
