"""
    MilMove Internal API

    The Internal API is a RESTful API that enables the Customer application for MilMove.  All endpoints are located under `/internal`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: ppp@truss.works
    Generated by: https://openapi-generator.tech
"""


import unittest

import internal_client
from internal_client.api.moves_api import MovesApi  # noqa: E501


class TestMovesApi(unittest.TestCase):
    """MovesApi unit test stubs"""

    def setUp(self):
        self.api = MovesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_patch_move(self):
        """Test case for patch_move

        Patches the move  # noqa: E501
        """
        pass

    def test_show_move(self):
        """Test case for show_move

        Returns the given move  # noqa: E501
        """
        pass

    def test_show_shipment_summary_worksheet(self):
        """Test case for show_shipment_summary_worksheet

        Returns Shipment Summary Worksheet  # noqa: E501
        """
        pass

    def test_submit_amended_orders(self):
        """Test case for submit_amended_orders

        Submits amended orders for review  # noqa: E501
        """
        pass

    def test_submit_move_for_approval(self):
        """Test case for submit_move_for_approval

        Submits a move for approval  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
