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

from pulpcore.client.pulp_python.models.python_python_publication_response import PythonPythonPublicationResponse

class TestPythonPythonPublicationResponse(unittest.TestCase):
    """PythonPythonPublicationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PythonPythonPublicationResponse:
        """Test PythonPythonPublicationResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PythonPythonPublicationResponse`
        """
        model = PythonPythonPublicationResponse()
        if include_optional:
            return PythonPythonPublicationResponse(
                pulp_href = '',
                prn = '',
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                repository_version = '',
                repository = '',
                distributions = [
                    ''
                    ]
            )
        else:
            return PythonPythonPublicationResponse(
        )
        """

    def testPythonPythonPublicationResponse(self):
        """Test PythonPythonPublicationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
