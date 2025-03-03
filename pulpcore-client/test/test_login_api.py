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

import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.api.login_api import LoginApi  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException


class TestLoginApi(unittest.TestCase):
    """LoginApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulpcore.api.login_api.LoginApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login(self):
        """Test case for login

        """
        pass

    def test_login_read(self):
        """Test case for login_read

        """
        pass

    def test_logout(self):
        """Test case for logout

        """
        pass


if __name__ == '__main__':
    unittest.main()
