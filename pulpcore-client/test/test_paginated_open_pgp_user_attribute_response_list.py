# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.paginated_open_pgp_user_attribute_response_list import PaginatedOpenPGPUserAttributeResponseList  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestPaginatedOpenPGPUserAttributeResponseList(unittest.TestCase):
    """PaginatedOpenPGPUserAttributeResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedOpenPGPUserAttributeResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.paginated_open_pgp_user_attribute_response_list.PaginatedOpenPGPUserAttributeResponseList()  # noqa: E501
        if include_optional :
            return PaginatedOpenPGPUserAttributeResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulpcore.models.open_pgp_user_attribute_response.OpenPGPUserAttributeResponse(
                        pulp_href = '0', 
                        prn = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sha256 = '0', 
                        signatures = [
                            pulpcore.client.pulpcore.models.nested_open_pgp_signature_response.NestedOpenPGPSignatureResponse(
                                issuer = '0', 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                expiration_time = '0', 
                                signers_user_id = '0', 
                                key_expiration_time = '0', 
                                expired = True, 
                                key_expired = '0', )
                            ], 
                        public_key = '0', )
                    ]
            )
        else :
            return PaginatedOpenPGPUserAttributeResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulpcore.models.open_pgp_user_attribute_response.OpenPGPUserAttributeResponse(
                        pulp_href = '0', 
                        prn = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sha256 = '0', 
                        signatures = [
                            pulpcore.client.pulpcore.models.nested_open_pgp_signature_response.NestedOpenPGPSignatureResponse(
                                issuer = '0', 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                expiration_time = '0', 
                                signers_user_id = '0', 
                                key_expiration_time = '0', 
                                expired = True, 
                                key_expired = '0', )
                            ], 
                        public_key = '0', )
                    ],
        )

    def testPaginatedOpenPGPUserAttributeResponseList(self):
        """Test PaginatedOpenPGPUserAttributeResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
