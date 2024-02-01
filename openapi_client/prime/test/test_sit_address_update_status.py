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
from prime_client.model.sit_address_update_status import SitAddressUpdateStatus


class TestSitAddressUpdateStatus(unittest.TestCase):
    """SitAddressUpdateStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSitAddressUpdateStatus(self):
        """Test SitAddressUpdateStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SitAddressUpdateStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
