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
from pulpcore.client.pulp_rpm.models.artifact_response import ArtifactResponse  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestArtifactResponse(unittest.TestCase):
    """ArtifactResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ArtifactResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.artifact_response.ArtifactResponse()  # noqa: E501
        if include_optional :
            return ArtifactResponse(
                pulp_href = '0', 
                prn = '0', 
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                file = '0', 
                size = 56, 
                md5 = '0', 
                sha1 = '0', 
                sha224 = '0', 
                sha256 = '0', 
                sha384 = '0', 
                sha512 = '0'
            )
        else :
            return ArtifactResponse(
                file = '0',
        )

    def testArtifactResponse(self):
        """Test ArtifactResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
