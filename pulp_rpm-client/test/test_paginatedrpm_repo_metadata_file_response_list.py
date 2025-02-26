# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.paginatedrpm_repo_metadata_file_response_list import PaginatedrpmRepoMetadataFileResponseList  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestPaginatedrpmRepoMetadataFileResponseList(unittest.TestCase):
    """PaginatedrpmRepoMetadataFileResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedrpmRepoMetadataFileResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.paginatedrpm_repo_metadata_file_response_list.PaginatedrpmRepoMetadataFileResponseList()  # noqa: E501
        if include_optional :
            return PaginatedrpmRepoMetadataFileResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulp_rpm.models.rpm/repo_metadata_file_response.rpm.RepoMetadataFileResponse(
                        pulp_href = '0', 
                        prn = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        md5 = '0', 
                        sha1 = '0', 
                        sha224 = '0', 
                        sha256 = '0', 
                        sha384 = '0', 
                        sha512 = '0', 
                        artifact = '0', 
                        relative_path = '0', 
                        data_type = '0', 
                        checksum_type = '0', 
                        checksum = '0', )
                    ]
            )
        else :
            return PaginatedrpmRepoMetadataFileResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulp_rpm.models.rpm/repo_metadata_file_response.rpm.RepoMetadataFileResponse(
                        pulp_href = '0', 
                        prn = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        md5 = '0', 
                        sha1 = '0', 
                        sha224 = '0', 
                        sha256 = '0', 
                        sha384 = '0', 
                        sha512 = '0', 
                        artifact = '0', 
                        relative_path = '0', 
                        data_type = '0', 
                        checksum_type = '0', 
                        checksum = '0', )
                    ],
        )

    def testPaginatedrpmRepoMetadataFileResponseList(self):
        """Test PaginatedrpmRepoMetadataFileResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
