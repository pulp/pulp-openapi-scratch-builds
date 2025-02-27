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

from pulpcore.client.pulp_maven.models.paginatedmaven_maven_artifact_response_list import PaginatedmavenMavenArtifactResponseList

class TestPaginatedmavenMavenArtifactResponseList(unittest.TestCase):
    """PaginatedmavenMavenArtifactResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedmavenMavenArtifactResponseList:
        """Test PaginatedmavenMavenArtifactResponseList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedmavenMavenArtifactResponseList`
        """
        model = PaginatedmavenMavenArtifactResponseList()
        if include_optional:
            return PaginatedmavenMavenArtifactResponseList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    pulpcore.client.pulp_maven.models.maven/maven_artifact_response.maven.MavenArtifactResponse(
                        pulp_href = '', 
                        prn = '', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        artifact = '', 
                        group_id = '', 
                        artifact_id = '', 
                        version = '', 
                        filename = '', )
                    ]
            )
        else:
            return PaginatedmavenMavenArtifactResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulp_maven.models.maven/maven_artifact_response.maven.MavenArtifactResponse(
                        pulp_href = '', 
                        prn = '', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        artifact = '', 
                        group_id = '', 
                        artifact_id = '', 
                        version = '', 
                        filename = '', )
                    ],
        )
        """

    def testPaginatedmavenMavenArtifactResponseList(self):
        """Test PaginatedmavenMavenArtifactResponseList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
