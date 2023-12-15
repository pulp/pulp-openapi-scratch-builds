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
from pulpcore.client.pulp_rpm.models.rpm_rpm_publication_response import RpmRpmPublicationResponse  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestRpmRpmPublicationResponse(unittest.TestCase):
    """RpmRpmPublicationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RpmRpmPublicationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.rpm_rpm_publication_response.RpmRpmPublicationResponse()  # noqa: E501
        if include_optional :
            return RpmRpmPublicationResponse(
                pulp_href = '0', 
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                repository_version = '0', 
                repository = '0', 
                metadata_checksum_type = null, 
                package_checksum_type = null, 
                gpgcheck = 0, 
                repo_gpgcheck = 0, 
                sqlite_metadata = True
            )
        else :
            return RpmRpmPublicationResponse(
        )

    def testRpmRpmPublicationResponse(self):
        """Test RpmRpmPublicationResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
