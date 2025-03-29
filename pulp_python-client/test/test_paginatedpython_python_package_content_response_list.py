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

from pulpcore.client.pulp_python.models.paginatedpython_python_package_content_response_list import PaginatedpythonPythonPackageContentResponseList

class TestPaginatedpythonPythonPackageContentResponseList(unittest.TestCase):
    """PaginatedpythonPythonPackageContentResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedpythonPythonPackageContentResponseList:
        """Test PaginatedpythonPythonPackageContentResponseList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedpythonPythonPackageContentResponseList`
        """
        model = PaginatedpythonPythonPackageContentResponseList()
        if include_optional:
            return PaginatedpythonPythonPackageContentResponseList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    pulpcore.client.pulp_python.models.python/python_package_content_response.python.PythonPackageContentResponse(
                        pulp_href = '', 
                        prn = '', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_labels = {
                            'key' : ''
                            }, 
                        artifact = '', 
                        filename = '', 
                        packagetype = '', 
                        name = '', 
                        version = '', 
                        sha256 = '', 
                        metadata_version = '', 
                        summary = '', 
                        description = '', 
                        description_content_type = '', 
                        keywords = '', 
                        home_page = '', 
                        download_url = '', 
                        author = '', 
                        author_email = '', 
                        maintainer = '', 
                        maintainer_email = '', 
                        license = '', 
                        requires_python = '', 
                        project_url = '', 
                        project_urls = null, 
                        platform = '', 
                        supported_platform = '', 
                        requires_dist = null, 
                        provides_dist = null, 
                        obsoletes_dist = null, 
                        requires_external = null, 
                        classifiers = null, )
                    ]
            )
        else:
            return PaginatedpythonPythonPackageContentResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulp_python.models.python/python_package_content_response.python.PythonPackageContentResponse(
                        pulp_href = '', 
                        prn = '', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_labels = {
                            'key' : ''
                            }, 
                        artifact = '', 
                        filename = '', 
                        packagetype = '', 
                        name = '', 
                        version = '', 
                        sha256 = '', 
                        metadata_version = '', 
                        summary = '', 
                        description = '', 
                        description_content_type = '', 
                        keywords = '', 
                        home_page = '', 
                        download_url = '', 
                        author = '', 
                        author_email = '', 
                        maintainer = '', 
                        maintainer_email = '', 
                        license = '', 
                        requires_python = '', 
                        project_url = '', 
                        project_urls = null, 
                        platform = '', 
                        supported_platform = '', 
                        requires_dist = null, 
                        provides_dist = null, 
                        obsoletes_dist = null, 
                        requires_external = null, 
                        classifiers = null, )
                    ],
        )
        """

    def testPaginatedpythonPythonPackageContentResponseList(self):
        """Test PaginatedpythonPythonPackageContentResponseList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
