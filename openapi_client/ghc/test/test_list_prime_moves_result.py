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
from ghc_client.model.list_prime_moves import ListPrimeMoves
globals()['ListPrimeMoves'] = ListPrimeMoves
from ghc_client.model.list_prime_moves_result import ListPrimeMovesResult


class TestListPrimeMovesResult(unittest.TestCase):
    """ListPrimeMovesResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListPrimeMovesResult(self):
        """Test ListPrimeMovesResult"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListPrimeMovesResult()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
