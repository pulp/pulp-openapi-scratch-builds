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

from pulpcore.client.pulp_service.models.service_feature_content_guard_response import ServiceFeatureContentGuardResponse

class TestServiceFeatureContentGuardResponse(unittest.TestCase):
    """ServiceFeatureContentGuardResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceFeatureContentGuardResponse:
        """Test ServiceFeatureContentGuardResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceFeatureContentGuardResponse`
        """
        model = ServiceFeatureContentGuardResponse()
        if include_optional:
            return ServiceFeatureContentGuardResponse(
                pulp_href = '',
                prn = '',
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                description = '',
                header_name = '',
                jq_filter = '',
                features = [
                    ''
                    ]
            )
        else:
            return ServiceFeatureContentGuardResponse(
                name = '',
                header_name = '',
                features = [
                    ''
                    ],
        )
        """

    def testServiceFeatureContentGuardResponse(self):
        """Test ServiceFeatureContentGuardResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
