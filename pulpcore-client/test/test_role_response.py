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
from pulpcore.client.pulpcore.models.role_response import RoleResponse  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestRoleResponse(unittest.TestCase):
    """RoleResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RoleResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.role_response.RoleResponse()  # noqa: E501
        if include_optional :
            return RoleResponse(
                pulp_href = '0', 
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name = '0', 
                description = '0', 
                permissions = [
                    '0'
                    ], 
                locked = True
            )
        else :
            return RoleResponse(
                name = '0',
                permissions = [
                    '0'
                    ],
        )

    def testRoleResponse(self):
        """Test RoleResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
