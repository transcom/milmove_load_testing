"""
    MilMove Internal API

    The Internal API is a RESTful API that enables the Customer application for MilMove.  All endpoints are located under `/internal`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import internal_client
from internal_client.api.queues_api import QueuesApi  # noqa: E501


class TestQueuesApi(unittest.TestCase):
    """QueuesApi unit test stubs"""

    def setUp(self):
        self.api = QueuesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_show_queue(self):
        """Test case for show_queue

        Show all moves in a queue  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
