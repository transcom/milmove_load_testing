"""
    MilMove GHC API

    The GHC API is a RESTful API that enables the Office application for MilMove.  All endpoints are located under `/ghc/v1`.   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: milmove-developers@caci.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ghc_client
from ghc_client.api.move_api import MoveApi  # noqa: E501


class TestMoveApi(unittest.TestCase):
    """MoveApi unit test stubs"""

    def setUp(self):
        self.api = MoveApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_move(self):
        """Test case for get_move

        Returns a given move  # noqa: E501
        """
        pass

    def test_get_move_counseling_evaluation_reports_list(self):
        """Test case for get_move_counseling_evaluation_reports_list

        Returns counseling evaluation reports for the specified move that are visible to the current office user  # noqa: E501
        """
        pass

    def test_get_move_history(self):
        """Test case for get_move_history

        Returns the history of an identified move  # noqa: E501
        """
        pass

    def test_get_move_shipment_evaluation_reports_list(self):
        """Test case for get_move_shipment_evaluation_reports_list

        Returns shipment evaluation reports for the specified move that are visible to the current office user  # noqa: E501
        """
        pass

    def test_search_moves(self):
        """Test case for search_moves

        Search moves by locator, DOD ID, or customer name  # noqa: E501
        """
        pass

    def test_set_financial_review_flag(self):
        """Test case for set_financial_review_flag

        Flags a move for financial office review  # noqa: E501
        """
        pass

    def test_update_closeout_office(self):
        """Test case for update_closeout_office

        Updates a Move's PPM closeout office for Army and Air Force customers  # noqa: E501
        """
        pass

    def test_upload_additional_documents(self):
        """Test case for upload_additional_documents

        Patch the additional documents for a given move  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
