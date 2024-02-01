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
from prime_client.model.orders_type import OrdersType


class TestOrdersType(unittest.TestCase):
    """OrdersType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrdersType(self):
        """Test OrdersType"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrdersType()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
