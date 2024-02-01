"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ghc_client
from ghc_client.api.queues_api import QueuesApi  # noqa: E501


class TestQueuesApi(unittest.TestCase):
    """QueuesApi unit test stubs"""

    def setUp(self):
        self.api = QueuesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_moves_queue(self):
        """Test case for get_moves_queue

        Gets queued list of all customer moves by GBLOC origin  # noqa: E501
        """
        pass

    def test_get_payment_requests_queue(self):
        """Test case for get_payment_requests_queue

        Gets queued list of all payment requests by GBLOC origin  # noqa: E501
        """
        pass

    def test_get_services_counseling_queue(self):
        """Test case for get_services_counseling_queue

        Gets queued list of all customer moves needing services counseling by GBLOC origin  # noqa: E501
        """
        pass

    def test_list_prime_moves(self):
        """Test case for list_prime_moves

        getPrimeMovesQueue  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
