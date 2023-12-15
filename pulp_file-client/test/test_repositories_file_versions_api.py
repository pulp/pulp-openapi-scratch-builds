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

import pulpcore.client.pulp_file
from pulpcore.client.pulp_file.api.repositories_file_versions_api import RepositoriesFileVersionsApi  # noqa: E501
from pulpcore.client.pulp_file.rest import ApiException


class TestRepositoriesFileVersionsApi(unittest.TestCase):
    """RepositoriesFileVersionsApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_file.api.repositories_file_versions_api.RepositoriesFileVersionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete(self):
        """Test case for delete

        Delete a repository version  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List repository versions  # noqa: E501
        """
        pass

    def test_read(self):
        """Test case for read

        Inspect a repository version  # noqa: E501
        """
        pass

    def test_repair(self):
        """Test case for repair

        """
        pass


if __name__ == '__main__':
    unittest.main()
