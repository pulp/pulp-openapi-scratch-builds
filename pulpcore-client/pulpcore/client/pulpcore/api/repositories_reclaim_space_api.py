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


class RepositoriesReclaimSpaceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def reclaim(self, reclaim_space, pulp_domain="default", **kwargs):  # noqa: E501
        """reclaim  # noqa: E501

        Trigger an asynchronous space reclaim operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reclaim(pulp_domain, reclaim_space, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str pulp_domain: (required)
        :param ReclaimSpace reclaim_space: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AsyncOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.reclaim_with_http_info(reclaim_space, pulp_domain=pulp_domain, **kwargs)  # noqa: E501

    def reclaim_with_http_info(self, reclaim_space, pulp_domain="default", **kwargs):  # noqa: E501
        """reclaim  # noqa: E501

        Trigger an asynchronous space reclaim operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reclaim_with_http_info(pulp_domain, reclaim_space, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str pulp_domain: (required)
        :param ReclaimSpace reclaim_space: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AsyncOperationResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'pulp_domain',
            'reclaim_space'
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
                    " to method reclaim" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pulp_domain' is set
        if self.api_client.client_side_validation and ('pulp_domain' not in local_var_params or  # noqa: E501
                                                        local_var_params['pulp_domain'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pulp_domain` when calling `reclaim`")  # noqa: E501
        # verify the required parameter 'reclaim_space' is set
        if self.api_client.client_side_validation and ('reclaim_space' not in local_var_params or  # noqa: E501
                                                        local_var_params['reclaim_space'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reclaim_space` when calling `reclaim`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pulp_domain' in local_var_params:
            path_params['pulp_domain'] = local_var_params['pulp_domain']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reclaim_space' in local_var_params:
            body_params = local_var_params['reclaim_space']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pulp/{pulp_domain}/api/v3/repositories/reclaim_space/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncOperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
