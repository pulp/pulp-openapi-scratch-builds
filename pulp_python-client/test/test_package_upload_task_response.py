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

from pulpcore.client.pulp_python.models.package_upload_task_response import PackageUploadTaskResponse

class TestPackageUploadTaskResponse(unittest.TestCase):
    """PackageUploadTaskResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PackageUploadTaskResponse:
        """Test PackageUploadTaskResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PackageUploadTaskResponse`
        """
        model = PackageUploadTaskResponse()
        if include_optional:
            return PackageUploadTaskResponse(
                session = '',
                task = '',
                task_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PackageUploadTaskResponse(
                session = '',
                task = '',
                task_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testPackageUploadTaskResponse(self):
        """Test PackageUploadTaskResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
