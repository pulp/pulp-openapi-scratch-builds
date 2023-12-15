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

import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.paginated_repository_version_response_list import PaginatedRepositoryVersionResponseList  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestPaginatedRepositoryVersionResponseList(unittest.TestCase):
    """PaginatedRepositoryVersionResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedRepositoryVersionResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.paginated_repository_version_response_list.PaginatedRepositoryVersionResponseList()  # noqa: E501
        if include_optional :
            return PaginatedRepositoryVersionResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulpcore.models.repository_version_response.RepositoryVersionResponse(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        number = 56, 
                        repository = '0', 
                        base_version = '0', 
                        content_summary = null, )
                    ]
            )
        else :
            return PaginatedRepositoryVersionResponseList(
        )

    def testPaginatedRepositoryVersionResponseList(self):
        """Test PaginatedRepositoryVersionResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
