"""
    MilMove Prime API

    The Prime API is a RESTful API that enables the Prime contractor to request information about upcoming moves, update the details and status of those moves, and make payment requests. It uses Mutual TLS for authentication procedures.  All endpoints are located at `/prime/v1/`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import prime_client
from prime_client.model.re_service_code import ReServiceCode
globals()['ReServiceCode'] = ReServiceCode
from prime_client.model.mto_service_item_basic_all_of import MTOServiceItemBasicAllOf


class TestMTOServiceItemBasicAllOf(unittest.TestCase):
    """MTOServiceItemBasicAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMTOServiceItemBasicAllOf(self):
        """Test MTOServiceItemBasicAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MTOServiceItemBasicAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
