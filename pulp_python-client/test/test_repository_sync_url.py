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

from pulpcore.client.pulp_python.models.repository_sync_url import RepositorySyncURL

class TestRepositorySyncURL(unittest.TestCase):
    """RepositorySyncURL unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositorySyncURL:
        """Test RepositorySyncURL
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositorySyncURL`
        """
        model = RepositorySyncURL()
        if include_optional:
            return RepositorySyncURL(
                remote = '',
                mirror = True
            )
        else:
            return RepositorySyncURL(
        )
        """

    def testRepositorySyncURL(self):
        """Test RepositorySyncURL"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
