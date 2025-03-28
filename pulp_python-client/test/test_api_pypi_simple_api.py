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

from pulpcore.client.pulp_python.api.api_pypi_simple_api import ApiPypiSimpleApi


class TestApiPypiSimpleApi(unittest.TestCase):
    """ApiPypiSimpleApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ApiPypiSimpleApi()

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        Upload a package
        """
        pass

    def test_pypi_simple_package_read(self) -> None:
        """Test case for pypi_simple_package_read

        Get package simple page
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Get index simple page
        """
        pass


if __name__ == '__main__':
    unittest.main()
