"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ghc_client
from ghc_client.model.search_customers import SearchCustomers
globals()['SearchCustomers'] = SearchCustomers
from ghc_client.model.search_customers_result import SearchCustomersResult


class TestSearchCustomersResult(unittest.TestCase):
    """SearchCustomersResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchCustomersResult(self):
        """Test SearchCustomersResult"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchCustomersResult()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()