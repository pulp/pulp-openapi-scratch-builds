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
from pulpcore.client.pulpcore.models.storage_class_enum import StorageClassEnum  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestStorageClassEnum(unittest.TestCase):
    """StorageClassEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StorageClassEnum
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.storage_class_enum.StorageClassEnum()  # noqa: E501
        if include_optional :
            return StorageClassEnum(
            )
        else :
            return StorageClassEnum(
        )

    def testStorageClassEnum(self):
        """Test StorageClassEnum"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
