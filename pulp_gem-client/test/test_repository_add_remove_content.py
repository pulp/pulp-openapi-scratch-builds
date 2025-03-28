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

from pulpcore.client.pulp_gem.models.repository_add_remove_content import RepositoryAddRemoveContent

class TestRepositoryAddRemoveContent(unittest.TestCase):
    """RepositoryAddRemoveContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryAddRemoveContent:
        """Test RepositoryAddRemoveContent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryAddRemoveContent`
        """
        model = RepositoryAddRemoveContent()
        if include_optional:
            return RepositoryAddRemoveContent(
                add_content_units = [
                    '0'
                    ],
                remove_content_units = [
                    '0'
                    ],
                base_version = ''
            )
        else:
            return RepositoryAddRemoveContent(
        )
        """

    def testRepositoryAddRemoveContent(self):
        """Test RepositoryAddRemoveContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
