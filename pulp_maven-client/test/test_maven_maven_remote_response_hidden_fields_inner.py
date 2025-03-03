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

from pulpcore.client.pulp_maven.models.maven_maven_remote_response_hidden_fields_inner import MavenMavenRemoteResponseHiddenFieldsInner

class TestMavenMavenRemoteResponseHiddenFieldsInner(unittest.TestCase):
    """MavenMavenRemoteResponseHiddenFieldsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MavenMavenRemoteResponseHiddenFieldsInner:
        """Test MavenMavenRemoteResponseHiddenFieldsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MavenMavenRemoteResponseHiddenFieldsInner`
        """
        model = MavenMavenRemoteResponseHiddenFieldsInner()
        if include_optional:
            return MavenMavenRemoteResponseHiddenFieldsInner(
                name = '',
                is_set = True
            )
        else:
            return MavenMavenRemoteResponseHiddenFieldsInner(
                name = '',
                is_set = True,
        )
        """

    def testMavenMavenRemoteResponseHiddenFieldsInner(self):
        """Test MavenMavenRemoteResponseHiddenFieldsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
