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

from pulpcore.client.pulp_maven.api.distributions_maven_api import DistributionsMavenApi


class TestDistributionsMavenApi(unittest.TestCase):
    """DistributionsMavenApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DistributionsMavenApi()

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        Create a maven distribution
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Delete a maven distribution
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        List maven distributions
        """
        pass

    def test_partial_update(self) -> None:
        """Test case for partial_update

        Update a maven distribution
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Inspect a maven distribution
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

    def test_update(self) -> None:
        """Test case for update

        Update a maven distribution
        """
        pass


if __name__ == '__main__':
    unittest.main()
