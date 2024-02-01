"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ghc_client
from ghc_client.api.tac_api import TacApi  # noqa: E501


class TestTacApi(unittest.TestCase):
    """TacApi unit test stubs"""

    def setUp(self):
        self.api = TacApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tac_validation(self):
        """Test case for tac_validation

        Validation of a TAC value  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
