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
from pulpcore.client.pulp_rpm.models.rpm_rpm_repository import RpmRpmRepository  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestRpmRpmRepository(unittest.TestCase):
    """RpmRpmRepository unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RpmRpmRepository
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.rpm_rpm_repository.RpmRpmRepository()  # noqa: E501
        if include_optional :
            return RpmRpmRepository(
                pulp_labels = {
                    'key' : '0'
                    }, 
                name = '0', 
                description = '0', 
                retain_repo_versions = 1, 
                remote = '0', 
                autopublish = True, 
                metadata_signing_service = '0', 
                retain_package_versions = 0, 
                metadata_checksum_type = null, 
                package_checksum_type = null, 
                gpgcheck = 0, 
                repo_gpgcheck = 0, 
                sqlite_metadata = True, 
                repo_config = None
            )
        else :
            return RpmRpmRepository(
                name = '0',
        )

    def testRpmRpmRepository(self):
        """Test RpmRpmRepository"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
