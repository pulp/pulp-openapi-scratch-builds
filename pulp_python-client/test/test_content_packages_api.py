# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pulpcore.client.pulp_python.api.content_packages_api import ContentPackagesApi


class TestContentPackagesApi(unittest.TestCase):
    """ContentPackagesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ContentPackagesApi()

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        Create a python package content
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        List python package contents
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Inspect a python package content
        """
        pass

    def test_set_label(self) -> None:
        """Test case for set_label

        Set a label
        """
        pass

    def test_unset_label(self) -> None:
        """Test case for unset_label

        Unset a label
        """
        pass


if __name__ == '__main__':
    unittest.main()
