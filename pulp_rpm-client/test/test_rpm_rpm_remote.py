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
from pulpcore.client.pulp_rpm.models.rpm_rpm_remote import RpmRpmRemote  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestRpmRpmRemote(unittest.TestCase):
    """RpmRpmRemote unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RpmRpmRemote
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.rpm_rpm_remote.RpmRpmRemote()  # noqa: E501
        if include_optional :
            return RpmRpmRemote(
                name = '0', 
                url = '0', 
                ca_cert = '0', 
                client_cert = '0', 
                client_key = '0', 
                tls_validation = True, 
                proxy_url = '0', 
                proxy_username = '0', 
                proxy_password = '0', 
                username = '0', 
                password = '0', 
                pulp_labels = {
                    'key' : '0'
                    }, 
                download_concurrency = 1, 
                max_retries = 56, 
                policy = null, 
                total_timeout = 0.0, 
                connect_timeout = 0.0, 
                sock_connect_timeout = 0.0, 
                sock_read_timeout = 0.0, 
                headers = [
                    None
                    ], 
                rate_limit = 56, 
                sles_auth_token = '0'
            )
        else :
            return RpmRpmRemote(
                name = '0',
                url = '0',
        )

    def testRpmRpmRemote(self):
        """Test RpmRpmRemote"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
